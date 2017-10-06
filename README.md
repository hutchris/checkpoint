# checkpoint
Python class for interacting with Checkpoint R80.10+ SmartCenter

This makes interacting the the SmartCenter API much simpler. You can use the API to modify firewall policy, objects VPN etc. API documentation can be found here: https://sc1.checkpoint.com/documents/latest/APIs/index.html#introduction~v1.1

Example usage:
```
from checkpoint import SmartCenter

sc = SmartCenter('10.1.1.1','username','password')
payload = {'parametername':'parametervalue'}
command_output = sc.api_call('command',payload)
```
```
sc = SmartCenter('10.1.1.1','username','password')
payload = {'name': 'hostname', 'ip-address': '10.2.2.2', 'comments': 'Test Device Being Added'}
output = sc.api_call('add-host',payload)
```

You can set auto-publish=False when initializing the object:
```
sc = SmartCenter('10.1.1.1','username','password',autopublish=False)
```
which will add any changes you make to your "session". You can view changes to be published with the api_call command: show-session. You can cancel changes by using the command: discard.

To publish you changes run:
```
sc.api_call('publish')

```
