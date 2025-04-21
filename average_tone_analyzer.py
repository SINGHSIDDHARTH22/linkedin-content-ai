import pandas as pd
import requests
import re

# Replace this with your actual OpenRouter API Key
OPENROUTER_API_KEY = "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"
REFERER = "https://github.com/SINGHSIDDHARTH22/linkedin-content-ai"

BATCH_SIZE = 10  # Number of posts to process in each batch

def analyze_average_tone_with_llama(post_tones, post_contents, hashtags):
    """
    Use LLaMA API to analyze the average tone of multiple LinkedIn posts.
    The tone is determined by analyzing a list of tones, contents, and hashtags from the posts.
    """
    # Build a structured prompt with the tones, content, and hashtags of all posts
    posts_info = []
    for i in range(len(post_tones)):
        post_content = post_contents[i]  # No truncation here
        posts_info.append(f"Post {i+1}: Tone: {post_tones[i]}, Content: {post_content}, Hashtags: {hashtags[i]}")

    prompt = f"""You are an AI tone analyzer. Here is a list of LinkedIn posts with their respective tones, content, and hashtags:
    {posts_info}
    
    Based on this, determine the average tone across all posts and provide an explanation for your analysis. 
    Choose a tone from the following options: insightful, casual, inspirational, funny, or professional.
    """

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

        # Debugging: Print out the raw response to understand its structure
        print("API Response:", response.json())

        # Check if 'choices' is in the response and extract the tone
        if "choices" in response.json():
            tone = response.json()["choices"][0]["message"]["content"].strip()
            return tone
        else:
            return "Error: 'choices' not found in the response"
    except Exception as e:
        return f"Error analyzing tone: {e}"

def get_hashtags_from_text(text):
    """Extract hashtags from the text, ensuring the text is a valid string."""
    if not isinstance(text, str):  # Check if the input is a string
        text = ""  # If not, treat it as an empty string
    return re.findall(r"#\w+", text)

# Read LinkedIn posts with tone CSV file
df = pd.read_csv("linkedin_posts_with_tone.csv")

# Collect the necessary data for tone analysis
post_tones = df['tone'].tolist()
post_contents = df['content'].tolist()
hashtags = df['hashtags'].apply(get_hashtags_from_text).tolist()

# Process posts in batches
batch_results = []
for i in range(0, len(post_tones), BATCH_SIZE):
    batch_tones = post_tones[i:i+BATCH_SIZE]
    batch_contents = post_contents[i:i+BATCH_SIZE]
    batch_hashtags = hashtags[i:i+BATCH_SIZE]

    # Get the explanation of the average tone across this batch of posts
    average_tone_explanation = analyze_average_tone_with_llama(batch_tones, batch_contents, batch_hashtags)

    batch_results.append(average_tone_explanation)

    # Print status after each batch
    print(f"✅ Batch {i // BATCH_SIZE + 1} processed: {len(batch_tones)} posts analyzed.")

# Print all batch results
for result in batch_results:
    print(f"Average Tone Explanation for Batch: {result}")
