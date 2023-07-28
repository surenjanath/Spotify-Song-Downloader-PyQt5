# Spotify Song Downloader with Python and PyQt5

![image](https://github.com/surenjanath/Spotify-Song-Downloader-PyQt5/assets/42503383/c0d34f74-2545-4b5b-aa3f-de1bc6a33321)

## Introduction

In this project, we have created a Spotify song downloader using Python and PyQt5. The application allows users to download their favorite Spotify songs by providing the playlist link. We utilize web scraping techniques to extract the song data and PyQt5 for building an interactive and user-friendly desktop application.<br>
This is the code for the User Interface.<br>

## Spotify Song Downloader EXE
You can find the program here : [https://mega.nz/folder/hw4R3KRK#qAepUHnE5QoQPxUCSTak8g](https://mega.nz/folder/hw4R3KRK#qAepUHnE5QoQPxUCSTak8g) <br>
Please note that your antivirus may be triggered but I Guarantee you, there are no malicious activity in the exe file. You can recreate it base on this code in this repository.
Do Let me know if the Link is Live Still.

## How it Works

The Spotify song downloader uses web scraping to interact with a specific website and extract song information, including the song title, artists, and YouTube ID. It then utilizes the YouTube ID to generate Analyze and Conversion IDs, which are used to download the songs. The PyQt5 interface allows users to input the Spotify playlist link, view real-time download progress, and receive updates on the downloaded songs.

### Medium article For this : 
- [Building an Interface for our Spotify Song Downloader with PyQt5](https://surenjanath.medium.com/building-an-interface-for-our-spotify-song-downloader-with-pyqt5-fa0442909be9)

## Requirements

- Python 3.x
- PyQt5
- requests
- string
- re

## Installation

1. Clone the repository: `git clone https://github.com/surenjanath/Spotify-Song-Downloader-PyQt5.git 
cd spotify-song-downloader`
2. Install the required libraries

2. Enter the Spotify playlist link and press Enter.

3. The application will start scraping the website and downloading the songs to a local folder named "music."

## Folder Structure

- `main.py`: The main script to run the Spotify song downloader.
- `Template.ui`: The UI template file created using Qt Designer.
- `scraper.py`: Contains the MusicScraper class with web scraping functions.
- `scraper_thread.py`: Contains the ScraperThread class for handling web scraping in a separate thread.

## Author

- [Surenjanath Singh](https://github.com/surenjanath)

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

Please use the Spotify song downloader responsibly and respect copyright laws. Only download songs that you have the rights to use.
