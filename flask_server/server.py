import cv2
import base64
import random
import os
import sys
sys.path.append('../')

from deeplens.struct import *
from deeplens.utils import *
from deeplens.dataflow.map import *
from deeplens.full_manager.full_manager import *
from deeplens.full_manager.condition import Condition
from deeplens.full_manager.full_video_processing import CropSplitter
from deeplens.tracking.background import FixedCameraBGFGSegmenter

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

def do_filter(conn, video_name):
    c = conn.cursor()
    c.execute("SELECT clip_id FROM clip WHERE video_name = '%s'" % (video_name))
    res = c.fetchall()
    print(res[0])
    return [cl[0] for cl in res]

args = {'encoding': XVID, 'size': -1, 'sample': 1.0, 'offset': 0, 'limit': 1000, 'batch_size': 500}

# change the 3 parameters that get passed into the BGFG segmenter based on user input
manager = FullStorageManager(CustomTagger(FixedCameraBGFGSegmenter().segment, batch_size=500), CropSplitter(), 'test_store')

def get_frames(name):
    try:
        def filter(header_data):
            return True
        res = manager.get(name, Condition(label='foreground', custom_filter=do_filter))
        vid = res[0]
        html = "";
        for frame in vid:
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
    manager.put('videos/' + filename, filename, args, False, False)
    return get_frames(filename)

@app.route("/names")
def names():
    conn = manager.conn
    cursor = conn.cursor()
    cursor.execute("SELECT video_name FROM clip")
    select_result = cursor.fetchall()
    names = set([cl[0] for cl in select_result])
    print(names)
    return ""
