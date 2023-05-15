even_2 = [i for i in range(1, 11) if not i%2]
odd_3 = [i for i in range(1, 11) if (not i%3) and i%2]
not_divisible_2_3 = [i for i in range(1, 11) if i%2 and i%3]
print(even_2, odd_3, not_divisible_2_3, sep = "\n") 
