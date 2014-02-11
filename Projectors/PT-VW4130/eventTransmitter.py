import os
import sys
import urllib2, base64

# Projector PT-VW4310 config:
# 	Standby mode: Network (NOT ECO)
# 	Default Port: 80
#
# Script config:
# 	First Line: username
# 	Second Line: password

config = open("config", "r")
config_args = []

for line in config:
	config_args.append(line.strip('\n'))

if len(config_args) < 2: # Check if password is in config
	password = ''
else:
	password = config_args[1]

if len(config_args) < 1: # Check if username is in config; default to 'admin1'
	username = 'admin1'
else:
	username = config_args[0]

ip = sys.argv[1]
cmd = sys.argv[2]

def contact(n):
	request = urllib2.Request("http://" + ip + n)
	base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)   
	result = urllib2.urlopen(request)


if cmd == 'ON':
	contact('/base_conf.htm?CTL=fon')
elif cmd == 'OFF':
	contact('/base_conf.htm?CTL=foff')
elif cmd == 'RGB1':
	contact('/act.htm?SET=inp_RG1')
elif cmd == 'RGB2':
	contact('/act.htm?SET=inp_RG2')
elif cmd == 'HDMI':
	contact('/act.htm?SET=inp_HD1')
elif cmd == 'VIDEO':
	contact('/act.htm?SET=inp_VID')
elif cmd == 'SVIDEO':
	contact('/act.htm?SET=inp_SVD')
elif cmd == 'VOLUMEUP':
	contact('/act.htm?SET=vol_u')
elif cmd == 'VOLUMEDOWN':
	contact('/act.htm?SET=vol_d')
elif cmd == 'SHUTTERON':
	contact('/act.htm?SET=shut_on') # Shutter On
elif cmd == 'SHUTTEROFF':
	contact('/act.htm?SET=shut_off') # Shutter Off

# under act.htm?SET=
# img_STD
# img_REA
# img_CIN
# img_BBD
# img_CBD
# inp_SCT - ???
# inp_RG1.ORF:1 - ???




