def merge_sort(list):
    if len(list) > 1:

        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        # i left arr idx
        # j right arr idx
        # k merged arr idx

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        # for case where the right arr is empty
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        # for case where left arr is empty
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

    return list
