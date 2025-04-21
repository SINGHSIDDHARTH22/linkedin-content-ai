import streamlit as st
from generate_post import generate_post

# ---------- UI: Main App ----------
st.title("📢 LinkedIn Post Generator")

# User inputs
topic = st.text_input("Enter a topic or idea:")
hashtags_input = st.text_input("Enter hashtags (comma-separated):", "#founderlife,#growthmindset")
hashtags = [tag.strip() for tag in hashtags_input.split(",") if tag]

tone = st.selectbox("Choose tone", ["storytelling", "listicle", "opinion", "professional","insightful","casual", "inspirational", "funny"])
style = st.selectbox("Choose style", ["inspirational", "insightful", "casual", "funny", "suggestive"])

# Generate Posts
if topic and st.button("Generate 3 Post Variations"):
    st.subheader("🔄 AI-generated Posts")

    for i in range(3):
        post = generate_post(topic, tone=tone, style=style, hashtags=hashtags)

        st.markdown(f"#### ✏️ Variation {i+1}")
        st.text_area(label="", value=post, height=200, key=f"post_{i}")
