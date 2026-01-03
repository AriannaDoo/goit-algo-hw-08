import heapq

def merge_k_lists(lists: list[list[int]]) -> list[int]:
    """
    Об'єднує k відсортованих списків в один відсортований список
    з використанням мінімальної купи.

    Часова складність: O(n log k),
    де n — загальна кількість елементів.
    """
    heap = []
    result = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        value, list_idx, elem_idx = heapq.heappop(heap)
        result.append(value)

        if elem_idx + 1 < len(lists[list_idx]):
            next_tuple = (
                lists[list_idx][elem_idx + 1],
                list_idx,
                elem_idx + 1
            )
            heapq.heappush(heap, next_tuple)

    return result


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Відсортований список:", merge_k_lists(lists))
