x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

# def draw_stars(x):
#     for i in range(0, len(x)):
#         print "*" * x[i]


def draw_stars(y):
    for i in range(0, len(y)):
        if isinstance(y[i], str):
            print y[i][:1].lower() * len(y[i])
        else:
            print "*" * y[i]

# draw_stars(x)

draw_stars(y)