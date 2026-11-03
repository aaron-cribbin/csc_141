# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

def make_album(artist_name, album_title, number_of_songs=None):
    album = {"artist" : f"{artist_name}", "title": f"{album_title}"}
    if number_of_songs is not None:
        album["tracks"] = number_of_songs
    return album

album_1 = make_album('Queen', 'Sheer Heart Attack')
album_2 = make_album('Mili', 'To Kill a Living Book')
album_3 = make_album('Will Wood', '"In Case We Make It"', 12)

print(album_1)
print(album_2)
print(album_3)

while True:
    print("\nIf you want to add an album and songs, please enter the information: ")
    print("Enter '0' at any time to quit")
    art_name = input("Enter the artist's name: ")
    if art_name == '0':
        break
    alb_title = input("Enter the album title: ")
    if alb_title == '0':
        break
    formated_album = make_album(art_name, alb_title)
    print(formated_album)