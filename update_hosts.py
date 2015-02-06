import os
import sys
import urllib2

url_host = "https://raw.githubusercontent.com/racaljk/hosts/master/hosts"
pos_host = "C:\\Windows\\System32\\drivers\etc\\hosts"


fp = open(pos_host, 'w')
fp.write(urllib2.urlopen(url_host).read())
fp.close()
