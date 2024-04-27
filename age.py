# User will input (3ages).Find the oldest one
# orginal solution
def age(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Enter the age a: "))
b = int(input("Enter the age b: "))
c = int(input("Enter the age c: "))

print(age(a, b, c))


# best method
# def oldest_age(a, b, c):
#     return max(a, b, c)

# a = int(input("Enter the age a: "))
# b = int(input("Enter the age b: "))
# c = int(input("Enter the age c: "))

# oldest = oldest_age(a, b, c)
# print("The oldest age is:", oldest)

