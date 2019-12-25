import requests
def httpGet(url):

    session = requests.session()
    resp = session.get(url)
    return resp

def httpPost(url,data):

    session = requests.session()
    resp = session.post(url,data)
    return resp