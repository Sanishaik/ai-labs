
from rag import policy, split_into_chunks, retrieve, ask

chunks = split_into_chunks(policy)

test_cases = [
    {
        "question": "How many casual leave days do employees get?",
        "expected": "12 days",
        "section": "4.1"
    },
    {
        "question": "How many paternity leave days are provided?",
        "expected": "15 working days",
        "section": "4.2"
    },
    {
        "question": "How many sick leave days are allowed?",
        "expected": "10 days",
        "section": "4.3"
    },
    {
        "question": "When is a doctor's note required?",
        "expected": "after 2 days",
        "section": "4.3"
    },
    {
        "question": "How many annual leave days are provided?",
        "expected": "20 days",
        "section": "4.4"
    },
    {
        "question": "How many work-from-home days are allowed?",
        "expected": "2 days per week",
        "section": "4.5"
    },
    {
        "question": "How many public holidays do employees receive?",
        "expected": "10 public holidays",
        "section": "4.6"
    },
    {
        "question": "Who approves leave requests?",
        "expected": "reporting manager",
        "section": "4.7"
    },
    {
        "question": "How many annual leave days can be carried forward?",
        "expected": "5",
        "section": "4.8"
    },
    {
        "question": "What is the probation period for new employees?",
        "expected": "6 months",
        "section": "4.10"
    }
]

passed = 0

for number, test in enumerate(test_cases, start=1):
    print("\nTest", number)
    print("Question:", test["question"])

    relevant_chunks = retrieve(test["question"], chunks)
    answer = ask(test["question"], relevant_chunks)

    print("Expected:", test["expected"])
    print("Actual:", answer)

    answer_lower = answer.lower()

    if (
        test["expected"].lower() in answer_lower
        and test["section"] in answer
    ):
        print("Result: PASS")
        passed += 1
    else:
        print("Result: FAIL")

print("\n-------------------------")
print("FINAL RESULT:", passed, "/", len(test_cases))
print("-------------------------")
