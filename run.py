
def main():
    """
    main calls all the other functions
    """
    artist_name = input("Enter the name of the artist to search:")
    print("You entered: " + artist_name)


# from urllib2 import Request, urlopen

# request = Request('https://api.lyrics.ovh/v1/artist/title')

# response_body = urlopen(request).read()
# print response_body


main()
