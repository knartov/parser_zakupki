# -*- coding: utf-8 -*-

import ftplib
from zipfile import *
import os


ftp = ftplib.FTP('ftp.zakupki.gov.ru')
ftp_user = 'free'
ftp_password = 'free'
print(ftp.login(ftp_user, ftp_password))

working_catalogue = '/Users/nartov/Box Sync/Project One/Zakupki/Adygeja_2017/xml'

ftp.cwd('fcs_regions')
ftp.cwd('Adygeja_Resp')
ftp.cwd('notifications')

filenames = ftp.nlst()  # собираем список имен всех файлов

# print(filenames)

new_filenames = []  # набираем новый список с условием, 2017 - год в названии архива
exceptions = []
for x in filenames:
    for i in range(len(x)):
        chunk = x[i:i + 4]
        if chunk == '2017':
            new_filenames.append(x)
            break
uniq_filenames = list(set(new_filenames + new_filenames))  # создаем список без дубликатов
'''
выгружаем все данные по списку uniq_filenames

for filename in uniq_filenames:
    host_file = os.path.join(
        working_catalogue, filename
    )

    try:
        with open(host_file, 'wb') as local_file:
            ftp.retrbinary('RETR ' + filename, local_file.write)
    except ftplib.error_perm:
        pass
'''

os.chdir(working_catalogue)  # меняем директорию на локальной машине, куда грузили архивы

dir_list = os.listdir()  # получаем список имен архивов

# вытаскиваем файлы из всех архивов
for s in dir_list:
    m = ZipFile(s, 'r')
    m.extractall(working_catalogue)


# m = ZipFile('/Users/nartov/Box Sync/Project One/Zakupki/notification_Adygeja_Resp_2016120100_2017010100_001.xml.zip', 'r')
# m.extractall('/Users/nartov/Box Sync/Project One/Zakupki/')

"""
for s in uniq_filenames:
    m = ZipFile(s, 'r')
    m.extractall('/Users/nartov/Box Sync/Project One/Zakupki')
"""

"""
for filename in uniq_filenames:
    host_file = os.path.join(
        'C:\\Users\\nartok\\Box Sync\\Project One\\Zakupki\\Adygeja_2017', filename
    )

    try:
        with open(host_file, 'wb') as local_file:
            ftp.retrbinary('RETR ' + filename, local_file.write)
    except ftplib.error_perm:
        pass

ftp.quit()
"""

print('ready')
