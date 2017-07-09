import spotilib


class SpotifySongFetcher:

    def __init__(self):
        self._artist = spotilib.artist()
        self._song = spotilib.song()
        self._new_song = True
        print("Artist: {0} || Song: {1}".format(self._artist, self._song))

