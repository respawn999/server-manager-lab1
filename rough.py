class Server:

    def __init__(self, cap):
        self.cap = cap
        self.started = False
    

number_of_servers = 10
servers = [Server(5) for _ in range(number_of_servers)]



print(servers)