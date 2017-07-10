import spotilib


class SpotifySongFetcher:

    def fetch(self):
        print(spotilib.song_info())
        return (spotilib.artist(), spotilib.song())

    def is_new_song(self):
        return not(spotilib.artist() == self._artist and spotilib.song() == self._song)