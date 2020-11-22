## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t":"day"}

response = requests.get('https://oauth.reddit.com/r/python/top',headers=headers,params=params)

python_top = response.json()

## 3. Getting the Most Upvoted Post ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t":"day"}

response = requests.get('https://oauth.reddit.com/r/python/top',headers=headers , params=params)

python_top = response.json()

python_top_articles = python_top['data']['children']

most_upvotes = 0

for art in python_top_articles :
    ar = art['data']
    if ar['ups'] >= most_upvotes:
        most_upvoted = ar['id']
        most_upvotes = ar['ups']


## 4. Getting Post Comments ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t":"day"}

response = requests.get('https://oauth.reddit.com/r/python/top',headers=headers , params=params)

python_top = response.json()

python_top_articles = python_top['data']['children']

most_upvotes = 0

for art in python_top_articles :
    ar = art['data']
    if ar['ups'] >= most_upvotes:
        most_upvoted = ar['id']
        most_upvotes = ar['ups']

url = 'https://oauth.reddit.com/r/python/comments/'+ most_upvoted

response2 = requests.get(url,headers=headers)
comments = response2.json()


## 5. Getting the Most Upvoted Comment ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t":"day"}

response = requests.get('https://oauth.reddit.com/r/python/top',headers=headers , params=params)

python_top = response.json()

python_top_articles = python_top['data']['children']

most_upvotes = 0

for art in python_top_articles :
    ar = art['data']
    if ar['ups'] >= most_upvotes:
        most_upvoted = ar['id']
        most_upvotes = ar['ups']

# find the comments linked to the article id most upvoted

url = 'https://oauth.reddit.com/r/python/comments/'+ most_upvoted

response2 = requests.get(url,headers=headers)
comments = response2.json()
comments_list = comments[1]['data']['children']
most_upvoted_comment=""
most_upvotes_comment = 0

for comment in comments_list :
    el = comment['data']
    if el['ups'] >=most_upvotes_comment:
        most_upvotes_comment = el['ups']
        most_upvoted_comment = el['id']

## 6. Upvoting a Comment ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t":"day"}

response = requests.get('https://oauth.reddit.com/r/python/top',headers=headers , params=params)

python_top = response.json()

python_top_articles = python_top['data']['children']

most_upvotes = 0

for art in python_top_articles :
    ar = art['data']
    if ar['ups'] >= most_upvotes:
        most_upvoted = ar['id']
        most_upvotes = ar['ups']

# find the comments linked to the article id most upvoted

url = 'https://oauth.reddit.com/r/python/comments/'+ most_upvoted

response2 = requests.get(url,headers=headers)
comments = response2.json()
comments_list = comments[1]['data']['children']
most_upvoted_comment=""
most_upvotes_comment = 0

for comment in comments_list :
    el = comment['data']
    if el['ups'] >=most_upvotes_comment:
        most_upvotes_comment = el['ups']
        most_upvoted_comment = el['id']
params3 = {"dir":1,"id":most_upvoted_comment}
response3 = requests.post('https://oauth.reddit.com/api/vote',headers=headers,json=params3)
status=response3.status_code