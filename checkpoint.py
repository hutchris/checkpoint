import requests
import json

class SmartCenter(object):
    def __init__(self,ip,user,password,port='443',autopublish=True):
        self.ip = ip
        self.user = user
        self.password = password
        self.port = port
        self.autopublish = autopublish
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
        success,resp = self.parse_resp(req)
        if not success:
            if resp == 'generic_err_wrong_session_id':
                self.login()
                req = requests.post(url,verify=False,data=payload,headers=self.headers)
                success,resp = self.parse_resp(req)
        if success and self.autopublish:
            self.publish()
        return(resp)
        
    def parse_resp(self,req):
        resp = json.loads(req.text)
        if 'code' in resp.keys():
            out = resp['code']
            success = False
        else:
            out = resp
            success = True
        return(success,out)
                
    def publish(self):
        url = "{b}publish".format(b=self.base_url)
        req = requests.post(url,verify=False,data='{}',headers=self.headers)
    
    def discard(self):
        url = "{b}discard".format(b=self.base_url)
        req = requests.post(url,verify=False,data='{}',headers=self.headers)
        
    def logout(self):
        self.api_call('logout')
        
    def get_host_by_ip(self,ip):
        hostsResp = self.api_call('show-hosts')
        hosts = hostsResp['objects']
        host = [h for h in hosts if h['ipv4-address'] == ip]
        return(host)
        
    def install_policy(self,access=True,threatPrevention=True,targets=[]):
        payload = {'access':access,'threat-prevention':threatPrevention,'policy-package':'standard'}
        if targets:
            payload['targets'] = targets
        resp = self.api_call('install-policy',payload)
        return(resp)