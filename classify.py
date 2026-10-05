import os
import json
import sys
import urllib.request

def classify_text(text, model_name):
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    url = "https://openrouter.ai/api/v1/chat/completions"
    prompt = f"Classify the following user input into EXACTLY ONE category:\n- billing\n- technical_support\n- account_access\n- unknown\n\nReturn ONLY a raw JSON object with no markdown formatting or triple backticks:\n{{\"category\": \"<one of above>\", \"confidence\": <float 0-1>, \"reasoning\": \"<short explanation>\"}}\n\nUser input: {text}"

    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            content = res_data["choices"][0]["message"]["content"].strip()
            if content.startswith("```json"): content = content[7:]
            if content.startswith("```"): content = content[3:]
            if content.endswith("```"): content = content[:-3]
            content = content.strip()
            
            parsed = json.loads(content)
            usage = res_data.get("usage", {})
            return parsed, usage, res_data.get("model", model_name)
    except Exception as e:
        return {"category": "error", "reasoning": str(e)}, {}, model_name

def run_eval():
    model = os.environ.get("CHAT_MODEL", "anthropic/claude-3.5-haiku")
    with open("cases.json") as f:
        cases = json.load(f)

    print(f"=== Running Evaluation Matrix for Model: {model} ===")
    for c in cases:
        result, usage, returned_model = classify_text(c["input"], model)
        passed = result.get("category") in c["expected_categories"]
        status = "PASS" if passed else "FAIL"
        print(f"Case {c['id']} [{c['purpose']}]: {status}")
        print(f"  Input: {c['input']}")
        print(f"  Returned Category: {result.get('category')}")
        print(f"  Reasoning: {result.get('reasoning')}")
        print(f"  Usage Tokens: {usage}")
        print("-" * 50)

if __name__ == "__main__":
    run_eval()
