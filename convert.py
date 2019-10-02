import os
import ffmpy
from ffmpy import FFmpeg


def main(path, framerate):
        for filename in os.listdir(path):
                if (filename.endswith(".mov") or filename.endswith(".wmv") or filename.endswith(".avi")):                        
                        try:
                            os.mkdir(filename[:-4])
                        os.chdir(path)
                        ff = FFmpeg(inputs={filename: None}, outputs={'..\\'+filename[:-4]+'\img%04d.png': ['-vf', 'fps='+str(framerate)]})
                        ff.run()
                        os.chdir('..') 
