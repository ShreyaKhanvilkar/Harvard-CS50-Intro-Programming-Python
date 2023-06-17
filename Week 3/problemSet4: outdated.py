months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ")
        meo = date.split()[0].title()
        if meo in months and "," in date:
            m = months.index(meo) + 1
            d = date.split()[1].removesuffix(",")
            y = date.split()[2]
        elif "/" in date:
            m, d, y = date.split("/")
        if int(m) > 12 or int(d) > 31:
            raise ValueError

    except (AttributeError, ValueError, NameError, KeyError):
        pass

    else:
        print(f"{int(y)}-{int(m):02}-{int(d):02}")
        break
