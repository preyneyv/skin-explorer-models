import os
import subprocess
import urllib.request
import requests

d = requests.get(
    "https://sieve.services.riotcdn.net/api/v1/products/lol/version-sets/PBE1?q[platform]=windows").json()
latest = sorted((x for x in d['releases'] if x['release']['labels']['riot:artifact_type_id']['values'][0] == 'lol-game-client'),
                key=lambda x: tuple(map(int, x['compat_version']['id'].split('+')[0].split('.'))))[-1]

print("Game version:", latest['compat_version']['id'].split('+')[0])
print("Manifest URL:", latest['download']['url'])

urllib.request.urlretrieve(
    'https://github.com/Morilli/ManifestDownloader/releases/latest/download/ManifestDownloader.exe', 'ManifestDownloader.exe')

subprocess.check_call(['./ManifestDownloader.exe', latest['download']['url'], '-f',
                       'DATA/FINAL/Champions/.*wad\.client$', '-t', '8', '--no-langs', '-o', os.environ['GAME_FILES_PATH'] or 'game', '-v'])
