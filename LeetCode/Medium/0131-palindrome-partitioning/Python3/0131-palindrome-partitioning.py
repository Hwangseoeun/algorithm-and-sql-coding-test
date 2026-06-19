class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtarcking(s, start, current):
            if start == len(s):
                result.append(current[::])
                return

            for i in range(start, len(s)):
                word = s[start:i+1]

                if word == word[::-1]:
                    current.append(word)
                    backtarcking(s, start + len(word), current)
                    current.pop()

        result = []

        backtarcking(s, 0, [])

        return result