# print("hello world")
# print("assalomu alaykum")
# print("salom")
# print(" \"nexia\", \"tiko\", 'damas', ko'rganlar qilar havas")
# print(5**4)
# print("22 ni 4 ga bo'lganda qoldiq", 22%4)
# print("tomonlari 125 ga teng kvadratning yuzi", 125*125, "ga teng", 
# "perimetri", 4*125, "ga, teng bo'ladi")
# print('diametri 12 ga teng bo\'lgan doiraning yuzi', 3.14*(12/2)**2, 'ga teng')
# print("Katetlari 6 va 7 ga teng bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi", (6**2+7**2)**1/2, "ga teng")
# matn="hello world"
# print(matn)
# xabar="ta'til bugun tugadi"
# print(xabar)

# xabar="ta'tildan keldim"
# print(xabar)
# class=256
# printO(class)
# radius=5
# pi=3.14159
# aylana_yuzi=pi*radius**2
# print("Radiusi", radius, "ga teng aylananing yuzi=", aylana_yuzi)
# 06 dars
# x=int(input('istalgan son kiriting:\n>>>'))
# print(x, "ning kvadrati", x**2, "ga teng")
# print(x, "ning kubi", x**3, "ga teng")
# yosh=int(input("yoshingiz nechida? \n>>>"))
# t_yil=2026-yosh
# print("siz", t_yil, "da tug'ulgansiz")
# a=float(input("birinchi sonni kiriting "))
# b=float(input("ikkinchi sonni kiriting "))
# print(f"(a)+(b)=", a+b)
# print(f"(a)-(b)=", a-b)
# print(f"(a)x(b)=", a*b)
# print(f"(a)/(b)=", a/b)
# 07 dars
# davlatlar=["O'zbekiston", "Rossiya", "Turkiya", "Qozog'iston", "AQSH", "Singapur"]
# print(davlatlar)
# print(len(davlatlar))
# sonlar=list(range(120, 1200))
# sonlar = list(range(120,1200))
# taomlar = ['osh','somsa','norin','shashlik','qozonkabob']
# nonushta[0] = "qaymoq va non"
# ismlar=['ali', 'vali', 'hasan', 'husan', 'kamron']
# for ism in ismlar:
 #    print(f'assalomu alaykum, {ism}. xush kelibsiz toyga')
    
# print(f"Kod {len(ismlar)} marta takrorlandi")

# sonlar=list(range(10,100,2))
# for son in sonlar:
#     print(son**3)
# kinolar = []
# print("5 ta sevimli kinoingiz qaysilar?")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino:"))
# print(kinolar) 

# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car.lower() == "gm":
#     print(car.upper())
#   else:
#     print(car.title())
        
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car!= "gm":
#     print(car.title())
#   else:
#     print(car.upper())
# login=input("login kiriting ")
# if login.lower()=="admin":
#     print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#      print(f"Xush kelibsiz {login.title()}!")
# x=float(input("birinchi sonni kiriting: "))
# y=float(input("ikkinchi sonni kiriting: "))
# if x==y: print(f"sonlar teng: {x}={y}")
# son=float(input("istalgan son kiriting: "))
# print("son manfiy") if son<0 else print("son musbat")
# son=float(input("istalgan son kiriting: "))
# print(son**(1/2)) if son>0 else print('Musbat son kiriting')

# son = float(input("Juft son kiriting: "))
# if son%2:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")

# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0;
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# users = ['alisher','aziza','yasina','umar']

# login = input("Yangi login tanlang: ")

# if login.lower() in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
            
# 12-dars

# son = int(input("Juft son kiriting: "))
# if son%2==0:
#     print("Bu son juft.")
# else:
#     print("Bu son juft emas")
    
    
    
# yosh = int(input("Yoshingiz nechida?"))
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh<18:
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")



# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}')
# else:
#     print(f"{x}>{y}")


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")   



#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)

#if mavjud_emas:
#  print("Do'konimizda quyidagi mahsulotlar yo'q:")
#for mahsulot in mavjud_emas:
#  print(mahsulot)
#else:
#  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")       



#users = ['alisher1983','aziza','yasina' 'umar']

#login = input("Yangi login tanlang:" )

#if login in users:
#    print('Login band, yangi login tanalng!')
#else:
#    print("Xush kelibsiz!")






























        