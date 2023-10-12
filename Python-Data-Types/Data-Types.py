# Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.

def calculate_len_of_str(str) -> int:
    length_of_str = 0
    for _ in str:
        length_of_str += 1
       
    return length_of_str

# Task 1.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:
# Input: 'Oh, it is python' 
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

def count_number_and_frequency(str) -> dict:
    str_for_result = str.lower()
    char_count = 0
    result = {}
    for i in str_for_result:
        if i not in result:
            char_count = str_for_result.count(i)
            result[i] = char_count

    return result

# Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
# Examples:
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white']

def find_unique_words(input_list) -> list:
    result = []
    for i in input_list:
        if i not in result:
            result.append(i)
    
    return sorted(result)

# Task 1.3
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# Examples: 
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}

def get_all_divisors_of_input_number(number) -> tuple:
    result = tuple(i for i in range(1, number+1) if (number%i) == 0)

    return result

# Task 1.4
# Write a Python program to sort a dictionary by key.

def sort_dict_by_key(input_dict) -> dict:
    
    return dict(sorted(input_dict.items()))

# Task 1.5
# Write a Python program to print all unique values of all dictionaries in a list.
# Examples:
# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

def find_unique_values(input_list) -> list:
    result = []
    for dicts in input_list:
        for value in dicts:
            if dicts.get(value) not in result:
                result.append(dicts.get(value))

    return result

# Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer. 
# Examples:
# Input: (1, 2, 3, 4)
# Output: 1234

def convert_tuple(input_tuple) -> int:
    result = ""
    temp_list = []
    for item in input_tuple:
        temp_list.append(str(item))
    
    result = "".join(temp_list)
    
    return int(result)

# ### Task 1.6
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# Input:
# a = 2
# b = 4
# c = 3
# d = 7
# Output:
# 	3	4	5	6	7	
# 2	6	8	10	12	14	
# 3	9	12	15	18	21	
# 4	12	16	20	24	28

def print_of_multiplication_table(a, b, c, d) -> None:
    
    print("\t", end=" ")
    for j in range(c, d + 1):
        print(f"{j}\t", end=" ")
    print()

    
    for i in range(a, b + 1):
        print(f"{i}\t", end=" ")
        for j in range(c, d + 1):
            print(f"{i * j}\t", end=" ")
        print()
    

if __name__ == '__main__':
    print(calculate_len_of_str("SGH ii"))
    print(count_number_and_frequency('Oh, it is python'))
    print(find_unique_words(['red', 'white', 'black', 'red', 'green', 'black']))
    print(get_all_divisors_of_input_number(60))
    print(sort_dict_by_key({"Ostap": 12, "Serg": 14, "Denis": 22, "Dmitry": 18, "Julia": 16}))
    print(find_unique_values([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))
    print(convert_tuple((1, 2, 3, 4)))
    print_of_multiplication_table(2, 4, 3, 7)
