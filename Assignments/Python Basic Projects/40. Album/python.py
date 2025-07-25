def make_album(artist: str, title: str, number: int = 1):
    return {
        'name': artist,
        'album': title,
        'track': number
    }


print(make_album('Justin Bieber', 'Purpose', 3))
print(make_album('Michael Jackson', 'Thriller'))
