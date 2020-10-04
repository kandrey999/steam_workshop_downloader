import re
import os
from zipfile import ZipFile
from downloader import Downloader


class Installer:
    def __init__(self, install_dir: str):
        self._install_dir = install_dir
        self._downloader = Downloader()

    @staticmethod
    def _save_file(content, path: str):
        with open(path, 'wb') as f:
            f.write(content)

    @staticmethod
    def _unpack_file(file_name: str, dst_dir: str):
        with ZipFile(file_name, 'r') as z:
            z.extractall(path=dst_dir)

    def _set_file_name(self, craft_id: str):
        os.rename(os.path.join(self._install_dir, 'vehicle.xml'), os.path.join(self._install_dir, f'{craft_id}.xml'))
        os.rename(os.path.join(self._install_dir, 'workshop_preview.png'),
                  os.path.join(self._install_dir, f'{craft_id}.png'))

    def _remove_files(self, craft_id: str):
        path = os.path.join(self._install_dir, f'{craft_id}')
        files = [f'{path}.xml', f'{path}.png']
        for file in files:
            if os.path.exists(file):
                os.remove(file)

    def _get_last_num(self):
        nums = set()
        files = os.listdir(self._install_dir)
        for file in files:
            m = re.search('(\d+)', file)
            if m:
                nums.add(int(m[1]))
        return max(nums) if nums else 1

    def install(self, craft_id):
        content = self._downloader.get_file(craft_id)
        zip_file_name = os.path.join(self._install_dir, f'{craft_id}.zip')
        self._save_file(content, zip_file_name)
        self._unpack_file(zip_file_name, self._install_dir)
        self._remove_files(craft_id)
        self._set_file_name(craft_id)
        os.remove(zip_file_name)
