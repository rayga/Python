import requests
import sys

url = sys.argv[1]
init = "'"

print "Testing "+url
first = requests.post(url+init)

if "mysql" in first.text.lower():
	print "Injectable MySQL detected"
elif "native client" in first.text.lower():
	print "Injectable MSQL detected"
elif "syntax error" in first.text.lower():
	print "Injectable PostGRES detected"
elif "ORA" in first.text.lower():
	print "Injectable Oracle detected"
elif "warning" in first.text.lower():
	print "This site vulnerable with SQL"
else:
	print "Not Injectable J J"

