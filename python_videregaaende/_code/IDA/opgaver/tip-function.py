# Tip function
def total_betaling(belob,tip_perc=10):
  total = belob*(1 + 0.01*tip_perc)
  #total = round(total,2)
  print(f"Du skal betale {total:.2f} kr.")

total_betaling(100, 10.5)