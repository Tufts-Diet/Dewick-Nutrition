# File: json_sender.py
#
# Purpose: To post a json to localhost
#
# date: 10/15/16 
# by: Ashton Stephens
# 
# compile & run: python json_sender.py


import json			
import requests			
# Also make sure you have these libraries	
				

def main():
	
	payload = {'weenie':'nathan'}
	r = requests.post( "http://localhost:8000/post", data = json.dumps(payload) )
	print r.text

main()

# HOST A LOCALHOST LIKE THIS:
#	python -m SimpleHTTPServer
#
