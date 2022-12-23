import time
class Song:
    def __init__(self, bpm,length):
        self._bpm=bpm
        self._length=length
        self._stop_time=time.time()+length
    
    def single_loop(self):
        print("not implemented")
    def play(self):
        start_time = time.time()
        sleep_time=60/self._bpm
        while time.time() <self._stop_time:
            self.single_loop()
            time.sleep(sleep_time)

        
