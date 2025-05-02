class Solution:
    def restoreIpAddresses(self, s):
        def valid(s, start, length):
            if start >= len(s):
                return False
            return length == 1 or (
                s[start] != "0"
                and (length < 3 or int(s[start : start + length]) <= 255)
            )

        ans = []
        length = len(s)
        for len1 in range(max(1, length - 9), min(4, length - 2) + 1):
            if not valid(s, 0, len1):
                continue
            for len2 in range(
                max(1, length - len1 - 6), min(4, length - len1 - 1) + 1
            ):
                if not valid(s, len1, len2):
                    continue
                for len3 in range(
                    max(1, length - len1 - len2 - 3),
                    min(4, length - len1 - len2) + 1,
                ):
                    if valid(s, len1 + len2, len3) and valid(
                        s, len1 + len2 + len3, length - len1 - len2 - len3
                    ):
                        ans.append(
                            s[:len1]
                            + "."
                            + s[len1 : len1 + len2]
                            + "."
                            + s[len1 + len2 : len1 + len2 + len3]
                            + "."
                            + s[len1 + len2 + len3 :]
                        )
        return ans