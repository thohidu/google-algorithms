"""You'll create a HashTable class, methods to store and lookup values,
 and a helper function to calculate a hash value given a string."""
"""
def hashvalue(word):
     hash_val = (ord(word[0])*100) + ord(word[1])
     return hash_val 

class HashTable():
    table = []
    def __init__(self): pass 
    def store(self, word):
        hash_val = hashvalue(word)
        table[hash_val].append(word)


    def lookup(self, word):
        hash_val = hashvalue(word)
        ll = table[hash_val]
        found = False
        for w in range(len(ll)):
            if w == word:
                found = True 
                break
        return found 
                 
"""

"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable():
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash_val = self.calculate_hash_val(string)
        if self.table[hash_val]:
            self.table[hash_val].append(string)
        else:
            self.table[hash_val] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_val = self.calculate_hash_val(string)
        if self.table[hash_val]:
            for word in self.table[hash_val]:
                if string == word:
                    return hash_val 
            
        return -1

    def calculate_hash_val(self, string):
        """Helper function to calculate a hash value from a string"""
        hash_val = ord(string[0])*100 + ord(string[1])
        return hash_val 

if __name__ == "__main__":
    # Setup
    hash_table = HashTable()

    # Test calculate_hash_val
    # Should be 8568
    print(hash_table.calculate_hash_val('UDACITY'))

    # Test lookup edge case
    # Should be -1
    print(hash_table.lookup('UDACITY'))

    # Test store
    hash_table.store('UDACITY')
    # Should be 8568
    print(hash_table.lookup('UDACITY'))

    # Test store edge casee
    hash_table.store('UDACIOUS')
    # Should be 8568
    print(hash_table.lookup('UDACIOUS'))

