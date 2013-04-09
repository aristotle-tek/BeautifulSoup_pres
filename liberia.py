# Liberia election results

import sys
sys.path.append('/usr/lib/python2.7/dist-packages/')
from bs4 import BeautifulSoup

import urllib2
import csv
import os
import re

os.chdir("/home/andrew/Dropbox/python/presentation/")

########   Pres/VP   #####################
f= csv.writer(open("presidential_res.csv", "w"))
f.writerow(["PresVPcand","lastname","party","votes","county","precinct"]) # Write column headers as the first line

#orig
page1 = urllib2.urlopen("http://www.necliberia.org/results2011/pp_results/03002.html")
page2 = urllib2.urlopen("http://www.necliberia.org/results2011/pp_results/09006.html")

pages = [page1, page2]

for page in pages:
	soup = BeautifulSoup(page)

	# h2 - has county
	h2 = soup.find_all("h2")
	county = str(h2[0].get_text())

	#h4 has voting precinct.
	h4 = soup.find_all("h4")
	precinct = str(h4[0].get_text())

	# get the results tables
	res = soup.findAll('div', {'class': 'res'})

	pres = res[0]

	for row in pres.find_all("tr"):
		tds = row.find_all("td")
		try:
			a = str(tds[0].get_text())
			b = str(tds[1].get_text())

		except:
			print "bad string"
			continue

		m = re.search(r'\(([A-Z]+)\)', a)
		if m:
			party = m.group(1)

		else:
			party = ''
		
		m = re.search(r'([A-Z]+),', a)
		if m:
			lastname = m.group(1)
		else:
			lastname = ''

		f.writerow([a, lastname, party, b, county, precinct])
