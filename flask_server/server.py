import cv2
import base64
import random
import os
import sys
sys.path.append('../')

from deeplens.struct import *
from deeplens.utils import *
from deeplens.dataflow.map import *
from deeplens.simple_manager.manager import *
from deeplens.utils.testing_utils import *

from flask import Flask, request, render_template, Markup, abort
from flask_uploads import UploadSet, configure_uploads

# creates a Flask application, named app
app = Flask(__name__)

try:
    os.mkdir('test_store')
except:
    pass

app.config['UPLOADED_VIDEOS_DEST'] = 'videos'
videos = UploadSet('videos', ['mp4'])
configure_uploads(app, videos)

args = {'encoding': XVID, 'sample': 1.0, 'offset': 0, 'limit': 1000, 'batch_size': 1000}

manager = SimpleStorageManager('test_store')

def get_frames(name):
    try:
        def filter(header_data):
            return True
        res = manager.get(name, filter, args)
        vid = res[0]
        html = "";
        for frame in vid:
            print(getFrameNumber(frame))
            ret, buff = cv2.imencode('.jpg', getFrameData(frame))
            b64 = base64.b64encode(buff)
            html += "<img src='data:image/jpg;base64," + b64.decode("utf-8") + "'>"
        return Markup(html)
    except:
        return ''
        # abort(404)

@app.route("/")
def index():
    return render_template('index.html', rand=random.randrange(100000))

@app.route("/frames")
def frames():
    name = request.args.get('name')
    return get_frames(name)

@app.route('/upload', methods=['POST'])
def upload():
    filename = videos.save(request.files['file'])
    manager.put('videos/' + filename, filename, args)
    return get_frames(filename)
