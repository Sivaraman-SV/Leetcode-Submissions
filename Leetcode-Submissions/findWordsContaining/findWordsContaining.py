class Solution(object):
    def findWordsContaining(self, words, x):
        l = []
        for i in range(len(words)):
            if x.lower() in words[i]:
                l.append(i)
        return l
