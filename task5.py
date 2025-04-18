birinci_reqem = input("Birinci rəqəmi daxil edin: ")
ikinci_reqem = input("İkinci rəqəmi daxil edin: ")

birinci_reqem = int(birinci_reqem)
ikinci_reqem = int(ikinci_reqem)

cem = birinci_reqem + ikinci_reqem
print("Cəm:", cem)

boy = input("Boyunuzu daxil edin (m): ")
ceki = input("Çəkini daxil edin (kg): ")

boy = float(boy)
ceki = float(ceki)

bki = ceki / (boy ** 2)

print("Bədən Kütlə İndeksiniz (BKİ):", bki)