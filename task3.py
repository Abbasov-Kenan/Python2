age = int(input("Yaşınızı daxil edin: "))

if age < 18:
    print("Giriş qadağandır")
else:
    print("Xoş gəldiniz!")

score1 = float(input("1-ci imtahan balı: "))
score2 = float(input("2-ci imtahan balı: "))
score3 = float(input("3-cü imtahan balı: "))

orta_score = (score1 + score2 + score3) / 3

if orta_score > 90:
    print("Əla!")
elif orta_score > 70:
    print("Yaxşı")
elif orta_score > 50:
    print("Kafi")
else:
    print("Zəif")


user_age = int(input("Təkrar yaşınızı daxil edin: "))
user_score = float(input("Təkrar balınızı daxil edin: "))

if user_age >= 18:
    if user_score >= 70:
        print("Şərtlərə uyğundur!")
    else:
        print("Bal yetərli deyil.")
else:
    print("Yaş yetərli deyil.")