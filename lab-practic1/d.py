def find_second_hight_number_number(numbers):
  second_hight_number  = numbers[0]
  hight = numbers[0]
  for num in numbers:
    if num > hight:
      second_hight_number = hight
      hight = num
    elif  num > second_hight_number and num != hight:
      second_hight_number = num
  return second_hight_number
        
set_numbers = [1,3,2,8,4,8,3,2,7,8,5]

second_hight_number = find_second_hight_number_number(set_numbers)
print("Second hight number: ", second_hight_number)
