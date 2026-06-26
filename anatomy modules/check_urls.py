import urllib.request

urls = [
    "https://commons.wikimedia.org/wiki/Special:FilePath/Gray203.png",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Gray573.png",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Gray812and814.svg",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Gray326.png",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Brachial_plexus_color.svg",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Gray523.png",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Gray574.png",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Femur_-_anterior_view.png",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Gray343.png",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Gray348.png",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Gray544.png",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Gray433.png",
    "https://commons.wikimedia.org/wiki/Special:FilePath/Dermatoms.svg"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
        resp = urllib.request.urlopen(req)
        print(f"{resp.status} - {u.split('/')[-1]}")
    except Exception as e:
        print(f"Error {u.split('/')[-1]}: {e}")
