def appearance(intervals):
    """
    appearance(intervals)
    Считает общее количество секунд
    :param intervals: словарь интервалами
    :return: количество общих секунд: int
    """
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    lesson_range = range(lesson[0], lesson[1])
    lesson = set(counter for counter in lesson_range)
    pupil = set(second for range_count in make_list_ranges(pupil) for second in range_count)
    tutor = set(second for range_count in make_list_ranges(tutor) for second in range_count)
    all_seconds = lesson & pupil & tutor
    return len(all_seconds)


def make_list_ranges(intervals):
    """
    make_list_ranges(intervals)
    Создает список range функций, для каждого интервала
    :param intervals: список интервалов
    :return: список range функций
    """
    check_list = [[range(intervals[0], intervals[1]), intervals[0], intervals[1]]]
    for i in range(0, len(intervals), 2):
        for id_count, j in enumerate(check_list):
            if intervals[i] in j[0]:
                if intervals[i + 1] not in j[0]:
                    check_list[id_count] = [range(check_list[id_count][1], intervals[i + 1]),
                                            check_list[id_count][1], intervals[i + 1]]
                    break
                else:
                    break
        else:
            check_list.append([range(intervals[i], intervals[i + 1]), intervals[i], intervals[i + 1]])
    return [val[0] for val in check_list]


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        print(test_answer)
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
