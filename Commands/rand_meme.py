# ...

# Get a random meme

import random
import requests

class RandMeme:
    @staticmethod
    async def randmeme(ctx):
        response = requests.get('https://api.imgflip.com/get_memes')
        data = response.json()

        # Check if response is valid
        if data['success']:
            # Pick a random meme from the list of memes
            # print(data['data']['memes'])
            meme = random.choice(data['data']['memes'])
            meme_url = meme['url']  # Meme URL to send
            await ctx.send(meme_url)
        else:
            await ctx.send("Could not fetch a meme. Please try again later.")