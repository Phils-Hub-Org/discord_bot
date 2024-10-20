import traceback

class OnError:
    @staticmethod
    async def on_error(event, *args, **kwargs):
        """
        Triggered when an error occurs in the bot.

        Parameters:
        - event (str): The name of the event that caused the error.
        - *args: Positional arguments passed to the event.
        - **kwargs: Keyword arguments passed to the event.
        """
        print(f"on_error: {event}")
        print(f"Arguments: {args}, Keyword arguments: {kwargs}")
        
        # Log the actual error with traceback details for better debugging
        exc_info = traceback.format_exc()
        if exc_info:
            print("Traceback details:")
            print(exc_info)