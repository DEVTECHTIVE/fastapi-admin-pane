import subprocess


def start():
    cmd = ["poetry", "run", "uvicorn", "src.app:app", "--reload"]
    subprocess.call(cmd, shell=True)
