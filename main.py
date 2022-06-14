import os
import shutil

def zapis_file(fi):

    with open (log,'a') as logi:
        path_file = f"{path_first}\\{fi}"
        df = (os.path.getsize(path_file))/1024 # Вывод в килобайтах
        print(f"{fi};{df}",file=logi)

def copy_win(fi):
    source = f"{path_first}\\{fi}"
    final = f"{path_second}\\{fi}"
    shutil.copy(source, final)

def check_exist(dir_first,dir_second):
    res_list = list()
    for i in dir_first:
        if i not in dir_second:
            res_list.append(i)
            zapis_file(i)
            #copy_win(i) - Убрать комментарий чтобы переместить

    print("Число элементов которых нет в первой последовательности - ", len(res_list))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path_first = r"******" # Первый путь
    path_second = r"******" # Второй путь
    log = "log.txt"


    dir_first = os.listdir(path_first)
    dir_second = os.listdir(path_second)

    print(f"Количество файлов паке {path_first}    -  ",len(dir_first))
    print(f"Количество файлов паке {path_second}    -  ",len(dir_second))

    check_exist(dir_first,dir_second)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
