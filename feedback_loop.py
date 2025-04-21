import json

FEEDBACK_FILE = "feedback.json"

def store_feedback(post_text, rating, reason=""):
    feedback_entry = {
        "post": post_text,
        "rating": rating,
        "reason": reason
    }
    with open(FEEDBACK_FILE, "a") as f:
        f.write(json.dumps(feedback_entry) + "\n")

def get_average_score():
    try:
        scores = []
        with open(FEEDBACK_FILE) as f:
            for line in f:
                entry = json.loads(line)
                scores.append(entry["rating"])
        return sum(scores) / len(scores) if scores else 0
    except FileNotFoundError:
        return 0
