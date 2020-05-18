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

* For each of the 64 songs that fit the pattern *song-\*.wav* we will store its signature and name. This will be our 'database' of songs. Rather than hardcoding all the 64 names, we are using the `glob` library to build a list of filenames that match the pattern.

* The signature for each song will be a list of the maximum frequencies within each segment of the spectrogram. There will be one value for each of the time segments. For example, if the results of the spectrogram were to produce the plot in  

![](https://github.com/ShameenShetty/CSE-3313--HW09/blob/master/Sample%20Spectrogram.png)  

then the signature would be [20, 30, 0] since the max value in col 0 is 8 (frequency = 20Hz), the max val in col 1 is 7 (freq = 30Hz), and the max val in col 3 is 9 (freq = 0Hz).  
So, using *song-beatles.wav* as an example, the signature of that song is *(148.0, 146.0, 72.0, 72.0, 108.0, 176.0, 146.0, 148.0, 148.0, 72.0, 72.0, 110.0, 176.0, 148.0, 148.0, 148.0, 72.0, 72.0, 108.0, 176.0, 148.0, 148.0, 108.0, 112.0, 112.0, 132.0, 134.0, 110.0, 112.0, 112.0, 56.0, 112.0, 132.0, 134.0, 110.0, 102.0, 98.0, 98.0, 48.0, 48.0, 48.0, 48.0, 48.0, 50.0, 38.0, 2476.0, 48.0, 52.0, 48.0, 72.0, 72.0, 110.0, 176.0, 176.0, 148.0, 146.0, 74.0, 146.0, 176.0, 176.0, 146.0, 146.0, 72.0, 72.0, 108.0, 176.0, 146.0, 146.0)*. 

* To test our program we will read a file called testSong.wav which is just a copy of one of the corrupted songs matching the pattern *test-*.wav*. 

* The metric used to compare the signatures of the test song and a song in our database is the vector *1-norm*. Given a vector <a href="https://www.codecogs.com/eqnedit.php?latex=\overrightarrow{v}&space;=&space;[v_1&space;,&space;v_2&space;,&space;.&space;.&space;.,&space;v_n&space;]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\overrightarrow{v}&space;=&space;[v_1&space;,&space;v_2&space;,&space;.&space;.&space;.,&space;v_n&space;]" title="\overrightarrow{v} = [v_1 , v_2 , . . ., v_n ]" /></a> , the vector 1-norm is   
<a href="https://www.codecogs.com/eqnedit.php?latex=\left&space;\|&space;\overrightarrow{v}&space;\right&space;\|_1&space;=&space;\sum_{i&space;=&space;1}^{n}=&space;\left&space;|&space;v_i&space;\right&space;|&space;=&space;\left&space;|&space;v_1&space;\right&space;|&space;&plus;&space;\left&space;|&space;v_2&space;\right&space;|&space;&plus;&space;.&space;.&space;.&space;&plus;&space;\left&space;|&space;v_n&space;\right&space;|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left&space;\|&space;\overrightarrow{v}&space;\right&space;\|_1&space;=&space;\sum_{i&space;=&space;1}^{n}=&space;\left&space;|&space;v_i&space;\right&space;|&space;=&space;\left&space;|&space;v_1&space;\right&space;|&space;&plus;&space;\left&space;|&space;v_2&space;\right&space;|&space;&plus;&space;.&space;.&space;.&space;&plus;&space;\left&space;|&space;v_n&space;\right&space;|" title="\left \| \overrightarrow{v} \right \|_1 = \sum_{i = 1}^{n}= \left | v_i \right | = \left | v_1 \right | + \left | v_2 \right | + . . . + \left | v_n \right |" /></a>
