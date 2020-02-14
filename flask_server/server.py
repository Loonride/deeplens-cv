import cv2
import base64
import random
import sys
sys.path.append('../')

from deeplens.struct import *
from deeplens.utils import *
from deeplens.dataflow.map import *
from deeplens.simple_manager.manager import *
from deeplens.utils.testing_utils import *

from flask import Flask, request, render_template, Markup, abort

# from flask_uploads import (UploadSet, configure_uploads, IMAGES,
#                               UploadNotAllowed)

# creates a Flask application, named app
app = Flask(__name__)

class TestFilter(object):
    def filter(self, header_data):
        return True

manager = SimpleStorageManager(TestTagger(), 'test_store')
manager.put('test.mp4', 'test', args={'encoding': XVID, 'size': -1, 'sample': 1.0, 'offset': 0, 'limit': 100})

@app.route("/")
def index():
    return render_template('index.html', rand=random.randrange(100000))

@app.route("/frames")
def frames():
    name = request.args.get('name')
    try:
        res = manager.get(name, TestFilter(), 100)
        vid = res[0]
        html = "";
        for frame in vid:
            ret, buff = cv2.imencode('.jpg', frame['data'])
            b64 = base64.b64encode(buff)
            html += "<img src='data:image/jpg;base64," + b64.decode("utf-8") + "'>"
        return Markup(html)
    except:
        abort(404)


# run the application
if __name__ == "__main__":
    app.run(debug=True)
