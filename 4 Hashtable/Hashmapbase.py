# Basic Hashtable without check collision
class HashTable:
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]  # Empty bucket

    # Create a hash function to get index from key by using hash function
    # (a randomized Multiply-Add-and-Divide(MAD) formula)
    def hash_function(self, key):
        return hash(key) % self.size

    # Insert values into hash map
    def insert_value(self, key, value):
        # get index from hash function
        hash_key_index = self.hash_function(key)
        # Move index into bucket
        bucket = self.hash_table[hash_key_index]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record

            # Check if the bucket has same key as the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise, append the new key-value pair to the bucket
        if found_key:  # true
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    # Return searched value with specific key
    def get_value(self, key):
        # get index from hash function
        hash_key_index = self.hash_function(key)

        # Move index into bucket
        bucket = self.hash_table[hash_key_index]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record

            # check if the bucket has same key as the key being searched
            if record_key == key:
                found_key = True
                break
        # if the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_value
        else:
            return "No record found"

    # Remove a value with a specific key
    def delete_value(self, key):
        # get index from the key by using hash function
        hash_key_index = self.hash_function(key)

        # Move index inside bucket
        bucket = self.hash_table[hash_key_index]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record

            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # print the items of hash map
    def __str__(self):
        str_map = ""
        for item in self.hash_table:
            str_map += str(item)
        return str_map
        # OR use this method:
        # return "".join(str(item) for item in self.hash_table)


hash_table = HashTable(20)

# insert some values
hash_table.insert_value('gfg@example.com', 'some value')
print(hash_table)
print()

hash_table.insert_value('portal@example.com', 'some other value')
print(hash_table)
print()

# search/access a record with key
print(hash_table.get_value('portal@example.com'))
print()

# delete or remove a value
hash_table.delete_value('portal@example.com')
print(hash_table)
