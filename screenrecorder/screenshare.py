import cv2
import numpy as np
from flask import Flask, Response
import dxcam

app = Flask(__name__)

# Create a DXCamera instance for the primary screen
camera = dxcam.create(device_idx=0, output_idx=0)

@app.route('/screen')
def screen():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen():
    while True:
        frame = camera.grab()
        if frame is not None and frame.size:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            ret, imgencode = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + imgencode.tobytes() + b'\r\n')
        else:
            continue

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
