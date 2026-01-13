# save using Cmd + S
fruits = ["apple", "banana", "cantaloupe", "dragonfruit"]
output = [fruit for fruit in fruits]
print(output)

user_fruit = input("what is your favorite fruit?: ")
if user_fruit in fruits: 
    print("that is a fruit!")
else: 
    print("that's not a fruit. the valid fruits are " + ", ".join(fruits))