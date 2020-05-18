'''
    Name: Shameen Shetty
    ID: 1001429743
'''

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import soundfile as sf
from scipy.signal import spectrogram
import glob

'''
    Function: classifyMusic
    Parameters: None
    Returns: None
    Description: Our function reads the data of our test Song - testSong.wav - and finds its
    signature. Then it reads the signatures of all songs matching the format 'song-*.wav' and
    finds the one-norm of the diff between the 2 signatures ||(currentSong - testSong)||_1
    and then finds the closest 5 songs, and prints them out, as well as plots the spectrogram
    of the test song, and the 2 closest matching songs to the test song.
'''
def classifyMusic() :

    # Our test song that we are finding the most similar songs of, we read wav file and extract
    # the song data, and its sample rate. Then get the spectogram of it, find the max values within it
    # and find the frequencies corresponding to those values to get our signature for the test song.
    testSongname = "testSong.wav"
    test_songData, test_songSampleRate = sf.read(testSongname)
    test_songFreq, test_songTime, test_Sxx = spectrogram(test_songData, fs = test_songSampleRate, nperseg = test_songSampleRate//2)
    testSongSig = []

    testSong_listOfMaxVals = test_Sxx.max(axis = 0)
    for num in testSong_listOfMaxVals:
        x, y = np.where(test_Sxx == num)
        index = x[0]
        testSongSig.append(test_songFreq[index])    

    # Here we get the list of songs that match the condition of "song-*.wav"
    # meaning, the name of the file starts with 'song-', and could be anything
    # after the hypen, hence the "*". Finally we are searching for wav files, so
    # ".wav".

    listOfSongs = glob.glob('song-*.wav')
    freqSig = []
    oneNormList = []
        

    # In this for loop, we enumerate over the list of songs that match the format 'song-*.wav'
    # and for each song at index = i, we get their data and sample rate.
    # Then we get the spectrogram of the current song we are at (spectrogram func).
    # From Sxx, we get the list of max values, which is stored in listOfMaxVals 
    # and then we iterate over the numbers in that list, and use np.where to find the
    # index of that num.
    # finally for freqSig[i].append(songFreq[index]) we find the freq at that index
    # (songFreq[index]) and store it into our frequency signature list - freqSig.append()
    for i, song in enumerate(listOfSongs):
        songData, songSampleRate = sf.read(song)
        songFreq, songTime, Sxx = spectrogram(songData, fs = songSampleRate, nperseg = songSampleRate//2)

        listOfMaxVals = Sxx.max(axis = 0)

        freqSig.append([])
        for num in listOfMaxVals:
            x, y = np.where(Sxx == num)
            index = x[0]
            freqSig[i].append(songFreq[index])
        
        # Getting the one norm for the distance between the frequency signature for the song
        # at index = i and the test song signature.
        oneNorm = np.linalg.norm(np.array(freqSig[i]) - np.array(testSongSig), ord = 1)
        
        # Our infomation list, stores the current index i, current song name and the current norm
        # We will use this to find the norms and the song-names later
        info_list = [i, listOfSongs[i], oneNorm]
        oneNormList.append(info_list)
    
    # closestMatchInfo will store the info of the songs that most closely match our test song
    closestMatchInfo = []
    
    # We need to find the 5 songs closest to the test song, hence we use 'for i in range(5)'
    # minIndex stores the index of the song closest to test song
    for i in range(5):
        minIndex = 0

        # normList stores the norm of the songs
        normList = []
        for i, info in enumerate(oneNormList):
            norm = oneNormList[i][2]
            normList.append(norm)
    
            # we find min of the norms, which gives the song closest to the test song
            minimum = np.min(normList)

            index = np.where(normList == minimum)
            minIndex = index[0][0]

        # Here, once we have found the index of the song, minIndex, we
        # find the information of that song (oneNormList[minIndex]) and store
        # it in var info, and from that var, we get the norm result and the name
        # of the song, and append those 2 values as a list into our list of
        # closest matches (closestMatchInfo)
        info = oneNormList[minIndex]
        normResult = info[2]
        songName = info[1]
        closestMatchInfo.append([normResult, songName])

        # Here we remove that song from the oneNormList, because we have already stored
        # it, and we want to find the next smallest norm, which we can do by removing
        # the smallest norm, and then running min() again to find the next smallest.
        # We do this 5 times (range(5)) to get the list of the 5 smallest norms, which
        # are the songs closest to the test song.
        oneNormList.remove(info)
    
    # Finally once we have gathered the 5 closest songs to our test song, we
    # print them.
    for i, info in enumerate(closestMatchInfo):
        print(f"{int(info[0])}  {info[1]}")

    # Now we need to plot the test song, and the 2 closest songs to it.
    # Hence we create a list called songNames, and first store the name of the test song
    # and then the name of the song closest to it, and the name of the 2nd closest song.
    # (note, we are using closestMatchInfo[0][1] and then CMI[1][1] because our min() func
    # gives the val of the closest song which is the first to be stored in CMI, hence the 1st closest
    # match is at index = 0, the 2nd closest song is at index = 1, etc. We use [n][1] because
    # the name of the (n-1)th song is the 2nd val)
    songNames = []
    songNames.append(testSongname)
    songNames.append(closestMatchInfo[0][1])
    songNames.append(closestMatchInfo[1][1])

    # Finally we read the song and get the data and fs
    # then we need to plot each song in its own separate window, hence we use
    # plt.figure() which creates a new window.
    # Then we plot the values using plt.specgram(x, fs)
    # and then title that plot using the var info, which is the song name
    for info in songNames:
        data, fs = sf.read(info)
        plt.figure()
        plt.specgram(data, Fs=fs)
        plt.title(info)
    plt.show()


###################  main  ###################
if __name__ == "__main__" :
    classifyMusic()
