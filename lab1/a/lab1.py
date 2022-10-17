import os  # модуль для работы с операционной системой
import hashlib  # модуль для хэширования пароля
import sys  # модуль для получения аргументов


def help():
    print(
        "Usage\n sudo lab1.py [options]\nOptions:\n -h \t\t\t print help message\n --help \t\t\t the same as -h \n --start \t\t\t start the program\n --stop <password>  stop the program through the password")


# Справка для пользователя

def stop(password, count=0):
    passw_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()  # хеширование ввода пользователя по sha1
    true_passw = open("/root/templates.tbl").readline().rstrip()  # достаём хеш правильного пароля из templates.tbl
    if passw_hash == true_passw:
        with open('/root/templates.tbl', 'r') as f:  # открываем файл с именами файлов
            temps = f.read().splitlines()  # разделяем
        for fname in temps[1:]:  # итерируемся по каждому кроме 0-го, т.к это хэш пароля
            check = os.path.exists(fname)  # переменная для проверки существования файла
            if check:
                os.system(
                    " sudo chattr -auiD " + fname + " 1>/dev/null#")  # если существует то сразу убираем бит i Запрещающий удаление и изменение руту
                os.chmod(fname, 0o777)  # даём всё права файлу обратно
        os.system(" sudo chattr -auiD " + "/root/templates.tbl" + " 1>/dev/null#")  # снимаем запреты с templates.tbl
        os.system(" sudo chmod 777 /root/templates.tbl")

    else:
        if count > 2:
            print("Wrong password!")
        else:
            print("Wrong password. Try again")
            new_pass = input("type new password:")
            stop(new_pass, count + 1)  # count - количество неверных попыток


def start():
    with open('/root/templates.tbl', 'r') as f:
        temps = f.read().splitlines()
    for fname in temps[1:]:
        check = os.path.exists(fname)
        if check:
            os.chmod(fname, 0o000)
            os.system("sudo chattr +auiD " + fname + " 1>/dev/null#")
        else:
            closing = open(fname, 'tw', encoding='utf-8')  # открываем файл в текстовом режиме для записи
            closing.close()  # закрываем
            os.chmod(fname, 0o000)
            os.system(" sudo chattr +auiD " + fname + " 1>/dev/null#")
    os.chmod(" /root/templates.tbl", 0o100)
    os.system(" sudo chattr +auiD " + "/root/templates.tbl" + " 1>/dev/null#")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        option = sys.argv[1]
        if option == "-h" or option == "--help":
            help()
        if option == "--start":
            start()
        if option == "--stop":
            stop(sys.argv[2], 0)
    else:
        print("Wrong options. See -h or --help")
os.chmod(os.getcwd() + "/" + sys.argv[0],
         444)  # даём ТЕКУЩЕМУ файлу права ТОЛЬКО на чтение(т.к интерпретатор питона нуждается только во флагах r)
# hochu_5
