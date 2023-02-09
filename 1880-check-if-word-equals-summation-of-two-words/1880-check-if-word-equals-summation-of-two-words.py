class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        fw=''
        for i in firstWord:
            fw=fw+str(ord(i)-97)
        sw=''
        for i in secondWord:
            sw=sw+str(ord(i)-97)
        tw=''
        for i in targetWord:
            tw=tw+str(ord(i)-97)
        if (int(fw)+int(sw))==int(tw):
            return True