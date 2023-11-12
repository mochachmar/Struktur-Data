# Moch Achmar_22362_K
class LinearProbingHash:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash_function(self, data):
        return data % self.size

    def insert(self, data):
        hash_value = self.hash_function(data)
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = data
        else:
            next_slot = (hash_value + 1) % self.size
            while self.hash_table[next_slot] is not None and next_slot != hash_value:
                next_slot = (next_slot + 1) % self.size
            if self.hash_table[next_slot] is None:
                self.hash_table[next_slot] = data
            else:
                print("Tabel hash penuh. Tidak dapat memasukkan data.")

    def display(self):
        for index, data in enumerate(self.hash_table):
            print(f"Slot {index}: {data}")


def linear_probing(data):
    array = [None] * 11

    for num in data:
        position = num % 11

        while array[position] is not None:
            position = (position + 1) % 11

        array[position] = num

    return array


hash_table = LinearProbingHash(11)
data_list = [13, 15, 17, 19, 24, 35, 47]

for data in data_list:
    hash_table.insert(data)

hash_table.display()

result = linear_probing(data_list)

print("\nArray:")
print(result)
