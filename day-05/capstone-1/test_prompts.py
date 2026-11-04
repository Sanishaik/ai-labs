
from pathlib import Path
import anthropic

client = anthropic.Anthropic()

PROMPT_DIR = Path("prompts")
RESULT_DIR = Path("results")
RESULT_DIR.mkdir(exist_ok=True)

prompt_files = [
    "01-abap-code-explainer.md",
    "02-st22-dump-analyzer.md",
    "03-odata-analyzer.md",
    "04-performance-optimizer.md",
    "05-functional-spec-to-abap.md"
]

success_count = 0
failure_count = 0

for filename in prompt_files:
    print(f"\nTesting: {filename}")

    try:
        prompt = (PROMPT_DIR / filename).read_text(
            encoding="utf-8"
        )

        response = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=3000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        text_parts = []

        for block in response.content:
            if isinstance(block, anthropic.types.TextBlock):
                text_parts.append(block.text)

        result = "\n".join(text_parts)

        if not result.strip():
            raise ValueError(
                "Claude returned no text block. "
                f"Response block types: "
                f"{[type(block).__name__ for block in response.content]}"
            )

        output_file = filename.replace(
            ".md", "-result.md"
        )

        output_path = RESULT_DIR / output_file
        output_path.write_text(result, encoding="utf-8")

        print(f"SUCCESS: Result saved to {output_path}")
        success_count += 1

    except Exception as error:
        print(f"FAILED: {filename}")
        print(f"Error: {error}")
        failure_count += 1

print("\n========== TEST SUMMARY ==========")
print(f"Successful prompts: {success_count}")
print(f"Failed prompts: {failure_count}")
print("=================================")
