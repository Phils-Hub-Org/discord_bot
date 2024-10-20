# ...

class OnScheduledEventDelete:
    @staticmethod
    async def on_scheduled_event_delete(event):
        """
        Triggered when a scheduled event is deleted from a guild.

        Parameters:
        - event (discord.ScheduledEvent): The event that was deleted.
        """
        print(f'Scheduled event deleted: {event.name} (ID: {event.id})')