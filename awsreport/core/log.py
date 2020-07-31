from colorama import Fore, init

class Logging():
    def __init__(self):
        init(autoreset=True)

    def print_verbose(self, msg):
        print(Fore.GREEN + msg)

    def print_msg(self, msg):
        print(Fore.YELLOW + msg)
