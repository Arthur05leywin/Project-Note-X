import urllib.request, json, urllib.parse

def search(q):
    url = f'https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote("file:" + q)}&utf8=&format=json'
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
    "Gray393",
    "Gray1224",
    "Gray1146",
    "Gray1058",
    "Liver_Couinaud",
    "Gray591",
    "Gray1120"
]

for q in queries:
    search(q)
