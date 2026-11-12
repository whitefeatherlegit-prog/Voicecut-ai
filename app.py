import streamlit as st
import tempfile
import os
import json

from voicecut.pipeline import create_edit_plan

st.set_page_config(
    page_title="VoiceCut AI",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 VoiceCut AI")
st.subheader("AI Free Fire Voiceover Video Editor")

st.write(
    "Upload gameplay and voiceover to analyse "
    "your video with AI."
)

st.divider()

st.header("1. Upload files")

gameplay = st.file_uploader(
    "Free Fire Gameplay",
    type=["mp4", "mov", "mkv"]
)

voiceover = st.file_uploader(
    "Voiceover Audio",
    type=["mp3", "wav", "m4a", "mp4"]
)

st.divider()

st.header("2. Select editing mode")

mode = st.radio(
    "Choose mode",
    [
        "Rearrange Mode",
        "Original Gameplay Mode",
        "Both Modes"
    ]
)

st.divider()

st.header("3. Export preference")

quality = st.selectbox(
    "Video Quality",
    ["720p", "1080p", "4K"]
)

if st.button("🚀 Analyse my video", type="primary"):

    if gameplay is None or voiceover is None:
        st.error("Please upload both files.")

    else:
        try:
            with st.spinner(
                "AI is analysing your gameplay and voiceover..."
            ):
                with tempfile.TemporaryDirectory() as temp_dir:

                    video_path = os.path.join(
                        temp_dir, "gameplay.mp4"
                    )

                    audio_path = os.path.join(
                        temp_dir, "voiceover" +
                        os.path.splitext(voiceover.name)[1]
                    )

                    with open(video_path, "wb") as f:
                        f.write(gameplay.getbuffer())

                    with open(audio_path, "wb") as f:
                        f.write(voiceover.getbuffer())

                    plan = create_edit_plan(
                        video_path,
                        audio_path,
                        mode
                    )

                    st.success("Analysis completed!")

                    st.subheader("Voiceover transcript")

                    for item in plan["narration"]:
                        st.write(
                            f'{item["start"]:.2f}s - '
                            f'{item["end"]:.2f}s: '
                            f'{item["text"]}'
                        )

                    st.subheader("Detected gameplay scenes")

                    st.write(
                        f'Total scenes detected: '
                        f'{len(plan["scenes"])}'
                    )

                    st.json(plan)

        except Exception as e:
            st.error(f"Processing error: {e}")

st.caption("VoiceCut AI | Development version")
