counter = 250

def increment_counter():
    global counter
    for i in range(5, 51):
        for j in range(i + 1, 201):
            counter = counter + 7
            for k in range(j + 1, 151):
                counter = counter + 9
    return counter

print(increment_counter())