
# Main
# if __name__ == '__main__':from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import  QCursor
from Template import Ui_MainWindow

import sys
import os
import string
import requests
import re
import webbrowser


class MusicScraper(QThread):
    song_downloaded = pyqtSignal(str)
    count_updated = pyqtSignal(int)



    def __init__(self):
        super(MusicScraper, self).__init__()
        self.counter = 0  # Initialize the counter to zero
        self.session = requests.Session()

    def get_ID(self, yt_id):
        # The 'get_ID' function from your scraper code
        LINK = f'https://api.spotifydown.com/getId/{yt_id}'
        headers = {
            'authority': 'api.spotifydown.com',
            'method': 'GET',
            'path': f'/getId/{id}',
            'origin': 'https://spotifydown.com',
            'referer': 'https://spotifydown.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-fetch-mode': 'cors',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        response = self.session.get(url=LINK, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        return None

    def generate_Analyze_id(self, yt_id):
        # The 'generate_Analyze_id' function from your scraper code
        DL = 'https://corsproxy.io/?https://www.y2mate.com/mates/analyzeV2/ajax'
        data = {
            'k_query': f'https://www.youtube.com/watch?v={yt_id}',
            'k_page': 'home',
            'hl': 'en',
            'q_auto': 0,
        }
        headers = {
            'authority': 'corsproxy.io',
            'method': 'POST',
            'path': '/?https://www.y2mate.com/mates/analyzeV2/ajax',
            'origin': 'https://spotifydown.com',
            'referer': 'https://spotifydown.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-fetch-mode': 'cors',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        RES = self.session.post(url=DL, data=data, headers=headers)
        if RES.status_code == 200:
            return RES.json()
        return None

    def generate_Conversion_id(self, analyze_yt_id, analyze_id):
        # The 'generate_Conversion_id' function from your scraper code
        DL = 'https://corsproxy.io/?https://www.y2mate.com/mates/convertV2/index'
        data = {
            'vid'   : analyze_yt_id,
            'k'     : analyze_id,
        }
        headers = {
            'authority': 'corsproxy.io',
            'method': 'POST',
            'path': '/?https://www.y2mate.com/mates/analyzeV2/ajax',
            'origin': 'https://spotifydown.com',
            'referer': 'https://spotifydown.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-fetch-mode': 'cors',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        RES = self.session.post(url=DL, data=data, headers=headers)
        if RES.status_code == 200:
            return RES.json()
        return None

    def get_PlaylistMetadata(self, Playlist_ID):
        # The 'get_PlaylistMetadata' function from your scraper code
        URL = f'https://api.spotifydown.com/metadata/playlist/{Playlist_ID}'
        headers = {
            'authority': 'api.spotifydown.com',
            'method': 'GET',
            'path': f'/metadata/playlist/{Playlist_ID}',
            'scheme': 'https',
            'origin': 'https://spotifydown.com',
            'referer': 'https://spotifydown.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }
        meta_data = self.session.get(headers=headers, url=URL)
        if meta_data.status_code == 200:
            return meta_data.json()['title'] + ' - ' + meta_data.json()['artists']
        return None

    def errorcatch(self, SONG_ID):
        # The 'errorcatch' function from your scraper code
        print('[*] Trying to download...')
        headers = {
            'authority': 'api.spotifydown.com',
            'method': 'GET',
            'path': f'/download/{SONG_ID}',
            'scheme': 'https',
            'origin': 'https://spotifydown.com',
            'referer': 'https://spotifydown.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }
        x = self.session.get(headers=headers, url='https://api.spotifydown.com/download/' + SONG_ID)
        if x.status_code == 200:
            return x.json()['link']
        return None

    def scrape_playlist(self, spotify_playlist_link, music_folder):
        ID = self.returnSPOT_ID(spotify_playlist_link)
        PlaylistName = self.get_PlaylistMetadata(ID)

        headers = {
            'authority': 'api.spotifydown.com',
            'method': 'GET',
            'path': f'/trackList/playlist/{ID}',
            'scheme': 'https',
            'accept': '*/*',
            'dnt': '1',
            'origin': 'https://spotifydown.com',
            'referer': 'https://spotifydown.com/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        Playlist_Link = f'https://api.spotifydown.com/trackList/playlist/{ID}'
        offset_data = {}
        offset = 0
        offset_data['offset'] = offset

        while offset is not None:
            response = self.session.get(url=Playlist_Link, params=offset_data, headers=headers)
            if response.status_code == 200:
                Tdata = response.json()['trackList']
                page = response.json()['nextOffset']
                for count, song in enumerate(Tdata):
                    yt_id = self.get_ID(song['id'])
                    if yt_id is not None:
                        filename = song['title'].translate(str.maketrans('', '', string.punctuation)) + ' - ' + song['artists'].translate(str.maketrans('', '', string.punctuation)) + '.mp3'
                        try:
                            data = self.generate_Analyze_id(yt_id['id'])
                            try:
                                DL_ID = data['links']['mp3']['mp3128']['k']
                                DL_DATA = self.generate_Conversion_id(data['vid'], DL_ID)
                                DL_LINK = DL_DATA['dlink']
                            except Exception as NoLinkError:
                                CatchMe = self.errorcatch(song['id'])
                                if CatchMe is not None:
                                    DL_LINK = CatchMe
                            if DL_LINK is not None:
                                ## DOWNLOAD
                                link = self.session.get(DL_LINK)

                                # Create Folder for Playlist
                                if not os.path.exists(music_folder):
                                    os.makedirs(music_folder)

                                ## Save
                                with open(os.path.join(music_folder, filename), 'wb') as f:
                                    f.write(link.content)

                                #Increment the counter
                                self.increment_counter()

                                # Emit the signal with the downloaded song name
                                self.song_downloaded.emit(filename.replace('.mp3',''))
                            else:
                                print('[*] No Download Link Found.')
                        except Exception as error_status:
                            print('[*] Error Status Code : ', error_status)

                    else:
                        print('[*] No data found for : ', song)
            if page is not None:
                offset_data['offset'] = page
                response = self.session.get(url=Playlist_Link, params=offset_data, headers=headers)
            else:
                break

    def returnSPOT_ID(self, link):
        # # The 'returnSPOT_ID' function from your scraper code
        # return link.split('/')[-1].split('?si')[0]

        # Define the regular expression pattern for the Spotify playlist URL
        pattern = r"https://open\.spotify\.com/playlist/([a-zA-Z0-9]+)\?si=.*"

        # Try to match the pattern in the input text
        match = re.match(pattern, link)

        if not match:
            raise ValueError("Invalid Spotify playlist URL.")
        # Extract the playlist ID from the matched pattern
        extracted_id = match.group(1)

        return extracted_id

    def increment_counter(self):
            self.counter += 1
            self.count_updated.emit(self.counter)  # Emit the signal with the updated count

# Scraper Thread
class ScraperThread(QThread):
    progress_update = pyqtSignal(str)

    def __init__(self, playlist_link):
        super().__init__()
        self.playlist_link = playlist_link
        self.scraper = MusicScraper()  # Create an instance of MusicScraper

    def run(self):
        music_folder = os.path.join(os.getcwd(), "music")  # Change this path to your desired music folder
        self.progress_update.emit("Scraping started...")
        try:
            self.scraper.returnSPOT_ID(self.playlist_link)
            self.scraper.scrape_playlist(self.playlist_link, music_folder)
            self.progress_update.emit("Scraping completed.")
        except Exception as e:
            self.progress_update.emit(f"{e}")




# Main Window
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        """MainWindow constructor"""
        super(MainWindow, self).__init__()

        # Main UI code goes here
        # loadUi("Template.ui", self)

        self.setupUi(self)


        self.PlaylistLink.returnPressed.connect(self.on_returnButton)
        self.Closed.clicked.connect(self.exitprogram)
        self.Select_Home.clicked.connect(self.Medium)
        # End main UI code

    # https://open.spotify.com/playlist/37i9dQZF1E36hkEAnydKTA?si=20caa5adfed648d3

    @pyqtSlot()
    def on_returnButton(self):
        playlist_id = self.PlaylistLink.text()
        try:
            # self.PlaylistMsg.setText('Playlist Code : %s' % playlist_id)

            # Start the scraper in a separate thread
            self.scraper_thread = ScraperThread(playlist_id)
            self.scraper_thread.progress_update.connect(self.update_progress)
            self.scraper_thread.finished.connect(self.thread_finished)  # Connect the finished signal
            self.scraper_thread.scraper.song_downloaded.connect(self.update_song_name)  # Connect the signal
            # Connect the count_updated signal to the update_counter slot
            self.scraper_thread.scraper.count_updated.connect(self.update_counter)

            self.scraper_thread.start()

        except ValueError as e:
            self.statusMsg.setText(str(e))

    def thread_finished(self):
        self.scraper_thread.deleteLater()  # Clean up the thread properly

    def update_progress(self, message):
        self.statusMsg.setText(message)

    @pyqtSlot(str)
    def update_song_name(self, song_name):
        self.SongName.setText(song_name)

    @pyqtSlot(int)
    def update_counter(self, count):
        self.CounterLabel.setText("Counter : Songs downloaded " + str(count))

    # DRAGGLESS INTERFACE

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:

            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.ClosedHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def exitprogram(self):
        sys.exit()

    def Medium(self):
        webbrowser.open('https://surenjanath.medium.com/')


# Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Screen = MainWindow()
    Screen.setFixedHeight(390)
    Screen.setFixedWidth(320)
    Screen.setWindowFlags(Qt.FramelessWindowHint)
    Screen.setAttribute(Qt.WA_TranslucentBackground)
    Screen.show()
    sys.exit(app.exec())


