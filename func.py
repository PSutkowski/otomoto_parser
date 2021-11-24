import yaml

def read_yml(yml_name):
    with open(yml_name, "r") as f:
        try:
            cfg = yaml.safe_load(f)
            return cfg
        except yaml.YAMLError as exc:
            raise exc(f'{yml_name} reading error')

def build_URL_from_filters(yml):
    url = "wwww.google.pl"
    return url

if __name__ == "__main__":
    build_URL_from_filters(read_yml('config.yml'))