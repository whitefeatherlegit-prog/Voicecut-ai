
import json
import os
import subprocess

import cv2
from faster_whisper import WhisperModel
from scenedetect import open_video, SceneManager
from scenedetect.detectors import ContentDetector


def get_scenes(video_path):
    video = open_video(video_path)
    manager = SceneManager()
    manager.add_detector(ContentDetector(threshold=27.0))
    manager.detect_scenes(video)

    scenes = []

    for start, end in manager.get_scene_list():
        scenes.append({
            "start": start.get_seconds(),
            "end": end.get_seconds()
        })

    return scenes


def transcribe_voice(audio_path):
    model = WhisperModel(
        "tiny",
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        audio_path,
        word_timestamps=True
    )

    transcript = []

    for segment in segments:
        transcript.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })

    return transcript


def create_edit_plan(gameplay_path, voice_path, mode):
    scenes = get_scenes(gameplay_path)
    narration = transcribe_voice(voice_path)

    if not scenes:
        raise ValueError("No gameplay scenes detected.")

    plan = {
        "mode": mode,
        "scenes": scenes,
        "narration": narration,
        "status": "analysis_complete"
    }

    if mode == "Original Gameplay Mode":
        plan["editing_order"] = list(range(len(scenes)))

    elif mode == "Rearrange Mode":
        plan["editing_order"] = list(range(len(scenes)))

    else:
        plan["editing_order"] = list(range(len(scenes)))

    return plan


def save_edit_plan(plan, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(plan, file, indent=2, ensure_ascii=False)

    return output_path
  
