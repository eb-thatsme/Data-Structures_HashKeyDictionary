################################################################################
### Engineering Computation: Project 5
### By Ellisa Booker
### 
### This program allows you to create a dictionary of values at custom keys
### You can directly set any key to a value using myDict[key] = value
### You can print the list in alphabetized order based on their keys (numerical keys come first)
### 
################################################################################


# Create a class of type "dictionary" that holds various keys and values
class dictionary:
    
    # Initialize the dictionary with a buffer length, dictValues array that will store values, and dictKeys array that stores keys
    def __init__(self, _buffLen = 1000):
        self.buffLen = _buffLen
        self.dictValues = [None]*self.buffLen
        self.dictKeys = []
        self.origKeys = []
    
    # Hashing function for the key
    def hash_function(self,key):
        
        # First we convert the key to a string if it is not already a string
        # This allows us to use the same hashing function no matter the data type of the key
        string1 = str(key)
        
        # Iterate through each character in the string and convert to ascii values. Then raise to 1.2 power and add
        # (This is the hash function given by project 4 solution)
        s = 0
        for c in string1:
            s += ord(c)**1.2
        hashed_key = s%self.buffLen
            
        # Append the key to the hashed key to the keys array
        self.dictKeys.append(hashed_key)
     
        # Find the index of the key in the keys array so we can store the value in the values array at the same index
        index = self.dictKeys.index(hashed_key)
        return index
    
    # Allows us to directly set the value of dictionary at the given key value
    def __setitem__(self, key, value):
        index = self.hash_function(key)
        # Store value in dictionary at the same index as the hashed key
        self.dictValues[index] = value
        # Store original keys so that we can alphabetize them in the print function
        self.origKeys.append(key)
        
    
    # Allows us to directly get the value of the dictionary
    def __getitem__(self, key):
        index = self.hash_function(key)
        # Get value in dictionary at the same index as the key
        return self.dictValues[index]
    
    # Print the values in the dictionary     
    def printDict(self):
        print("--------------\nPrinting the current dictionary...")
        
        # Sort the keys by numeric integer, numeric float, and alphatbetical order respectively
        intKeys = list(filter(lambda x: type(x) == int, self.origKeys))
        floatKeys = list(filter(lambda x: type(x) == float, self.origKeys))
        strKeys = list(filter(lambda x : type(x) ==str,self.origKeys))
        
        sortedDict = sorted(intKeys) + sorted(floatKeys) + sorted(strKeys) 
        
        # Rehash the sorted key list and print it
        for x in range(self.buffLen):
            index = self.hash_function(sortedDict[x])
            print(self.dictValues[index])

#################################################
# Main Function
#################################################

def main():
    
    # Create a dictionary of length 3 and insert values at the given keys
    myDict = dictionary(3)
    myDict[3822] = 'fun'
    myDict['Temple'] = 12345
    myDict[3.84] = 'an important number'
    
    # Print the value at a specific key
    print(myDict[3.84])
    
    # Print the whole dictionary in numeric and alphabetical order
    myDict.printDict()
    
    
if __name__=="__main__":
    main()