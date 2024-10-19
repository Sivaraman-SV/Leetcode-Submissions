class Solution(object):
    def capitalizeTitle(self, title):
        title.strip()
        s = title.lower()
        s = s.title()
        l = s.split()
        l1 = []
        for i in l:
            if len(i) == 1 or len(i) == 2:
                i = i.lower()
            else:
                pass
            l1.append(i)
            s1 = " ".join(l1)    
        return s1

        