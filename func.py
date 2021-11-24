import yaml

def read_yml(yml_name):
    with open(yml_name, "r") as f:
        try:
            cfg = yaml.safe_load(f)
            return cfg
        except yaml.YAMLError as exc:
            raise exc(f'{yml_name} reading error')

def build_URL_from_filters(yml):
    prefix = 'https://www.otomoto.pl/osobowe?'
    asd = yml['filters']['min_price'])
    sufix = '&search%5Badvanced_search_expanded%5D=1'
    min_price = f'search%5Bfilter_float_price%3Afrom%5D={yml['filters']['min_price']}'
    max_price = f'search%5Bfilter_float_price%3Afrom%5D={yml['filters']['max_price']}'
    seat_list = list(range(yml['filters']['min_pax'], yml['filters']['max_pax'] + 1))
    seats = [f'&search%5Bfilter_float_nr_seats%5D%5B{index}%5D='{str(seatcount)} for index,seatcount in enumerate(seat_list)]
    url =  prefix + min_price + max_price + seats +suffix
        # https://www.otomoto.pl/osobowe?
        # search%5Bfilter_float_price%3Afrom%5D=25000
        # &search%5Bfilter_float_price%3Ato%5D=35000
        # &search%5Bfilter_float_nr_seats%5D%5B0%5D=7
        # &search%5Bfilter_float_nr_seats%5D%5B1%5D=8
        # &search%5Bfilter_float_nr_seats%5D%5B2%5D=9
        # &search%5Badvanced_search_expanded%5D=1
    return url

if __name__ == "__main__":
    build_URL_from_filters(read_yml('config.yml'))