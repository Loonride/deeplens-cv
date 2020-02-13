from deeplens.full_manager.full_video_processing import CropSplitter
from deeplens.struct import *
from deeplens.tracking.background import FixedCameraBGFGSegmenter
from deeplens.utils import *
from deeplens.dataflow.map import *
from deeplens.full_manager.full_manager import *
from deeplens.utils.testing_utils import *


manager = FullStorageManager(CustomTagger(FixedCameraBGFGSegmenter().segment), CropSplitter(), 'videos')
manager.put('cut2.mp4', 'test', args={'encoding': XVID, 'size': -1, 'sample': 1.0, 'offset': 0, 'limit': 100})
