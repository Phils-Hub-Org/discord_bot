# ...

import os
import json
import random
import aiohttp
from Components.youtube import YouTube

import Utils.py_utility as PyUtility
from Utils.globals_manager import GlobalsManager

# Get a random trailor

class RandTrailor:
    @staticmethod
    # """ 1 request """
    async def rand_trailor(ctx):  # Command to get a random movie/series trailer
        """
        Total Requests Allowed per Day: 100
        Commands You Can Run per Day: 100 (because each command makes 1 requests)
        Total Video IDs You Can Retrieve per Day: 5000

        So, with this setup you could potentially retrieve up to 5000 unique video IDs per day if all goes perfectly, which is a good amount of variety.
        """
        # Load previously sent trailers from the JSON file into memory
        if YouTube.SETN_TRAILORS_CACHE is None:
            YouTube.SETN_TRAILORS_CACHE = RandTrailor.load_trailors_cache()

        async with aiohttp.ClientSession() as session:
            search_term = random.choice(YouTube.RAND_TRAILOR_SEARCH_TERMS)
            search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=50&q={search_term}&key={PyUtility.decryptData(GlobalsManager.get('youtube_token'), GlobalsManager.get('symmetric_key')).decode()}"

            try:
                async with session.get(search_url, timeout=10) as response:
                    response.raise_for_status()
                    data = await response.json()

                if 'items' in data and len(data['items']) > 0:
                    video_ids = [item['id']['videoId'] for item in data['items']]
                    unique_video_ids = list(set(video_ids)) if video_ids else []

                    if unique_video_ids:
                        selected_video_id = None

                        # Check if any of the trailers have been sent before
                        for video_id in unique_video_ids:
                            if not RandTrailor.was_trailor_sent(video_id):
                                selected_video_id = video_id
                                break

                        if selected_video_id:
                            await ctx.send(f"Watch this trailer: https://www.youtube.com/watch?v={selected_video_id}")
                            RandTrailor.store_trailor(selected_video_id)
                            return  # Exit after successfully sending a trailer
                        else:
                            # Fallback: Send a random video if all have been sent before
                            random_video_id = random.choice(unique_video_ids)
                            await ctx.send(f"Watch this trailer: https://www.youtube.com/watch?v={random_video_id}")
                else:
                    await ctx.send("Could not fetch any trailers.")
            except aiohttp.ClientError as e:
                await ctx.send("Error fetching trailer. Please try again later.")
                return
            except Exception as e:
                await ctx.send("Error fetching trailer: " + str(e))

    """
    2 requests, more advanced filtering
    """
    # def parse_duration(duration_str):
    #     duration = isodate.parse_duration(duration_str)
    #     return int(duration.total_seconds())

    # @bot.command()
    # async def randtrailor(ctx):  # Command to get a random movie/series trailer
    #     """
    #     Total Requests Allowed per Day: 100
    #     Commands You Can Run per Day: 50 (because each command makes 2 requests)
    #     Total Video IDs You Can Retrieve per Day: 2500

    #     So, with this setup you could potentially retrieve up to 2500 unique video IDs per day if all goes perfectly, which is a good amount of variety.
    #     """
    #     async with aiohttp.ClientSession() as session:
    #         search_term = random.choice(YouTube.RAND_TRAILOR_SEARCH_TERMS)
    #         search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=50&q={search_term}&key={PyUtility.decryptData(GlobalsManager.get('youtube_token'), GlobalsManager.get('symmetric_key')).decode()}"

    #         try:
    #             async with session.get(search_url, timeout=10) as response:
    #                 response.raise_for_status()
    #                 data = await response.json()

    #             if 'items' in data and len(data['items']) > 0:
    #                 video_ids = [item['id']['videoId'] for item in data['items']]
    #                 unique_video_ids = list(set(video_ids))

    #                 if unique_video_ids:
    #                     # Create a comma-separated list of video IDs for the batch request
    #                     ids_param = ','.join(unique_video_ids)

    #                     # Create the batch request URL
    #                     batch_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id={ids_param}&key={PyUtility.decryptData(GlobalsManager.get('youtube_token'), GlobalsManager.get('symmetric_key')).decode()}"

    #                     # Fetch video details in a batch request
    #                     async with session.get(batch_url, timeout=10) as batch_response:
    #                         batch_response.raise_for_status()
    #                         batch_data = await batch_response.json()

    #                     if 'items' in batch_data and len(batch_data['items']) > 0:
    #                         selected_video_id = None

    #                         # Filter trailers based on video duration and view count
    #                         for item in batch_data['items']:
    #                             video_id = item['id']

    #                             # Check if the video has already been sent
    #                             if was_trailor_sent(video_id):
    #                                 continue

    #                             # Get video duration and view count
    #                             duration = item['contentDetails']['duration']  # e.g., "PT2M30S"
    #                             view_count = int(item['statistics'].get('viewCount', 0))

    #                             # Convert ISO 8601 duration format to seconds
    #                             duration_seconds = parse_duration(duration)

    #                             # Advanced filtering logic (e.g., duration between 1 and 10 minutes, at least 10k views)
    #                             if 60 <= duration_seconds <= 600 and view_count > 10000:
    #                                 selected_video_id = video_id
    #                                 break

    #                         if selected_video_id:
    #                             await ctx.send(f"Watch this trailer: https://www.youtube.com/watch?v={selected_video_id}")
    #                             store_trailor(selected_video_id)
    #                             return  # Exit after successfully sending a trailer
    #                         else:
    #                             await ctx.send("No trailers found that match the filtering criteria.")
    #                     else:
    #                         await ctx.send("Could not fetch details for the trailers.")
    #             else:
    #                 await ctx.send("Could not fetch any trailers.")
    #         except aiohttp.ClientError as e:
    #             await ctx.send("Error fetching trailer. Please try again later.")
    #             return
    #         except Exception as e:
    #             await ctx.send("Error fetching trailer: " + str(e))

    # @rand_trailor.error
    # async def randtrailor_error(ctx, error):
    #     # print(traceback.format_exc())
    #     # print(f"Error: {error}")
    #     await ctx.send(f"Error: {error}")

    @staticmethod
    def load_trailors_cache():
        if os.path.exists(YouTube.TRAILOR_CACHE_FILE):
            with open(YouTube.TRAILOR_CACHE_FILE, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []  # Return empty list if JSON is invalid
        else:
            return []  # If file doesn't exist, start with an empty list

    @staticmethod
    def save_trailor_cache(cache):
        with open(YouTube.TRAILOR_CACHE_FILE, 'w') as file:
            json.dump(cache, file)

    @staticmethod
    def was_trailor_sent(video_id):
        return video_id in YouTube.SETN_TRAILORS_CACHE

    @staticmethod
    def store_trailor(video_id):
        # Check if the video ID is already in the cache before adding
        if video_id not in YouTube.SETN_TRAILORS_CACHE:
            YouTube.SETN_TRAILORS_CACHE.append(video_id)
            # Increase the limit to 250
            if len(YouTube.SETN_TRAILORS_CACHE) > 250:
                YouTube.SETN_TRAILORS_CACHE.pop(0)  # Remove the oldest entry
            RandTrailor.save_trailor_cache(YouTube.SETN_TRAILORS_CACHE)