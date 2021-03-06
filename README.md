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

The autopublish parameter is set to True by default. This means after each api_call the changes will be commited to the config. You can set auto-publish=False when initializing the object:
```
sc = SmartCenter('10.1.1.1','username','password',autopublish=False)
```
which will add any changes you make to your "session". You can view changes to be published with the api_call command: show-session. You can cancel changes by using the command: discard.

To publish you changes run:
```
sc.publish()

```

Once your changes are published you can install the policy to your gateways. The method:
```
sc.install_policy()
```
Will install both access and thread-prevention policies to all gateways. You can modify the default parameters:
```
sc.install_policy(access=True,threatPrevention=False,targets=['firewall1','firewall2'])
```
