# ...
 
welcome_responses = [
    "Who let this guy in? :eyes:",
    "Uh-oh, we got a new face! Who are you? :thinking:",
    "New recruit alert! What's your story? :eyes:",
    "Is this someone's lost friend? :eyes:",
    "Look who just showed up! What brings you here? :shrug:",
    "A wild member has appeared! Who are you, mysterious stranger? :eyes:",
    "Did someone order a new member? Who dis? :thinking:",
    "Looks like we've got a fresh face! What's your deal? :eyes:",
    "Who invited this person? Let's get to know you! :eyes:",
    "We've got a new guest! What shenanigans are you here for? :grin:",
    "Aha! A new member has entered the arena! What's your game plan? :eyes:",
    "Who's this mysterious newcomer? Let's unravel the mystery! :detective:",
    "Looks like the party just got bigger! Who are you? :eyes:",
    "New member in the house! What's your favorite meme? :eyes:",
    "Oh look, another brave soul! What's your story? :eyes:",
    "Well, well, well... who do we have here? :thinking:",
    "New face detected! Prepare for an interrogation! :eyes:",
    "Who's the fresh meat? Welcome to the chaos! :eyes:",
    "Looks like a new player has joined the game! What's your move? :eyes:",
    "Another one bites the dust! Who are you? :eyes:"
]

class OnMemberJoin:
    @staticmethod
    async def on_member_join(member):
        """
        Triggered when a member joins the guild.

        Parameters:
        - member (discord.Member): The member who joined the guild.
        """
        print(f'Member joined: {member.name} (ID: {member.id})')