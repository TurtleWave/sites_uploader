import argparse
import os.path

import cloudscraper


def write_in_file(file_path: str, file_name: str, text: str):
    with open(f'{os.path.join(file_path, file_name)}.html', 'x') as f:
        f.write(text)


def make_request(url: str):
    scraper = cloudscraper.create_scraper(
        interpreter='nodejs',
        delay=5000,
        browser={
            'browser': 'chrome',
            'platform': 'android',
            'desktop': False,
        },
        captcha = {
            'provider': '2captcha',
            'api_key': f'{os.environ.get("2CAPTCHA_API_KEY")}',
        }
    )

    return scraper.get(url).text


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-u', "--url", type=str, help="url сайта", required=True)
    arg_parser.add_argument('-d', "--dir", type=str, help="Путь для выгрузки кода")

    args = arg_parser.parse_args()

    write_in_file((lambda: os.getcwd() if args.dir is None else args.dir)(),
                  f"{args.url.split("/")[2]}", make_request(args.url))


if __name__ == '__main__':
    main()
