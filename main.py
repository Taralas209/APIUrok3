import os
import requests
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(link, access_token, custom_title):
    bitly_linkshortener_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    payload = {
        "long_url": link,
        "title": custom_title
    }
    shortened_link_response = requests.post(bitly_linkshortener_url, headers=headers, json=payload)
    shortened_link_response.raise_for_status()
    return shortened_link_response.json()['link']


def count_link_clicks(link, access_token):
    parsed_link = urlparse(link)
    bitly_linkcounter_url = 'https://api-ssl.bitly.com/v4/bitlinks/bit.ly{}/'\
                'clicks/summary'.format(parsed_link.path)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    payload = {
        "units": "-1"
    }
    clicks_summary_response = requests.get(bitly_linkcounter_url, headers=headers, params=payload)
    clicks_summary_response.raise_for_status()
    return clicks_summary_response.json()['total_clicks']


def is_bitlink(link, access_token):
    parsed_link = urlparse(link)
    modified_link = f"{parsed_link.netloc}{parsed_link.path}"
    bitly_linkstatus_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(modified_link)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    linkstatus_response = requests.get(bitly_linkstatus_url, headers=headers)
    return linkstatus_response.ok


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--link', type=str, help='Введите ссылку', default='test.test')
    parser.add_argument('--link_title', type=str, help='Введите название ссылки', default='another bitlink')
    return parser.parse_args()


def main():
    load_dotenv()
    access_token = os.environ['BITLY_ACCESS_TOKEN']
    parser  = create_parser()
    link = parser.link
    link_title = parser.link_title
    try:
        if is_bitlink(link, access_token):
            clicks_count = count_link_clicks(link, access_token)
            print(clicks_count)
        else:
            shortened_link = shorten_link(link, access_token, link_title)
            print(shortened_link)
    except requests.exceptions.HTTPError as error:
         print(f"HTTP error occurred: {error}")


if __name__ =="__main__":
    main()


    