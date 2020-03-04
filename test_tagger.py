from deeplens.full_manager.full_video_processing import CropSplitter
from deeplens.struct import *
from deeplens.tracking.background import FixedCameraBGFGSegmenter
from deeplens.utils import *
from deeplens.dataflow.map import *
from deeplens.full_manager.full_manager import *
from deeplens.utils.testing_utils import *
import os
import shutil

if os.path.exists('./videos'):
    shutil.rmtree('./videos')
manager = FullStorageManager(CustomTagger(FixedCameraBGFGSegmenter().segment, batch_size=5), CropSplitter(), 'videos')
manager.put_many(['./cut2.mp4', './cut3.mp4'], ['test', 'test_2'], args={'encoding': XVID, 'size': -1, 'sample': 1.0, 'offset': 0, 'limit': 100, 'batch_size': 100, 'num_processes': 4})
