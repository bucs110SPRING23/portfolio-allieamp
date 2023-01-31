import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week=3
cost_per_class= (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)
print("Cost per class:", type(cost_per_class))

snacklist = ["pretzel", "pickle", "banana", "apple", "cracker", "carrot"]
randomsnack = random.choice(snacklist)
print(randomsnack)