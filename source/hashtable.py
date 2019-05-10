#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n), loops through every item in each bucket"""
        # Collect all keys in each bucket
        all_keys = list()
        for bucket in self.buckets:
            for key, value in bucket.items():   # O(n)
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n), loops through every item in each bucket"""
        all_values = list()
        for bucket in self.buckets:
            for _, value in bucket.items():   # O(n)
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n), loops through every item in each bucket"""
        # Collect all pairs of key-value entries in each bucket
        all_items = list()
        for bucket in self.buckets:             # b iterations => O(b * l) => O(n)    
            all_items.extend(bucket.items())    # O(l) because l is list length
        return all_items    # O(1)

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n), loops through every item in each bucket"""
        length = 0      # O(1)
        for bucket in self.buckets:     # b iterations => O(b * l) => O(n)
            length += bucket.length()   # O(n) from ll.length(each b); or O(l = n/b)
        return length   # O(1)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(l) where l is a bucket's length (find method)
        """
        index = self._bucket_index(key)     # O(1)
        bucket = self.buckets[index]        # O(1)
        entry = bucket.find(lambda entry: key == entry[0])  #O(l), l = length
        return entry is not None    # O(1)

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(1) if it's found and doesn't go through all of the nodes, or O(l) to raise error"""
        bucket_index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[bucket_index]     # O(1)
        entry = bucket.find(lambda entry: key == entry[0])  #O(l), l = length
        
        if entry is not None:
            return entry[1]

        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(l) where l = length of bucket """
        bucket_index = self._bucket_index(key)              # find bucket index, O(1)
        bucket = self.buckets[bucket_index]                 # get bucket, O(1)
        entry = bucket.find(lambda entry: key == entry[0])  # O(l), l = length
        
        if entry is not None:       # O(1)
            bucket.delete(entry)    # O(l)    

        bucket.append((key, value))    # append key value pair, O(1)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(1) if it isn't found, O(l) if not found in bucket"""
        bucket_index = self._bucket_index(key)              # find bucket index
        bucket = self.buckets[bucket_index]                 # get bucket
        entry = bucket.find(lambda entry: key == entry[0])

        if entry is not None:
            bucket.delete(entry)
            return
        
        raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
