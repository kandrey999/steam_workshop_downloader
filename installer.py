import re
import os
import zipfile

class Installer:
    def __init__(self, install_path):
        self.install_path = install_path
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
            zip.extractall(path=self.install_path)

    def rename_excracted_files(self, files_path, name):
        os.rename(fr'{files_path}\vehicle.xml', fr'{files_path}\{name}.xml')
        os.rename(fr'{files_path}\workshop_preview.png', fr'{files_path}\{name}.png')

    def install(self, file_path, name):
        # last_number = self.get_last_number() + 1
        install_path = fr'{file_path}\{name}.zip'
        self.unpack_file(install_path)
        self.rename_excracted_files(file_path, name)




