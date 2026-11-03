
import anthropic
import re
from pathlib import Path

client = anthropic.Anthropic()

MODEL = "claude-haiku-5-5"

# Read HR policy
POLICY_FILE = Path(__file__).with_name("hr_policy.txt")
policy = POLICY_FILE.read_text(encoding="utf-8")


# Split policy into numbered sections
def split_into_chunks(text):
    sections = re.split(
        r"(?m)(?=^\d+\.\d+\s)",
        text
    )

    return [
        section.strip()
        for section in sections
        if re.match(r"^\d+\.\d+\s", section.strip())
    ]


# Remove common words from questions
STOP_WORDS = {
    "how", "many", "what", "when", "do", "i",
    "get", "is", "the", "a", "an", "of", "for",
    "are", "does", "days", "can", "my", "me",
    "to", "per", "and", "in", "on", "with"
}


def get_keywords(text):
    words = re.findall(r"\b[a-z0-9]+\b", text.lower())
    return {word for word in words if word not in STOP_WORDS}


# Retrieve the top 3 relevant policy sections
def retrieve(question, chunks):
    question_words = get_keywords(question)

    scored_chunks = []

    for chunk in chunks:
        chunk_words = get_keywords(chunk)

        score = len(question_words.intersection(chunk_words))

        if score > 0:
            scored_chunks.append((score, chunk))

    scored_chunks.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        chunk
        for score, chunk in scored_chunks[:3]
    ]


# Ask Claude using retrieved policy sections
def ask(question, chunks):

    if not chunks:
        return "Not in policy."

    context = "\n\n".join(chunks)

    system_prompt = """
You are an HR policy question-answering assistant.

Follow these rules:
1. Answer only using the supplied policy sections.
2. Do not use outside knowledge.
3. Do not guess or invent information.
4. Mention the correct policy section number.
5. If the answer is not available in the supplied sections,
   reply exactly: Not in policy.
6. Keep the answer short and clear.
"""

    msg = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": (
                    f"POLICY SECTIONS:\n{context}\n\n"
                    f"QUESTION: {question}"
                )
            }
        ]
    )

    for block in msg.content:
        if block.type == "text":
            return block.text

    return "No text response received from Claude."


# Run the Mini RAG application
if __name__ == "__main__":

    chunks = split_into_chunks(policy)

    print("HR POLICY - MINI RAG ASSISTANT")
    print("Sections loaded:", len(chunks))

    question = input("\nEnter your HR policy question: ")

    relevant_chunks = retrieve(question, chunks)

    print("\nRetrieved sections:")

    for chunk in relevant_chunks:
        print(chunk)

    answer = ask(question, relevant_chunks)

    print("\nClaude's Answer:")
    print(answer)
