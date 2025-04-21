
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

## Example Results

![image](https://github.com/user-attachments/assets/ed5de4eb-3327-4e72-8f60-7129e3c556eb)


## Variation 1:

🚀 Your Next Chapter Awaits! 💡

I still remember the days when I was job searching and feeling stuck. I applied to dozens of positions, only to face rejection after rejection. But one day, it hit me: **I wasn't looking for a job, I was looking for a purpose**. 🤯

That mindset shift changed everything. I started focusing on what I wanted to achieve in my career, rather than just accepting any role. I began to invest in myself, learning new skills and networking with people who shared my passion.

The result? A fulfilling career that's taken me on a journey of growth, entrepreneurship, and innovation 🌟.

If you're in a similar spot, I urge you to reflect on what drives you. What's your purpose? What problems do you want to solve? What impact do you want to make?

What's your experience? Have you faced similar struggles or successes? Share with us in the comments below 👇 #founderlife #growthmindset #careertransformation



## Variation 2:

🚀 "The Unstoppable Force of Passion"

As a founder, I've seen countless job aspirants walk into my office, filled with enthusiasm and determination. But what sets the truly remarkable ones apart? It's not just their skills or experience - it's their unrelenting passion to create a meaningful impact. 💡

I remember when I was starting out, I was convinced that success was solely dependent on talent and hard work. But it wasn't until I met someone who was willing to take risks, face failures, and learn from them that I realized the power of passion. It was a wake-up call that changed the course of my journey.

So, to all the job aspirants out there, I urge you to tap into your inner drive and let your passion be the fuel that propels you forward. Don't be afraid to take the leap, and trust that your uniqueness will be your greatest strength. 💪

What's your experience? Have you ever let passion guide your decisions? Share your story in the comments below! 👇

#founderlife #growthmindset #passiondriven



## Variation 3:
🚀 "The Spark That Ignites Your Career" 🚀

As founders, we've all been there - trying to motivate job aspirants to take the leap and pursue their dreams. But what drives us to take that first step? 💡

For me, it was a conversation with a mentor who asked me: "What's the worst that could happen if you fail?" That simple question sparked a fire within me to take the risk and go for it. Today, I'm living proof that taking the leap can lead to incredible growth and success.

As founders, we have the power to inspire and motivate others to do the same. So, what's your experience? What sparked your passion for your current career path? Share your story and let's inspire others to take the leap and pursue their dreams! 💥

Comment below 👇

#founderlife #growthmindset #motivation
