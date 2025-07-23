import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write


class Recorder:
    def __init__(self, device_index = 8, fs= 44100, output_file="output.wav"):
        self.output_file = output_file
        self.device_index = device_index
        self.fs = fs
        self.is_recording = False
        self.stream = None
        self.recording = []

    def callback(self, indata, frames, time_info, status):
        if self.is_recording:
            self.recording.append((indata.copy()))

    def record_start(self, something):
        if not self.is_recording:
            self.is_recording = True
            self.recording = []
            self.stream = sd.InputStream(
                callback=self.callback,
                device= self.device_index,
                channels=1,
                samplerate= self.fs)
            self.stream.start()


    def record_stop(self, something):
        if self.is_recording:
            self.is_recording = False
            self.stream.close()
            audio = np.concatenate(self.recording, axis=0)
            write(self.output_file, self.fs, audio)

    def cleanup(self):
        if self.stream is not None:
            self.stream.close()




