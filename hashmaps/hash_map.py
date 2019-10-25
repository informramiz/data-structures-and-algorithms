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
"""


class HashMap:
    def __init__(self, initial_size = 10):
        self.array = [None for _ in range(initial_size)]
        self.entries_count = 0
        self.prime = 37

    def put(self, key, value):
        pass

    def get(self, key):
        pass

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