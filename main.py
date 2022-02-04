from dtu.server import Parameters, dtu


@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: bool = False
    time: int = 3600

    b: float = 2.0
    a: int = 1
    c: bool = True
    d: str = "fd"

    def run(d: str, b: float, a: int, c: bool) -> None:
        print(b, d, a, c)
        print(b.__class__, d.__class__, a.__class__, c.__class__)


Defaults.start()
