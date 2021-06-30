import os
import pickle


class folder_tree_copier():
    def __init__(self, sample_path: str):
        if os.path.exists(sample_path):
            robot = sample_path.split("/")[-1]
            self._robot_tree = {robot: {}}
            self._folder2dict(self._robot_tree[robot], sample_path)
            with open('folder_sample', "wb") as f:
                pickle.dump(self._robot_tree, f)
        else:
            raise TypeError("样本文件夹不存在, 请确认路径正确性")
        self.robot_tree = []

    def _folder2dict(self, outer_folder: dict, path: str) -> None:
        l = os.listdir(path)
        for i in l:
            new_path = os.path.join(path, i)
            if os.path.isdir(new_path):
                outer_folder[i] = {}
                self._folder2dict(outer_folder[i], new_path)


if __name__ == '__main__':
    documents_dir = os.path.expanduser(f'~/Documents')
    folder_tree_copier(f'{documents_dir}/_XYZ/drawing/Robot')
