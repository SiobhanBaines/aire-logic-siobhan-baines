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
        # print(song_titles, len(song_titles))
        if total_songs !=0:
           total_songs += songs  
        else:
            total_songs = songs
    
    print(f'This artist wrote {total_songs} songs.')
    return(song_titles)    


def get_lyrics(titles, artist_name):
    print(titles, artist_name)
    
    total_words = 0
    for title in titles:

        print("title ", title)

        response = requests.get(LYRICS_OVH_GET.format(artist_name, title))
        song = response.json()
        # print(song)
        song_lyrics = song['lyrics']
        # print(song_lyrics)
        word_count = 0
        for lyric in song_lyrics:
            lyric = lyric.strip()
            lyric = lyric.lower()
            lyric = lyric.translate(lyric.maketrans("", "", string.punctuation))
            words = lyric.split()
            # total_words = len(words)
            # print(total_words)

            for word in words:
                if word_count != 0:
                    word_count = word_count + 1
                else:
                    word_count = 1

        print("word_count ",word_count)
        if word_count != 0:
            if total_words != 0:
                total_words = total_words + word_count
            else:
                total_words = word_count

        # except:
        #     print("no lyrics in this song")
        #     total_songs -= 1

    print(total_songs)        
    print(total_words)
    return(total_words, total_songs)
    # print(total_words)  


def main():
    """
    main calls all the other functions
    """
    artist_name = input("Enter the name of the artist to search:")
    print("You entered: " + artist_name)
    
    titles = get_song_titles(artist_name)
    if titles == None:
        print(f'{artist_name}, has not songs in MusicBrainz')
        return

    words = get_lyrics(titles, artist_name)
    
    print(f'This artist wrote {total_songs} songs.')
    print(total_words)

    # calculate_average_words()
# from urllib2 import Request, urlopen

# request = Request('https://api.lyrics.ovh/v1/artist/title')

# response_body = urlopen(request).read()
# print response_body


main()
