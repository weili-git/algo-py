class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split("\n")
        stack = [] # len(stack) => level, stack[i] => length
        max_length = 0
        for line in lines:
            level = self.get_level(line)
            for i in range(len(stack) - level):
                stack.pop()
            if '.' not in line: # a dir
                stack.append(len(line) - level)
            else: # a file
                max_length = max(max_length, sum(stack) + len(stack) + len(line) - level)
        return max_length

    # 进入目录只能一层一层加，退出目录可以一次性退出多层

    def get_level(self, line):
        level = 0
        for i in range(len(line)):
            if line[i] == '\t':
                level += 1
            else:
                break
        return level