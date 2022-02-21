import os
import json
import musicbrainzngs
# import urllib2
import urllib.request
import requests
import string
import sys

LYRICS_OVH_GET = "https://api.lyrics.ovh/v1/{}/{}"


def get_song_titles(artist_name):
    """
    Get all the song titles for the chosen artist
    """
    songs = 0
    total_songs = 0
    song_titles = []
    
    musicbrainzngs.set_useragent(
    "aire-logic-siobhan-baines",
    "0.1",
    "https://siobhanbaines-airelogics-dcio80ur4qb.ws-eu33.gitpod.io/",
    )
    get_artist_id = musicbrainzngs.search_artists(artist=artist_name)
    
    artist_id =get_artist_id['artist-list'][0]["id"]
   
    get_release_group_ids = musicbrainzngs.get_artist_by_id(artist_id, 
        includes=["release-groups"], release_type=["album", "ep"])

    for release_group in get_release_group_ids["artist"]["release-group-list"]:

        title = release_group["title"]

        get_album_ids = musicbrainzngs.search_releases(artist=artist_id, release=title, limit=1)
        album_id = get_album_ids["release-list"][0]["id"]

        recording_result = musicbrainzngs.get_release_by_id(album_id, ["recordings"])
        tracks = (recording_result["release"]["medium-list"][0]["track-list"])
        
        for x in range(len(tracks)):
            line = (tracks[x])
            song_title = line["recording"]["title"]
            song_titles.append(song_title)
                                
        songs = len(tracks)
        
        if total_songs !=0:
           total_songs += songs  
        else:
            total_songs = songs
    
    return(song_titles, total_songs)    


def get_lyrics(titles, artist_name, total_songs):
    """
    Calculate the total numbers of words in all the 
    songs written by the chosen artist and decrement 
    total number of songs where no lyrics are found.
    """
    total_words = 0
    for title in titles:

        response = requests.get(LYRICS_OVH_GET.format(artist_name, title))
        try:
            song = response.json()
            try:
                song_lyrics = song['lyrics']

                word_count = 0
                for lyric in song_lyrics:
                    lyric = lyric.strip()
                    lyric = lyric.lower()
                    lyric = lyric.translate(lyric.maketrans("", "", string.punctuation))
                    words = lyric.split()
                    
                    for word in words:
                        if word_count != 0:
                            word_count = word_count + 1
                        else:
                            word_count = 1

                if word_count != 0:
                    if total_words != 0:
                        total_words = total_words + word_count
                    else:
                        total_words = word_count

            except:
                total_songs -= 1
        except:
            print(f'')
    return(total_words, total_songs)


def main():
    """
    main calls all the other functions
    """
    artist_name = input("Enter the name of the artist to search:")
    print(f'Please wait while the artist average number of words in their songs')
    
    titles, total_songs = get_song_titles(artist_name)
    if titles == None:
        print(f'{artist_name}, has not songs in MusicBrainz')
        return

    total_words, total_songs = get_lyrics(titles, artist_name, total_songs)

    if total_songs == 0:
        print(f'We cannot find any songs by {artist_name}.')
    elif total_words == 0:
        print(f'We cannot find any words to the songs written by {artist_name}.')
    else:
        average_words = round(total_words / total_songs)

        print(f'The average number of words in songs written by {artist_name} is {average_words}.')


main()
