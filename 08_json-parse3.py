# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:23:00 2019

@author: CEC
"""
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "BHxAJJA6TCZNxekmKrBBBSGSoZiSq6bK"

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")