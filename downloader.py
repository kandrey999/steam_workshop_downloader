from requests import Session
import json


class Downloader:
    def __init__(self):
        self.url = 'https://api.steamworkshopdownloader.io/api/download'
        self._session = self._create_session()

    @staticmethod
    def _create_session():
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
        session = Session()
        session.headers.update(headers)
        return session

    def _get_uuid(self, craft_id: str):
        """
        Get craft UUID by craft id
        :param craft_id:
        :return: craft UUID
        """
        d = {'publishedFileId': int(craft_id),
             'collectionId': None,
             'extract': True,
             'hidden': False,
             'direct': False,
             'autodownload': False}

        res = self._session.post(f'{self.url}/request', json.dumps(d))

        if not res.text:
            raise ValueError(f'uuid not received by craft_id={craft_id}')

        json_d = json.loads(res.text)

        return json_d['uuid']

    def _get_file(self, uuid):
        """
        Get file content by craft UUID
        :param uuid: craft UUID
        :return: file content
        """
        return self._session.get(f'{self.url}/transmit?uuid={uuid}').content

    def get_file(self, craft_id: str):
        """
        Get file by craft id
        :param craft_id:
        :return:
        """
        uuid = self._get_uuid(craft_id)
        return self._get_file(uuid)
