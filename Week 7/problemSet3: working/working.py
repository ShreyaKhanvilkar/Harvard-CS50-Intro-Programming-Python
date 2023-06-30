import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    helper = "(([1][0-2]|[1-9]):?([0-5][0-9])? (AM|PM))"
    if time := re.search(r"^" + helper + " to " + helper + "$", s):
        s_hour, e_hour = int(time.group(2)), int(time.group(6))
        s_min, e_min = time.group(3), time.group(7)
        s_mer, e_mer = time.group(4), time.group(8)

        if s_min == None and e_min == None:
            s_min, e_min = "00", "00"

        if s_hour == 12 and s_mer == "AM":
            s_hour = 0
        elif s_hour != 12 and s_mer == "PM":
            s_hour += 12

        if e_hour == 12 and e_mer == "AM":
            e_hour = 0
        elif e_hour != 12 and e_mer == "PM":
            e_hour += 12

        return f"{s_hour:02}:{s_min} to {e_hour:02}:{e_min}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
