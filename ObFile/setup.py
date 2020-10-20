from urllib.request import urlretrieve
from subprocess import Popen, call, PIPE
import os

def setup():
    try:
        Popen('python', stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
    except FileNotFoundError:
        print('Python Not Found, Installing Python. This Might Take A Few Minutes!')
        if download_python():
            print('Successfully Installed Python')

    download_dependencies()

def download_python() -> int:
    # Download Python
    download_path = ''

    if platform == 'win32':
        download_path = f'C:\\Users\\{getuser()}\\Downloads\\PythonSetup.exe'
    elif platform == 'darwin':
        download_path = f'\\Users\\{getuser()}\\Downloads\\PythonSetup.pkg'
    elif platform == 'linux':
        download_path = f'\\home\\{getuser()}\\Downloads\\PythonSetup.deb'

    python_download_url = None

    if platform == 'win32':
        python_download_url = 'https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe'
    elif platform == 'darwin':
        python_download_url = 'https://www.python.org/ftp/python/3.9.0/python-3.9.0-macosx10.9.pkg'

    urlretrieve(python_download_url, download_path)

    setup_python = []

    if platform == 'win32':
        setup_python = [f'{download_path} /passive']
    elif platform == 'macos':
        setup_python = [
            f'sudo installer -store -pkg "{download_path}" -target /Applications']

    for command in setup_python:
        call(command)

    success = True

    try:
        Popen('python', stdout=PIPE, stdin=PIPE, stderr=PIPE)
    except FileNotFoundError:
        success = False

    return success

def download_dependencies():
    # Download Dependencies Using Pip
    command = 'python -m pip install pyinstaller pyarmor colorama pyfiglet'
    call(command)
    os.system('Msgbox\setupmsg.vbs')
    os.system('python ObFile.py')

setup()
