from __future__ import annotations
from dtu.server import Parameters, dtu
from sys import argv


@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: bool = False
    time: int = 3600

    b: float = 2.0
    a: int = 1
    d: str = "fd"

    def run(d: str, b: float, a: int) -> None:
        print(b, d, a)
        print(b.__class__, d.__class__, a.__class__)
        print(argv)


Defaults.start()
