from bs4 import BeautifulSoup
import requests

urls = {"https://google.com", "https://facebook.com", "https://yahoo.com"}

#read a file

with open("top_100.csv") as f:
    data = f.read()
lines = data.split("\n")
# print(lines)

for line in lines:
    url = "https://"+line.split(",")[1]
    # print(url)

    try:
        print(f"🚀 URL: {url}")
        r = requests.get(url)
        # print(url)
        # print(r.text)
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.get_text()
        headers = r.headers
        if headers.get('x-powered-by', None) is None:
            print(" No x-powered-by header availabe to track the tech")

        # print(title)
        # print(r.text)
    except Exception as e:
        print("We couldn't figure the tech used")