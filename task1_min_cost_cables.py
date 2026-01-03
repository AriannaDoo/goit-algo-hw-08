import heapq

def min_cost_to_connect_cables(cables: list[int]) -> int:
    """
    Обчислює мінімальні загальні витрати на об'єднання кабелів.

    Алгоритм:
    Поміщаємо всі довжини кабелів у мінімальну купу --
    Поки в купі більше одного елемента:
       - дістаємо два найкоротші кабелі,
       - об'єднуємо їх,
       - додаємо вартість до загальної суми,
       - повертаємо новий кабель у купу.

    """
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    print("Мінімальні загальні витрати:", min_cost_to_connect_cables(cables))
