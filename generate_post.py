import requests

# Replace this with your actual OpenRouter API Key
OPENROUTER_API_KEY = "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"

# This is required by OpenRouter. Use your GitHub profile or project page.
REFERER = "https://github.com/SINGHSIDDHARTH22/linkedin-content-ai"

def generate_post(topic, tone="storytelling", style="inspirational", hashtags=None, include_cta=True, include_emojis=True):
    """
    Generate a LinkedIn post using LLaMA 3 (8B Instruct) via OpenRouter API.
    """

    # Build prompt dynamically based on flags
    prompt = f"""You are writing a LinkedIn post for a founder audience.

Write a {tone}-style post in an {style} tone about: "{topic}".

The post should:
- Be concise and engaging (under 200 words)
- Start with a hook
- Include a relatable personal insight or learning
"""
    if include_cta:
        prompt += "\n- End with a CTA like 'What’s your experience?' or 'Comment below 👇'"
    if include_emojis:
        prompt += "\n- Use emojis where they add clarity or tone (e.g., 🚀, 💡)"
    if hashtags:
        prompt += f"\n- Add 2-3 relevant hashtags at the end, such as: {' '.join(hashtags)}"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": REFERER,
        "X-Title": "LinkedIn Content AI"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt.strip()}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ Error generating post: {e}"
