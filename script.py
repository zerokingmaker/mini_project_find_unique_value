def unique_values(my_dictionary):
  unique_value_dict = []
  for value in my_dictionary.values():
    if value not in unique_value_dict:
      unique_value_dict.append(value)
  return len(unique_value_dict)    

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2

# should print 1
