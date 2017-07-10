import time


class FetcherFacade:

    def __init__(self, s_fetcher, l_fetcher, l_parser, l_data):
        self._spotify_fetcher = s_fetcher
        self._lyric_fetcher = l_fetcher
        self._lyric_parser = l_parser
        self._lyric_data = l_data
        self._start = True

    def start(self):
        while self._start:
            if self._spotify_fetcher.is_new_song():     # TODO Functional decomposition
                pass
                # Get the new lyric
                # Parse the new lyric
                # Set the new lyric in the model
            time.sleep(3)

    def stop(self):
        self._start = False