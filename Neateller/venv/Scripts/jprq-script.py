#!d:\python\neateller\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'jprq==2.1.0','console_scripts','jprq'
__requires__ = 'jprq==2.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('jprq==2.1.0', 'console_scripts', 'jprq')()
    )
