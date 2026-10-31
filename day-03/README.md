# Day 3 – Task 1: Few-Shot Accuracy

## Objective
Classify 20 expense descriptions into six company expense categories using Zero-Shot and Few-Shot Prompting techniques.

## Expense Categories
1. CAPEX-IT
2. OPEX-Welfare
3. OPEX-Maintenance
4. OPEX-Travel
5. OPEX-Office
6. OPEX-Training

## Methodology

**1. Zero-Shot Prompting**
- Provided an expense description directly to Gemini.
- Asked Gemini to classify the expense into the appropriate category.
- Recorded the output and checked its correctness.

**2. Few-Shot Prompting**
- Provided examples of expenses with their correct categories.
- Asked Gemini to classify a new expense using those examples.
- Recorded the output and checked its correctness.

## Accuracy Results

| Method | Correct Answers | Total Questions | Accuracy |
|---|---:|---:|---:|
| Zero-Shot | 18 | 20 | 90% |
| Few-Shot | 18 | 20 | 90% |

## Observations
- Both prompting techniques achieved 90% accuracy.
- Zero-Shot and Few-Shot each produced 18 correct classifications.
- Q11 and Q12 were incorrectly classified by both methods.
- Providing examples in Few-Shot Prompting did not improve accuracy in this experiment.

## Conclusion
Completed the expense classification experiment using Gemini. Compared Zero-Shot and Few-Shot Prompting techniques and recorded the results in an Excel workbook.

**Result:** Zero-Shot Accuracy – 90%; Few-Shot Accuracy – 90%.

## Proof
Excel file: `Day_03_Task_1_Few_Shot_Accuracy.xlsx`
