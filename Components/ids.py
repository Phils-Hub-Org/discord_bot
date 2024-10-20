from Components.env import Env

class IDs:

    ALLOWED_GUILDS: list
    ADMIN_ROLE_ID: int
    MOD_ROLE_ID: int
    BANNED_MEMBERS_IDS: list

    @staticmethod
    def initialize():
        match Env.get():
            case Env.DEVELOPMENT:
                # server id
                # ...

                # list of servers that are allowed to use this bot
                IDs.ALLOWED_GUILDS = []

                # channel ids
                # ...

                # member ids
                # ...

                # Role ID
                IDs.ADMIN_ROLE_ID = None
                IDs.MOD_ROLE_ID = None

                # banned member ids
                # ...
                # banned members list
                IDs.BANNED_MEMBERS_IDS = []

            case Env.PRODUCTION:
                # server id
                # ...

                # list of servers that are allowed to use this bot
                IDs.ALLOWED_GUILDS = []

                # channel ids
                # ...

                # member ids
                # ...

                # Role ID
                IDs.ADMIN_ROLE_ID = None
                IDs.MOD_ROLE_ID = None

                # banned member ids
                # ...
                # banned members list
                IDs.BANNED_MEMBERS_IDS = []