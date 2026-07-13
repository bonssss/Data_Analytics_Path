numbers =[3, 5, 2, 8, 1]

for num in numbers:
    # print(num)  # Print each number in the list

    search_num = 8
    found = False
    if search_num in numbers:
        found = True
        print(f"{search_num} is found in the list.")
        break  # Exit the loop if the number is found
    if not found:
        print(f"{search_num} is not found in the list.")
        break