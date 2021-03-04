import os

cur_url = os.getcwd()
start_url = os.getcwd()
last_opened = ''

while True:
    if os.path.isfile(cur_url):
        print('\nCurrent opened file:', cur_url)
        print('\nChoose option:')
        print('1. Print "Delete", if you want to delete this file.')
        print('2. Print "Rename", if you want to rename this file.')
        print('3. Print "Add", if you add text to this file.')
        print('4. Print "Rewrite", if you want to rewrite this file.')
        print('5. Print "Back", if you want to return to previous directory.')
        print('6. Print "Stop", if you want to finish work.')

        option = input()

        if option == 'Delete':
            os.remove(cur_url)
            print('Operation done successfully.')
            cur_url = cur_url[:cur_url.find(last_opened)]

        elif option == 'Rename':
            while True:
                print('Please, enter the name.\n')
                name = input()
                if(name == ''):
                    print('Error: This name is not available.\n')
                else:
                    break
            os.rename(cur_url, name)
            cur_url = os.path.join(cur_url[:len(cur_url) - len(last_opened)] + name)
            print('Operation done successfully.')

        elif option == 'Add':
            print('Please, enter the text.\n')
            text = input()
            with open(cur_url, 'a', encoding='utf-8') as f:
                f.write(text)
            print('The text was successfully added to the file.')

        elif option == 'Rewrite':
            print('Please, enter the text.')
            text = input()
            with open(cur_url, 'w', encoding='utf-8') as f:
                f.write(text)
            print('The text was successfully written to the file.')

        elif option == 'Back':
            cur_url1 = cur_url[::-1]
            if cur_url1[cur_url1.find('\\')+1] != ':':
                cur_url1 = cur_url1[cur_url1.find('\\')+1:]
                cur_url = cur_url1[::-1]
                print('Successfully returned to the previous directory.')
            else:
                print('Error: Impossible to move back.')

        elif option == 'Stop':
            break

        else:
            print('Error: There is no such command.')

        print('To continue enter any character...')
        abc = input()
    else:
        print('\nCurrent opened directory', cur_url)
        print('\nChoose option:')
        print('1. Print "Rename", if you want to rename this directory.')
        print('2. Print "Dirs", if you want to display the number of directories here.')
        print('3. Print "Files", if you want to display the number of files here.')
        print('4. Print "Content", if you want to display the content of current directory.')
        print('5. Print "mkfile", if you want to create new file here.')
        print('6. Print "mkdir", if you want to create new directory here.')
        print('7. Pring "Open", if you want to open file or directory.')
        print('8. Print "Back", if you want to return to the previous directory.')
        print('9. Print "Stop", if you want to finish work.')
        
        option = input()

        if option == 'Rename':
            dirs = [i for i in os.listdir(cur_url) if os.path.isdir(i)]
            while True:
                print('Please, enter the name.')
                name = input()
                if(name == '' or name == '.'):
                    print('Error, this name is not available.')
                elif name in dirs:
                    print('Error, directory with such name already exists.')
                else:
                    break
            os.rename(cur_url, name)
            cur_url = cur_url[:len(cur_url) - cur_url[::-1].find('\\')]
            cur_url = os.path.join(cur_url[:cur_url.find(last_opened)], name)
            print('Operation done successfully.')
        
        elif option == 'Dirs':
            cnt, l = 0, []
            for i in os.listdir(cur_url):
                if os.path.isdir(i):
                    l.append(i)
                    cnt += 1
            if cnt == 0:
                print('There is no directory here.')
            else:
                print('   List of directories:')
                print(*l, sep='\n')
                print('Total amount of directories:', cnt)

        elif option == 'Files':
            cnt, l = 0, []
            for i in os.listdir(cur_url):
                if os.path.isfile(i):
                    l.append(i)
                    cnt += 1
            if cnt == 0:
                print('There is no file here.')
            else:
                print('   List of files:')
                print(*l, sep='\n')
                print('Total amount of files:', cnt)
        
        elif option == 'Content':
            cnt, l = 0, []
            for i in os.listdir(cur_url):
                l.append(i)
                cnt += 1
            if cnt == 0:
                print('This directory is empty.')
            else:
                print('   List of files and directories:')
                print(*l)
                print('Total amount of files and directories:', len(os.listdir(cur_url)))
        
        elif option == 'mkfile':
            files = [i for i in os.listdir(cur_url) if os.path.isfile(i)]
            while True:
                print('Please, enter the name.')
                print('or enter ",." if you want to cancel.')
                name = input()
                if name == ',.':
                    break
                if name == '' or name == '.':
                    print('Error: This name is not available.\n')
                elif name in files:
                    print('Error: File with this name already exists.\n')
                else:
                    break
            if name == ',.':
                continue
            os.chdir(cur_url)
            with open(name, 'w', encoding='utf-8') as f:
                f.write('')
            print('Operation done successfully.')

        elif option == 'mkdir':
            dirs = [i for i in os.listdir(cur_url) if os.path.isdir(i)]
            while True:
                print('Please, enter the name')
                print('or enter ",." to cancel.')
                name = input()
                if name == ',.':
                    break
                if name == '' or name == '.':
                    print('Error: This name is not available.\n')
                elif name in dirs:
                    print('Error: Directory with this name already exists.\n')
                else:
                    break
            if name == ',.':
                continue
            os.chdir(cur_url)
            os.mkdir(name)
            print('Operation done successfully.')

        elif option == 'Open':
            os.chdir(cur_url)
            files = [i for i in os.listdir() if os.path.isfile(i)]
            dirs = [i for i in os.listdir() if os.path.isdir(i)]
            a = 1
            if len(files) == 0 and len(dirs) == 0:
                print('There is nothing to open.')
                a = 0
            while a == 1:
                if(len(files) == 0):
                    print('There are no files here.')
                else:
                    print('   Files:')
                    print(*files, sep='\n')
                if(len(dirs) == 0):
                    print('There are no directories here.')
                else:
                    print('   Directories:')
                    print(*dirs, sep='\n')
                print('\nWhat needs to be opened?')
                name = input()
                if name not in files and name not in dirs:
                    print('Such file or directory does not exits.')
                    print('Enter any character to continue...')
                    abc = input()
                else:
                    break
            if a == 1:
                if name in files:
                    cur_url = os.path.join(cur_url, name)
                    print(f'File "{name}" was successfully opened.')
                else:
                    cur_url = os.path.join(cur_url, name)
                    print(f'Directory "{name}" was successfully opened.')
                last_opened = name

        elif option == 'Back':
            cur_url1 = cur_url[::-1]
            if cur_url1[cur_url1.find('\\')+1] != ':':
                cur_url1 = cur_url1[cur_url1.find('\\')+1:]
                cur_url = cur_url1[::-1]
                print('Successfully returned to the previous directory.')
            else:
                print('Error: Impossible to move back.')
            
        elif option == 'Stop':
            break
            
        else:
            print('Error: There is no such command.')

        print('To continue enter any character...')
        abc = input()   