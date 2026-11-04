# Capstone 1 – SAP Prompt Toolkit

## Project Overview

The SAP Prompt Toolkit is a collection of five AI prompts designed to support common SAP ABAP development and troubleshooting activities.

The prompts use Claude AI through the Anthropic API to generate explanations, analyze errors, suggest performance improvements, and convert functional requirements into technical designs.

## Objectives

- Build reusable prompts for SAP ABAP tasks.
- Use clear instructions to guide AI responses.
- Test all five prompts using the Anthropic API.
- Save AI-generated responses for review.
- Identify limitations and document validation requirements.

## Project Structure

```text
capstone-1/
├── prompts/
│   ├── 01-abap-code-explainer.md
│   ├── 02-st22-dump-analyzer.md
│   ├── 03-odata-analyzer.md
│   ├── 04-performance-optimizer.md
│   └── 05-functional-spec-to-abap.md
│
├── results/
│   ├── 01-abap-code-explainer-result.md
│   ├── 02-st22-dump-analyzer-result.md
│   ├── 03-odata-analyzer-result.md
│   ├── 04-performance-optimizer-result.md
│   └── 05-functional-spec-to-abap-result.md
│
├── failure-notes/
│   └── failure-notes.md
│
├── test_prompts.py
└── README.md
```

## Five SAP Prompts

1. **ABAP Code Explainer** – Explains ABAP code in simple, beginner-friendly steps.
2. **ST22 Dump Analyzer** – Helps analyze SAP runtime errors and identify possible causes.
3. **OData Error Analyzer** – Helps troubleshoot SAP OData service errors.
4. **ABAP Performance Optimizer** – Reviews ABAP code and suggests performance improvements.
5. **Functional Specification to ABAP** – Converts functional requirements into a technical design for ABAP development.

## Technologies Used

- Python
- Anthropic Python SDK
- Claude Haiku 5.5
- Markdown
- SAP ABAP concepts
- SAP OData concepts

## How to Run

1. Open the `capstone-1` folder in the terminal.
2. Ensure Python and the Anthropic SDK are installed.
3. Configure the `ANTHROPIC_API_KEY` environment variable securely.
4. Run the following command:

```bash
python test_prompts.py
```

5. Check the `results/` folder for the generated responses.

## Testing Results

All five prompt tests completed successfully.

- Total prompts tested: 5
- Successful prompts: 5
- Failed prompts: 0

Generated responses were saved in the `results/` folder.

## Failure Notes

Limitations and validation requirements for all five prompts are documented in:

`failure-notes/failure-notes.md`

## Important Safety Note

AI-generated explanations, troubleshooting steps, and ABAP code suggestions are for learning and assistance. They must be reviewed and validated by an SAP developer in the relevant SAP system before implementation.

## Conclusion

This project demonstrates how structured prompts and the Anthropic API can support SAP ABAP development and troubleshooting. It also highlights the importance of providing sufficient technical context and validating AI-generated results.