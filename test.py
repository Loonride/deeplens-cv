from dlstorage.utils.benchmark import *
from dlstorage.utils.vdmsbench import *

<<<<<<< HEAD
<<<<<<< HEAD



f = FileSystemStorageManager(TestTagger(), 'videos')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
p = PerformanceTest(f, '/Users/sanjaykrishnan/Downloads/BigBuckBunny.mp4')
=======
p = PerformanceTest(f, 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')
<<<<<<< HEAD
>>>>>>> Updated to clean up and make clear installation directions.
p.getParaTenTenSec()
#p.runAll()
=======
#p.getParaTenTenSec()
p.runAll()
>>>>>>> Updated with some new error handling

=======
f.put('/Users/sanjaykrishnan/Downloads/BigBuckBunny.mp4', 'bunny')
print(f.get('bunny', TRUE, 60*30))
=======
=======
#<<<<<<< HEAD
>>>>>>> commented out merge notes
#f.put('BigBuckBunny.mp4', 'bunny')
#print(f.get('bunny', TRUE, 60*30))
<<<<<<< HEAD
>>>>>>> changed constants, directories, for Ubuntu
"""
>>>>>>> removed filesys test
=======
>>>>>>> Update test.py
vd = VDMSStorageManager(TestTagger())
vd.put('enter actual directory here', 'desired name')
print(vd.get('desired name', TRUE, 438))
<<<<<<< HEAD

=======
"""
#These tests are complete, which is why they are commented out
#p = PerformanceTest(f, 'f20sec.mp4')
#p.getParaTenTenSec()
#p.runAll()
<<<<<<< HEAD
=======
=======
>>>>>>> changed number of cores
#=======
#p = PerformanceTest(f, 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')
#p.getParaTenTenSec()
#p.runAll()
#>>>>>>> master
>>>>>>> commented out merge notes

=======
>>>>>>> removed unnecessary tests
vd = VDMSStorageManager(TestTagger())
p2 = VDMSPerfTest(vd, 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')
p2.runAll()
>>>>>>> changed constants, directories, for Ubuntu
