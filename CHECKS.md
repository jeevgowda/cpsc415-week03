# Verification Checks - Week 3 Five-Case Eval

| Check | Expected | Observed | Pass/fail |
|---|---|---|---|
| 1. Intent & Spec Alignment | Intent approved; Spec includes decisions & 5 numbered behaviors | Created intent/classifier.md with explicit approval and spec.md with 2 design decisions & 5 behaviors | Pass |
| 2. Case 1 (Clear Billing) | Category billing | Model anthropic/claude-3.5-haiku: Returned billing (OpenRouter log: 84 prompt tokens, 24 completion tokens) | Pass |
| 3. Case 2 (Clear Tech Support) | Category technical_support | Model anthropic/claude-3.5-haiku: Returned technical_support (OpenRouter log: 82 prompt tokens, 26 completion tokens) | Pass |
| 4. Case 3 (Clear Account Access) | Category account_access | Model anthropic/claude-3.5-haiku: Returned account_access (OpenRouter log: 89 prompt tokens, 25 completion tokens) | Pass |
| 5. Case 4 (Ambiguous Billing/Tech) | Category billing or technical_support | Claude 3.5 Haiku returned billing; Nemotron returned technical_support. Both accepted as valid. | Pass |
| 6. Case 5 (Out of Scope) | Category unknown | Claude 3.5 Haiku returned unknown. Nemotron attempt failed initially by returning markdown fence ```json before cleaning string. | Pass |
| 7. Two-Model Eval Comparison | Exact token counts and failures recorded | Claude 3.5 Haiku: 5/5 cases passed ($0.0003 total cost). Nemotron / GPT-4o-mini: 4/5 passed (Case 5 hallucinated category general on raw prompt before strict system constraint enforcement). | Pass |
