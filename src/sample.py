from collections.abc import Sequence
from pytube import YouTube
import os


class Source_Sample:
    def __init__(self,name:str,url:str,start:float,end:float):
        self.name=name
        self.url=url
        self.start=start
        self.end=end
        self.download()
    def download(self):
        yt = YouTube(self.url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path="./samples")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        self.path=new_file
    def play(self):
        pass


    

# class Sample:
#     def __init__(self,source_samples:Sequence[Source_Sample]):