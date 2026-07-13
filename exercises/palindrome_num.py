def palindrome_num(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

print(palindrome_num(121))  # Example usage of the palindrome_num function
 
def palindrome_str(input_string):
    # Check if the string is equal to its reverse
    return input_string == input_string[::-1]

print(palindrome_str("racecar"))  # Example usage of the palindrome_str function