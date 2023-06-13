class WordDictionary:

    def __init__(self):
        self.dic = {}
        self.max_len = -1

    def addWord(self, word: str) -> None:
        self.max_len = max(self.max_len, len(word))
        dic = self.dic
        for ch in word:
            if not dic.get(ch):
                dic[ch] = {'wd': False}
            dic = dic.get(ch)
        dic['wd'] = True

    def search(self, word: str) -> bool:
        if len(word) > self.max_len:
            return False
        dic = self.dic
        dic_list = [dic]  # . search
        for ch in word:
            next_list = []
            for d in dic_list:
                if ch == '.':  # go down 1 level, bfs
                    for k, v in d.items():
                        if k != 'wd':
                            next_list.append(v)
                else:
                    if d.get(ch):
                        next_list.append(d[ch])
            dic_list = next_list

        for d in dic_list:
            if d['wd']:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

