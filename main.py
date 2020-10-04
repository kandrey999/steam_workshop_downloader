from installer import Installer

install_dir = r'E:\Tutorial\Python\steam_workshop_downloader\test\testing'
craft_id_file = r'E:\Tutorial\Python\steam_workshop_downloader\crafts.txt'


def craft_ids(self):
    with open(self._craft_id_file, 'r') as crafts:
        yield next(crafts).split(' ')


installer = Installer(install_dir)

for craft_id in craft_ids():
    installer.install(craft_id)
