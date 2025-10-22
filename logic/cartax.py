
def calculate_cartax(amnt):
 if  amnt <  15000:
    print("No tax!")
 elif amnt <= 25000 and amnt >= 15000:
    tax = 15
    amnta = (amnt * tax / 100)
 elif amnt <= 50000 and amnt >= 25000:
    tax = 20
    amnta = (amnt * tax / 100)
 elif amnt <= 80000 and amnt >= 50000:
    tax = 30
    amnta = (amnt * tax / 100)
 elif amnt <= 100000 and amnt >= 80000:
    tax = 40
    amnta = (amnt * tax / 100) 
 elif amnt > 100000 and amnt <= 250001:
    tax = 55
    amnta = (amnt * tax / 100)
 elif amnt > 250000:
        return None, None, None  # too much
 else:
        return None, None, None  # invalid input

 amnta = int(amnt * tax / 100)
 amntb = int(amnt - amnta)
 return amnta, amntb, tax
