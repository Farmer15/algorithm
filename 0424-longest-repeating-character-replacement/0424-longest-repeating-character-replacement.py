class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        hash_map = defaultdict(int)
        hash_map[s[0]] = 1
        max_length = 0
        max_count = 1

        while right < len(s):
            slide_length = right - left + 1

            if slide_length - max_count <= k:
                max_length = max(max_length, slide_length)
                right += 1

                if right < len(s):
                    hash_map[s[right]] += 1
                    max_count = max(max_count, hash_map[s[right]])
            else:
                hash_map[s[left]] -= 1
                left += 1

        return max_length


            