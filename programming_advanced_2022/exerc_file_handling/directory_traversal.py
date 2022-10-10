from os import listdir
from os.path import isfile


def directory_traversal(path, files_by_ext):
    for element in listdir(path):
        if isfile(element):
            ext = element.split(".")[-1]
            if ext not in files_by_ext:
                files_by_ext[ext] = []
            files_by_ext[ext].append(element)


result = {}
directory_traversal("./", result)

with open("report.txt", "w") as output_file:
    for extension, files in sorted(result.items(), key=lambda x: (x[0], x[1])):
        output_file.write(f".{extension}\n")
        for current_file in files:
            output_file.write(f"- - - {current_file}\n")


# from os import walk
#
# result = {}
# for root, dirs, files in walk("."):
#     for file in files:
#         ext = file.split(".")[-1]
#         if ext not in result:
#             result[ext] = []
#         result[ext].append(file)
#
# for key, value in result.items():
#     print(key, value)


# from os import listdir
# from os.path import isdir, join
#
#
# def directory_traversal(path, files_by_ext):
#     for el in listdir(path):
#         if isdir(join(path, el)):
#             directory_traversal(join(path, el), files_by_ext)
#         else:
#             extension = el.split(".")[-1]
#             if extension not in files_by_ext:
#                 files_by_ext[extension] = []
#             files_by_ext[extension].append(el)
#
#
# result = {}
# directory_traversal("./", result)
#
# for key, value in result.items():
#     print(f".{key}")
#     print(f"{value}")
