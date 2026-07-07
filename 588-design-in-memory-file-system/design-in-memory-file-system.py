class FileSystem:

    def __init__(self):
        self.fileSystem = {}
    

    def ls(self, path: str) -> List[str]:
        # go as far into path as possible
        # if cannot reach the farthest directory, return []
        # if path is file, return [file name]
        # if path is directory, return all files and subdirectories
        path = path.split("/")
        curr_level = self.fileSystem
        for level in path:
            if level == "":
                continue
            if (level, "dir") in curr_level:
                curr_level = curr_level[(level, "dir")]
            else:
                return [level]
        
        return sorted([item[0] for item in curr_level])


    def mkdir(self, path: str) -> None:
        path = path.split("/")
        curr_level = self.fileSystem
        for level in path:
            if level == "":
                continue
            if (level, "dir") not in curr_level:
                curr_level[(level, "dir")] = {}
            curr_level = curr_level[(level, "dir")]

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr_level = self.fileSystem
        path = filePath.split("/")
        for level in path:
            if level == "":
                continue
            if (level, "dir") in curr_level:
                curr_level = curr_level[(level, "dir")]
            elif (level, "file") in curr_level: # file already exists, append content
                curr_level[(level, "file")] += content
            else: # create new file
                curr_level[(level, "file")] = content

    def readContentFromFile(self, filePath: str) -> str:
        curr_level = self.fileSystem
        path = filePath.split("/")
        curr_level = self.fileSystem
        for level in path:
            if level == "":
                continue
            if (level, "dir") in curr_level:
                curr_level = curr_level[(level, "dir")]
            else:
                return curr_level[(level, "file")]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)