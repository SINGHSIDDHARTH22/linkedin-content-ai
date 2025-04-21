import os
import time
import re
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def extract_hashtags(text):
    return " ".join(re.findall(r"#\w+", text))

def detect_cta(text):
    cta_phrases = ["what do you think", "comment below", "share your thoughts", "let me know"]
    return any(phrase in text.lower() for phrase in cta_phrases)

def scrape_linkedin_profile(base_url, scrolls=3, pause=0.8):
    profile_path = os.path.join(os.getcwd(), "selenium_profile")
    os.makedirs(profile_path, exist_ok=True)
    cookies_file = os.path.join(profile_path, "linkedin_cookies.json")

    opts = Options()
    opts.add_argument(f"--user-data-dir={profile_path}")
    opts.headless = False
    opts.set_capability("pageLoadStrategy", "eager")

    driver = webdriver.Chrome(options=opts)

    try:
        if os.path.exists(cookies_file):
            driver.get("https://www.linkedin.com")
            driver.implicitly_wait(5)
            with open(cookies_file, "r") as f:
                cookies = json.load(f)
            for c in cookies:
                driver.add_cookie(c)
        else:
            driver.get("https://www.linkedin.com")
            driver.implicitly_wait(30)
            print("🔐 Please log in manually...")
            while True:
                time.sleep(2)
                ck = driver.get_cookies()
                if any(c['name'] == 'li_at' for c in ck):
                    with open(cookies_file, "w") as f:
                        json.dump(ck, f, indent=2)
                    break

        shares_url = base_url.rstrip("/") + "/detail/recent-activity/shares/"
        driver.get(shares_url)
        time.sleep(2)

        for _ in range(scrolls):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause)

        posts = driver.find_elements(
            By.CSS_SELECTOR, "article, div.occludable-update, div.feed-shared-update"
        )
        print(f"🔍 Found {len(posts)} posts at {shares_url}")

        rows = []
        for p in posts:
            try:
                # Expand full post if needed
                try:
                    see_more_btn = p.find_element(By.CSS_SELECTOR, 'button[aria-label^="See more"]')
                    driver.execute_script("arguments[0].click();", see_more_btn)
                    time.sleep(0.3)
                except:
                    pass

                # ✅ Clean: Try to get only the post content block
                try:
                    content_block = p.find_element(By.CSS_SELECTOR, 'div.feed-shared-update-v2__description')
                    main_content = content_block.get_attribute("innerText").strip()
                except:
                    main_content = p.get_attribute("innerText").strip()

                if not main_content:
                    continue

                # Check for reposted/shared content
                try:
                    shared_block = p.find_element(By.CSS_SELECTOR, "div.update-components-shared-update-content")
                    shared_content = shared_block.get_attribute("innerText").strip()
                    full_content = main_content + "\n---\n[Repost Content]\n" + shared_content
                except:
                    full_content = main_content

                hashtags = extract_hashtags(full_content)
                word_count = len(full_content.split())
                has_emoji = bool(re.search(r"[^\w\s,]", full_content))
                has_cta = detect_cta(full_content)

                try:
                    l = p.find_element(By.CSS_SELECTOR, "span.social-details-social-counts__reactions-count")
                    likes = int(re.sub(r"\D", "", l.text))
                except:
                    likes = 0

                try:
                    c = p.find_element(By.CSS_SELECTOR, "button.social-details-social-counts__comments")
                    comments = int(re.sub(r"\D", "", c.text))
                except:
                    comments = 0

                try:
                    t = p.find_element(By.CSS_SELECTOR,
                        "span.feed-shared-actor__sub-description > span.visually-hidden")
                    post_time = t.text
                except:
                    post_time = ""

                if p.find_elements(By.TAG_NAME, "img"):
                    post_type = "Image"
                elif p.find_elements(By.TAG_NAME, "video"):
                    post_type = "Video"
                elif "http" in full_content:
                    post_type = "Link"
                else:
                    post_type = "Text"

                rows.append([
                    base_url, full_content, hashtags,
                    likes, comments, post_time,
                    post_type, word_count, has_cta, has_emoji
                ])

                print(f"✅ Scraped post {len(rows)}: {word_count} words, {likes} likes, {comments} comments")

            except Exception as e:
                print("⚠️ Skipped post due to error:", e)

        return rows

    finally:
        driver.quit()


if __name__ == "__main__":
    profiles = [
        "https://www.linkedin.com/in/aarongolbin/",
        "https://www.linkedin.com/in/robertsch%C3%B6ne/",
        "https://www.linkedin.com/in/jaspar-carmichael-jack/"
    ]
    all_rows = []

    for prof in profiles:
        print(f"\n🚀 Starting scrape for: {prof}")
        start = time.time()
        rows = scrape_linkedin_profile(prof, scrolls=20, pause=2)
        duration = round(time.time() - start, 2)
        print(f"✅ Done: {len(rows)} posts scraped in {duration}s for {prof}")
        all_rows.extend(rows)

    with open("linkedin_posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "profile_url", "content", "hashtags",
            "likes", "comments", "post_time",
            "post_type", "word_count", "has_cta", "has_emoji"
        ])
        writer.writerows(all_rows)

    print(f"\n📦 All done! Total posts saved: {len(all_rows)}")
