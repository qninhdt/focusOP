import sys, signal

def on_ctrlC(handler):

    def _wrapper(sig, frame):
        handler()

    signal.signal(signal.SIGINT, _wrapper)
    return handler