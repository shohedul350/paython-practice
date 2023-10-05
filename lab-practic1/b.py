def find_smallest_number(numbers):
  small_number  = numbers[0]
  for num in numbers:
    if num < small_number:
      small_number = num
  return small_number
        
set_numbers = [1,3,2,8,4,8,3,2,7,8,5]

smallest_number = find_smallest_number(set_numbers)
print("smallest number: ", smallest_number)
