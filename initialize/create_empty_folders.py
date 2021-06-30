import os
import shutil
import pickle

class _initializer:
    pass



def create_empty_folders(path: str, version_name: str):
    def create_folder(d: dict, outer_path: str) -> None:
        for key, subfolder in d.items():
            if _exam_version_folder(key):
                key = version_name
            new_path = os.path.join(outer_path, key)
            os.mkdir(new_path)
            create_folder(subfolder, new_path)

    def _exam_version_folder(folder_name: str) -> bool:
        if "-" in folder_name:
            try:
                int(folder_name.split("-")[-1])
                return True
            except:
                pass
        return False

    def add_ini(out_path):
        l = os.listdir(out_path)
        for i in l:
            new_path = os.path.join(out_path, i)
            if os.path.isdir(new_path):
                if i in ini_dict.keys():
                    print()
                    shutil.copy(ini_dict[i], os.path.join(new_path, version_name))
                    continue
                add_ini(new_path)


    if not _exam_version_folder(version_name):
        raise TypeError("请以'xxx-日期'的全小写名称命名版本，例如：example-0630")
    if "." in version_name:
        raise TypeError("版本名不可含有'.'")
    sample_path = os.path.join(os.getcwd(), "initialize/sample/folder_sample")
    if os.path.exists(sample_path):
        with open(sample_path, 'rb') as f:
            folder_tree = pickle.load(f) # type:dict
    else:
        raise TypeError("没有文件夹样本, 请滴滴程序员在程序员的电脑上跑一遍get_foler_sample.py，生成样本文件")
    if folder_tree:
        pathd = os.path.join(path, version_name)
        if os.path.exists(pathd):
            shutil.rmtree(pathd)
        os.mkdir(pathd)
        create_folder(folder_tree, pathd)
        ini_dict = {"Stand": os.path.join(os.getcwd(), "initialize/sample/stand_index.ini"),
                    "Wash": os.path.join(os.getcwd(), "initialize/sample/wash_index.ini"),
                    "Wind": os.path.join(os.getcwd(), "initialize/sample/wind_index.ini")}
        add_ini(pathd)

if __name__ == '__main__':
    documents_dir = os.path.expanduser(f'~/Desktop')
    create_empty_folders(documents_dir, "a-0212")