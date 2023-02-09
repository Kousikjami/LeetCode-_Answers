class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstword=[i for i in firstWord]
        secondword=[i for i in secondWord]
        targetword=[i for i in targetWord]
        fw=[]
        sw=[]
        tw=[]
        f,s,t=0,0,0
        for i in firstword:
            fw.append(ord(i)-97)
        for i in secondword:
            sw.append(ord(i)-97)
        for i in targetword:
            tw.append(ord(i)-97)
        fw=[str(i) for i in fw]
        f = int("".join(fw))
        sw=[str(i) for i in sw]
        s = int("".join(sw))
        tw=[str(i) for i in tw]
        t = int("".join(tw))
        if (f+s)==t:
            return True
        else:
            return False