import bs4
from time import sleep
from config import *
import requests
import xlsxwriter


def find_urls_in_page(start_page : str =object_page) -> list:
    """
    Find all card_urls in page and return by generator
    Start with 1 and end by config.number_of_pages
    :param start_page: start page
    :return: list with urls of card
    """
    for i in range(1, number_of_pages + 1):
        page = start_page.format(number_page=i)
        request = requests.get(page, headers={'User-Agent': browser})
        if request.status_code != 200:
            print(f"Bad status!!! Code: {request.status_code} Page: {page}")
            yield []

        soup = bs4.BeautifulSoup(request.text, "lxml")
        links = soup.find_all("h4", class_="card-title")
        result_links = []
        for link in links:
            result_links.append(main_page + link.find("a").get("href"))

        yield result_links


def find_data_in_page(url_cards : list) -> data:
    """
    Find all info in urls list
    :param url_cards: list of urls cards
    :return: data (watch config.py)
    """
    for url_card in url_cards:
        request = requests.get(url_card, headers={'User-Agent': browser})

        if request.status_code != 200:
            print(f"Bad status!!! Code: {request.status_code} Page: {url_card}")
            yield data(0, 0, 0, 0, 0)

        sleep(sleep_time)

        soup = bs4.BeautifulSoup(request.text, "lxml")
        name = soup.find("h3", class_="card-title").text
        price = soup.find("div", class_="card-body").find("h4").text
        description = soup.find("p", class_="card-text").text
        link_page = url_card
        img_link = main_page + soup.find("img", class_="card-img-top img-fluid").get("src")

        download_img(img_link)

        yield data(name, price, description, link_page, img_link)

def download_img(img_url : str) -> bool:
    """
    Download image from url and save it in images
    :param img_url: url of image
    :return: True - Good result or False - Bad result
    """
    request = requests.get(img_url, stream=True)
    if request.status_code != 200:
        return False

    name = img_url.split("/")[-1]
    with open(img_folder + name, "wb") as file:
        for data_block in request.iter_content(chunk_size=chunk_size):
            file.write(data_block)

def find_and_write_book():
    """
    Main function
    Find nessesary info of url pages and save in xlxs
    :return: nums of errors, 0 - no errors, > 0 - have errors
    """
    book = xlsxwriter.Workbook("Data.xlsx")
    page = book.add_worksheet("Товары")

    page.set_column("A:A", 20)
    page.set_column("B:B", 10)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)
    page.set_column("E:E", 50)

    row = 0
    column = 0
    error = 0

    for urls in find_urls_in_page(object_page):
        if not urls:
            error += 1
        for info in find_data_in_page(urls):
            if info.name != 0:
                page.write(row, column, info.name)
                page.write(row, column + 1, info.price)
                page.write(row, column + 2, info.description)
                page.write(row, column + 3, info.link_page)
                page.write(row, column + 4, info.img_link)
                row += 1
            else:
                error += 1

    book.close()
    return error

if __name__ == "__main__":
    result = find_and_write_book()
    print(f"Errors: {result}")



