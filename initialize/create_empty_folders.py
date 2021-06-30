import os
import shutil
import pickle

class _initializer:
    pass



def create_empty_folders(path: str, version_name: str):
    def create_folder(d: dict, outer_path: str) -> None:
        for key, subfolder in d.items():
            key = _exam_version_folder(key)
            new_path = os.path.join(outer_path, key)
            os.mkdir(new_path)
            create_folder(subfolder, new_path)

    def _exam_version_folder(folder_name: str) -> str:
        if "-" in folder_name:
            try:
                int(folder_name.split("-")[-1])
                return version_name
            except:
                pass
        return folder_name

    sample_path = os.path.join(os.getcwd(), "initialize/folder_sample")
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


if __name__ == '__main__':
    documents_dir = os.path.expanduser(f'~/Desktop')
    create_empty_folders(documents_dir, "a")