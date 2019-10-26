"""
For a string, say abcde, a very effective function is treating this as number of prime number base p. Let's elaborate
this statement.

For a number, say 578, we can represent this number in base 10 number system as
5*10^2+7*10^1+8*10^0

Similarly, we can treat abcde in prime P base as

a*P^4 + b*P^3 + c*P^2 + d*P^1 + e*P^0
 Here, we replace each character with its corresponding ASCII value.

A lot of research goes into figuring out good hash functions and this hash function is one of the most popular functions
 used for strings. We use prime numbers because the provide a good distribution. The most common prime numbers used for
 this function are 31 and 37.

Thus, using this algorithm, we can get a corresponding integer value for each string key and store it in the array.

Note that the array used for this purpose is called a bucket array. It is not a special array. We simply choose to give
a special name to arrays for this purpose. Each entry in this bucket array is called a bucket and the index in which we store a bucket is called bucket index.

Rehasing:

On average, the distribution of entries is such that if we have n entries and b buckets,
then each bucket does not have more than n/b key-value pair entries. This number which determines
the load on our bucket array n/b is known as load factor.
Generally, we try to keep our load factor around or less than 0.7.
This essentially means that if we have a bucket array of size 10, then the number of
key-value pair entries will not be more than 7.
What happens when we get more entries and the value of our load factor crosses 0.7?
In that scenario, we must increase the size of our bucket array. Also, we must recalculate the bucket index for each entry in the hashn map.

Note: the hash code for each key present in the bucket array would still be the same. However, because of the compression function, the bucket index will change.

Therefore, we need to rehash all the entries in our hash map. This is known as Rehashing.
"""


from lists.LinkedList import LinkedList


class MapNode(object):
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return isinstance(other, MapNode) and self.key == other.key

    def __repr__(self):
        return f"MapNode({self.key}, {self.value})"


class HashMap:
    def __init__(self, initial_size = 10):
        self.array = [LinkedList() for _ in range(initial_size)]
        self.entries_count = 0
        self.prime = 37
        self.load_factor = 0.7

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)
        bucket = self.array[bucket_index]
        key_node = bucket.search(MapNode(key, value))
        if key_node is None:
            bucket.append(MapNode(key, value))
        else:
            key_node.value = value

        self.entries_count += 1
        current_load_factor = self.entries_count / len(self.array)
        # we need to make sure our load factor is under self.load_factor
        if current_load_factor > self.load_factor:
            # as the load factor has increased so let's increase size of our buckets array
            self._rehash()

    def __put(self, map_node):
        self.put(map_node.key, map_node.value)

    def get(self, key):
        bucket_index = self.get_bucket_index(key)
        linked_list_node = self.array[bucket_index].search(MapNode(key))
        if linked_list_node is not None:
            map_node = linked_list_node.value
            return map_node.value
        else:
            return None

    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        is_deleted = self.array[bucket_index].remove(MapNode(key))
        if is_deleted:
            self.entries_count -= 1
        return is_deleted

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        # start from P^0 = 1
        coefficient = 1
        hash_code = 0
        for c in key:
            hash_code += coefficient * ord(c)
            # increase coefficient by one `self.prime` to get the right value of P^i
            coefficient *= self.prime

        # compress hash code to bring it in range [0, len(array)-1]
        return hash_code % len(self.array)

    def _rehash(self):
        """
        Increases the size of the bucket array and copies the entries from old array to new array
        by putting each entry in new array by getting a fresh hash code as our hash code compression
        result will differ because we have increased the array size
        """
        # create new array
        old_array = self.array
        self.array = [LinkedList() for _ in range(2 * len(self.array))]

        # reset entries count
        self.entries_count = 0
        for bucket in old_array:
            for list_node in bucket:
                self.__put(list_node)

    def size(self):
        return self.entries_count
