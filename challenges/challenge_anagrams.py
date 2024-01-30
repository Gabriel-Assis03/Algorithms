def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)

    if (end - start) > 1:
        mid = (start + end) // 2

        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        order(numbers, start, mid, end)


def order(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0
    general_index = start

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index += 1
        else:
            numbers[general_index] = right[right_index]
            right_index += 1
        general_index += 1

    while left_index < len(left):
        numbers[general_index] = left[left_index]
        left_index += 1
        general_index += 1

    while right_index < len(right):
        numbers[general_index] = right[right_index]
        right_index += 1
        general_index += 1


def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return ('', '', False)
    first_string = first_string.lower()
    second_string = second_string.lower()
    word1 = list(first_string)
    word2 = list(second_string)
    merge_sort(word1)
    merge_sort(word2)

    if ''.join(word1) == ''.join(word2):
        return (''.join(word1), ''.join(word2), True)
    else:
        return (''.join(word1), ''.join(word2), False)
