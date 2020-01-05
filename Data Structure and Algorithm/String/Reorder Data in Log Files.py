class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        order(letterlogs, digitlog)
        letterlogs: lexicographical order
        """
        def f(logs):
            id_, rest = logs.split(" ", 1)
            return (0,rest,id_) if rest[0].isalpha() else (1, )
        return sorted(logs, key=f)
