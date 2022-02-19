import os
import json
import musicbrainzngs
# import request

# const config = {
#         headers: {
#             Accept: 'application/json'
#         },
#     }

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


def main():
    """
    main calls all the other functions
    """
    artist_name = input("Enter the name of the artist to search:")
    print("You entered: " + artist_name)
    
    get_song_titles(artist_name)
    
    # get_lyrics(titles)
# from urllib2 import Request, urlopen

# request = Request('https://api.lyrics.ovh/v1/artist/title')

# response_body = urlopen(request).read()
# print response_body


main()
