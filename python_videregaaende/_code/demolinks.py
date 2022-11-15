# Imports
import requests
import re
import argparse

# Paser
parser = argparse.ArgumentParser(
    description="Get list of links from a website"
)
 
parser.add_argument("url", nargs="?", help="URL", default=None)
 
arguments = parser.parse_args()
 
use_arguments = True if arguments.url is not None else False
 
# Check om det en URL
if use_arguments:
    url = arguments.url
else:
    while True:
        url = input("Enter the URL: ")
 
        if url == "":
            print("Invalid URL")
            continue
        break
 
html = requests.get(url).text
 
links = re.findall('"(https?://.*?)"', html)

# Print URL'er
for link in links:
    print(link)