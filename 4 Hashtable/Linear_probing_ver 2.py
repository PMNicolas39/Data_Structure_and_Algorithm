class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]  # Create a array contains key-value pairs.

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX  # hash(key): to return the Unicode. Could use ord(char for char in key) instead.

    # use __getattribute__ method of python to get item/ value.
    def __getitem__(self, key):
        index = self.get_hash(key)
        if self.arr[index] is None:
            return
        # Find slot contains key-value pair
        list_prob = self.get_prob_range(index)
        for prob_index in list_prob:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        if self.arr[index] is None:
            self.arr[index] = (key, value)
        else:
            # find new empty slot
            new_index = self.find_slot(key, index)
            self.arr[new_index] = (key, value)
        print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        list_prob = self.get_prob_range(index)
        for prob_index in list_prob:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap is FULL")

    def __delitem__(self, key):
        index = self.get_hash(key)
        list_prob = self.get_prob_range(index)
        for prob_index in list_prob:
            if self.arr[prob_index] is None:
                return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)


t = Hash_table()
t['march 6'] = 20
t['march 17'] = 88
