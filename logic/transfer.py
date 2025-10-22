def calculate_transfer(amnt):
 if amnt < 5000:
        return 0, amnt, 0
 elif 5001 <= amnt <= 10000:
        tax = 10
 elif 10001 <= amnt <= 25000:
        tax = 15
 elif 25001 <= amnt <= 35000:
        tax = 25
 elif 35001 <= amnt <= 50000:
        tax = 30
 elif amnt >= 50001:
        tax = 40
 else:
        return None, None, None  # invalid

 amnta = int(amnt * tax / 100)
 amntb = int(amnt - amnta)
 return amnta, amntb, tax
