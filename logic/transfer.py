def calculate_transfer(amnt):
    if amnt <= 5000:
        return 0, 0, 0  # No tax applies
    elif 5000 < amnt <= 10000:
        tax = 10
    elif 10000 < amnt <= 25000:
        tax = 15
    elif 25000 < amnt <= 35000:
        tax = 25
    elif 35000 < amnt <= 50000:
        tax = 30
    elif amnt > 50000:
        tax = 40
    else:
        return None, None, None  # invalid input

    amnta = int(amnt * tax / 100)
    amntb = int(amnt - amnta)
    return amnta, amntb, tax