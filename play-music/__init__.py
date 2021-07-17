import simpleaudio as sa
from multiprocessing import Process
import numpy as np
sounds_playing = []
def loopAsync(filename):
    while True:
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()

def notLoopAsync(filename):
    try:
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except:
        raise Exception("play_music: Failed to play music")
def NumpyLoopAsync(a,b):
    while True:
        try:
            play_obj = sa.play_buffer(a, 1, 2, b)
            play_obj.wait_done()
        except:
            raise Exception("play_music: Failed to play music")
def NumpyNotLoopAsync(a,b):
    try:
        play_obj = sa.play_buffer(a, 1, 2, b)
        play_obj.wait_done()
    except:
        raise Exception("play_music: Failed to play music")
def playMusic(filename, loop=False, threaded=False):
    #if loop is true threaded is also true
    #if loop is not true and threaded is not true sound_id will not be returned
    if loop:
        if threaded:
            loopThread = Process(target=loopAsync, args=(filename,))
            sounds_playing.append(loopThread)
            loopThread.start()
            return loopThread
        else:
            loopNotThread = Process(target=loopAsync, args=(filename,))
            sounds_playing.append(loopNotThread)
            loopNotThread.start()
            while loopNotThread.is_alive():
                    pass
            sounds_playing.remove(loopNotThread)
    elif loop == False:
        if threaded:
            notLoopThread = Process(target=notLoopAsync, args=(filename,))
            sounds_playing.append(notLoopThread)
            notLoopThread.start()
            return notLoopThread
        else:
            notLoopNotThread = Process(target=notLoopAsync, args=(filename,))
            sounds_playing.append(notLoopNotThread)
            notLoopNotThread.start()
            while notLoopNotThread.is_alive():
                pass
            sounds_playing.remove(notLoopNotThread)
def playNormalizedNumpy(a,b, loop=False, threaded=False):
    #if loop is true threaded is also true
    #if loop is not true and threaded is not true sound_id will not be returned
    if loop:
        if threaded:
            loopThread = Process(target=NumpyLoopAsync, args=(a,b))
            sounds_playing.append(loopThread)
            loopThread.start()
            return loopThread
        else:
            loopNotThread = Process(target=NumpyLoopAsync, args=(a,b))
            sounds_playing.append(loopNotThread)
            loopNotThread.start()
            while loopNotThread.is_alive():
                    pass
            sounds_playing.remove(loopNotThread)
    elif loop == False:
        if threaded:
            notLoopThread = Process(target=NumpyNotLoopAsync, args=(a,b))
            sounds_playing.append(notLoopThread)
            notLoopThread.start()
            return notLoopThread
        else:
            notLoopNotThread = Process(target=NumpyNotLoopAsync, args=(a,b))
            sounds_playing.append(notLoopNotThread)
            notLoopNotThread.start()
            while notLoopNotThread.is_alive():
                pass
            sounds_playing.remove(notLoopNotThread)
def stopAllSounds():
    try:
        for i in sounds_playing:
            i.terminate()
            sounds_playing.remove(i)
    except:
        raise Exception("play_music: Process is invalid.")
def stopSpecificSound(process):
    try:
        process.terminate()
        sounds_playing.remove(process)
    except:
        raise Exception("play_music: Process is invalid.")
def stopSpecificSounds(process_list):
    try:
        for i in process_list:
            i.terminate()
            sounds_playing.remove(i)
    except:
        raise Exception("play_music: Process List is invalid.")