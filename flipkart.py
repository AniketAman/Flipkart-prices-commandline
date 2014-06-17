#flipkart Script To Get Prices from FlipKart
#url eg. http://www.flipkart.com/s?query=n&vertical=search.flipkart.com
import sys
import requests as req
import json

headers = {
	'Accept-Language':'en-US,en;q=0.5',
'Host':'www.flipkart.com',
'Referer':'http://www.flipkart.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:29.0) Gecko/20100101 Firefox/29.0',
'X-Requested-With':'XMLHttpRequest',
}
try:
 query = sys.argv[1]
except IndexError:
 print "No args passed!! Pass product name as arguments"
 exit()
url  = 'http://www.flipkart.com/s?query='+ query +'&vertical=search.flipkart.com'

getItems = req.get(url , headers = headers)
items = json.loads(getItems.text)

price = items[items.keys()[0]][3]
try:
 print '\nMatching Items :-'	
 print '1.\''+price[0][1]+'\' is available at Rs',price[0][3]
 print '2.\''+price[1][1]+'\' at Rs',price[1][3]
except IndexError:
 print "Seems your search doest'n return any reults!!! :( "
