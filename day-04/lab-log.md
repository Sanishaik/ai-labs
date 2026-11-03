
# Day 04 – Lab Log

**Name:** Shaik Saniya  
**Date:** 03 November 2026  
**Phase:** Phase 4 – Prompt Engineering

## 1. Day 04 Activities

| Task | Activity | Status |
|---|---|---|
| Task 1 | First Anthropic API Call | Completed |
| Task 2 | Mini RAG Application | Completed |
| Task 3 | Red Team Your RAG | Completed |
| Task 4 | Capstone 1 – SAP Prompt Toolkit | Completed |
| Task 5 | Proof and Lab Log | In Progress |

## 2. Task 1 – First API Call

- Created Anthropic API key.
- Configured the API key securely.
- Installed Anthropic Python SDK.
- Created and executed `hello.py`.
- Successfully received a response from Claude Haiku 5.5.

## 3. Task 2 – Mini RAG

- Created an HR leave policy document.
- Split the policy into numbered sections.
- Implemented keyword-based retrieval.
- Retrieved the top three relevant sections.
- Generated answers using Claude Haiku 5.5.
- Created test questions in `tests.py`.

**Files:** `rag.py`, `hr_policy.txt`, `tests.py`

**Test result:** Record the actual result from your test execution.

## 4. Task 3 – Red Team Your RAG

- Added five prompt injection examples to the HR policy.
- Implemented basic suspicious-pattern filtering.
- Updated the system instructions to treat policy content as data, not instructions.
- Created and executed attack test cases.

**Test result: ATTACKS BLOCKED: 5 / 5**

**Files:** `hr_policy_attack.txt`, `tests_attack.py`, `attacks.md`

## 5. Task 4 – Capstone 1

Created the first two SAP Prompt Toolkit prompts:

1. SAP ABAP Code Explainer.
2. SAP ABAP ST22 Dump Analyzer.

For both prompts, documented:
- Before prompt and response.
- Improved six-building-block prompt.
- Improved prompt response.
- Failure notes.

**Files:**
- `prompt-1-abap-code-explainer.md`
- `prompt-2-abap-dump-analyzer.md`

## 6. API Usage and Cost

**Provider:** Anthropic  
**Model:** Claude Haiku 5.5  
**Purpose:** API testing, Mini RAG, and red-team testing.

**Actual API cost:** To be checked and entered from Anthropic Console.

## 7. Safety Practices

- Never expose API keys.
- Use sample data for testing.
- Treat retrieved documents as untrusted data.
- Validate AI-generated code.
- Test changes before production use.

## 8. Learning Outcomes

- Learned how to call an AI model using Python.
- Understood how RAG retrieves information from documents.
- Learned basic prompt injection defense.
- Practiced prompt engineering using six building blocks.
- Understood the importance of testing AI-generated responses.

## 9. Conclusion

Completed the main Day 04 practical activities: API integration, Mini RAG, red-team testing, and the first two SAP Prompt Toolkit prompts.

The exercises helped me understand how AI applications work and why grounding, testing, and safety are important.

**Day 04 Goal:** Call AI from code, ground it in documents, and defend it.