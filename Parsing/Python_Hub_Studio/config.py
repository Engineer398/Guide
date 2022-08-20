from collections import namedtuple
from fake_useragent import UserAgent

# MAIN PAGE OF SERVER
main_page = "https://scrapingclub.com"

# OBJECT PAGE - ANALIS
object_page = "https://scrapingclub.com/exercise/list_basic/?page={number_page}"

# Number of pages, need for object_page
number_of_pages = 7

# Optimized code
data = namedtuple("Data", ["name", "price", "description", "link_page", "img_link"])

# Folder with images
img_folder = "images\\"

# 1 Mbyte chunk size of img
chunk_size = 1024 * 1024

# Sleep time in seconds
sleep_time = 3

# Info about Browser
browser = UserAgent().data["browsers"]["chrome"][0]

# URL for authtorization
url_auth = "https://quotes.toscrape.com"
url_auth_login = "https://quotes.toscrape.com/login"