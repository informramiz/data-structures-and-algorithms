from hash_map import HashMap

def test_hash_map():
    hash_map = HashMap()
    expected = 4
    input = "abcd"
    actual = hash_map.get_hash_code(input)
    assert(expected == actual)


test_hash_map()