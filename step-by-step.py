# Liberia election results

import sys
sys.path.append('/usr/lib/python2.7/dist-packages/')
from bs4 import BeautifulSoup

import urllib2
import csv
import os
import re

# set working directory:
os.chdir("/home/andrew/Dropbox/python/presentation/")

#####  Open a website ##################

# from the web:
page1 = urllib2.urlopen("http://www.necliberia.org/results2011/pp_results/09006.html")

# stored locally:
page2 = urllib2.urlopen("file:///home/andrew/Liberia/data/pp_1/03002.html")

soup = BeautifulSoup(page2)

print(soup.prettify())
print(soup.get_text())

# To get the county - find <h2> tag
h2 = soup.find_all("h2")
county = str(h2[0].get_text())
print county

# To get the precinct - find <h4>
h4 = soup.find_all("h4")
precinct = str(h4[0].get_text())
print precinct


## Now let's get the election results

res = soup.findAll('div', {'class': 'res'})
len(res) # so there are 3 results tables.

# the first results are the presidential/VP:
pres = res[0] # (python is 0 indexed)

###########   2 ways to proceed.

#### (1) use attributes to identify candidates, votes.
# Use the css class to identify candidates (note underscore):
cand = pres.find_all("td", class_="n")
print cand[7]

# For votes we could look for width="35"
vts = pres.find_all("td", width="35")
print vts[7]
print vts[7].get_text()

#### (2) using the table structure itself
# we can get the rows of the table:
rows = pres.find_all("tr")

# let's look at the 8th row:
print rows[7]

print rows[7].get_text() # just the text

# Within this row, we'll separate the cells.
# Now let's loop over rows, cols:
for row in pres.find_all("tr"):
	tds = row.find_all("td")
	try:
		a = str(tds[0].get_text())
		b = str(tds[1].get_text())
		print "Candidate:" + a 
		print "votes:" + b + "\n"
	except:
		print "bad string"
		continue


#################################################################################

### Regular expressions
s = """Before the Freedom of Information Act, I used to say at meetings, 'The illegal we do immediately; the unconstitutional takes a little longer. Kissinger, 1975"""

re.search(r'illegal', s)

# get the first undercase
word = re.search(r'[a-z]+', s)
word.group(0)

# use of pipe | for or
pc = re.search(r'(Act|longer,)', s)
pc.group(1)

# get the first word:
pc = re.search(r'([A-Za-z]+)',s)
pc.group(1)

# $ match from end
# get the last word
pc = re.search(r'([A-Za-z]+)[\w\s,]+$', s)
pc.group(1)

######### Returning to our example
# We want to get the candidate's party, lastname

ex = rows[7].get_text()

# the last name is the first all caps
m = re.search(r'([A-Z]+),', ex)
# group(0) has the full matched string
print(m.group(0))
# group(1) has the first string in parentheses:
lastname = m.group(1)
print lastname

# Now let's get the party, in caps b/w parentheses:
re.search(r'\(([A-Z]+)\)', ex)

m=re.search(r'\(([A-Z]+)\)', ex)
party = m.group(1)
print party
	

### Finally, we want to write to csv:
f= csv.writer(open("example1.csv", "w"))
f.writerow(["PresVPcand","lastname","party","votes","county","precinct"]) # Write column headers as the first line


rowout = [a, lastname, party, b, county, precinct]
print rowout


######## Other

print soup.head
print soup.title
print soup.body




		f.writerow([a, lastname, party, b, county, precinct])




####  House  ####################################
f= csv.writer(open("house.csv", "w"))
f.writerow(["HouseCandidate", "votes"]) # Write column headers as the first line

house = res[2]

for row in house.find_all("tr"):
	tds = row.find_all("td")
	try:
		a = str(tds[0].get_text())
		b = str(tds[1].get_text())

	except:
		print "bad string"
		continue

	f.writerow([a, b])





########   Senate   #####################
f= csv.writer(open("house.csv", "w"))
f.writerow(["HouseCandidate", "votes"]) # Write column headers as the first line

sen = res[1]

for row in sen.find_all("tr"):
	tds = row.find_all("td")
	try:
		a = str(tds[0].get_text())
		b = str(tds[1].get_text())
	#	c = str(tds[2].get_text())
	#	d = str(tds[3].get_text())
	except:
		print "bad string"
		continue

	f.writerow([a, b])

##########################

for res in soup.findAll('div', {'class': 'res'}):
	for row in res.find_all("tr"):
		tds = row.find_all("td")
		try:
			a = str(tds[0].get_text())
			b = str(tds[1].get_text())
			c = str(tds[2].get_text())
			d = str(tds[3].get_text())
		except:
			print "bad string"
			continue

		print ([a, b, c, d])
		f.writerow([a, b, c, d])



######################################################################
####################################################################
# approach 2

tbls = soup.find_all('table')
len(tbls)

tables = soup.find_all('table')

len(tables)

# look at:
tables[0].get_text()
tables[2].get_text()
tables[3].get_text()
tables[4].get_text()
tables[5].get_text()


# useful tables are 0, 2, 4, 6-9 as content and 5 as header


res = tbls[-2]


t0 = tables[0]
rows = t0.find_all("tr") #find all of the table rows

for row in rows:
	tds = row.find_all("td")

	try:
		a = str(tds[0].get_text())
		b = str(tds[1].get_text())
		c = str(tds[2].get_text())
		d = str(tds[3].get_text())
	except:
		print "bad string"
		continue

	print ([a, b, c, d])
	f.writerow([a, b, c, d])




###################################################

#rogue = soup.find(width="950")
#rogue.decompose()

#dat = [ map(str, row.findAll("td")) for row in res.findAll("tr") ]







f.writerow(["a", "b", "c", "d"])	# Write column headers as the first line

###### decompose unneeded tables (no unique identifying chars)

final_link = soup.p.a
final_link.decompose()

rows = soup.find_all("tr") #find all of the table rows

for row in rows:
	tds = row.find_all("td")

	try: #we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
		a = str(tds[0].get_text())
		b = str(tds[1].get_text())
		c = str(tds[2].get_text())
		d = str(tds[3].get_text())
#		e = tds[4].get_text()
#		f = tds[5].get_text()
#		g = tds[6].get_text()
#		h = tds[7].get_text()
#		i = tds[8].get_text()
	except:
		print "bad string"
		continue

	print ([a, b, c, d])
	f.writerow([a, b, c, d])



###################################################################
width="100%"

rows = soup.find_all("tr") #find all of the table rows

for row in rows:
	tds = row.find_all("td")
 
	try: #we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
		first = str(tds[0].get_text()) # This structure isolate the item by its column in the table and converts it into a string.
		second = str(tds[1].get_text())
		third = str(tds[2].get_text())
		fourth = str(tds[3].get_text())
		fifth = str(tds[4].get_text())
		sixth = tds[5].get_text()

	except:
		print "bad string"
		continue


for tr in trs:
        for link in tr.find_all('a'):
#this is a bit tricky - you are combining the search for anchor tags and the for loop in one step
		fullLink = link.get('href') #get the value of the href
 
	tds = tr.find_all("td") #run another search for all of the table data
 
	try: #we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
		names = str(tds[0].get_text()) # This structure isolate the item by its column in the table and converts it into a string.
		years = str(tds[1].get_text())
		positions = str(tds[2].get_text())
		parties = str(tds[3].get_text())
		states = str(tds[4].get_text())
		congress = tds[5].get_text() 
		
 
	except:
		print "bad tr string"
		continue #This tells the computer to move on to the next item after it encounters an error
 
	f.writerow([names, years, positions, parties, states, congress, fullLink])
