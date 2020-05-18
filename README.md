# CSE-3313--HW09
This is the coding assignment for Homework 9 for CSE3313 (Introduction to Signal Processing). 


## Purpose
Learn to extract features from the spectrogram of an audio file.

### Process
* In the folder *All Songs* There are 64 songs provided from *song-bagpipe.wav* to *song-winds.wav*, along with *testSong.wav*. 
  - The 64 songs of the form *song-\*.wav*, these are the original songs that we will build a database of signatures from.
  - *testSong.wav* is a sample test file.
* We are using scipy function `spectrogram()` to analyze each song. `f, t, Sxx = spectrogram(x, fs=fs, nperseg=fs//2)` where
  - f is an m-element vector of the frequencies evaluated in the signal.
  - t is an n-element vector of the times at which the signal was evaluated.
  - Sxx is an m × n matrix of the amplitudes of each frequency/time pair.

* 
