import os
import subprocess
import urllib.request

print(os.environ)

urllib.request.urlretrieve(
    'https://github.com/Morilli/ManifestDownloader/releases/latest/download/ManifestDownloader.exe', 'ManifestDownloader.exe')

subprocess.check_call(['./ManifestDownloader.exe', os.environ['GAME_FILES_MANIFEST'], '-f',
                       'DATA/FINAL/Champions/.*wad\.client$', '-t', '8', '--no-langs', '-o', os.environ['GAME_FILES_PATH'], '-v'])
