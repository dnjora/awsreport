from colorama import Fore, init

class Logging():
    def __init__(self):
        init(autoreset=True)

    def print_green(self, msg):
        print(Fore.GREEN + msg)

    def print_yellow(self, msg):
        print(Fore.YELLOW + msg)
