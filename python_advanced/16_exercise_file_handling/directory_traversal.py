from os import listdir, path


def directory_traversing(current_path, extensions):
    for el in listdir(current_path):
        # if path.isfile(el):
        #     ext = el.split(".")[-1]
        #     try:
        #         extensions[ext].append(el)
        #     except KeyError:
        #         extensions[ext] = [el]
        # traversing over nested directory if presents!!!
        if path.isdir(el):
            directory_traversing(path.join(current_path, el), extensions)
        else:
            ext = el.split(".")[-1]
            try:
                extensions[ext].append(el)
            except KeyError:
                extensions[ext] = [el]


def get_report(extensions, path):
    with open(path, "w") as file:
        for ext, names in sorted(extensions.items()):
            file.writelines(f".{ext}\n")
            file.writelines([f"- - - {x}\n" for x in sorted(names)])


#desktop path for Windows users only!!
#for Linux replace with this -> path.join(os.path.join(os.path.expanduser('~')), 'Desktop' + "\\report.txt")

desktop_path = path.join(path.join(path.expanduser('~')), 'OneDrive\Desktop') + "\\report.txt"

extensions_with_files = {}

directory_traversing(".", extensions_with_files)
get_report(extensions_with_files, desktop_path)
