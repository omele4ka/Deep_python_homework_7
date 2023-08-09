# Напишите функцию группового переименования файлов.
# Она должна:
# принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов
# внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик
# файлов и расширение.
# Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами.
# Пример:
# rename(wanted_name = "video", count_nums=3,
# extension_old=".txt", extension_new=".csv",
# diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv

__all__ = ['rename_file']

import os

def rename_file(wanted_name, count_nums, extension_old, extension_new, diapazon):
    file_list = [f for f in os.listdir() if f.endswith(extension_old)]
    file_list.sort()

    for index, filename in enumerate(file_list):
        original_name = filename[:-len(extension_old)]
        original_chars = original_name[diapazon[0] - 1:diapazon[1]]
        counter_str = str(index + 1).zfill(count_nums)
        new_filename = original_chars + wanted_name + counter_str + extension_new
        os.rename(filename, new_filename)

if __name__ == '__main__':
    rename_file(wanted_name="video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])