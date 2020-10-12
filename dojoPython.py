#F-Strings
name = 'Ricky'
age = 29
hobbies = 'Sports'

print(f"Hello my name is {name} and I am {age} years old. I really love ALL {hobbies}")

#String format() older version of python
print("Hello my name is {} and i am {} years old. I really love ALL {}".format(name, age, hobbies))



#loop thru list
my_list = [1,5,9,13,20]
print(my_list)
for item in my_list:
    print(item)

print('--------')

for i in range(0,len(my_list)):
    print(my_list[i])

print(my_list)

print('------------------------')
#loop thru a dictionary/object
my_dict = {
    "first_name" : "Ricky",
    "last_name" : "Rodriguez",
    "age" : 29,
    "eye_color" : "Brown"
}

print(my_dict)
for k in my_dict:
    print(my_dict[k])