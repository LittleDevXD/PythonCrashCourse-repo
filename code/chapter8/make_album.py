def make_album(name, artist, number_of_songs=None):
    album = {}

    album["name"] = name
    album["artist"] = artist

    if number_of_songs:
        album["number of songs"] = number_of_songs
    return album

while True:
    print("Please tell me your album name and artist.")

    name = input("\nName: ")
    artist = input("Artist: ")
    number_of_songs = input("Number of songs(optional): ")

    album = make_album(name, artist, number_of_songs)
    print(album)

    quit = input("\nIf you are finished pressed 'q': ")

    if quit == 'q':
        break

