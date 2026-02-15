import streamlit as st
import time
import random

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Project V: Top Secret",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- SESSION STATE MANAGEMENT ---
if 'decrypted' not in st.session_state:
    st.session_state.decrypted = False
if 'name' not in st.session_state:
    st.session_state.name = "Guest"

# --- CUSTOM CSS ---
st.markdown("""
<style>
/* Hacker Mode Styles */
.hacker-text {
    font-family: 'Courier New', monospace;
    color: #00ff41;
}

/* Romantic Mode Styles */
.romantic-header {
    color: #ff4b4b;
    font-family: 'Comic Sans MS', 'Brush Script MT', cursive;
    text-align: center;
    font-size: 3em;
    animation: fadeIn 2s;
    text-shadow: 2px 2px 4px #000000;
}

.heart-beat {
    font-size: 100px;
    text-align: center;
    animation: heartbeat 1.5s infinite;
}

@keyframes heartbeat {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}

@keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}

/* Custom Button Styling */
div.stButton > button {
    width: 100%;
    border-radius: 10px;
    transition: all 0.3s ease 0s;
}

/* Specific button colors would need more specific selectors or Streamlit's theme config,
   but we'll rely on default theme + emoji for now to keep it simple and robust. */

</style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---
def typewriter_effect(text, speed=0.05):
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"### {displayed_text}▌")
        time.sleep(speed)
    placeholder.markdown(f"### {text}")

# --- APP LOGIC ---

if not st.session_state.decrypted:
    # --- HACKER INTERFACE ---
    st.markdown("<h1 style='text-align: center; color: #00ff41;'>🔒 RESTRICTED ACCESS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00ff41; font-family: monospace;'>ENTER AUTHORIZATION CODE TO PROCEED</p>", unsafe_allow_html=True)

    st.write("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        name_input = st.text_input("CODENAME:", placeholder="Enter your name...", key="name_input")

        if st.button("DECRYPT PROTOCOL 🔓"):
            if name_input:
                progress_bar = st.progress(0, text="Initializing...")

                steps = [
                    "Bypassing firewall...",
                    "Accessing mainframe...",
                    "Decrypting heart files...",
                    "Compiling love variables...",
                    "Access Granted."
                ]

                for i, step in enumerate(steps):
                    # Simulate work
                    time.sleep(random.uniform(0.5, 1.0))
                    progress = int((i + 1) / len(steps) * 100)
                    progress_bar.progress(progress, text=step)

                st.success(f"WELCOME, AGENT {name_input.upper()}")
                time.sleep(1)
                st.session_state.name = name_input
                st.session_state.decrypted = True
                st.rerun()
            else:
                st.error("ACCESS DENIED. IDENTIFY YOURSELF.")

else:
    # --- ROMANTIC INTERFACE ---

    # Attempt to change background color via trickery (works in some browsers/versions)
    # If not, the content itself will carry the theme.

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
         st.markdown(f"<div class='heart-beat'>❤️</div>", unsafe_allow_html=True)

    st.markdown(f"<h1 class='romantic-header'>Happy Valentine's Day, {st.session_state.name}!</h1>", unsafe_allow_html=True)

    st.write("---")

    # Message Content
    message = f"""
    Dear {st.session_state.name},

    Programming is like love. It's complicated, full of bugs,
    but when it works, it's absolutely beautiful.

    Just like code needs a compiler, my heart needs you to be complete.

    So I have one question for you...
    """

    # Only type it out once to avoid annoyance on rerun, or use a flag.
    # For now, let's just show it. Typewriter can be slow for repeated views.
    st.info(message)

    st.write("")
    st.markdown("### Will you be my Valentine? 🥺")

    col_yes, col_no = st.columns(2)

    with col_yes:
        if st.button("YES! 😍", key="yes_btn"):
            st.session_state.accepted = True

    with col_no:
        if st.button("NO... 😢", key="no_btn"):
            st.toast("Error 404: Rejection Not Found! Try the other button. 😉", icon="🚫")

    if st.session_state.get('accepted'):
        st.balloons()
        st.success("YAY! 🎉 You just made my infinite loop complete!")
        st.markdown("### ❤️❤️❤️")

    st.write("---")

    # --- LOVE CALCULATOR ---
    st.markdown("### 💘 Love Compatibility Calculator")

    with st.expander("Calculate Our Compatibility"):
        c1, c2 = st.columns(2)
        with c1:
            me = st.text_input("My Name", value=st.session_state.name)
        with c2:
            crush = st.text_input("Crush's Name")

        if st.button("Calculate Result"):
            if crush:
                with st.spinner("Running complex algorithms..."):
                    time.sleep(2)
                    score = random.randint(90, 100) # Biased algorithm ;)
                    st.metric(label="Compatibility Score", value=f"{score}%", delta="Perfect Match!")
                    st.balloons()
            else:
                st.warning("You need a crush for this to work!")
