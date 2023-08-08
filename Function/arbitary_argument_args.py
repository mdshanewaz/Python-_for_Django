def hello(fname, lname):
    print(f"Hello {fname} {lname}")

hello("Shah", "Newaz")

# 1st arguments will go to 1st parameter
# 2nd argumets will go to 2nd parameter
# Thats why we say it positional argument

#Arbitary Arguments if we dont know the parameters number and pass much as argument we want to the function.

def fun1(*args):
    print(args)
    print(args[2])

fun1("Shah", "Newaz", "Shawon", 26, "Feni", True) 