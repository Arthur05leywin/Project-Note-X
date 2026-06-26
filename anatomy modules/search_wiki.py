import urllib.request, json, urllib.parse

def search(q):
    url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote("file:" + q)}&utf8=&format=json'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        res = json.loads(response.read())
        print(f"Results for '{q}':")
        for r in res['query']['search'][:1]:
            print(f'  {r["title"]}')
    except Exception as e:
        print('error', e)

queries = [
    "scapula posterior gray",
    "superficial veins upper limb gray",
    "dermatome upper limb",
    "femur anterior gray",
    "hip joint anatomy gray",
    "knee joint gray",
    "femoral triangle gray",
    "popliteal fossa gray",
    "dermatome lower limb"
]

for q in queries:
    search(q)
