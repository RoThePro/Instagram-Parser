import urllib, json

def intersect(a, b):
    return list(set(a) & set(b))

def parse(url):
	list=[]
	response = urllib.urlopen(url);
	data = json.loads(response.read())
	for obj in data["data"]:
		list.append(obj["username"])
	return list
	
followers = parse("https://api.instagram.com/v1/users/489834446/followed-by?access_token="[ADD ACCESS TOKEN]"&count=10000")
following = parse("https://api.instagram.com/v1/users/489834446/follows?access_token="[ADD ACCESS TOKEN]"&count=10000")

mutual = intersect(followers, following)

unfollowers = set(following).difference(set(mutual))

f = open('unfollowers.txt','w')

for obj in unfollowers:
	f.write(obj+"\n")
