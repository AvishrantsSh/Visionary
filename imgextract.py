# A custom class for extracting image assets from videos
import cv2, os
from multiprocessing import Pool

class Extractor(object):
    def __init__(self, FRAME_SIZE = (64, 64), FRAME_SKIP = 10):
        self.size = FRAME_SIZE
        self.skip = FRAME_SKIP
        self.count = 0

    def extract(self, path, DIR = 'tmp'):
        folder = "./Data/" + DIR
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        cap = cv2.VideoCapture(path)   # capturing the video from the given path
        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, self.count*self.skip)
            frame = []
            ret, frame = cap.read()
            if ret is False:
                break
            
            frame = cv2.resize(frame, self.size)
            fname = '%s/%d.jpeg' % (folder, self.count)
            cv2.imwrite(fname, frame)
            self.count += 1
        # cap.release()