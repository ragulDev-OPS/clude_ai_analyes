import json
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Read only the last 50 lines of tfplan.json
with open("tfplan.json") as f:
    lines = f.readlines()
plan = "".join(lines[-20:])  # <-- Added this line

prompt = f"""
Analyze this Terraform plan and find:
1. Security issues
2. Misconfiguration
3. Cost risks
4. Best practice violations

Terraform Plan:
{plan}
"""

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(message.content[0].text)
