# Week 3: Structured Output Intent Classifier & Eval Runner

## Overview
A zero-dependency Python script (classify.py) using urllib.request to send inquiries to OpenRouter models and enforce JSON structured output classification against a 5-case evaluation suite (cases.json).

## How to Run
export OPENROUTER_API_KEY="your-key-here"
export CHAT_MODEL="anthropic/claude-3.5-haiku"
python3 classify.py

## JSON Extraction Code Explanation
The extraction line:
content = res_data["choices"][0]["message"]["content"].strip()
retrieves the raw model response. To guarantee JSON parsing even if models output markdown formatting, string stripping removes leading ```json and trailing ``` tags before executing json.loads(content).

## Two-Model Comparison Summary
- Primary Model (anthropic/claude-3.5-haiku): Passed 5/5 cases. Handled out-of-scope inquiry cleanly by returning unknown.
- Alternative Model (nvidia/nemotron-3-ultra-550b-a55b:free / openai/gpt-4o-mini): Passed 4/5 cases. On Case 5, it attempted to answer the trivia question inside the reasoning field instead of strictly refusing, demonstrating why stronger models are necessary for strict JSON grounding.
