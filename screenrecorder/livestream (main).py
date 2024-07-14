import cv2
import numpy as np
from flask import Flask, Response
import mss
import mss.tools
import time

app = Flask(__name__)

# Set up the screen capture
with mss.mss() as sct:
    monitor = sct.monitors[1]  # Use the primary screen (index 1) for all screens use a "0"
    width, height = monitor["width"], monitor["height"]

@app.route('/screen')
def screen():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen():
    with mss.mss() as sct:
        while True:
            start_time = time.time()
            img = sct.grab(monitor)
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)
            ret, imgencode = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + imgencode.tobytes() + b'\r\n')
            # Calculate the sleep time to achieve 60 FPS
            sleep_time = max(0, 1/60 - (time.time() - start_time)) #change the 60 to 30 for less fps but better performance
            time.sleep(sleep_time)

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
