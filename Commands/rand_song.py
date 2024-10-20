# ...

import os
import json
import random
import aiohttp
from Components.youtube import YouTube

import Utils.py_utility as PyUtility
from Utils.globals_manager import GlobalsManager

# Get a random song

class RandSong:
    @staticmethod
    async def randsong(ctx):
        # Load previously sent songs from the JSON file into memory
        if YouTube.SETN_SONGS_CACHE is None:
            YouTube.SETN_SONGS_CACHE = RandSong.load_songs_cache()

        async with aiohttp.ClientSession() as session:
            search_term = random.choice(YouTube.RAND_SONG_SEARCH_TERMS)
            search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=50&q={search_term}&key={PyUtility.decryptData(GlobalsManager.get('youtube_token'), GlobalsManager.get('symmetric_key')).decode()}"

            try:
                async with session.get(search_url, timeout=10) as response:
                    response.raise_for_status()
                    data = await response.json()

                if 'items' in data and len(data['items']) > 0:
                    video_ids = [item['id']['videoId'] for item in data['items']]
                    unique_video_ids = list(set(video_ids))

                    if unique_video_ids:
                        selected_video_id = None

                        # Check if any of the songs have been sent before
                        for video_id in unique_video_ids:
                            if not RandSong.was_song_sent(video_id):
                                selected_video_id = video_id
                                break

                        if selected_video_id:
                            await ctx.send(f"Check out this song: https://www.youtube.com/watch?v={selected_video_id}")
                            RandSong.store_song(selected_video_id)
                        else:
                            # Fallback: Send a random video if all have been sent before
                            random_video = random.choice(unique_video_ids)
                            await ctx.send(f"Check out this song: https://www.youtube.com/watch?v={random_video}")
                else:
                    await ctx.send("Could not fetch any songs.")
            except aiohttp.ClientError as e:
                await ctx.send("Error fetching song. Please try again later.")
            except Exception as e:
                await ctx.send("Error fetching song: " + str(e))

    @staticmethod
    def load_songs_cache():
        if os.path.exists(YouTube.SONG_CACHE_FILE):
            with open(YouTube.SONG_CACHE_FILE, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []  # Return empty list if JSON is invalid
        else:
            return []  # If file doesn't exist, start with an empty list

    @staticmethod
    def save_songs_cache(cache):
        with open(YouTube.SONG_CACHE_FILE, 'w') as file:
            json.dump(cache, file)

    @staticmethod
    def was_song_sent(video_id):
        return video_id in YouTube.SETN_SONGS_CACHE

    @staticmethod
    def store_song(video_id):
        if video_id not in YouTube.SETN_SONGS_CACHE:
            YouTube.SETN_SONGS_CACHE.append(video_id)
            if len(YouTube.SETN_SONGS_CACHE) > 250:  # Limit the cache to 250 songs
                YouTube.SETN_SONGS_CACHE.pop(0)  # Remove the oldest entry
            RandSong.save_songs_cache(YouTube.SETN_SONGS_CACHE)

    