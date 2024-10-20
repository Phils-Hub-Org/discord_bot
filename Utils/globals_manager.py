class GlobalsManager:
    """A class for managing globals"""

    GLOBALS = {}

    @classmethod
    def register(cls, key, value):
        """Register a key/value pair"""
        if cls.exists(key):
            raise KeyError(f"Key '{key}' already exists.")
        cls.GLOBALS[key] = value
    
    @classmethod
    def unregister(cls, key):
        """Unregister a global."""
        if not cls.exists(key):
            raise KeyError(f"Global '{key}' is not registered.")
        del cls.GLOBALS[key]
    
    @classmethod
    def get(cls, key):
        """Retrieve a value by its key."""
        if not cls.exists(key):
            raise KeyError(f"'{key}' is not registered.")
        return cls.GLOBALS.get(key)

    @classmethod
    def update(cls, key, value):
        """Update a global."""
        if not cls.exists(key):
            raise KeyError(f"Global '{key}' is not registered.")
        cls.GLOBALS[key] = value

    @classmethod
    def exists(cls, key):
        """Check if a key exists"""
        return key in cls.GLOBALS
    
    @classmethod
    def print_all(cls):
        """Print the global variables"""
        for key, value in cls.GLOBALS.items():
            print(f"{key}: {value}")
