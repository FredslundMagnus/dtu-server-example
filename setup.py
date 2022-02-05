from dtu.server import setup

# see 'module available' on server for newest python version
setup(
    f"https://github.com/FredslundMagnus/dtu-server-example.git",
    python="3.9.6",
    packages=["torch", "torchvision", "matplotlib"]
)
