from downloader import *
from installer import *
import os


def get_last_number():
    files = os.listdir(install_path)
    numbers = set()
    for i in range(len(files)):
        f = files.pop(0)
        number = re.search('(\d+)', f)
        if number:
            numbers.add(int(number.group(1)))

    if numbers:
        return max(numbers)
    return 1

install_path = r'E:\Tutorial\Python\steam_workshop_downloader\test\testing'
crafts_id_path = r'E:\Tutorial\Python\steam_workshop_downloader\crafts.txt'

installer = Installer(install_path)
downloader = Downloader(crafts_id_path, save_path=install_path)  # save and install in 1 place


try:
    while True:
        # last_number = installer.get_last_number() + 1
        last_number = get_last_number() + 1
        # print(f'last_number{last_number}')
        downloader.download(name=last_number)       #last_number - последнее число(для имени)
        installer.install(install_path, name=last_number)

        os.remove(f'{install_path}\{last_number}.zip') #удаление зип архива

except IndexError:
    print('finish')


# os.remove(f'./data/{installer.get_last_number()}.zip')
