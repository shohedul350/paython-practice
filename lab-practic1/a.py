def sum_add_even(numbers):
  odd_sum =0
  even_sum = 0

  for num in numbers:
    if num % 2 == 0:
       even_sum += num
    else: 
       odd_sum += num

  return odd_sum, even_sum

set_numbers = [1,2,3,4,5,6,7,8,9,10]
odd_sum, even_sum =  sum_add_even(set_numbers)

print("sum of odd:", odd_sum)
print("sum of even:" , even_sum)