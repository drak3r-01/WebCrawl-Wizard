<div align="center">
<h1> WebCrawl Wizard 🧙‍♂️</h1>

```markdown
 __          __    _       _____                        _  __          __ _                      _  
 \ \        / /   | |     / ____|                      | | \ \        / /(_)                    | | 
  \ \  /\  / /___ | |__  | |      _ __  __ _ __      __| |  \ \  /\  / /  _  ____ __ _  _ __  __| | 
   \ \/  \/ // _ \| '_ \ | |     | '__|/ _` |\ \ /\ / /| |   \ \/  \/ /  | ||_  // _` || '__|/ _` | 
    \  /\  /|  __/| |_) || |____ | |  | (_| | \ V  V / | |    \  /\  /   | | / /| (_| || |  | (_| | 
     \/  \/  \___||_.__/  \_____||_|   \__,_|  \_/\_/  |_|     \/  \/    |_|/___|\__,_||_|   \__,_|
```

  <img src="WebCrawl Wizard Image.jpg" alt="WebCrawl Wizard Image" width="400" height="400">

*Generate by [![DALL-E 3](https://img.shields.io/badge/DALL--E%203-OpenAI-%233171E3)](https://openai.com)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-4.10%2B-orange)](https://www.crummy.com/software/BeautifulSoup/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4%2B-red)](https://www.sqlalchemy.org/)
[![Jinja2](https://img.shields.io/badge/Jinja2-3.1%2B-brightgreen)](https://jinja.palletsprojects.com/)

</div>

## Overview 🌐

WebCrawl Wizard is a Python project designed to scrape data from websites, store it in a database (`mysql`),
and generate reports based on the collected information. It allows indexing all the links from a given site across
multiple specified levels of crawling. This project serves as a hands-on experience for diving into more advanced
web scraping techniques in Python.

Future enhancements are planned to refine
its capabilities further. Please refer to the "Future Improvements" section for details on the
upcoming enhancements and features.

## Disclaimers 📢

The software provided under the MIT License is offered "as is" without any warranty, express or implied. The user of
this software acknowledges and agrees that the author and contributors are not liable for any direct, indirect,
incidental, special, exemplary, or consequential damages, including, but not limited to, procurement of substitute goods
or services, loss of use, data, or profits or business interruption, however caused and on any theory of liability,
whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of
this software, even if advised of the possibility of such damage.

The user assumes all responsibility for the use and potential consequences of this software. The author disclaims any
responsibility for any improper or illegal use of the software by third parties.

By using this software, you agree to the terms of the MIT License and acknowledge the provided disclaimer.

## Installation 🛠️

To install, venv and the required dependencies, run the following command:

- Windows (CMD):

  ```bash
  python -m venv .venv && .\.venv\Scripts\activate && pip install -r requirements.txt
  ```

- MacOS/Linux :

  ```bash
  python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
  ```

- Just required dependencies :

  ```bash
  pip install -r requirements.txt
  ```

## Configuration ⚙️

1. Clone the `config.model.json` file to `config.local.json`:

    ```bash
    cp config.model.json config.local.json
    ```

2. Open `config.local.json` and customize the configuration settings according to your needs.

    ```json
    {
      "database": {
        "user": "your_username",
        "password": "your_password",
        "host": "your_database_host",
        "port": 3306,
        "name": "your_database_name",
        "charset": "utf8mb4"
      }
    }
    ```

## Usage ▶️

1. **Without venv**
    - Using the following command:

      ```bash
      python __main__.py
      ```

    - Or navigate to your project folder and run:

      ```bash
      python "yourfolder"
      ```

2. **With venv**:
    - Windows (CMD) :

      ```bash
      .venv\Scripts\activate && python __main__.py && deactivate
      ```

    - MacOS/Linux :

      ```bash
      source .venv/bin/activate && python __main__.py && deactivate
      ```

## Contributing 🤝

If you would like to contribute to this project, please follow
the [GitHub Fork & Pull Request Workflow](https://gist.github.com/Chaser324/ce0505fbed06b947d962).

## Future Enhancements 🚀

- Global code improvement for enhanced readability and maintainability in accordance with best practices.
- Addition of support for a SQLite database.
- Inclusion of more use cases.
- Code optimization.

## Changelog 📜

### V 1.0

- Initial release serving as the foundation for the project.

## License 📄

<p>
    <a property="dct:title" rel="cc:attributionURL" href="https://github.com/drak3r-01/WebCrawl-Wizard">WebCrawl-Wizard</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/drak3r-01">drak3r-01</a> is licensed under the <a href="https://opensource.org/licenses/MIT" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">MIT License</a>.
</p>
