import random
result = "heads" if random.randint(0,1) == 0 else "tails"
print(result)
with open("output.txt", "w") as text_file:
    print(result, file=text_file)