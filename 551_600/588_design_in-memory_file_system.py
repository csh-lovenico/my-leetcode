from typing import List


class DirNode:
    def __init__(self):
        self.dirs = dict()
        self.files = dict()


class FileSystem:

    def __init__(self):
        self.root_dir = DirNode()

    def ls(self, path: str) -> List[str]:
        dirs = path.split('/')
        curr_dir = self.root_dir
        if path == '/':
            return sorted(list(curr_dir.dirs.keys()) + list(curr_dir.files.keys()))
        for i in range(1, len(dirs)):
            if i == len(dirs) - 1:
                if dirs[i] in curr_dir.dirs:
                    curr_dir = curr_dir.dirs[dirs[i]]
                    return sorted(list(curr_dir.dirs.keys()) + list(curr_dir.files.keys()))
                else:
                    return [dirs[i]]
            else:
                curr_dir = curr_dir.dirs[dirs[i]]

    def mkdir(self, path: str) -> None:
        dirs = path.split('/')[1:]
        curr_dir = self.root_dir
        for dir in dirs:
            if dir not in curr_dir.dirs:
                curr_dir.dirs[dir] = DirNode()
                curr_dir = curr_dir.dirs[dir]
            else:
                curr_dir = curr_dir.dirs[dir]

    def addContentToFile(self, filePath: str, content: str) -> None:
        dirs = filePath.split('/')
        curr_dir = self.root_dir
        for i in range(1, len(dirs)):
            if i == len(dirs) - 1:
                if dirs[i] in curr_dir.files:
                    curr_dir.files[dirs[i]] += content
                else:
                    curr_dir.files[dirs[i]] = content
            else:
                curr_dir = curr_dir.dirs[dirs[i]]

    def readContentFromFile(self, filePath: str) -> str:
        dirs = filePath.split('/')
        curr_dir = self.root_dir
        for i in range(1, len(dirs)):
            if i == len(dirs) - 1:
                return curr_dir.files[dirs[i]]
            else:
                curr_dir = curr_dir.dirs[dirs[i]]


if __name__ == '__main__':
    print('/a/b/c/d'.split('/')[1:-1])
    fs = FileSystem()
    # fs.mkdir('/a/b/c/d')
    print(fs.ls('/'))
