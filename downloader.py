from requests import Session
import json
import os


class Downloader:
    def __init__(self, crafts_id_folder_name: str,
                 save_path):  # last_number - Чтобы игра крафты различала(они цифрами названы)                                                                            # в crafts_id_folder_name передавать имя txt файла с 1 строкой(id) без \n

        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
        self.session = Session()
        self.session.headers.update(self.headers)
        self.url = 'https://api.steamworkshopdownloader.io/api/download'
        self.crafts_id_folder_name = crafts_id_folder_name
        # self.last_number = last_number
        self.save_path = save_path
        self.crafts_id = None
        self.upload_crafts_id()

    def upload_crafts_id(self):
        with open(self.crafts_id_folder_name, 'r') as crafts:
            self.crafts_id = next(crafts).split(' ')

    def get_id(self):
        return self.crafts_id.pop(0)

    def get_uuid(self, id):
        d = {'publishedFileId':int(id),
             'collectionId': None,
             'extract': True,
             'hidden': False,
             'direct': False,
             'autodownload': False}

        res = self.session.post(f'{self.url}/request', json.dumps(d))

        json_d = json.loads(res.text)
        return json_d['uuid']

    def get_file(self, uuid):
        return self.session.get(f'{self.url}/transmit?uuid={uuid}').content

    @staticmethod
    def save_file(content, path):
        with open(path, 'wb') as f:
            f.write(content)

    # def rename_unpacked_files(self):
    #     os.rename()

    def download(self, name):
        id = self.get_id()
        if id:
            print(id)
            uuid = self.get_uuid(id)
            file = self.get_file(uuid)
            self.save_file(file, f'{self.save_path}/{name}.zip')

# downloader = Downloader('crafts.txt', 5)
