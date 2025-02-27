my_likes = ["Gaming", "Baking", "Football", "Art", "Coding"]
my_favorite_car = "GT3 RS"
tester = False
things = ["ball", "t-shirt", "coffee"]

for like in my_likes:
    if like == "Football":
        print("Football is fun!")
    else:
        print("That is also pretty fun..")

if my_favorite_car == "GT3 RS":
    print("Great car.")
else:
    print("Interesting...")

if False != True:
    print("True")
else:
    print("False")

# 1 > 0      1 < 2

if False == False and False == tester:
    print("All conditions are met")
else:
    print("All conditions are not 100%")

if "jacket" in things:
    print("That is in there")
else:
    print("That is not in there")