# Siobhan Baines 
## Aire Logic Technical Test 

Date : ** February 2022**


## Design Phase
### Requirement

Produce a program which, when given the name of an artist, will produce the average
(mean) number of words in their songs.

### User Experience
######  User Story 1:
**Given** the name of an artist has been entered and it exists,
**When** there are songs available,
**Then** display the average number of words in the songs written by the artist

### APIs Used

https://musicbrainz.org/doc/MusicBrainz_API

https://lyricsovh.docs.apiary.io/#reference


### Language Used
Python

### Steps

1. Create a command to pull back the information from the API for MusicBrainz
2. Load Song titles into an array
3. Use the song titles array to pull back the lyrics from the API for luricsovh
4. Load lyrics into another array for each song title
5. Count the number of spaces in the lyrics string and add 1 to give the number of words in the string.
6. Accummulate the number of words for each song.
7. Keep a count of the number of songs.
8. Divid the total number of words by the total number of songs.
9. Output the name of the artist and the average number of words.

### Testing
1. Check artist exists, if not display an error
2. Check song lyrics exist in second api, if not display and error
2. Display total number of songs
3. Display number of words in each song
4. Display total number of words



#### Notes 
To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

