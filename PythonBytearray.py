prime_numbers = [2, 3, 5, 7]

# convert list to bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)

# Output: bytearray(b'\x02\x03\x05\x07')


# The bytearray() method returns a bytearray object which is an array of the given bytes.

# Example
# Array of bytes from a string


string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)



# Example 3: Array of bytes from an iterable list

rList = [1, 2, 3, 4, 5]

arr = bytearray(rList)
print(arr)
