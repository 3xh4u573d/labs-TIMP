import os
from tqdm import tqdm
import time

file_with_names = "/root/.do_not_enter/.file_with_names"  # файл с именами
file_4_times = "/root/.do_not_enter/.file_with_times"  # файл для просмотра оставшегося времени
file_4_starts = "/root/.do_not_enter/.file_with_starts"  # файл для просмотра оставшихся запусков
absolute_secret_file = "/root/.flag/.seriously/.true_flag/.im_sure/.really/.more/.directories/.u/.cant/.do/.this/.more/.absolutely/.just/.chill/.flag_{ch3ck_1n_4_1os3rs}"  # лицензия есть)))
flag_4_1_start = "/root/.flag/.seriously/.true_flag/.im_sure/.really/.more/.directories/.u/.cant/.do/.this/.more/.absolutely/.just/.chill/.flag_4_1_start"  # кончилось?))
file_4_hashes = "/root/.do_not_enter/.file_with_hashes"  # names,times,starts
list_of_files = [file_with_names, file_4_times, file_4_starts, absolute_secret_file, flag_4_1_start, file_4_hashes]
if sum([os.path.exists(path) for path in
        list_of_files]) == 6:  # Если все файлы остались на месте то востанавливаем значения
    if int(open(flag_4_1_start).read().split()[0]) == 0:
        if os.path.exists("main.py"):
            print("all it's ok, dont use it without trouble")
        else:
            if os.path.exists(".main.py"):
                os.system("mv .main.py main.py")  # Удаляем из скрытых сам скрипт
            else:
                print("something went wrong. You delete main.py?")
    else:
        print("No. You spend all your abilities. BUY LICENSE!!!")

elif sum([os.path.exists(path) for path in list_of_files]) == 0:  # Если ни одного файла из нужных нет
    if not os.path.exists("/root/.do_not_enter/"):
        os.makedirs("/root/.do_not_enter/", mode=0o777, exist_ok=True)
    if not os.path.exists(
            "/root/.flag/.seriously/.true_flag/.im_sure/.really/.more/.directories/.u/.cant/.do/.this/.more/.absolutely/.just/.chill/"):
        os.makedirs(
            "/root/.flag/.seriously/.true_flag/.im_sure/.really/.more/.directories/.u/.cant/.do/.this/.more/.absolutely/.just/.chill/"
            , mode=0o777, exist_ok=True)

        list_of_values = [None, '120', '3', '0', '0',
                          "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n2abaca4911e68fa9bfbf3482ee797fd5b9045b841fdff7253557c5fe15de6477\n4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce"]  # записываем в файлы стартовые значения
    for i in range(len(list_of_files)):
        file = open(list_of_files[i], "w")
        if i != 0:
            file.write(list_of_values[i])  # Пишем стандартные значения при первом запуске
        file.close()
        os.chmod(list_of_files[i], 0o777)

else:
    print("Nice try, but not today")
    os.system("clear")
    print("Deleting system...")
    for i in tqdm(range(1000)):  # Вывод бара прогресса
        time.sleep(0.002)

    print("\nDeleted!!")
    os.system("poweroff")  # Отключение системы если таковое есть
