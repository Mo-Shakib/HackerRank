import os, time, git
from datetime import datetime
from git.objects.commit import Commit 
import urllib.parse

directory = os.path.dirname(os.path.realpath(__file__))

folderTree = {}
w_folders = ['1. Algorithms', '2. Data Structures','3. Mathematics']
ignoreFiles = ['.DS_Store', 'README.md']
fileTyp = {'py':'Python','cpp':'C++','c':'C','js':'JavaScript','java':'Java'}
totalSolved = 0
dir_path = os.path.dirname(os.path.realpath(__file__))
repo = git.Repo(dir_path)
            

readme_file = open('README.md', 'w')
readme_file.write(""" 
<p align="center">
	<a href="https://www.hackerrank.com/mo_shakib"><img src="https://cloud.githubusercontent.com/assets/19765741/25342064/d17a563c-28d8-11e7-83fc-763d4ab4820a.jpg" ></a>
</p>
<p align="center">
   <b> Solutions to problems on HackerRank. </b>
</p>

<p align="center">
	If you are interested in helping or have a solution in a different language feel free to make a pull request.
</p>
<p align="right">
    <img src="https://wakatime.com/badge/user/8e02bfd3-85d8-4d9d-88df-fa983f91ff30/project/b82b047d-1e9b-4267-a6db-5430b5c24ed5.svg">
	<img src="https://img.shields.io/badge/Language-Python-orange.svg">
""")

lastUpdate = datetime.now()
lastUpdate = lastUpdate.strftime("%d/%m/%y")
readme_file.write(f'<img src="https://img.shields.io/badge/Latest%20Update-{lastUpdate}-brightgreen.svg"></p> \n')
readme_file.write('\n')
readme_file.write('\n')

for root, subdirectories, files in os.walk(directory):
    if any(folder in root for folder in w_folders) and len(subdirectories) > 1:
        subdirectories.sort(key=lambda x: int(x[0].split('/')[-1].split('.')[0]))
        folder_name = root.split('/')[-1]
        folderTree[folder_name] = subdirectories
        
dictionary_items = folderTree.items()
sorted_folders = sorted(dictionary_items)

for f in sorted_folders:
    # ---------- Writing parent folders ----------
    PF_name = urllib.parse.quote(f[0])
    readme_file.write(f'## :open_file_folder: [{f[0].split(".")[1]}]({PF_name})\n')
    if len(f[1]) > 0:
        for i in f[1]:
            #------------- Writing sub folders ------------
            subf_name = urllib.parse.quote(i)
            readme_file.write(f'- #### :open_file_folder: [{i.split(".")[1]}]({PF_name}//{subf_name})\n')
            
            #------------- Making table of content ------------------
            filesPath = f'{directory}//{f[0]}//{i}'
            filenames = next(os.walk(filesPath), (None, None, []))[2]
            table_of_contents = open(filesPath + '/README.md', 'w')
            table_of_contents.write(f'### Table of Contents\n')
            
            for i in filenames:
                if i not in ignoreFiles:
                    print('File:', i)
                    fileName = urllib.parse.quote(i)
                    tablefilename = i.split('.')[0]
                    f_type = i.split('.')[-1]
                    table_of_contents.write(f'- :page_facing_up: __{tablefilename.capitalize()}__ - [{fileTyp[f_type]}]({fileName})\n')
                    totalSolved += 1
            table_of_contents.close()
            # ----------End of making take of content -------------------

readme_file.close()
time.sleep(1)

# Push to GitHub

commit_message = "Updated by automated commit 🤖"
repo.git.add('--all')
repo.git.commit('-m', commit_message, author='Shakib')
print('[*] Pushing......')
origin = repo.remote(name='origin')
origin.push()

print("[=] Successfull")
