# __main__.py

from database.database import *
from reporting.report_generator import *
from scrapers.universalScraper import *


def main():
    print(
        f"""{Fore.MAGENTA}
 __          __    _       _____                        _  __          __ _                      _  
 \ \        / /   | |     / ____|                      | | \ \        / /(_)                    | | 
  \ \  /\  / /___ | |__  | |      _ __  __ _ __      __| |  \ \  /\  / /  _  ____ __ _  _ __  __| | 
   \ \/  \/ // _ \| '_ \ | |     | '__|/ _` |\ \ /\ / /| |   \ \/  \/ /  | ||_  // _` || '__|/ _` | 
    \  /\  /|  __/| |_) || |____ | |  | (_| | \ V  V / | |    \  /\  /   | | / /| (_| || |  | (_| | 
     \/  \/  \___||_.__/  \_____||_|   \__,_|  \_/\_/  |_|     \/  \/    |_|/___|\__,_||_|   \__,_| 

        {Style.RESET_ALL}""")
    # print("Starting WebCrawl Wizard 🧙‍♂️")

    try:
        # Database configuration
        session = init_database()
    except Exception:
        # Handling database connection error
        print("DataBase connection fail")
        exit(1)

    # Main loop of the application
    while True:
        print(f"""
Choose an option :
[{Fore.GREEN}1{Style.RESET_ALL}] : {Fore.GREEN}Scrap a website and his tree{Style.RESET_ALL}
[{Fore.BLUE}2{Style.RESET_ALL}] : {Fore.BLUE}Generate database rapport{Style.RESET_ALL}
[{Fore.RED}3{Style.RESET_ALL}] : {Fore.RED}Exit{Style.RESET_ALL}
{Style.RESET_ALL}""")
        try:
            match int(input("")):

                # Selected scraping
                case 1:
                    console_clear()
                    base_url = str(input("Enter the base URL : "))
                    crawler_level_max = int(input("Enter max crawler level : "))
                    console_clear()

                    # Data scraping from the website.
                    data_to_store = scrape_website(base_url, crawler_level_max if crawler_level_max >= 1 else 1, False)

                    if data_to_store:
                        # Storing data in the database.
                        save_data_to_database(session, data_to_store)

                # Selected report
                case 2:
                    console_clear()
                    print(f"""
Choose an option :
[{Fore.GREEN}1{Style.RESET_ALL}] : {Fore.GREEN}Generate by domain{Style.RESET_ALL}
[{Fore.BLUE}2{Style.RESET_ALL}] : {Fore.BLUE}Generate by date{Style.RESET_ALL}
                    """)

                    match int(input("")):

                        # Report related to the domain
                        case 1:
                            console_clear()
                            output_file_name = str(input("Enter the output file name [defaults : 'report'] : "))
                            console_clear()
                            print_sraping_domains(session)
                            domain_id = int(input("Enter scraping domain id for generate the report : "))
                            console_clear()

                            # Generating the report related to the domain
                            generate_report_html_by_domain(session,
                                                           output_file_name if output_file_name != "" else "report",
                                                           domain_id)

                        # Report based on the date
                        case 2:
                            console_clear()
                            output_file_name = str(input("Enter the output file name [defaults : 'report'] : "))
                            console_clear()
                            print_sraping_dates(session)
                            scraping_id = int(input("Enter scraping date id for generate the report : "))
                            console_clear()

                            # Generating the report based on the date
                            generate_report_html_by_date(session,
                                                         output_file_name if output_file_name != "" else "report",
                                                         scraping_id)

                        # Case by default
                        case _:
                            raise ValueError()

                # Exit program
                case 3:
                    exit(0)

                # Case by default
                case _:
                    raise ValueError()

        except ValueError:
            print("Invalid input")
            input("Press any key to continue:")
            console_clear()


def console_clear():
    """
    Clear the console screen.

    This function checks the operating system and uses the appropriate command to clear the console screen.
    On Windows, it uses 'cls', and on Unix-based systems, it uses 'clear'.
    """

    os.system('cls' if os.name == 'nt' else 'clear')


# Check if the file is executed as the main program; if not, do nothing
if __name__ == "__main__":
    main()
    exit(0)
