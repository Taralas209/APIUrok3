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
        "domain": "bit.ly",
        "title": custom_title
    }
    response_post = requests.post(bitly_linkshortener_url, headers=headers, json=payload)
    response_post.raise_for_status()
    return response_post.json()['link']

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
    response_count = requests.get(bitly_linkcounter_url, headers=headers, params=payload)
    response_count.raise_for_status()
    return response_count.json()['total_clicks']

def is_bitlink(link, access_token):
    parsed_link = urlparse(link)
    modified_link = parsed_link.netloc + parsed_link.path
    bitly_linkstatus_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(modified_link)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response_link = requests.get(bitly_linkstatus_url, headers=headers)
    return response_link.ok


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url_link', type=str, help='Введите ссылку', default='test.test')
    args = parser.parse_args()
    link = args.url_link
    return link

def main():
    load_dotenv()
    access_token = os.environ.get('BITLY_ACCESS_TOKEN')
    link = createParser()
    try:
        if is_bitlink(link, access_token):
            clicks_count = count_link_clicks(link, access_token)
            print(clicks_count)
        else:
            shorten_link(link, access_token)
            custom_title = input('Дайте название вашему битлинку:')
            shortened_link = shorten_link(link, access_token, custom_title)
            print(shortened_link)
    except requests.exceptions.HTTPError as error:
         print(f"HTTP error occurred: {error}")

if __name__ =="__main__":
    main()


    