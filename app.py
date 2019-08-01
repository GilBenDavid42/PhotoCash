from flask import Flask, render_template, Response
import cv2
import sys
import numpy


app = Flask(__name__)


# Route for main page
@app.route('/')
def index():
    return render_template("index.html")


def get_frame():
    camera_port = 0
    # Making a web cam object
    camera = cv2.VideoCapture(camera_port)

    while True:
        retval, im = camera.read()
        imgencode = cv2.imencode('.jpg',im)[1]
        stringData = imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n' + stringData + b'\r\n')
    del(camera)


@app.route('/frame')
def frame():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


# Run the flask server
if __name__ == '__main__':
    app.run()
