import cv2
import base64
import random

from flask import Flask, request, render_template, Markup
# creates a Flask application, named app
app = Flask(__name__)

@app.route("/")
def index():
    vidcap = cv2.VideoCapture('test.mp4')
    success, image = vidcap.read()

    html = "";
    count = 0
    while success:
        # cv2.imwrite("frames/frame%d.jpg" % count, image)
        ret, buff = cv2.imencode('.jpg', image)
        b64 = base64.b64encode(buff)
        success, image = vidcap.read()
        count += 1
        html += "<img src='data:image/jpg;base64," + b64.decode("utf-8") + "'>"

    return render_template('index.html', images=Markup(html), rand=random.randrange(100000))

# run the application
if __name__ == "__main__":
    app.run(debug=True)
