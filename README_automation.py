import os, time, git
from datetime import datetime
from git.objects.commit import Commit 
import urllib.parse

directory = os.path.dirname(os.path.realpath(__file__))
w_folders = ['1. Algorithms', '2. Data Structures','3. Mathematics']
all_folders_files = []
readme_file = open('README.md', 'w')
readme_file.write('# Automated README\n')
dir_path = os.path.dirname(os.path.realpath(__file__))
repo = git.Repo(dir_path)

for root, subdirectories, files in os.walk(directory):
    if any(folder in root for folder in w_folders):
        all_folders_files.append([root] + [subdirectories] + [files])
    
for folder in all_folders_files:
    if len(folder) != 0:
        folder_name = folder[0].split('/')[-1]
        print(folder_name)
        readme_file.write(f'#### :open_file_folder: [{folder_name}]({folder_name})\n')
        print('-'*(len(folder[0])))
        
        for subfolder in folder[1]:
            readme_file.write(f'- ##### :open_file_folder: [{subfolder}]({folder[0]}\\{subfolder})\n')
            print('   |--',subfolder)
            print('Writeing folders')
            print(subfolder)
        
        table_of_contents = open(folder[0] + '/README.md', 'w')
        table_of_contents.write(f'### Table of Contents\n')
        for file in folder[2]:
            if file != 'README.md':
                # table_of_contents.write(f'1. :page_facing_up: [{file[:-3]}]({folder_name}/{file})\n')
                fileName = urllib.parse.quote(file)

                table_of_contents.write(f'1. :page_facing_up: [{file[:-3]}]({fileName})\n')
                print('   |--',file)
        table_of_contents.close()
        
readme_file.close()
time.sleep(1)
# Push to GitHub

# commit_message = "Updated by automated commit 🤖"
# repo.git.add('--all')
# repo.git.commit('-m', commit_message, author='Shakib')
# print('[*] Pushing......')
# origin = repo.remote(name='origin')
# origin.push()

print("[=] Successfull")
