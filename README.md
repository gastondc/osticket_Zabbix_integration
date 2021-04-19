# osticket_Zabbix_integration

source: http://sirlagz.net/2016/08/10/integrating-zabbix-with-osticket/

It was necessary to edit the code to be able to use it.

0 ) Check script conf: 

/* data = {
"name":"Zabbix",
"email":"zabbix@<YOURDOMAIN>",
"phone":"111111111111",
"subject":args.summary,
"message":args.detail,
"topicId":"Zabbix",
"empresa":"Zabbix"
}
*/

** Configure according to your osticket configuration.


1 ) Copy alertscript.py   alertscripts/

In Zabbix default installations it can be in:

/usr/lib/zabbix/alertscripts

2 )permit execute: 

chmod +x alertscript.py


3) In Zabbix -> Administration -> Medita Type

4 ) Create media type

![image](https://user-images.githubusercontent.com/10785756/115292606-9677d200-a12c-11eb-90d2-fc2b4fcdce01.png)

5) Create parameters. 

6) Create message templates:

![image](https://user-images.githubusercontent.com/10785756/115292732-bc04db80-a12c-11eb-8400-3b9371d59f01.png)

Use default configuration. 
