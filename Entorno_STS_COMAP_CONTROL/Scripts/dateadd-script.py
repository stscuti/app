#!c:\django\sts_comap_control\entorno_sts_comap_control\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'dateutils==0.6.7','console_scripts','dateadd'
__requires__ = 'dateutils==0.6.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('dateutils==0.6.7', 'console_scripts', 'dateadd')()
    )
