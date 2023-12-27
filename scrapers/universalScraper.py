# scrapers/scrapers.py
from typing import Any

import requests
from bs4 import BeautifulSoup
from colorama import Style, Fore


def scrape_website(
        url: str, crawler_level_max: int = 1,
        log_output: bool = False,
        crawler_current_level: int = 1) \
        -> list[dict[str, str | Any]] | None:
    """
    Scrape links from a website and optionally follow links to specified levels.

    :param url: The URL of the website to scrape.
    :type url: str

    :param crawler_level_max: The maximum number of levels to follow links. Defaults to 1.
    :type crawler_level_max: int

    :param log_output: Whether to log error messages. Defaults to False.
    :type log_output: bool

    :param crawler_current_level: The current level of the crawler (internal use). Defaults to 1.
    :type crawler_current_level: int

    :return: A list of dictionaries containing link information or None if an error occurs.
    :rtype: List[Dict[str, str | Any]] | None

    This function scrapes links from a website up to a specified level. It returns a list of dictionaries,
    each containing information about a link (name, URL, and site). If an error occurs during the request,
    it returns None.
    """

    # Indicates that the elements of the list are dictionaries where the keys are strings
    # and the values can be either strings or any type
    level_data: list[dict[str, str | Any]] = []

    try:
        response = requests.get(url)
        response.raise_for_status()  # We check if the query was successful
    except requests.exceptions.RequestException as err:
        if log_output:
            print(f"Erreur de requête : {err}")
        return None

    # We create a soup with the HTML if possible
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Erreur lors de l'analyse HTML : {e}")
        return None

    # We find all the links on the page
    for link in soup.find_all('a'):

        # We extract the link name (anchor text) and the URL
        # We trim anything that might exceed the fields of our table
        link_name = link.text.strip()[:512] if link.text.strip() is not None else None
        link_url = link.get('href')[:1024] if link.get('href') is not None else None

        # We ensure that the link has a name and a URL before adding it to the list
        if link_name and link_url:
            level_data.append({"name": link_name, "url": link_url, "site": url})

            # We go one level deeper if possible
            if crawler_level_max > crawler_current_level:
                lower_level_data = scrape_website(link_url, crawler_level_max, log_output, crawler_current_level + 1)
                level_data += lower_level_data if lower_level_data is not None else []

    print(
        f"End scraping {Fore.GREEN}level {crawler_current_level}{Style.RESET_ALL} of {url}, total {Fore.RED}{len(level_data)} links{Style.RESET_ALL}")
    return level_data
