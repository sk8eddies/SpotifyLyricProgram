from controller.SpotifySongFetcher import SpotifySongFetcher
import time


def main():
    # Init parts of the controller
    fetcher = SpotifySongFetcher()
    # fetcher.fetch()

    while(True):
        # if fetcher.is_new_song():
        #    fetcher.fetch()
        time.sleep(3)

main()
