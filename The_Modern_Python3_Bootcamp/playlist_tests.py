import unittest
from playlist_oop import Song, Playlist
from datetime import time


class SongTests(unittest.TestCase):
    def setUp(self):
        self.zbawiony = Song(
            "Zbawiony",
            ["Manitou"],
            "Nie daj się życiu",
            time(0, 4, 6))

    def init_errors_tests(self):
        """__init__ should raise TypeError if type of any argument is not correct (title: str, artist: list, album: str, duration: datetime.time)"""
        with self.assertRaises(TypeError):
            Song(1, [""], "", time(0))
        with self.assertRaises(TypeError):
            Song("", 1, "", time(0))
        with self.assertRaises(TypeError):
            Song("", [1], "", time(0))
        with self.assertRaises(TypeError):
            Song("", [""], 1, time(0))
        with self.assertRaises(TypeError):
            Song("", [""], "", 1)
    
    def init_assignment_tests(self):
        """__init__ should"""
            


if __name__ == "__main__":
    unittest.main()
        