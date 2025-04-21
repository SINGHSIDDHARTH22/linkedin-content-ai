
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
import requests

# Replace this with your actual OpenRouter API Key
OPENROUTER_API_KEY = "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"
REFERER = "https://github.com/SINGHSIDDHARTH22/linkedin-content-ai"

def analyze_tone_with_llama(post_content, hashtags=None):
    """
    Use LLaMA API to analyze the tone of a LinkedIn post.
    The tone is influenced by both the content and relevant hashtags.
    """
    hashtags_text = " ".join(hashtags) if hashtags else ""
    
    # Build a prompt with both content and hashtags
    prompt = f"""You are a tone analyzer. Analyze the tone of this LinkedIn post and its hashtags.\n\nPost content: {post_content}\nHashtags: {hashtags_text}\n\nProvide a tone from these options: storytelling, listicle, opinion ,insightful, casual, inspirational, funny, or professional."""
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": REFERER,
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [{"role": "user", "content": prompt.strip()}],
        "temperature": 0.7
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        tone = response.json()["choices"][0]["message"]["content"].strip()
        return tone
    except Exception as e:
        return f"Error analyzing tone: {e}"

def get_hashtags_from_text(text):
    """Extract hashtags from the text, ensuring the text is a valid string."""
    if not isinstance(text, str):  # Check if the input is a string
        text = ""  # If not, treat it as an empty string
    return re.findall(r"#\w+", text)

# Read LinkedIn posts CSV file
df = pd.read_csv("linkedin_posts.csv")

# Compute engagement metrics
df["engagement"] = df["likes"] + df["comments"]
df["engagement_rate"] = df["engagement"] / df["word_count"].replace(0, 1)

# Analyze tone for each post using LLaMA and consider hashtags
tones = []
for index, row in df.iterrows():
    content = row["content"]
    hashtags = get_hashtags_from_text(row["hashtags"])
    tone = analyze_tone_with_llama(content, hashtags)
    tones.append(tone)

    # Tone checker after each post
    print(f"Post {index + 1} Tone: {tone} | Content: {content[:50]}...")

df['tone'] = tones

# Hashtag Analysis
all_tags = " ".join(df["hashtags"].fillna("")).split()
top_hashtags = Counter(all_tags).most_common(10)
print("Top 10 Hashtags:", top_hashtags)

# CTA Analysis (detect if CTA exists in the post content)
cta_effect = df.groupby(df["has_cta"])["engagement"].mean()
print("Engagement with CTA vs Without CTA:\n", cta_effect)

# Emoji Analysis (detect emoji in the post)
emoji_effect = df.groupby(df["has_emoji"])["engagement"].mean()
print("Engagement with Emoji vs Without Emoji:\n", emoji_effect)

# Plot Engagement by Hour (even though no post_time, use available engagement data)
sns.barplot(data=df, x="engagement", y="word_count")
plt.title("Engagement vs Word Count")
plt.xlabel("Engagement")
plt.ylabel("Word Count")
plt.tight_layout()
plt.savefig("engagement_vs_word_count.png")

# Save analyzed data to new CSV
df.to_csv("linkedin_posts_with_tone.csv", index=False)

# Average Tone Analysis
average_tone = df["tone"].mode()[0]
print(f"Most common tone across all posts: {average_tone}")
