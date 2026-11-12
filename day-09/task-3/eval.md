# Day 9 - Task 3: Model Evaluation

## Objective
Compare Claude Haiku 5.5 and Claude Sonnet 5.5 using 20 labelled invoices based on accuracy, execution time, and estimated API cost.

## Evaluation Results

| Metric | Haiku 5.5 | Sonnet 5.5 |
|---|---:|---:|
| Correct predictions | 18/20 | 20/20 |
| Accuracy | 90% | 100% |
| Execution time | 21.42 seconds | 42.55 seconds |
| Input tokens | 11,791 | 11,791 |
| Output tokens | 571 | 4,349 |
| Estimated cost | $0.001465 | $0.067072 |

## Observations
- Haiku classified 18 out of 20 invoices correctly.
- Haiku incorrectly classified INV16 and INV20.
- Sonnet classified all 20 invoices correctly.
- Sonnet took approximately twice as long as Haiku.
- Sonnet had a higher estimated API cost.

## Model Choice
Claude Sonnet 5.5 is selected for this evaluation because it achieved 100% accuracy.

Although Sonnet is more expensive and slower, accurate invoice validation is important for financial workflows.

## Production Recommendation
Use deterministic Python validation for critical checks such as PO matching, vendor verification, duplicate detection, and amount validation.

An AI model should assist with invoice understanding, but financial posting must require validation and human approval.

## Limitations
- The evaluation used only 20 synthetic invoices.
- Results may differ with real-world invoice data.
- API costs are estimates based on the rates configured in the evaluation script.
