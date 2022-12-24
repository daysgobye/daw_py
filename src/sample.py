from collections.abc import Sequence
from pytube import YouTube
import os
import  vlc


class Source_Sample:
    def __init__(self,name:str,url:str,start:float,end:float):
        self.name=name
        self.url=url
        self.start=start
        self.end=end
        self.download()
        self.play()
    def download(self):
        yt = YouTube(self.url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path="./samples")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        try:
            os.rename(out_file, new_file)
        except FileExistsError:
            print("error")
            print(FileExistsError)
        self.path=new_file
    def play(self):
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(self.path)
        # Media.get_mrl()
        Media.add_option(f'start-time={self.start}')
        Media.add_option(f'stop-time={self.end}')
        player.set_media(Media)
        # player = vlc.MediaPlayer(self.path)
        
        player.play()
        pass


    

# class Sample:
#     def __init__(self,source_samples:Sequence[Source_Sample]):