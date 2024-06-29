def math(name):
    print("hello " + name)


# math("abdul")
# math(name="abdul")


# def math():
#     result = 5 + 5
#     return result

# print(math())


# def arguments(x=2, y=2):
#     print(x + y)

# arguments(2, 3)


# def greet(name=None):
#     if name is None:
#         print("hello stranger!:")
#     else:
#         print(f"hello, {name}")



name = None


def get_name():
    first_name = input("enter your first name: ")
    last_name = input("enter your last name: ")
    global name
    name = first_name +  " " + last_name

    return {"first": first_name, "last": last_name}

user = get_name()
# print("user first name is", name['first'])
# print("user last name is", name['last'])
print(user['first'], user['last'])
print(name)
