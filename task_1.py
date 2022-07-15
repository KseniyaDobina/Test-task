def task(array):
    """
    task(array)
    :param array: список цифр
    :return: индекс первого встреченного 0
    """
    count = 0
    for i in array:
        if int(i) == 0:
            return count
        count += 1


print(task("111111111110000000000000000"))
