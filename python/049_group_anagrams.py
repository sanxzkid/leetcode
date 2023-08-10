from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Function printing python version."""
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return groups.values()

if __name__ == '__main__':
    ans = group_anagrams(["asd", "dsa", "das","sda", "dds", "dsd"])
    print(ans)
