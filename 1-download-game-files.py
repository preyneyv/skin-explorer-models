import subprocess
import urllib.request
import requests

# Download game files.
urllib.request.urlretrieve(
    'https://github.com/Morilli/ManifestDownloader/releases/latest/download/ManifestDownloader.exe', 'ManifestDownloader.exe')

d = requests.get(
    "https://sieve.services.riotcdn.net/api/v1/products/lol/version-sets/PBE1?q[platform]=windows").json()
latest = sorted((x for x in d['releases'] if x['release']['labels']['riot:artifact_type_id']['values'][0] == 'lol-game-client'),
                key=lambda x: tuple(map(int, x['compat_version']['id'].split('+')[0].split('.'))))[-1]
print(latest['download']['url'])
 
subprocess.run(['./ManifestDownloader.exe', latest['download']['url'], '-f' ,'"DATA/FINAL/Champions/.*wad\.client$"', '-t' ,'8' ,'--no-langs', '-o', 'game'])
