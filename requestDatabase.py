import requests
import json

class requestDatabase:
    f = open("token.txt", "r")
    token=f.read()
    def getAll(self):
        url = "https://marty-2afb.restdb.io/rest/my-todo"

        headers = {
            'content-type': "application/json",
            'x-apikey': requestDatabase.token,
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers)

        return json.loads(response.text)
    
    def get(self, id):
        url = "https://marty-2afb.restdb.io/rest/my-todo/"+str(id)

        headers = {
            'content-type': "application/json",
            'x-apikey': requestDatabase.token,
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers)
        if response.text == '[]':
            return None
        return json.loads(response.text)
    
    def add(self, content, time):
        url = "https://marty-2afb.restdb.io/rest/my-todo"

        payload = json.dumps( {"Content": content,"dateTime": time} )
        headers = {
            'content-type': "application/json",
            'x-apikey': requestDatabase.token,
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        rt=json.loads(response.text)
        return rt["_id"]

    def update(self, id, content):
        url = "https://marty-2afb.restdb.io/rest/my-todo/"+str(id)
        temp=self.get(id)
        if temp == None:
            return 'id not found'
        time=temp['dateTime']
        load = {"Content": content,"dateTime": time}
        payload=json.dumps(load)
        headers = {
            'content-type': "application/json",
            'x-apikey': requestDatabase.token,
            'cache-control': "no-cache"
            }

        response = requests.request("PUT", url, data=payload, headers=headers)
        rt=json.loads(response.text)
        return rt['_id']

    def delete(self, id):
        url = "https://marty-2afb.restdb.io/rest/my-todo/"+str(id)

        headers = {
            'content-type': "application/json",
            'x-apikey': requestDatabase.token,
            'cache-control': "no-cache"
            }

        response = requests.request("DELETE", url, headers=headers)
        return response.text

    def getAllId(self):
        js=self.getAll()
        d = []
        for t in js:
            d.append(t['_id'])
        return d

    def len(self):
        c=0;
        js=self.getAll()
        for t in js:
            c=c+1
        return c
