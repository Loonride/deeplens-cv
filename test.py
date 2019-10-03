
"""Test defines a number of test scenarios that are informative of how the API works
"""

from dlcv.struct import *
from dlcv.utils import *
from dlcv.dataflow.map import *
from dlcv.dataflow.agg import *
from dlcv.tracking.contour import *
from dlcv.tracking.event import *

import cv2
import numpy as np


#count the number of cars in the left lane
v = VideoStream('tcam.mp4', limit=1000)
region = Box(200,550,350,750)
pipeline = v[KeyPoints()][ActivityMetric('one', region)][Filter('one', [-0.25,-0.25,1,-0.25,-0.25],1.5, delay=10)]
print('Left', count(pipeline, ['one'], stats=True))


#count the number of cars in the right lane
v = VideoStream('tcam.mp4', limit=1000)
region = Box(500,550,650,750)
pipeline = v[KeyPoints()][ActivityMetric('one', region)][Filter('one', [-0.25,-0.25,1,-0.25,-0.25],1.5, delay=10)]
print('Right', count(pipeline, ['one'], stats=True))



#optimize car counting by pushing down a crop()
v = VideoStream('tcam.mp4', limit=1000)
region = Box(200,550,350,750)

k = KeyPoints()
k.setCrop(Box(100,450,450,950)) #notice it is slightly bigger than the actual region

pipeline = v[k][ActivityMetric('one', region)][Filter('one', [-0.25,-0.25,1,-0.25,-0.25],1.5, delay=10)]
print('Left', count(pipeline, ['one'], stats=True))


#Optimize car counting by sampling
v = VideoStream('tcam.mp4', limit=1000)
region = Box(200,550,350,750)
pipeline = v[Sample(0.5)][KeyPoints()][ActivityMetric('one', region)][Filter('one', [-0.25,-0.25,1,-0.25,-0.25],1.5, delay=10)]
print('Left', count(pipeline, ['one'], stats=True))


