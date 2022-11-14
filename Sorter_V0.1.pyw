import os
import time
import shutil
import datetime


def main():
	if not os.path.exists('setup.txt'):
		setup()
	setup_file = open('setup.txt', 'r')
	setup_val = setup_file.readlines()
	file_list = []
	while True:
		for file in os.listdir(str(setup_val[0].split('|')[1])):
			if file == 'log.txt':
				continue
			else:
				file_list.append(file)
		time.sleep(1)
		files_moved = len(file_list)
		if len(file_list) > 0:
			file_move(file_list, setup_val)


def file_move(file_list, setup_val):
	log = open('log.txt', 'a')
	for file in file_list:
                Print(file)
		for folder in os.listdir(setup_val[1].split('|')[1]):
			if os.path.isdir(setup_val[1].split('|')[1] + '\\' + folder):
				if file.split('_')[0] in folder:
					shutil.copy2(setup_val[0].split('|')[1] + '\\' + file,setup_val[1].split('|')[1] + '\\' + folder)
					os.remove(setup_val[0].split('|')[1] + '\\' + file)
					file_list.remove(file)
					print(f'{datetime.datetime.now()} | {file} | ' + str(setup_val[1].split('|')[1] + '\\' + folder), file=log)
					continue
			elif os.path.isdir(setup_val[1].split('|')[1] + '/' + folder):
				if file.split('_')[0] in folder:
					shutil.copy2(setup_val[0].split('|')[1] + '/' + file, setup_val[1].split('|')[1] + '/' + folder)
					os.remove(setup_val[0].split('|')[1] + '/' + file)
					file_list.remove(file)
					print(f'{datetime.datetime.now()} | {file} | ' +str(setup_val[1].split('|')[1] + '/' + folder), file=log)
					continue
	for file in file_list:
		for folder in os.listdir(setup_val[2].split('|')[1]):
			if os.path.isdir(setup_val[2].split('|')[1] + '\\' + folder):
				if file.split('_')[0] in folder:
					shutil.copy2(setup_val[0].split('|')[1] + '\\' + file, setup_val[1].split('|')[1] + '\\' + folder)
					time.sleep(0.1)
					os.remove(setup_val[0].split('|')[1] + '\\' + file)
					file_list.remove(file)
					print(f'{datetime.datetime.now()} | {file} | ' + str(setup_val[1].split('|')[1] + '\\' + folder), file=log)
					continue
			elif os.path.isdir(setup_val[2].split('|')[1] + '/' + folder):
				if file.split('_')[0] in folder:
					print(setup_val[0].split('|')[1] + '/' + file)
					print(setup_val[1].split('|')[1] + '/' + folder)
					shutil.copy2(setup_val[0].split('|')[1] + '/' + file, setup_val[1].split('|')[1] + '/' + folder)
					time.sleep(0.1)
					os.remove(setup_val[0].split('|')[1] + '/' + file)
					file_list.remove(file)
					print(f'{datetime.datetime.now()} | {file} | ' +str(setup_val[1].split('|')[1] + '/' + folder), file=log)
					continue


def setup():
	setup_file = open('setup.txt', 'w')
	print('This is a one time setup. Please follow all instructions carefully to ensure all files are moved properly.')
	try: 
		if os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive\\Desktop')):
			if not os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive\\Desktop\\File Sorter')):
				os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive\\Desktop\\File Sorter'))
				path = os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive\\Desktop\\File Sorter')
				print(f"desktop_sorter_path = |{path}|", file=setup_file)
			else: 
				path = os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive\\Desktop\\File Sorter')
				print(f"desktop_sorter_path = |{path}|", file=setup_file)
		elif os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')):
			if not os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop\\File Sorter')):
				os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop\\File Sorter'))
				path = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop\\File Sorter')
				print(f"desktop_sorter_path = |{path}|", file=setup_file)
			else:
				path = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop\\File Sorter')
				print(f"desktop_sorter_path = |{path}|", file=setup_file)
		elif os.path.exists('File-Sorter'):
			if not os.path.exists('File-Sorter\\File Sorter'):
				os.mkdir('File-Sorter\\File Sorter')
	except KeyError: # For Testing with Repl.it
		if os.path.exists('/home/runner/File-Sorter'): # For Testing with Repl.it
			if not os.path.exists('/home/runner/File-Sorter/File Sorter'): # For Testing with Repl.it
				os.mkdir('/home/runner/File-Sorter/File Sorter') # For Testing with Repl.it
				path = '/home/runner/File-Sorter/File Sorter' # For Testing with Repl.it
				print(f'testing_sorter_path = |/home/runner/File-Sorter/File Sorter|', file = setup_file) # For Testing with Repl.it
			else:
				path = '/home/runner/File-Sorter/File Sorter' # For Testing with Repl.it
				print(f'testing_sorter_path = |/home/runner/File-Sorter/File Sorter|', file = setup_file) # For Testing with Repl.it
	print(
	 'You may notice a new folder has appeared on your desktop [File Sorter].',
	 'This is the folder you will move files to in order to sort them.',
	 'In order for the sorter to reconize where to put the file, keywords must be enter first and followed by an underscore',
	 'Ex. keyword_MyFile.txt',
	 'If entered incorrectly, fear not, your file will be in your My Files folder.',
	 '')
	print('As default, the File Sorter V0 is configured to sort to:',
	      'My Files in Documents', 'Custom Directory 1', 'Custom Directory 2.',
	      '')
	print(
	 'In this case, a directory refers to a folder containing other folders.',
	 'ex. School folder might contain Subject folders', '')
	while True:
		cust_dir1 = input('Enter Custom Directory 1: ')
		if not os.path.exists(cust_dir1):
			print('Directory does not exist')
			continue
		else:
			print('Directory Set')
		cust_dir2 = input('Enter Custom Directory 2: ')
		if not os.path.exists(cust_dir2):
			print('Directory does not exist')
			continue
		else:
			try:
				print(os.path.join(os.path.join(os.environ['USERPROFILE']),'Documents\\My Files'))
				print(f"sort_directory1 = |{cust_dir1}|", file=setup_file)
				print(f"sort_directory2 = |{cust_dir2}|", file=setup_file)
				if os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive\\Documents')):
					if not os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive\\Documents\\My Files')):
						os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE']),'\\OneDriveDocuments\\My Files'))
						path = os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive\\Documents\\My Files')
						print(f"my_files_path = |{path}|", file=setup_file)
					else:
						path = os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive\\Documents\\My Files')
						print(f"my_files_path = |{path}|", file=setup_file)
				elif os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')):
					if not os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']),'Documents\\My Files')):
						os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE']),'Documents\\My Files'))
						path = os.path.join(os.path.join(os.environ['USERPROFILE']),'Documents\\My Files')
						print(f"my_files_path = |{path}|", file=setup_file)
					else:
						path = os.path.join(os.path.join(os.environ['USERPROFILE']),'Documents\\My Files')
						print(f"my_files_path = |{path}|", file=setup_file)
				print('All Directories Set')
			except KeyError:
				print(f"sort_directory1 = |{cust_dir1}|", file=setup_file) # For Testing with Repl.it
				print(f"sort_directory2 = |{cust_dir2}|", file=setup_file) # For Testing with Repl.it
				if os.path.exists('/home/runner/File-Sorter/My Files'): # For Testing with Repl.it
					print(f"my_files_path = |/home/runner/File-Sorter/My Files|", file=setup_file) # For Testing with Repl.it
				else: # For Testing with Repl.it
					os.mkdir('/home/runner/File-Sorter/My Files') # For Testing with Repl.it
					print(f"my_files_path = |/home/runner/File-Sorter/My Files|", file=setup_file) # For Testing with Repl.it
				print('All Directories Set') # For Testing with Repl.it
		break
	setup_file.close()


if __name__ == '__main__':
	main()
