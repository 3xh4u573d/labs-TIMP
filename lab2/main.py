import hashlib
import os
import sys
import time


# names,times,starts

def sha256_of_file(file_path):
    hash = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(hash.block_size)
            if not chunk:
                break
            hash.update(chunk)

    return hash.hexdigest()


file_with_names = "/root/.do_not_enter/.file_with_names"  # файл с именами
file_4_times = "/root/.do_not_enter/.file_with_times"  # файл для просмотра оставшегося времени
file_4_starts = "/root/.do_not_enter/.file_with_starts"  # файл для просмотра оставшихся запусков
absolute_secret_file = "/root/.flag/.seriously/.true_flag/.im_sure/.really/.more/.directories/.u/.cant/.do/.this/.more/.absolutely/.just/.chill/.flag_{ch3ck_1n_4_1os3rs}"  # Лицуха?
flag_4_1_start = "/root/.flag/.seriously/.true_flag/.im_sure/.really/.more/.directories/.u/.cant/.do/.this/.more/.absolutely/.just/.chill/.flag_4_1_start"  # Кончилось да? ну ничего
file_4_hashes = "/root/.do_not_enter/.file_with_hashes"  # names,times,starts
if os.path.exists(flag_4_1_start):
    tmp = open(flag_4_1_start).read()
    if tmp == 0:
        current_hash_4_names = sha256_of_file(file_with_names)
        current_hash_4_times = sha256_of_file(file_4_times)
        current_hash_4_starts = sha256_of_file(file_4_starts)


def help():
    print("Hi, this program is designed to get credit.\n But you can enter your name and be surprised how quickly you will be offered to buy the paid version(2 minutes)\
          \n or how few times you can use my program from different users!(3 times)\n\ Do you want to delete any files? It won't work\n\ Any change of files important to the program will cause the free version to expire.")
    print("Usage: sudo python3 main.py [option]")
    print("Options:")
    print("\t-sl or --start-limited - Start-limited")
    print("\t-tl or --time-limited - Time-limited")
    print("\t--license - input your license")
    print("\t--uninstall - uninstall this program")
    print("\t--users - show all users")
    print("\t--check_security - check that's all work correctly")
    print("\t-h or --help - help")
    print("\n\nUsage of install.py: sudo python3 install.py")


def update_hashes():
    hashes = open(file_4_hashes, "w")
    hashes.write(
        sha256_of_file(file_with_names) + "\n" + sha256_of_file(file_4_times) + "\n" + sha256_of_file(file_4_starts))


def check_files_on_start():
    if os.path.exists(file_with_names) and os.path.exists(absolute_secret_file) and os.path.exists(
            file_4_starts) and os.path.exists(file_4_times) and os.path.exists(flag_4_1_start) and os.path.exists(
        file_4_hashes):
        return 1
    else:
        return 0


def change_file_with_times(last_time, solve=0):
    file = open(file_4_starts, "r")  # открываем на перезапись
    remaining_time = int(file.read())
    file.close()
    file = open(file_4_times, "w")
    if solve == 1:
        file.write("441")
    else:
        file.write(str(remaining_time - (int(time.time()) - last_time)))  # пишем в него новое значение
        if int(open(file_4_starts, "r").read()) < 0:
            fiiile = open(flag_4_1_start, "w")
            fiiile.write("1")
            fiiile.close()

    file.close()
    update_hashes()


def change_file_with_starts(n):  # функция для изменения файла с числом оставшихся попыток
    file = open(file_4_starts, "w")  # открываем на перезапись
    file.write(str(n))  # пишем в него новое значение ( предыдущее-1 )
    if n <= 0:
        fiiile = open(flag_4_1_start, "w")
        fiiile.write("1")
        fiiile.close()
    file.close()
    update_hashes()


def program_time_limit():
    remaining_time = int(open(file_4_times).read().split()[0])  # извлекаем оставшееся время
    if check_files_on_start() and remaining_time > 0 or int(
            open(absolute_secret_file).read().split()[0]) == 1:  # если все файлы на месте и время осталось
        now_time = int(time.time())
        fio = str(input("What is your name?\n "))  # пользователь вводит ФИО
        f = open(file_with_names)  # открываем файл с именами
        text = f.read()  # смотрим что там
        f.close()  # закрываем
        count = text.count(fio)
        if count == 0:  # если раньше такого не было - записываем и меняем хэш файла
            file = open(file_with_names, "a")
            file.write(fio + "\n")
            file.close()
            print("Hi,", fio)
        else:  # если не было
            print("Hi again,", fio)
        if int(open(absolute_secret_file).read().split()[0]) == 1 or remaining_time == 441:
            pass
        else:
            change_file_with_times(now_time)  # уменьшаем оставшееся время
        if remaining_time > 1 and remaining_time != 441 and int(open(absolute_secret_file).read().split()[0]) == 1:
            print("It's about time you bought a license!")
    elif remaining_time <= 0:
        inp = input("Did you want to uninstall this program or you have license?(u/l)\n")
        if inp[0] == "u":
            uninstall()
        elif inp[0] == "l":
            input_license()
        else:
            print("something went wrong...")


def program_start_limit():
    n = int(open(file_4_starts).read().split()[0])  # извлекаем количество оставшихся попыток
    if check_files_on_start() and n > 0 or int(
            open(absolute_secret_file).read().split()[0]) == 1:  # если все файлы на месте и остались попытки
        fio = str(input("What is your name?\n "))  # пользователь вводит ФИО
        f = open(file_with_names)  # открываем файл с именами
        text = f.read()  # смотрим что там
        f.close()  # закрываем
        count = text.count(fio)
        if count == 0:  # если раньше такого не было - записываем и меняем хэш файла
            file = open(file_with_names, "a")
            file.write(fio + "\n")
            file.close()
            print("Hi,", fio)
        else:  # если не было
            print("Hi again,", fio)
        if n == 441 or int(open(absolute_secret_file).read().split()[0]) == 1:
            pass
        else:
            change_file_with_starts(n - 1)  # уменьшаем количество попыток
        if n > 1 and n != 441 and int(open(absolute_secret_file).read().split()[0]) != 1:
            print("It seems there are only " + str(n - 1) + " uses left...\
It's about time you bought a license!")
    elif n == 0:
        inp = input("Did you want to uninstall this program or you have license or close program?(u/l/c)\n")
        if inp[0] == "u":
            uninstall()
        elif inp[0] == "l":
            input_license()
        elif inp[0] == "c":
            pass
        else:
            print("something went wrong...")


def input_license():
    license_str = input("Input license code\n")
    license_str = license_str.encode('utf-8')
    if hashlib.md5(license_str).hexdigest() == "c02cbb31d0b41dca3c23596aceee2369":  # hochu_5
        print("You're lucky!")
        change_file_with_times(441, solve=1)
        change_file_with_starts(441)
        update_hashes()
        solved = open(absolute_secret_file, "w")
        solved.write("1")
        solved.close()


    else:
        print("Shit happens. One more try?")
        license_str_new = input("Input license code again\n")
        license_str_new = license_str_new.encode('utf-8')
        if hashlib.md5(license_str_new).hexdigest() == "c02cbb31d0b41dca3c23596aceee2369":
            print("You're lucky!")
            change_file_with_times(441, solve=1)
            change_file_with_starts(441)
            update_hashes()
            solved = open(absolute_secret_file, "w")
            solved.write("1")
            solved.close()
        else:
            print("Okay,Uninstalling...")
            uninstall()


def uninstall():
    os.system("mv main.py .main.py")


def print_users():
    n = int(open(file_4_starts).read().split()[0])
    remaining_time = int(open(file_4_times).read().split()[0])
    solved = int(open(absolute_secret_file).read().split()[0])
    if (n > 0 and remaining_time > 0) or solved == 1:
        users = open(file_with_names, "r")
        for line in users:
            print(line)
    else:
        print("Let's buy a license!(--license) or try hack")


def check_hashes(silently=0):
    if int(open(absolute_secret_file).read().split()[0]) == 1 or (
            sha256_of_file(file_with_names) == open(file_4_hashes).read().split()[0] and sha256_of_file(file_4_times) ==
            open(file_4_hashes).read().split()[1] and sha256_of_file(file_4_starts) ==
            open(file_4_hashes).read().split()[2]):
        if silently == 0:
            pass
        else:
            print("all it's OK")
        return 1
    else:
        if silently == 0:
            pass
        else:
            print("Nice try, but not today")
        return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if check_files_on_start() and check_hashes(silently=0):  # если нужные файлы есть, то
            cmd = sys.argv[1]
            if (cmd == "-tl") or (cmd == "--time-limited"):  # запустим функцию
                program_time_limit()
            elif (cmd == "-sl") or (cmd == "--start-limited"):  # запустим функцию
                program_start_limit()
            elif (cmd == "-h") or (cmd == "--help"):  # справочная информация
                help()
            elif cmd == "--license":
                input_license()
            elif cmd == "--uninstall":
                uninstall()
            elif cmd == "--users":
                print_users()
            elif cmd == "--check_security":
                check_hashes(silently=1)
            else:
                print("Use -h or --help")
        else:
            print(
                "It looks like you tried to change or delete important files, I warned you about")  # если файлов не было(они создаются в инсталляторе)
            vote = input("Do you want to uninstall it?(y/n)")
            if vote[0] == "y":
                uninstall()
            elif vote[0] == "n":
                pass

    else:
        print("Use -h or --help")
