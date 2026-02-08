import streamlit as st
import time

# --- PAGE CONFIG (Hacker Title) ---
st.set_page_config(
    page_title="CareerOnFire HQ | The Lazy Engineer",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (Terminal/Hacker Theme) ---
st.markdown("""
    <style>
    /* Main Background Black */
    .stApp {
        background-color: #0e1117;
        color: #00ff41; /* Hacker Green */
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Hide Streamlit Header & Footer */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom Buttons (Neon Style) */
    .stButton>button {
        background-color: #000000;
        color: #00ff41;
        border: 1px solid #00ff41;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #00ff41;
        color: #000000;
        box-shadow: 0 0 10px #00ff41;
    }
    
    /* Card Container */
    .css-1r6slb0 {
        border: 1px solid #333;
        padding: 20px;
        border-radius: 10px;
        background-color: #161b22;
    }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION (Typing Effect) ---
def type_text(text):
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f"## {typed_text}█")
        time.sleep(0.05)
    placeholder.markdown(f"## {text}")

st.markdown("### > SYSTEM STATUS: ONLINE 🟢")
st.markdown("---")

# Intro
st.title("🔥 CareerOnFire HQ")
st.markdown("**Identity:** The Lazy Engineer | **Mission:** Automate Your Career")
st.markdown("> *Why work hard when you can work smart? Use my code to hack the hiring system.*")

st.write("") # Spacer

# --- THE ROI CALCULATOR (Fitur Cerdas) ---
st.markdown("### 🧮 The 'Lazy Logic' Calculator")
st.info("Calculate how much time you waste applying manually.")

hours_per_app = st.slider("Hours spent per application (Cover Letter + Tweak):", 0.5, 3.0, 1.0)
apps_per_week = st.slider("Applications per week:", 5, 50, 20)

saved_hours = (hours_per_app * apps_per_week) * 0.9 # Assume 90% savings
st.markdown(f"""
    <div style="border: 1px dashed #00ff41; padding: 15px; text-align: center;">
        <h3 style="color: #ffffff;">You are wasting {int(hours_per_app * apps_per_week)} hours/week.</h3>
        <h2 style="color: #00ff41;">My Tools Save You: {int(saved_hours)} HOURS/WEEK</h2>
        <p>That's {int(saved_hours * 4)} hours/month you could use to learn code or sleep.</p>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# --- THE ARSENAL (Main Products) ---
st.markdown("### 🛠️ The Arsenal (Tools)")

col1, col2 = st.columns(2)

with col1:
    st.image("https://img.icons8.com/fluency/96/console.png", width=50) # Icon Terminal
    st.markdown("#### 🎯 ATS Keyword Hacker")
    st.caption("Scan your resume against JD using Python logic. Beat the bot.")
    st.link_button("LAUNCH TOOL (FREE) 🚀", "https://lazy-career-hack.streamlit.app/")

with col2:
    st.image("https://img.icons8.com/fluency/96/document.png", width=50) # Icon Document
    st.markdown("#### 📄 Lazy Cover Letter")
    st.caption("Copy-paste templates that tricked 50+ companies.")
    st.link_button("GET THE PACK 📦", "https://careeronfire.gumroad.com/") 
    # Nanti ganti link di atas jadi link produk spesifik biar konversi naik!

st.write("---")

# --- ANTI-HUSTLE MANIFESTO ---
st.markdown("""
    <div style="background-color: #0f2e15; padding: 15px; border-left: 5px solid #00ff41;">
        <h4>📜 The Anti-Hustle Manifesto</h4>
        <p>"Applying to 100 jobs is desperation. Applying to 10 jobs with perfect optimization is Strategy.</p>
        <p>Stop grinding. Start engineering your career."</p>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# --- ENCRYPTED COMMS (Socials) ---
st.markdown("### 📡 Encrypted Channels")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.link_button("🐦 X (Intel)", "https://x.com/PrincessaB62827")
with c2:
    st.link_button("👽 Reddit", "https://www.reddit.com/user/Career_On_Fire/")
with c3:
    st.link_button("📌 Pinterest", "https://pin.it/2VgWRRc8t")
with c4:
    st.link_button("📝 Medium", "https://medium.com/@lazy-career-hack")

st.write("")
st.caption("© 2026 CareerOnFire. Built with Python & Coffee. 🇮🇩")
