import argparse
import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


URL_BITLY_CHECK = "https://api-ssl.bitly.com/v4/bitlinks/"


def count_click(user_bitlink, headers):
    user_bitlink = crop_url(user_bitlink)
    bitlink_params = {
        "unit": "month",
        "units": "-1",
    }
    url_count_click = f"{URL_BITLY_CHECK}{user_bitlink}/clicks/summary"
    url_count_response = requests.get(
        url_count_click, headers=headers, params=bitlink_params
    )
    url_count_response.raise_for_status()
    url_count_response_decoded = url_count_response.json()
    url_counts = url_count_response_decoded["total_clicks"]
    return url_counts


def shorten_link(url, headers):
    payload = {"long_url": url}
    json_bitly_response = requests.post(URL_BITLY_CHECK, headers=headers, json=payload)
    json_bitly_response.raise_for_status()
    json_decoded = json_bitly_response.json()
    bitlink = json_decoded["id"]
    return bitlink


def is_bitlink(is_bitlink_url):
    api_check_bitly_link = f"{URL_BITLY_CHECK}{is_bitlink_url}"
    retreive_bitlink_response = requests.get(api_check_bitly_link, headers=headers)
    return retreive_bitlink_response.ok


def validate_link(link_url):
    response = requests.get(link_url)
    response.raise_for_status()


def crop_url(url):
    parsed_url = urlparse(url)
    new_url = parsed_url.netloc + parsed_url.path
    return new_url


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["BITLY_DEVMAN_TOKEN"]
    headers = {"Authorization": f"Bearer {token}"}
    try:
        parser = argparse.ArgumentParser(description="Описание что делает программа")
        parser.add_argument("user_link", help="Ваша ссылка")
        args = parser.parse_args()
        validate_link(args.user_link)
        if is_bitlink(crop_url(args.user_link)):
            print(count_click(args.user_link, headers))
        else:
            print(shorten_link(args.user_link, headers))

    except requests.exceptions.HTTPError as error:
        exit(f"Не могу получить данные от сервера: \n {error}")

