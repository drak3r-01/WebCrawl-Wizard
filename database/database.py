# database/database.py
import json
import os
from typing import Any

import tldextract
from colorama import Fore, Style
from mysql.connector import ProgrammingError
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker, Session

from .models import *


def init_database() -> Session:
    """
    Initialize the database and return a session.

    :return: A SQLAlchemy session connected to the initialized database.
    :rtype: Session

    This function reads database configuration from a JSON file, creates tables, and returns a connected session.
    """

    # We load the information from the JSON file.
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../config.local.json'), 'r') as config_file:
        config = json.load(config_file)
        print("BD Config loaded")

    # We access the information from the database from the JSON.
    db_config = config.get('db_config', {})
    db_user = db_config.get('user', '')
    db_password = db_config.get('password', '')
    db_host = db_config.get('host', '')
    db_port = db_config.get('port', 3306)
    db_name = db_config.get('name', '')

    # Using the Connection URL for SQLAlchemy.
    db_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(db_url)

    try:
        # Attempt to create tables.
        Base.metadata.create_all(engine)
        print("The database has been created successfully.")
    except ProgrammingError as e:
        print(f"The database already exists. Error message :{e}")

    session = sessionmaker(bind=engine)
    print("Connected to database")
    return session()


def save_data_to_database(session: Session, data: list[dict[str, str | Any]]) -> None:
    """
    Save data to the database.

    :param session: The SQLAlchemy session.
    :type session: Session

    :param data: List of dictionaries containing link information.
    :type data: List[Dict[str, str | Any]]

    :return: None

    This function saves link data to the database, creating Sites, Domains, and Links as needed.
    """

    print("Saving data to database")
    # We retrieve the current date and time for the DateScraping table.
    current_date = datetime.now()

    # We add an instance of DateScraping.
    scraping_date = ScrapingDate(datetime=current_date)

    # We add the scraping date to the session.
    session.add(scraping_date)
    session.commit()

    row_saved = 0
    # We iterate through the data and add them to the Link table.
    for entry in data:
        name = entry.get("name")
        url = entry.get("url")
        site = entry.get("site")

        # We check if the site exists.
        try:
            existing_site = session.query(Sites).filter_by(name=site).one()
        except NoResultFound:

            domain = tldextract.extract(site).domain
            # We check if the domain exists.
            try:
                existing_domain = session.query(Domains).filter_by(name=domain).one()

            except NoResultFound:
                # The domain doesn't exist yet, we add it.
                new_domain = Domains(name=domain)
                session.add(new_domain)
                session.commit()

                # The site doesn't exist yet, we add it with the new domain
                new_site = Sites(name=site, domain=new_domain)
                session.add(new_site)
                session.commit()

                # We use the new site and domain to create the link
                link = Links(name=name, url=url, datetime=scraping_date, site=new_site)

            else:
                # The site doesn't exist yet, we add it with the existing domain
                new_site = Sites(name=site, domain=existing_domain)
                session.add(new_site)
                session.commit()

                link = Links(name=name, url=url, datetime=scraping_date, site=new_site)

        else:
            # The site already exists, we use it to create the link
            link = Links(name=name, url=url, datetime=scraping_date, site=existing_site)

        # We add the link to the session
        session.add(link)
        print(
            f"{Fore.GREEN}Save to database pourcent : {Fore.RED}{round(row_saved * 100 / len(data), 2)}%{Style.RESET_ALL}",
            end="\r")
        row_saved += 1

        # We save regularly to prevent a crash
        if row_saved % 100 == 0:
            session.commit()

    # We commit the latest changes
    session.commit()
    print(f"\n{Fore.RED}{len(data)} links{Style.RESET_ALL} are saved into the database")

    return None


def print_sraping_dates(session: Session) -> None:
    """
    Print information about scraping dates.

    :param session: The SQLAlchemy session.
    :type session: Session

    :return: None

    This function retrieves all scraping dates from the database and prints their information, including
    the ID and date.
    """

    # We retrieve all dates sorted by ID
    scraping_date = session.query(ScrapingDate).order_by(ScrapingDate.id).all()
    for date in scraping_date:
        print(
            f"{Fore.GREEN}ID : {Fore.RED}{date.id}{Style.RESET_ALL} | {Fore.GREEN}Scraping date: {Fore.RED}{date.datetime}{Style.RESET_ALL}")
    return None


def print_sraping_domains(session: Session) -> None:
    """
    Print information about scraping domains.

    :param session: The SQLAlchemy session.
    :type session: Session

    :return: None

    This function retrieves all scraping domains from the database and prints their information, including
    the ID and name.
    """

    # We retrieve all domains sorted by ID
    scraping_domains = session.query(Domains).order_by(Domains.id).all()
    for domain in scraping_domains:
        print(
            f"{Fore.GREEN}ID : {Fore.RED}{domain.id}{Style.RESET_ALL} | {Fore.GREEN}Domain: {Fore.RED}{domain.name}{Style.RESET_ALL}")
    return None
