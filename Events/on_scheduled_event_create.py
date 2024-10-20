# ...

class OnScheduledEventCreate:
    @staticmethod
    async def on_scheduled_event_create(event):
        """
        Triggered when a scheduled event is created in a guild.

        Parameters:
        - event (discord.ScheduledEvent): The event that was created.
        """
        print(f'Scheduled event created: {event.name} (ID: {event.id})')