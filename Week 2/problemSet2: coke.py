due = 50

while due > 0:
    print(f"Amount Due: {due}")
    user_input = int(input("Insert Coin: "))
    match user_input:
        case 25 | 10 | 5:
            due -= user_input

print(f"Change Owed: {abs(due)}")
