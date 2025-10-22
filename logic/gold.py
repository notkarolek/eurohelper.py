def calculate_gbcount(amnt):
 if amnt < 0:
        return None, None  # invalid input

 out = amnt // 1500000
 rest = amnt - (out * 1500000)
 return int(out), int(rest)
