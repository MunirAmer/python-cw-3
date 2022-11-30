# write your code here
#Question 1
favorite_animals = ["cat" , "dog" , "monkey" , "rabbit"]
print(favorite_animals)
print(favorite_animals[1])
favorite_animals.remove("dog")

#Question 2
favorite_animals.append("Horse")
for animal in favorite_animals:
    print(f'I love {animal}')

favorite_animals.remove("monkey")

#Question 3
numbers = [1 , 2 , 3 , 4 ,5]
numbers_sum = 0
for num in numbers:
    numbers_sum += num

print(numbers_sum)