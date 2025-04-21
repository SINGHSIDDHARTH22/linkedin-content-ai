
# LinkedIn Content AI

Welcome to LinkedIn Content AI — a project designed to automate, analyze, and optimize LinkedIn post creation using AI models and real-world data.

## 🔍 What This Does

This tool helps you:

- **Scrape public LinkedIn posts** from selected profiles using Selenium.
- **Analyze key engagement drivers** like hashtags, CTAs, emojis, post length, and timing.
- **Generate post ideas** using an AI model based on successful content.
- **Rate and interact** with generated posts in an interactive Streamlit app.
- **Improve over time** by learning from user feedback (optional).
- **Export scraped data** to CSV/Excel for manual inspection.

## 🧠 Key Features

### 🔍 Scraper with Selenium
- Simulates profile scrolling and extracts:
  - Post body
  - Post time
  - Hashtags
  - Likes/comments
  - Reposts (including shared content)

### 📊 Trend Analyzer
- Analyzes trends using Python:
  - Most used hashtags
  - Emoji usage vs. engagement
  - Best posting times (day/time heatmaps)
  - CTA impact on engagement

### 🔧 AI-Powered Post Generator
- Generates 2-3 AI-crafted posts in the tone/style of top-performing content.
- Learns from real performance data to refine the generation process.

### 👀 Post Rating + Feedback Loop (Optional)
- Allows manual rating of generated posts.
- Fine-tunes future generations based on feedback.

### 💡 Topic Suggester (Optional)
- Analyzes trending themes from scraped data and recommends new topics.

### 🌐 Streamlit App
- Input a topic, tone, and intent.
- View post suggestions and engagement scores.
- Submit feedback or ratings.

## 🛠️ Setup Instructions

### 1. Clone This Repo

```bash
git clone https://github.com/SINGHSIDDHARTH22/linkedin-content-ai.git
cd linkedin-content-ai
```

### 2. Set Up Python Environment

```bash
python -m venv env
env\Scripts\activate  # On Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Scraper

```bash
python scrape_linkedin_posts.py
```

You’ll be prompted to log in to LinkedIn once. Cookies are stored for reuse.

### 5. Run the Analyzer

```bash
python analyze_posts.py
```

Prints top hashtags, CTA analysis, time-based engagement patterns. Outputs visuals (e.g. engagement vs word count).

### 6. Run the Streamlit App

```bash
streamlit run app.py
```

Generates AI posts, predicts engagement, and accepts feedback.

## 📂 Files & Folders

| File/Folder                          | Purpose                                         |
| ------------------------------------- | ----------------------------------------------- |
| scrape_linkedin_posts.py             | Scrapes posts using Selenium                    |
| analyze_posts.py                     | Extracts trends & engagement patterns           |
| generate_post.py                     | Uses AI to generate post suggestions           |
| app.py                               | Streamlit app interface                        |
| engagement_predictor.py              | Predicts likes + comments from features (optional) |
| feedback_loop.py                     | Learns from user feedback (optional)           |
| topic_suggester.py                   | Suggests topics based on content trends (optional) |
| linkedin_posts.xlsx                  | Scraped dataset                                 |
| linkedin_posts_with_tone.xlsx        | Dataset enriched with tone classification       |
| average_tone_analyzer.py             | Analyzes average tone across posts             |
| selenium_profile/                    | Stores session cookies for login reuse         |

## 🔹 Engagement Prediction Model (Optional)

```bash
python engagement_predictor.py
```

Trains a model on features like word count, CTA usage, and emojis. Outputs `engagement_model.pkl`, auto-loaded by the Streamlit app for predictions.

## 💼 Notes

- If push fails due to large files, consider using Git LFS.
- Reposts are preserved with both user text and shared content.
- Scraper handles 'see more' expansions automatically.
- Some files like tone explanation and engagement-vs-word count graphs are saved in the directory.

## 📃 Example Row from Excel Output

| Profile     | Content | Hashtags | Likes | Comments | Type | CTA  | Emoji | URL |
|-------------|---------|----------|-------|----------|------|------|-------|-----|
| "Post"      | #ai #growth | 122 | 15 | text | Yes  | Yes   |       |

Feel free to fork, clone, or build on top of it! DM if you make something cool with it 🚀
