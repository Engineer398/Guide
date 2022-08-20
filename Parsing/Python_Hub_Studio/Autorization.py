from config import url_auth, browser, url_auth_login
import requests
from time import sleep
from bs4 import BeautifulSoup
from requests import Session

work = Session()
work.get(url_auth, headers={'User-Agent': browser})
response = work.get(url_auth_login, headers={'User-Agent': browser})

soup = BeautifulSoup(response.text, "lxml")
token = soup.find("form").find("input").get("value")

data = {"csrf_token" : token, "username" : "tst_username", "password" : "tst_password"}

result = work.post(url_auth_login, headers={'User-Agent': browser}, data=data, allow_redirects=True)
print(result.text)


