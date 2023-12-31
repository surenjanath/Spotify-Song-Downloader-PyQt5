# Spotify Song Downloader with Python and PyQt5

![image](https://github.com/surenjanath/Spotify-Song-Downloader-PyQt5/assets/42503383/c0d34f74-2545-4b5b-aa3f-de1bc6a33321)

DOWNLOAD LINK : [HERE MEGA.NZ](https://mega.nz/file/dpI0RAYC#8wnn8iqDa1BXgQQRUn7vU2-1kOzyqF-Dm7FWgsF4V10)

## Updates
- v2.1.2 **Release** 13th December 2023
  - Removed old API Method
  - Removed Progress Bar functionality due to stream method for downloading
  - Fix Downloading and addressed some issues.
  - New download link. here : https://mega.nz/file/dpI0RAYC#8wnn8iqDa1BXgQQRUn7vU2-1kOzyqF-Dm7FWgsF4V10
    
- v2.1.1  19th October 2023
  - Fixed API Paths
  
- v2.1 Stop Working [ 19th October 2023 ]
  
- v2.1 
  - Added Song Metadata such as song cover, artist, title and song release date
    
- v2.0
  - Added Progress bar and interface to view songs as it is being downloaded.
  - Used v2 method for 320 kbps songs and if not available will revert to 128 kbps
  - **Release**
  - version 2.0 is in the same mega download link below.
  - To get v2.0 files, use the release feature on the right side of the repository named : [Release](https://github.com/surenjanath/Spotify-Song-Downloader-PyQt5/releases/tag/SpotifyDownloader2.0)
    
- v1.0
  - Released
  
## Introduction

In this project, we have created a Spotify song downloader using Python and PyQt5. The application allows users to download their favorite Spotify songs by providing the playlist link. We utilize web scraping techniques to extract the song data and PyQt5 for building an interactive and user-friendly desktop application.<br>
This is the code for the User Interface.<br>

## Spotify Song Downloader EXE
You can find the program here also version 2.1.1 : [https://mega.nz/file/wpwyzLaD#P--jbIUIlnyoDLblzXPsXRVrfh6Q5zl9QubUMDSQ5_k](https://mega.nz/file/wpwyzLaD#P--jbIUIlnyoDLblzXPsXRVrfh6Q5zl9QubUMDSQ5_k) <br>
Please note that your antivirus may be triggered but I Guarantee you, there are no malicious activity in the exe file. You can recreate it base on this code in this repository.
Do Let me know if the Link is Live Still.

## How it Works

The Spotify song downloader uses web scraping to interact with a specific website and extract song information, including the song title, artists, and YouTube ID. It then utilizes the YouTube ID to generate Analyze and Conversion IDs, which are used to download the songs. The PyQt5 interface allows users to input the Spotify playlist link, view real-time download progress, and receive updates on the downloaded songs.


### Pictures of V2.1
![image](https://github.com/surenjanath/Spotify-Song-Downloader-PyQt5/assets/42503383/ad3d0d23-1005-49c1-b5c4-e8f2ee8f8094)

![image](https://github.com/surenjanath/Spotify-Song-Downloader-PyQt5/assets/42503383/e0bda50b-edea-4651-8d78-0f3c403b59a9)

![image](https://github.com/surenjanath/Spotify-Song-Downloader-PyQt5/assets/42503383/662093f2-fdaa-4cc5-af9a-f2d195f5165d)




### Youtube Demo for v2.1
[![Spotify Downloader Demo](https://img.youtube.com/vi/zVZHIXqoMSU/0.jpg)](https://www.youtube.com/watch?v=zVZHIXqoMSU)



### Medium article For this : 
- [Building an Interface for our Spotify Song Downloader with PyQt5](https://surenjanath.medium.com/building-an-interface-for-our-spotify-song-downloader-with-pyqt5-fa0442909be9)

## Features to Add [ Completed ]

- Proper Error handing in v2 using Spotifydown New API [ Easy Mode ] ✓
  With this new implementation the program will download songs at 320 kbps instead of 128 kbps but if an error occurs it will fall back to 128 kbps. ✓
- MP3 metadata such as song cover, artists, album and release date. ✓
- Each Playlist in separate folders instead of the main music folder ✓
  
## Requirements

- Python 3.x
- PyQt5
- requests
- string
- re
- mutagen

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


### Please Note Your Antivirus would do this : 
1. ![image](https://github.com/surenjanath/Spotify-Song-Downloader-PyQt5/assets/42503383/aa510f72-07ce-440f-8bf0-0ee2e5d7f192)

2. ![image](https://github.com/surenjanath/Spotify-Song-Downloader-PyQt5/assets/42503383/01b561fe-753a-4af1-85c8-f035ef4282e8)

It's a false detection.

Also if you are not able to download any songs, try using a vpn and see if that helps. If not then let me know in the issues section.

## ToC
Please use it to download Copyright Free Music on Spotify<br/>
For example : https://open.spotify.com/playlist/3fQ6EJdy6n1kF4Yw5bTAVx?si=2f26056713504154

## Author

- [Surenjanath Singh](https://github.com/surenjanath)

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

Please use the Spotify song downloader responsibly and respect copyright laws. Only download songs that you have the rights to use.


PS : CREATED TO DOWNLOAD COPYRIGHT FREE MUSIC
