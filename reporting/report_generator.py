# reporting/report_generator.py
import os

from jinja2 import Environment, FileSystemLoader

from database.models import *


def generate_report_html_by_date(session, output_file_name: str = "report", report_date_id: int = 1) -> None:
    """
    Generate an HTML report based on data related to a specific date.

    :param session: The SQLAlchemy session.
    :type session: Session

    :param output_file_name: The name of the output HTML file. Defaults to "report".
    :type output_file_name: str

    :param report_date_id: The date ID for which to generate the report. Defaults to 1.
    :type report_date_id: int

    :return: None

    This function retrieves relevant data from the database, uses Jinja2 templates to generate an HTML report,
    and saves the report to a specified file.
    """

    print("Get data from database")

    # We retrieve relevant data from the database
    # We retrieve all links corresponding to date_id
    links = (session
             .query(Links)
             .filter(Links.date_id == report_date_id)
             .all()
             )

    # We retrieve all distinct sites linked to these links.
    sites = (session
             .query(Sites)
             .join(Links).filter(Links.date_id == report_date_id)
             .distinct(Sites.id)
             .all()
             )

    # We retrieve all distinct domains linked to these sites.
    domains = (session
               .query(Domains)
               .join(Sites)
               .join(Links).filter(Links.date_id == report_date_id)
               .distinct(Domains.id)
               .all()
               )

    # We use Jinja2 to generate the HTML report
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    template = env.get_template('report_template.html.twig')

    print("Generating report")
    # We render the template with the data
    rapport = template.render(links=links, sites=sites, domains=domains)

    print("Export report")
    # We save the report to a file
    output_file_name = f"{output_file_name}.html"
    output_folder_name = 'output_rapport'
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", output_folder_name, output_file_name)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rapport)

    return None


def generate_report_html_by_domain(session, output_file_name: str, domain_id: int = 1) -> None:
    """
    Generate an HTML report based on data related to a specific domain.

    :param session: The SQLAlchemy session.
    :type session: Session

    :param output_file_name: The name of the output HTML file. Defaults to "report".
    :type output_file_name: str

    :param domain_id: The domain ID for which to generate the report. Defaults to 1.
    :type domain_id: int

    :return: None

    This function retrieves relevant data from the database, uses Jinja2 templates to generate an HTML report,
    and saves the report to a specified file.
    """

    print("Get data from database")

    # We retrieve relevant data from the database
    # We retrieve the domain
    domain = (
        session.query(Domains)
        .filter(Domains.id == domain_id)
    )

    # We retrieve all sites corresponding to the domain
    sites = (
        session.query(Sites)
        .join(Domains, Domains.id == Sites.domain_id)
        .filter(Domains.id == domain_id)
        .distinct(Sites.id)
        .all()
    )

    # We retrieve all links corresponding to the sites
    links = (
        session.query(Links)
        .join(Sites, Sites.id == Links.site_id)
        .join(Domains, Domains.id == Sites.domain_id)
        .filter(Domains.id == domain_id)
        .all()
    )

    # We use Jinja2 to generate the HTML report
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    template = env.get_template('report_template.html.twig')

    print("Generating report")
    # We render the template with the data
    rapport = template.render(links=links, sites=sites, domains=domain)

    print("Export report")
    # We save the report to a file
    output_file_name = f"{output_file_name}.html"
    output_folder_name = 'output_rapport'
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", output_folder_name, output_file_name)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rapport)

    return None
