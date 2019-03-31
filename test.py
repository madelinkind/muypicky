def M(*args, **kwargs):
    print("args={}".format(args))
    print("kwargs={}".format(kwargs))

# M(1, "hola", 3.8, "i am made")
# M(name="made", age=30)

M(1, "hola", 3.8, "i am made", age=30, name="made")


