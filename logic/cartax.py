def calculate_cartax(amnt):
    if amnt < 15000:
        return 0, amnt, 0  # no tax applies
    elif 15000 <= amnt <= 25000:
        tax = 15
    elif 25001 <= amnt <= 50000:
        tax = 20
    elif 50001 <= amnt <= 80000:
        tax = 30
    elif 80001 <= amnt <= 100000:
        tax = 40
    elif 100001 <= amnt <= 250000:
        tax = 55
    elif amnt > 250000:
        return None, None, None  # too much
    else:
        return None, None, None  # invalid input

    amnta = int(amnt * tax / 100)
    amntb = int(amnt - amnta)
    return amnta, amntb, tax