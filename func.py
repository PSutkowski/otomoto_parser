import yaml
import requests as req
from bs4 import BeautifulSoup


def read_yml(yml_name):
    with open(yml_name, "r") as f:
        try:
            cfg = yaml.safe_load(f)
            return cfg
        except yaml.YAMLError:
            return f'{yml_name} reading error'

def build_url_from_filters(yml):
    # Function builds URL to apply filtering, based on the sample below
    # https://www.otomoto.pl/osobowe?
    # search%5Bfilter_float_price%3Afrom%5D=25000
    # &search%5Bfilter_float_price%3Ato%5D=35000
    # &search%5Bfilter_float_nr_seats%5D%5B0%5D=7
    # &search%5Bfilter_float_nr_seats%5D%5B1%5D=8
    # &search%5Bfilter_float_nr_seats%5D%5B2%5D=9
    # &search%5Badvanced_search_expanded%5D=1
    prefix = 'https://www.otomoto.pl/osobowe?'
    sufix = '&search%5Badvanced_search_expanded%5D=1'
    min_price = f"search%5Bfilter_float_price%3Afrom%5D={yml['filters']['min_price']}"
    max_price = f"&search%5Bfilter_float_price%3Ato%5D={yml['filters']['max_price']}"
    seat_list = list(range(yml['filters']['min_pax'], yml['filters']['max_pax'] + 1))
    seats = [f"&search%5Bfilter_float_nr_seats%5D%5B{index}%5D={str(seatcount)}" for index,
                                                                                     seatcount in enumerate(seat_list)]
    url = prefix + min_price + max_price + ''.join(seats) + sufix
    return url

def get_full_list_of_pages(html_text):
    url_list=[first_page_url]
    #html = get_html_from_url(first_page_url)
    suffix = '&search%5Border%5D=created_at%3Adesc&page='
    soup = BeautifulSoup(html_text,'html.parser')
    my_list = soup.find_all('span',attrs={'class':'page'})
    print(my_list)
    max_page = my_list[-1].text
    print(max_page)


    return my_list


def get_html_text_from_url(url):
    response = req.get(url)
    return  response.text, response.status_code

if __name__ == "__main__":
    config_yml_object = read_yml('config.yml')
    first_page_url = build_url_from_filters(read_yml('config.yml'))
    html_text, status = get_html_text_from_url(first_page_url)
    print(f"Status code: {status}")
    print(first_page_url)
    with open("source_code_pre_first_page.txt", "w") as f:
         f.write(html_text)
    page_list = get_full_list_of_pages(html_text)
    # for page in page_list:
    #     print(page)
    #     print(page.text)

