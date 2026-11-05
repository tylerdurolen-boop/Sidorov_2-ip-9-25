import os
from pathlib import Path
import subprocess
import venv


game_folder = Path(__file__).resolve().parent / "Игра"
environment = game_folder / ".venv"

venv.create(environment, with_pip=True)

if os.name == "nt":
    python = environment / "Scripts" / "python.exe"
else:
    python = environment / "bin" / "python"

subprocess.run(
    [str(python), "-m", "pip", "install", "-r", "requirements.txt"],
    cwd=game_folder,
    check=True,
)

packages = subprocess.run(
    [str(python), "-m", "pip", "freeze"],
    cwd=game_folder,
    capture_output=True,
    text=True,
    check=True,
)
(game_folder / "requirements.txt").write_text(packages.stdout, encoding="utf-8")

subprocess.run(
    [str(python), "-m", "pip", "show", "colorama"],
    cwd=game_folder,
    check=True,
)
subprocess.run([str(python), "dungeon.py"], cwd=game_folder, check=True)
subprocess.run(
    [str(python), "-c", "import dungeon; help(dungeon)"],
    cwd=game_folder,
    check=True,
)
