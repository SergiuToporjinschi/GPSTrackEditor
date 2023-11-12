import subprocess

subprocess.check_output(['pyuic6', 'main.ui', '-o', 'main_ui.py'])