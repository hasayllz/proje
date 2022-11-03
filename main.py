

N = int(input("N: "))

toplam, carpim = 0, 1

kareler_toplami = 0

for sayi in range(1, N+1):

   if sayi % 2 == 1:

       toplam += sayi ** 2
   else:

       kareler_toplami += sayi ** 3

print(f"Tek sayıların kareleri toplamı: {toplam}")

print(f"Çift sayıların küpleri toplamı: {kareler_toplami}")



















