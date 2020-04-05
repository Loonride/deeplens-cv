import cv2
import base64
import random
import os
import sys
import shutil
from urllib.parse import quote
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

store_dir = 'test_store'
videos_dir = 'videos'

def clean_up():
    if os.path.exists(store_dir):
        shutil.rmtree(store_dir)
    if os.path.exists(videos_dir):
        shutil.rmtree(videos_dir)

if not os.path.exists(store_dir):
    os.mkdir(store_dir)
if not os.path.exists(videos_dir):
    os.mkdir(videos_dir)

app.config['UPLOADED_VIDEOS_DEST'] = videos_dir
videos = UploadSet('videos', ['mp4'])
configure_uploads(app, videos)

def do_filter(conn, video_name):
    c = conn.cursor()
    c.execute("SELECT clip_id FROM clip WHERE video_name = '%s'" % (video_name))
    res = c.fetchall()
    print(res[0])
    return [cl[0] for cl in res]

args = {'frame_rate': 30, 'encoding': XVID, 'limit': 1000, 'sample': 1.0, 'offset': 0, 'batch_size': 500, 'num_processes': 4, 'background_scale': 1}

# change the 3 parameters that get passed into the BGFG segmenter based on user input
manager = FullStorageManager(CustomTagger(FixedCameraBGFGSegmenter().segment, batch_size=500), CropSplitter(), 'test_store', reuse_conn=False)

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

def get_clip_names():
    conn = manager.create_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT video_name FROM clip")
    select_result = cursor.fetchall()
    names = set([cl[0] for cl in select_result])
    manager.remove_conn(conn)
    return names

def create_frames_json(name):
    frames = get_frames(name)
    return '{"imgs":"' + quote(frames) + '","name":"' + name + '"}'

@app.route("/")
def index():
    return render_template('index.html', rand=random.randrange(100000))

@app.route("/frames")
def frames():
    name = request.args.get('name')
    return create_frames_json(name)

@app.route('/upload', methods=['POST'])
def upload():
    filename = videos.save(request.files['file'])
    manager.put('videos/' + filename, filename, args, False, False)
    return create_frames_json(filename)

@app.route("/clips")
def clips():
    names = get_clip_names()
    res = ""
    for name in names:
        res += name + ","
    return res
