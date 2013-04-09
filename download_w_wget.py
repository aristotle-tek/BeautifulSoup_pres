import os


os.chdir("/home/andrew/Dropbox/python/7/")

os.system("wget --convert-links --no-clobber \
--wait=4 \
--limit-rate=10K \
--random-wait -r --no-parent http://www.necliberia.org/results2011/results.html")
