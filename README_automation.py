import os, time, git, re
from datetime import datetime
from git.objects.commit import Commit 
import urllib.parse
import markdown

directory = os.path.dirname(os.path.realpath(__file__))

folderTree = {}
w_folders = ['1. Algorithms', '2. Data Structures','3. Mathematics']
ignoreFiles = ['.DS_Store', 'README.md','index.html']
fileTyp = {'py':'Python','cpp':'C++','c':'C','js':'JavaScript','java':'Java'}
totalSolved = 0
dir_path = os.path.dirname(os.path.realpath(__file__))
repo = git.Repo(dir_path)

now = datetime.now()
date_time_str = now.strftime("%d/%m/%Y")

nfile = open(str(dir_path)+"/README.md", "r")
last_line = nfile.readlines()[-4]
date_is = re.findall(r"-[0-9]+",last_line)
totalSolved_0 = str(date_is[0])[1:]
nfile.close()

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
<p align="left">
    <img src="https://img.shields.io/badge/Language-Python-orange.svg">
    <img src="https://wakatime.com/badge/user/8e02bfd3-85d8-4d9d-88df-fa983f91ff30/project/b82b047d-1e9b-4267-a6db-5430b5c24ed5.svg">
</p>
""")

readme_file.write('\n')
readme_file.write('\n')

for root, subdirectories, files in os.walk(directory):
    if any(folder in root for folder in w_folders) and len(subdirectories) > 0:
        subdirectories.sort(key=lambda x: int(x[0].split('/')[-1].split('.')[0]))
        folder_name = root.split('/')[-1]
        folderTree[folder_name] = subdirectories

dictionary_items = folderTree.items()
sorted_folders = sorted(dictionary_items)

print('All folders:',sorted_folders)

for f in sorted_folders:
    # ---------- Writing parent folders ----------
    # f[0] ---> Parent folders
    for i in f[1]:
        filesPath = f'{directory}//{f[0]}//{i}'
        filenames = next(os.walk(filesPath), (None, None, []))[2]
    
    if len(filenames) > 0:
        PF_name = urllib.parse.quote(f[0])
        readme_file.write(f'# 📒 [{f[0].split(".")[1].lstrip()}]({PF_name})\n')
    
    if len(f[1]) > 0:
        # f[1] - stores all the sub-folders in the main folders
        for i in f[1]:
            filesPath = f'{directory}//{f[0]}//{i}'
            filenames = next(os.walk(filesPath), (None, None, []))[2]
            #------------- Writing sub folders ------------
            if len(filenames) > 1:
                subf_name = urllib.parse.quote(i)
                readme_file.write(f'- ### 📁 [{i.split(".")[1].lstrip()}]({PF_name}//{subf_name})\n')
            
            #------------- Making table of content ------------------
            filesPath = f'{directory}//{f[0]}//{i}'
            filenames = next(os.walk(filesPath), (None, None, []))[2]
            
            # ----------- Writing file index to main README.md --------------
            for j in filenames:
                if j not in ignoreFiles:
                    fileName = urllib.parse.quote(j)
                    tablefilename = j.split('.')[0]
                    f_type = j.split('.')[-1]
                    readme_file.write(f'	- [x] 📃 [_{tablefilename.capitalize()}_]({PF_name}/{subf_name}/{fileName})\n')
                    totalSolved += 1
            # ------- End of writing index to main readme file -------
            
            table_of_contents = open(filesPath + '/README.md', 'w')
            table_of_contents.write(f'### Table of Contents\n')
            
            for i in filenames:
                if i not in ignoreFiles:
                    fileName = urllib.parse.quote(i)
                    tablefilename = i.split('.')[0]
                    f_type = i.split('.')[-1]
                    table_of_contents.write(f'- :page_facing_up: __{tablefilename.capitalize()}__ - [{fileTyp[f_type]}]({fileName})\n')
            table_of_contents.close()
            # ----------End of making take of content -------------------

print('New total:',totalSolved)
print('Old total:', totalSolved_0)

readme_file.write('\n')
readme_file.write('\n')

if str(totalSolved_0) != totalSolved:
    readme_file.write(f"""<p align="left">
        <img src="https://img.shields.io/badge/Problems%20Solved-{totalSolved}-brightgreen.svg">
        <img src="https://img.shields.io/badge/Latest%20Update-{str(date_time_str)}-brightgreen.svg">
        <img src="https://github.com/Mo-Shakib/HackerRank/actions/workflows/README_automation.yml/badge.svg">
    </p>""")
else:
    readme_file.write(f"""<p align="left">
        <img src="https://img.shields.io/badge/Problems%20Solved-13-brightgreen.svg">
        <img src="https://img.shields.io/badge/Latest%20Update-01/09/2022-brightgreen.svg">
        <img src="https://github.com/Mo-Shakib/HackerRank/actions/workflows/README_automation.yml/badge.svg">    
    </p>""")

readme_file.close()
time.sleep(1)

# Writing website for the readme
print('Writing index.html file')
markdown.markdownFromFile(
    input='README.md',
    output='index.html',
    encoding='utf8',
)
print('Done writing index.html')

# Push to GitHub
<<<<<<< HEAD
=======

>>>>>>> c9a15f2dc3e951cd1dc2b06d20b9b4212022785f
commit_message = "Updated by automated commit 🤖"
repo.git.add('--all')
repo.git.commit('-m', commit_message, author='Shakib')
print('[*] Pushing......')
origin = repo.remote(name='origin')
origin.push()

print("[=] Successfull")
