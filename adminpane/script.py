import subprocess


def start():
    cmd = ["poetry", "run", "python", "src/app.py"]
    subprocess.call(cmd, shell=True)


def migration():
    cmd = ["poetry", "run", "alembic", "upgrade", "head"]
    subprocess.call(cmd, shell=True)


def makemigration():
    cmd = ["poetry", "run", "alembic", "revision", "--autogenerate"]
    subprocess.call(cmd, shell=True)
