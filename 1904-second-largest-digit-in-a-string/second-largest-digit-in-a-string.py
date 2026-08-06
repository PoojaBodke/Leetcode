class Solution(object):
    def secondHighest(self, s):
        first=-1
        second=-1
        for ch in s:
            if ch.isdigit():
                digit=int(ch)
                if digit==first or digit==second:
                    continue
                if digit>first:
                    second=first
                    first=digit
                elif digit>second:
                    second=digit
        return second

        