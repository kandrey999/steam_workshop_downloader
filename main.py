from requests import Session
import json
import os
import zipfile


class Downloader:
    def __init__(self, url, crafts_id_folder_name: str,
                 last_number: int):                                             # last_number - Чтобы игра крафты различала(они цифрами названы)
                                                                                # в crafts_id_folder_name передавать имя txt файла с 1 строкой(id) без \n

        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
        self.session = Session()
        self.session.headers.update(self.headers)
        self.url = url
        self.crafts_id_folder_name = crafts_id_folder_name
        self.crafts_id = None
        self.uuid = None

    def get_crafts_id(self):
        with open(self.crafts_id_folder_name, 'r') as crafts:
            for s in crafts:
                self.crafts_id = s.split(' ')
        print(self.crafts_id)

    def download_uuid(self):
        res = self.session.post('https://api.steamworkshopdownloader.io/api/download/request',
                                '{"publishedFileId":2245892621,"collectionId":null,"extract":true,"hidden":false,"direct":false,"autodownload":false}')

        json_d = json.loads(res.text)
        self.uuid = json_d['uuid']

    def download_binary_file(self):
        file_url = f'https://api.steamworkshopdownloader.io/api/download/transmit?uuid={self.uuid}'
        file = self.session.get(file_url).content
        with open('craft.txt', 'wb') as test:
            test.write(file)

    def reformat_and_unpack_binary_file(self):
        os.rename('craft.txt', 'craft.zip')
        with zipfile.ZipFile('craft.zip', 'r') as zip:
            zip.extractall()

    def run(self):
        while True:
            self.download_uuid()
            self.download_binary_file()
            self.reformat_and_unpack_binary_file()


url = 'https://api.steamworkshopdownloader.io/api/download/request'

downloader = Downloader(url, 'crafts.txt', 5)

downloader.run()
