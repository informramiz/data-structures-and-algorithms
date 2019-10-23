def is_list(item):
    return isinstance(item, list)


def _deep_reverse_recursive(items, index):
    if index >= len(items):
        return []

    output = _deep_reverse_recursive(items, index + 1)
    if is_list(items[index]):
        # the items[index] value itself is a list so traverse it as well
        output.append(_deep_reverse_recursive(items[index], 0))
    else:
        output.append(items[index])

    return output


def deep_reverse(items):
    return _deep_reverse_recursive(items, 0)


def run_test_case(input, expected_output):
    actual_output = deep_reverse(input)
    assert expected_output == actual_output, f"expected: {expected_output}, actual: {actual_output}"


def test_deep_reverse():
    run_test_case([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
    run_test_case([1, 2, [3, 4, 5], 4, 5], [5, 4, [5, 4, 3], 2, 1])
    run_test_case([1, [2, 3, [4, [5, 6]]]], [[[[6, 5], 4], 3, 2], 1])
    run_test_case([1, [2,3], 4, [5,6]], [ [6,5], 4, [3, 2], 1])


test_deep_reverse()


