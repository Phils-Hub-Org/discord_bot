# ...

class OnScheduledEventUpdate:
    @staticmethod
    async def on_scheduled_event_update(before, after):
        """
        Triggered when a scheduled event is updated in a guild.

        Parameters:
        - before (discord.ScheduledEvent): The event before the update.
        - after (discord.ScheduledEvent): The event after the update.
        """
        print(f'Scheduled event updated: {before.name} (ID: {before.id})')