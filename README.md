# Data-Structures_HashKeyDictionary
In this Python project, the following instructions were implemented: Your dictionary will consist of two arrays (one for keys and one for values). When the user asks to insert a new value into the array (such as myDict['Temple'] = 12345), you create a hash value from the key (convert 'Temple' into an integer that can index the arrays). Once you have the hash value, you should insert the key accordingly into the key array, and the value into the value array.  When the user wants to read a value from the dictionary, you use the same process. If the user wants to see what value is at myDict['Temple'], you should first convert 'Temple' into its hash value, and then return valueArray[hashValue]. See .docx file for greater project details