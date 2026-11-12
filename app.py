

import streamlit as st

st.set_page_config(
    page_title="VoiceCut AI",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 VoiceCut AI")
st.subheader("AI Free Fire Voiceover Video Editor")

st.markdown("""
Upload your Free Fire gameplay and voiceover.
Let AI help you create an engaging gaming video.
""")

st.divider()

st.header("1. Upload your files")

gameplay = st.file_uploader(
    "Upload Free Fire Gameplay",
    type=["mp4", "mov", "mkv"]
)

voiceover = st.file_uploader(
    "Upload Voiceover Audio",
    type=["mp3", "wav", "m4a", "mp4"]
)

st.divider()

st.header("2. Choose Editing Mode")

mode = st.radio(
    "Select your editing mode",
    [
        "Rearrange Mode",
        "Original Gameplay Mode",
        "Both Modes"
    ]
)

st.write("Selected mode:", mode)

st.divider()

st.header("3. Export Settings")

quality = st.selectbox(
    "Video Quality",
    ["720p", "1080p", "4K"]
)

if st.button("🚀 Start AI Editing"):
    if gameplay is None or voiceover is None:
        st.error("Please upload both gameplay and voiceover.")
    else:
        st.success("Files received! AI editing pipeline will be connected next.")

st.caption("VoiceCut AI | Built for Free Fire creators")
