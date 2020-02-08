import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "pygame"],
    "excludes": ["tkinter"],
    "include_files": ['game/', '/usr/share/fonts/'],
    "zip_includes": ["game/"],
    "zip_include_packages": ["os", "pygame"]
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(
    script="main.py",
    initScript=None,
    base=base,
    targetName='snakepy'
)

setup(  name = "snakepy",
        version = "0.1",
        description = "Basic snake game!",
        options = {"build_exe": build_exe_options},
        executables = [exe])