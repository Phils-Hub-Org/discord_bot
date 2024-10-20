import logging

logger = logging.getLogger(__name__)

class Env:

    DEVELOPMENT = 0
    PRODUCTION = 1

    state: int = -1

    @staticmethod
    def get():
        Env.state_ensurance()
        return Env.state
    
    @staticmethod
    def set(env):
        if env == Env.PRODUCTION:
            Env.state = Env.PRODUCTION
        else:
            Env.state = Env.DEVELOPMENT
    
    @staticmethod
    def getStr():
        Env.state_ensurance()

        match Env.get():
            case Env.DEVELOPMENT:
                env_state = 'DEV'
            case Env.PRODUCTION:
                env_state = 'PROD'
            case _:
                env_state = 'DEV'
        
        return env_state
    
    @staticmethod
    def state_ensurance():
        if Env.state == -1:
            print("Env state not set. Defaulting to development.")
            Env.set(Env.DEVELOPMENT)