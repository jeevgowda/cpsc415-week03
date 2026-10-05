# Specification: Intent Classifier Component

## Design Decisions

### Decision 1: Execution Language
- Chosen: Python 3 (Standard Library only - urllib.request, json, os).
- Alternative Considered: Java standard library (HttpClient).
- Reasoning: Python offers lightweight, zero-dependency JSON parsing and prompt execution scripts ideal for immediate CLI evaluation without compile steps.

### Decision 2: Model Selection
- Chosen Primary: anthropic/claude-3.5-haiku via OpenRouter.
- Chosen Alternative: nvidia/nemotron-3-ultra-550b-a55b:free (or openai/gpt-4o-mini).
- Reasoning: Claude 3.5 Haiku strictly follows JSON formatting constraints; testing against Nemotron/GPT-4o-mini allows evaluation of JSON compliance and refusal/unknown handling.

## Numbered Behaviors
1. Behavior 1 (Clear Billing): When input is "How do I update my credit card?", response JSON category must be billing.
2. Behavior 2 (Clear Tech Support): When input is "App keeps crashing on login screen", response JSON category must be technical_support.
3. Behavior 3 (Clear Account Access): When input is "I forgot my password and cannot sign in", response JSON category must be account_access.
4. Behavior 4 (Ambiguous Dual-Category): When input is "I was charged twice after my login failed", acceptable category must be either billing or technical_support.
5. Behavior 5 (Out-of-Scope / Unknown): When input is "What is the capital of France?", response JSON category MUST be unknown.
