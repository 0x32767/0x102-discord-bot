from colorama import Fore, Style, init


init(autoreset=False)


class BaseError:
    msg = "Base error"

    def __init__(self, line, msgs):
        self.line = line

        print(f"{Fore.RED}{type(self).__name__}{Style.RESET_ALL}:")
        print(f"{Fore.RED}    {line=} {Style.RESET_ALL}")
        print(f"{Fore.RED}    {self.msg.format(msgs)}{Style.RESET_ALL}")
