import redis

# TODO: Remove these test commands when the cache is officially deployed
testCommands = {
    # Community related commands
    "!community": "Community",
    # Context related commands
    "!namespace": "Context",
    # Marketplace Related Commands
    "!marketplace": "Marketplace",
    # Gateway route related commands
    "!gateway": "Gateway Manager",
    # Routing related commands
    "!route": "Routing Manager",
    # Currency related commands
    "!currency": "Currency",
    # Test script related commands
    "#test": "Test Module"
    
}

class RedisCache:
    def __init__(self, host: str, port: int):
        self.redis = redis.Redis(host=host, port=port, decode_responses=True)

    # Function to add the given test commands to redis, if they do not already exist.
    def add_test_commands(self) -> None:
        for command in testCommands:
            if not self.redis.exists(command):
                self.redis.set(command, testCommands[command])

    # Function to get a command from redis, return None if it does not exist.
    def get_command(self, command: str) -> str:
        if self.redis.exists(command):
            return self.redis.get(command)
        return None
    
    # Function to get all commands from redis
    def get_all_commands(self) -> list:
        commands = []
        for key in self.redis.keys():
            commands.append(key + ": " + self.redis.get(key))
        return commands
    
    # Function to get all keys from redis
    def get_all_keys(self) -> list:
        return self.redis.keys()
        

    