<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/johnentrieri/li-kick-scraper">
    <img src="images/likick-logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">LI Kick Scraper</h3>

  <p align="center">
    Scrapes LI Kick site & notifies users when a new event has been posted
    <br />
    <a href="https://github.com/johnentrieri/li-kick-scraper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/johnentrieri/li-kick-scraper/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/johnentrieri/li-kick-scraper/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Project was built using:
* [Python 3](https://www.python.org/)
  * [Requests](https://pypi.org/project/requests/)
  * [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
  * [MariaDB](https://pypi.org/project/mariadb/)
* [Docker](https://www.docker.com/)
* [PushBullet](https://www.pushbullet.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

Project relies on a running [MariaDB](https://mariadb.com/) with a database already established for storing persistent event data. 

Project also relies on [Pushbullet](https://www.pushbullet.com/) with a mobile device linked for sending notifications via SMS.

Once account is created and a phone device is linked, access token can via the [Account Settings](https://www.pushbullet.com/#settings/account) page.

Once access token is generated, a [GET request](https://docs.pushbullet.com/#list-devices) can be made to https://api.pushbullet.com/v2/devices to obtain Device ID for mobile device to send texts.

If running locally as a python script, ensure environment variables are set as follows:

```sh
# Database Info
DB_USER=mariadb_username
DB_PASSWORD=mariadb_username
DB_HOST=mariadb_hostname/IP
DB_PORT=mariadb_portnumber
DB_DATABASE=mariadb_database_name

# Pushbullet Info
PB_ACCESS_TOKEN=pushbullet_access_token
PB_PHONE_DEVICE_ID=pushbullet_device_id
PB_ADDRESS=recipient_phone_number
  ```

### Python Installation & Usage

1. Install Python Dependencies:
    ```sh
   pip install -r requirements.txt
   ```
2. Run the application
   ```sh
   python app.py
    ```

### Docker Installation & Usage

1. Build Docker Image:
    ```sh
   docker build -t likickscraper:latest
   ```
2. Run the image (setting environment variables)
    ```sh
    docker run --rm --env DB_USER=mariadb_username --env DB_PASSWORD=mariadb_username --env DB_HOST=mariadb_hostname/IP --env DB_PORT=mariadb_portnumber --env DB_DATABASE=mariadb_database_name --env PB_ACCESS_TOKEN=pushbullet_access_token --env PB_PHONE_DEVICE_ID=pushbullet_device_id --env PB_ADDRESS=recipient_phone_number likickscraper:latest
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/johnentrieri/li-kick-scraper.svg?style=for-the-badge
[contributors-url]: https://github.com/johnentrieri/li-kick-scraper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/johnentrieri/li-kick-scraper.svg?style=for-the-badge
[forks-url]: https://github.com/johnentrieri/li-kick-scraper/network/members
[stars-shield]: https://img.shields.io/github/stars/johnentrieri/li-kick-scraper.svg?style=for-the-badge
[stars-url]: https://github.com/johnentrieri/li-kick-scraper/stargazers
[issues-shield]: https://img.shields.io/github/issues/johnentrieri/li-kick-scraper.svg?style=for-the-badge
[issues-url]: https://github.com/johnentrieri/li-kick-scraper/issues
[def]: python-installation-&-usag