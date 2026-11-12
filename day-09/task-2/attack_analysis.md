The prompt injection attack was the hardest because the malicious instruction was hidden inside an invoice line-item description.
A simple top-level field check would not detect this nested instruction.
I fixed the validator to scan the complete invoice JSON, including nested fields.
The validator now rejects the invoice with the reason "Prompt injection detected."
The invoice remains unposted, and the decision is recorded in the audit log.
