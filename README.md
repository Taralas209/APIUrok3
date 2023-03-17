# Bitly URL Shortener and Click Counter

This is a simple Python script that allows you to shorten URLs using Bitly and check the click count for existing Bitly links. The script uses the Bitly API to interact with the service.

## Installation

To use this script, you need to have Python installed on your system. You can download the latest version of Python from the [official website](https://www.python.org/downloads/).

To install the required dependencies, run the following command:

"pip install -r requirements.txt"

## Installation

To use this script, you need to have Python installed on your system. You can download the latest version of Python from the [official website](https://www.python.org/downloads/).

To install the required dependencies, run the following command:

"pip install -r requirements.txt"


## Setup

1. Create an account on [Bitly](https://bitly.com/) and generate an access token from the [API section](https://app.bitly.com/settings/api/) in your account settings.
2. Create a `.env` file in the same directory as the script, and add the following line:

"BITLY_ACCESS_TOKEN=<your_access_token>"


Replace `<your_access_token>` with the access token you generated from Bitly.

## Usage

To use the script, open a terminal or command prompt and navigate to the directory where the script is located.

To shorten a URL, run the following command:

"python main.py --url_link <your_long_url>"

Replace `<your_long_url>` with the URL you want to shorten.

<br>

To check the click count for an existing Bitly link, run the same command with the Bitly link:

"python main.py --url_link <your_bitly_link>"

Replace `<your_bitly_link>` with the Bitly link you want to check the click count for.


## Dependencies

This script requires the following Python packages:

- python-dotenv==1.0.0
- requests==2.28.2

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).