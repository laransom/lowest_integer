def solution(array):
    length = len(array)
    int_present_array = [0] * length

    for number in array:
        if 0 < number <= length:
            int_present_array[number - 1] = 1

    for idx, value in enumerate(int_present_array):
        if value == 0:
            return idx + 1

    return length + 1
