from deeplens.media.youtube_tagger import YoutubeTagger
"""
I literally just want to make sure this iterator does what I think it does
I'm not going to worry about whether it's compatible with the storage manager
for now...
"""
youtubeTagger = YoutubeTagger('./train/AAI0cDTWFvE.mp4', './train/processed_yt_bb_detection_train.csv')
for frame in youtubeTagger:
    print(frame[0]['label'])

