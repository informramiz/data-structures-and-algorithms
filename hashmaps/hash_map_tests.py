from hash_map import HashMap
from asserts.asserts import assert_


def test_hash_map():
    hash_map = HashMap(2)

    # Test HashMap get and put
    key = "abcde"
    value = "ramiz"
    hash_map.put(key, value)
    output = hash_map.get(key)
    assert_(value, output)

    # Test size
    assert_(1, hash_map.size())

    # delete
    hash_map.delete("abcde")
    assert_(0, hash_map.size())

    # Test Rehash
    hash_map.put("mine", "mine")
    # this should trigger rehashing
    hash_map.put("hi", "hi")
    assert_(2, hash_map.size())
    print("All Tests Passed!")


test_hash_map()
