from installer import Installer

install_dir = r'E:\Tutorial\Python\steam_workshop_downloader\test\testing'
craft_id_file = r'E:\Tutorial\Python\steam_workshop_downloader\crafts.txt'

installer = Installer(install_dir)

with open(craft_id_file, 'r') as crafts:
    for craft_id in crafts:
        print(f'getting {craft_id}')
        installer.install(craft_id.strip())
    print('Done')
