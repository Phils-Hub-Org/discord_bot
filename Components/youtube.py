import os
from Utils.globals_manager import GlobalsManager

class YouTube:

    TRAILOR_CACHE_FILE = 'sent_trailors_cache.json'  # The file to store sent trailers
    SETN_TRAILORS_CACHE = None  # This will hold the loaded cache in memory
    RAND_TRAILOR_SEARCH_TERMS = ["action movie trailer", "comedy movie trailer", "horror movie trailer"]  # List of search terms

    SONG_CACHE_FILE = 'sent_songs_cache.json'  # The file to store sent songs
    SETN_SONGS_CACHE = None  # This will hold the loaded cache in memory
    RAND_SONG_SEARCH_TERMS = ["pop music", "rock music", "hip hop music", "electronic music"]  # List of search terms

    @staticmethod
    def initialize():
        GlobalsManager.register('youtube_token', os.getenv('DISCORD_BOT_YOUTUBE_TOKEN').encode())