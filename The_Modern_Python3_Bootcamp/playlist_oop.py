# Applying OOP to create playlist like on Spotify
# Priority #1: write tests!

from datetime import time

class Song:
    def __init__(self, title, artist, album, duration): # title: str, artist: list, album: str, duration: datetime.time 
        if type(title) != str:
            raise TypeError("title must be a string")
        elif type(artist) != list:
            raise TypeError("artist must be a list")
        elif not all((type(a) == str for a in artist)):
            raise TypeError("elements of artist list must be strings")
        elif type(album) != str:
            raise TypeError("album must be string")
        elif not isinstance(duration, time):
            raise TypeError("duration must be instance of datetime.time class")
        else:
            self.title = title
            self.artist = artist
            self.album = album
            self.duration = duration

    def __repr__(self):
        return f"{self.title} by {self.artist}"

class Playlist:
    def __init__(self, title, creator, songs): # title: str, creator: str, songs: list
        if type(title) != str:
            raise TypeError("title must be a string")
        elif type(creator) != str:
            raise TypeError("creator must be a string")
        elif type(songs) != list:
            raise TypeError("songs must be a list")
        elif not all((isinstance(song, Song) for song in songs)):
            raise TypeError("elements of song list must be instances of Song class")
        else:
            self.title = title
            self.creator = creator
            self.songs = songs

    def __iter__(self):
        return iter(self.songs)

    def __repr__(self):
        return f"{self.title} playlist created by {self.creator} ({self.count()} songs)"

    def add_song(self, song):
        if not isinstance(song, Song):
            raise TypeError("song must be instance of Song class")
        self.songs.append(song)

    def count(self):
        return len(self.songs)


zbawiony = Song("Zbawiony", ["Manitou"], "Nie daj się życiu", time(0,4,6))
pictures = Song("Pictures of you", ["The Cure"], "Disintegration", time(0,7,28))
playlist = Playlist("A few songs", "Somebody", [zbawiony, pictures])

