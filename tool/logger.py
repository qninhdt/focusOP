class BColor:
    HEADER = '\x1b[95m'
    OKBLUE = '\x1b[94m'
    OKCYAN = '\x1b[96m'
    OKGREEN = '\x1b[92m'
    WARNING = '\x1b[93m'
    FAIL = '\x1b[91m'
    ENDC = '\x1b[0m'
    BOLD = '\x1b[1m'
    UNDERLINE = '\x1b[4m'
    RESET = '\x1b[0;0m'


def print_prefix(on_server):
    if on_server:
        print((BColor.OKCYAN + '[SERVER] : '), end='')
    else:
        print((BColor.OKBLUE + '[APP]    : '), end='')


def info(text, flag=False):
    print_prefix(flag)
    print(BColor.HEADER + text)


def fail(text, flag=False):
    print_prefix(flag)
    print(BColor.FAIL + text)


def ok(text, flag=False):
    print_prefix(flag)
    print(BColor.OKGREEN + text)


def warn(text, flag=False):
    print_prefix(flag)
    print(BColor.WARNING + text)


def reset_color():
    print((BColor.RESET), end='')