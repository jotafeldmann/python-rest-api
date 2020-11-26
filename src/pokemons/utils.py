from typing import List


def remove_empty_items(list_items: List[str]) -> List[str]:
    return list(filter(None, list_items))
