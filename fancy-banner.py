import platform
import subprocess
import pyfiglet


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


clear_screen()
text = "\u001bPHOTON \u001bCRAWLER"

result = pyfiglet.figlet_format(text)
print(result)
