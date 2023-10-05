def find_smallest_numbers():
  sum_numbers = 0
  for i in range(50,100):
    if i % 3 == 0 and i % 5 != 0:
      sum_numbers += i
  return sum_numbers

sum_numbers =  find_smallest_numbers()
print("sum of numbers: ", sum_numbers)