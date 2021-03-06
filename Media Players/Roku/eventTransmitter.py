import urllib2
import sys
from selenium import webdriver
import urllib
import re

ip = '192.168.2.7'
port = '8060'
apps = {}

def contact(cmd): # Sending commands to Roku
	request = urllib2.Request('http://' + ip + ':' + port + cmd)
	request.add_data('') # Turn GET into POST
	result = urllib2.urlopen(request)
	print result.read()

def getApps(): # /query/apps requires GET - not POST
	request = urllib2.Request('http://' + ip + ':' + port + '/query/apps')
	result = urllib2.urlopen(request)
	l = []
	apps.clear() # Clear old apps out of dict

	for each in result.readlines():
		l.append(each.strip('\n'.strip('\r')))

	for line in l:
		if '<app ' in line:
			search = re.search(r'id="(\d+)"[w\W\s]*>([\w\W\s]+)<', line) # Capture any alphanumeric characters, whitespace or non-alphanumeric characters (',-) between '>' and '<'
			apps[search.group(2)] = search.group(1) #apps[appName] = appID

			#idNum = line.split('id="') [1] # Parse ID
			#idNum = line.split('"') [1]
			
			#appName = line.split('>') [1] # Parse App name
			#appName = appName.split('</app') [0]
			

def downloadImages(idNum, name):
	browser = webdriver.Chrome()
	browser.get('http://www.roku.com/channels/#!details/' + idNum)
	source = browser.page_source
	source = source.encode('utf-8').splitlines()
	browser.quit()

	link = ''

	for line in source:
		if 'http://channels.roku.com/images/' in line:
			link = line.split('src="') [1]
			link = link.split('"') [0]
			break

	name = name + '.jpg'
	urllib.urlretrieve(link, name)

def getAppImgs():
	for appName in apps:
		ID = apps[appName]
		print 'Downloading ' + appName + ' poster image...'
		downloadImages(ID, appName)
	print 'Done.'


getApps()
getAppImgs()
