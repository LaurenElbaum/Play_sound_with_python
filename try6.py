#Assignment number 0
#Nmae: Lauren Elbaum
#Date: Sept. 2 2018
#OS: macOS High Sierra Hardware:MacBook Pro 2 GHz Intel Core i5
#Python version:3.4.4
#Due Sunday at 11:55pm

#Record sound from exernal microphones


import sounddevice as sd
#sounddevice.rec(frames=None, samplerate=None, channels=None, dtype=None, out=None, mapping=None, blocking=False, **kwargs)

#from here down I copied this from the internet here: https://gist.github.com/mabdrabo/8678538
import pyaudio
import wave
from pygame import mixer

 
FORMAT = pyaudio.paInt16
CHANNELS = 2 # I changed the channels to 1, then back to 2 so it would work with pygame
RATE = 44100 # I could change the rate to 22050? But I think it works better at 44100.
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "lauren_recording5.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

import soundfile as sf
sig, samplerate = sf.read('lauren_recording5.wav')

'''
#I made this code:
#wave.open("lauren_recording4.wav", mode=rb)
mixer.init()
mixer.music.load("lauren_recording4.wav")
mixer.music.play(loops=0, start=0.0)
sd.play(myarray, RATE)
'''

#from playsound import playsound
#playsound('desktop/515/lauren_recording5.wav')

#this code is from http://code.activestate.com/recipes/579116-use-pyaudio-to-play-a-list-of-wav-files/
'''
import sys
import os.path
import time

CHUNK_SIZE = 1024

def play_wav(wav_filename, chunk_size=CHUNK_SIZE):
    '''
    #Play (on the attached system sound device) the WAV file
    #named wav_filename.
'''

    try:
        print( 'Trying to play file ' + wav_filename)
        wf = wave.open(wav_filename, 'rb')
    except IOError as ioe:
        sys.stderr.write('IOError on file ' + wav_filename + '\n' + \
        str(ioe) + '. Skipping.\n')
        return
    except EOFError as eofe:
        sys.stderr.write('EOFError on file ' + wav_filename + '\n' + \
        str(eofe) + '. Skipping.\n')
        return

    # Instantiate PyAudio.
    p = pyaudio.PyAudio()

    # Open stream.
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(chunk_size)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(chunk_size)

    # Stop stream.
    stream.stop_stream()
    stream.close()

    # Close PyAudio.
    p.terminate()

def usage():
    prog_name = os.path.basename(sys.argv[0])
    print ("Usage: {} filename.wav".format(prog_name))
    print ("or: {} -f wav_file_list.txt".format(prog_name))

def main():
    lsa = len(sys.argv)
    if lsa < 2:
        usage()
        sys.exit(1)
    elif lsa == 2:
        play_wav(sys.argv[1])
    else:
        if sys.argv[1] != '-f':
            usage()
            sys.exit(1)
        with open(sys.argv[2]) as wav_list_fil:
            for wav_filename in wav_list_fil:
                # Remove trailing newline.
                if wav_filename[-1] == '\n':
                    wav_filename = wav_filename[:-1]
                play_wav(wav_filename)
                time.sleep(3)

if __name__ == '__main__':
    main()
'''