import requests
import json

class SmartCenter(object):
    def __init__(self,ip,user,password,port='443',auto-publish=True):
        self.ip = ip
        self.user = user
        self.password = password
        self.port = port
        self.auto-publish = auto-publish
        self.base_url = "https://{i}:{p}/web_api/".format(i=self.ip,p=self.port)
        self.login()
        
    def login(self):
        url = "{b}login".format(b=self.base_url)
        payload = json.dumps({'user':self.user,'password':self.password})
        req = requests.post(url,verify=False,headers={'Content-Type':'application/json'},data=payload)
        dreq = json.loads(req.text)
        self.sid = dreq['sid']
        self.headers = {'Content-Type':'application/json','X-chkp-sid':self.sid}
        
    def api_call(self,command,payload={}):
        url = "{b}{c}".format(b=self.base_url,c=command)
        if isinstance(payload,dict):
            payload = json.dumps(payload)
        req = requests.post(url,verify=False,data=payload,headers=self.headers)
        if self.auto-publish:
            self.publish()
        return(json.loads(req.text))
    
    def publish(self):
        url = "{b}publish".format(b=self.base_url)
        req = requests.post(url,verify=False,data={},headers=self.headers)
        
    def logout(self):
        self.api_call('logout')