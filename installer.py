import re
import os
import zipfile


class Installer:
    def __init__(self, install_dir):
        self._install_dir = install_dir
        # self.files = self.get_files_names_from_path(self.install_path)
        # self.last_number = self.get_last_number()
        # self.name = files_name

    # def get_last_number(self):
    #     files = self.get_files_names_from_path(self.install_path)
    #     numbers = set()
    #     # print(len(self.files))
    #     for i in range(len(files)):
    #         f = files.pop(0)
    #         number = re.search('(\d+)', f)
    #         if number:
    #             numbers.add(int(number.group(1)))
    #     # print(numbers)
    #     return max(numbers)

    # def get_files_names_from_path(self, path):
    #     return os.listdir(path)

    def unpack_file(self, file_path):
        with zipfile.ZipFile(file_path, 'r') as zip:
            zip.extractall(path=self._install_dir)

    @staticmethod
    def _rename_files(file_dir, name):
        os.rename(fr'{file_dir}\vehicle.xml', fr'{file_dir}\{name}.xml')
        os.rename(fr'{file_dir}\workshop_preview.png', fr'{file_dir}\{name}.png')

    def install(self, file_path, name):
        # last_number = self.get_last_number() + 1
        install_path = fr'{file_path}\{name}.zip'
        self.unpack_file(install_path)
        self._rename_files(file_path, name)
