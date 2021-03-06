x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)

# x = "global"   Initial code
#
# def outer():
#     x = "local"
#
#     def inner():
#         x = "nonlocal"
#         print("inner:", x)
#
#     def change_global():
#         x = "global: changed!"
#
#     print("outer:", x)
#     inner()
#     print("outer:", x)
#     change_global()
#
# print(x)
# outer()
# print(x)
