# # # Modelin çıxışı (Simulyasiya)
# # prediction_class = "Person"
# # confidence_score = 0.72  # 72% inam
# #
# # # Mühəndis tərəfindən təyin olunan Hədd (Hyperparameter)
# # CONFIDENCE_THRESHOLD = 0.85
# #
# # # Yoxlama məntiqi
# # is_high_confidence = confidence_score >= CONFIDENCE_THRESHOLD
# #
# # print(f"Prediction: {prediction_class}")
# # print(f"Is Reliable: {is_high_confidence}")
# # # Output: False
# from ctypes import HRESULT
# from idlelib.debugger_r import restart_subprocess_debugger
# from math import trunc
# from operator import truediv
#
# # raw_value = None  # Bazadan gələn dəyər (bəzən boş ola bilər)
# # default_value = 0.0
# #
# # if raw_value is None:
# #     # Dəyər yoxdursa, default dəyəri mənimsət
# #     processed_value = default_value
# #     log_message = "Warning: Missing data detected. Used default."
# # elif isinstance(raw_value, str):
# #     # Dəyər string formatındadırsa, float-a çevirməyə çalış
# #     processed_value = float(raw_value)
# #     log_message = "Info: Data type converted from str to float."
# # else:
# #     # Dəyər normaldır
# #     processed_value = raw_value
# #     log_message = "Info: Data is valid."
# #
# # print(log_message)
#
#
# # name = "shahin"
# # age = 10
# # price = 12.99
# # telebedirmi = True
# #
# # print(type(name))
# # print(type(age))
# # print(type(price))
# # print(type(telebedirmi))
# #
# #
# # number1 = 10
# # number2 = 20
# #
# # result = number1 + number2
# # result = number1 - number2
# # result = number1 * number2
# # result = number1 / number2
# # result = number1 // number2
# #
# # print(f"""Neticeler
# # Toplama {number1}
# # Cixma {number2}""")
#
# # --- Logical operator
#
# # number = 10
# # number1 = 15
# #
# # result = number > number1
# # print(result)
# # result = number < number1
# # print(result)
#
#
# # metn = "Salam Python".casefold()
# # metn2 = "Salam Python".capitalize()
# # print(metn)
# # print(metn2)
# #
# # result = len(metn) > 8
# # print(f"Cavab {result}")
#
# # telebenin_neticesi = 95
# # imtahan_bali = 90
# # telebedir = True
# # resut_common = imtahan_bali > telebenin_neticesi and telebedir == True
# # resut_common2 = imtahan_bali > telebenin_neticesi or telebedir == True
# # resut_common3 = imtahan_bali > telebenin_neticesi or not telebedir
# # print(resut_common)
# # print(resut_common2)
# # print(resut_common3)
#
#
#
# # dogru AND sehv = sehv
# # sehv AND dogru = sehv
# # sehv AND sehv = sehv
# #
# # dogru OR dogru = dogru
# # dogru OR sehv = dogru
# # sehv OR dogru = dogru
# # sehv OR sehv = sehv
#
#
# # dogru = True
# # sehv = False
# #
# # print("AND nəticələri:")
# # print("dogru and dogru =", dogru and dogru)
# # print("dogru and sehv  =", dogru and sehv)
# # print("sehv and dogru  =", sehv and dogru)
# # print("sehv and sehv   =", sehv and sehv)
# #
# # print("\nOR nəticələri:")
# # print("dogru or dogru  =", dogru or dogru)
# # print("dogru or sehv   =", dogru or sehv)
# # print("sehv or dogru   =", sehv or dogru)
# # print("sehv or sehv    =", sehv or sehv)
# #
# # print("\nNOT nəticələri:")
# # print("not dogru =", not dogru)
# # print("not sehv  =", not sehv)
#
# # adlanma = input("SAlam Adinizi ve soyadinizi daxil edin: ").split()[0]
# # print(adlanma)
# #
# # adlanma = input("SAlam Adinizi ve soyadinizi daxil edin: ").split()[1]
# # print(adlanma)
#
# # yash_heddi = 18
# # mushterinin_yashi = int(input("Yashinizi daxil edin: "))
# # mushterinin_valideyn = input("validenyn_iledirmi: ")
# #
# # if (mushterinin_valideyn == "Beli"):
# #     mushterinin_valideyn = True
# # else:
# #     mushterinin_valideyn = False
# #
# # if mushterinin_yashi > yash_heddi or mushterinin_valideyn:
# #     print("Siz daxil ola bilersiz")
# # else:
# #     print("Siz daxil ola bilmersiniz")
#
# # telebenin_bali = int(input("zehmet olmazsa balnizi daxil edin: "))
#
# # if 90 < telebenin_bali < 100:
# #     print("Sizin Baliniz A-dir")
# # elif 89 >= telebenin_bali > 80:
# #     print("Sizin Baliniz B-dir")
# # elif 79 >= telebenin_bali > 70:
# #     print("Sizin Baliniz C-dir")
# # elif 69 >= telebenin_bali > 60:
# #     print("Sizin Baliniz D-dir")
# # elif 59 >= telebenin_bali > 50:
# #     print("Sizin Baliniz D-dir")
# # else:
# #     print("Sizin imtahandan kesildiz")
# # print("Sizin baliniz ", telebenin_bali)
#
#
# # import random
# #
# # can = 3
# # guest_number = random.randint(1,101)
# # print(guest_number)
# #
# # while can > 0 :
# #     musterinin_reqemi = int(input("texzmini etdiyiniz reqemi daxil edin  "))
# #     if musterinin_reqemi == guest_number:
# #         print("Texmini tapdiniz")
# #         break
# #     else:
# #         print("texmini tapa bilmediniz")
# #         can-=1
# #
# #     print("caniniz" + str(can))
#
#
# # -- varibale = [element1, element2, element3]
#
# # adlar_yashlar = ["Nurlan",32, "Huseyn",19]
# # adlar = ["Murad", "Nurlan, nermin, peri"]
# # reqemler = [3,6,10,13,19,32,23,34,45,12]
# #
# # # print(adlar[0])
# # # adlar.insert(__index:0)
# #
# # #print(reqemler[-1])
# #
# # # for list in reqemler:
# # #     print(list)
# #
# # # reqemler.append(55)
# # # print(reqemler)
# # #
# # # reqemler_yeni = []
# # #
# # # for list in reqemler:
# # #     if list > 13:
# # #         reqemler_yeni.append(list)
# # # print(reqemler_yeni)
# #
# # yeni_adlar = []
# # for list in adlar:
# #     if "a" in list:
# #         yeni_adlar.append(list)
# # print(yeni_adlar)
#
# # --dictionary_varibale = {key: value}
#
# # telebe = {
# #     "name": "Murad",
# #     "yash": 19,
# #     "avto" : True,
# #     "ixtisas" : "Developer",
# #     "cekisi" : 150.88,
# #     "boyu" : 1.86
# # }
#
# # print(telebe.get("name"))
# # print(telebe.get("avto"))
# # print(telebe["cekisi"])
#
# # for i in telebe.values():
# #     print(i)
# #
# # for i in telebe.keys():
# #     print(i)
# #
# # for i in telebe.items():
# #     print(i)
# #
# # for key, value in telebe.items():
# #     print(f"{key}: {value}", end=" ")
# #
# # for k, v in telebe.items():
# #     if telebe["yash"] > 20:
# #         print("telebenin 18 yashdan yuxaridir")
# #         break
#
#
# # telebe = {
# #      "name": "Murad",
# #      "ixtisas" : ["IT","Data Science","AI Engineer"]
# #
# #
# #  }
# # yeni_telebe = []
# #
# # for i in telebe.items():
# #     if i[1] == "Data Science":
# #         yeni_telebe.append(i)
# # print(yeni_telebe)
#
# list = [
#     {"name": "Nazim", "age": 23},
#     {"name": "Shahin", "age": 19},
#     {"name": "Emin", "age": 16},
#     {"name": "Peri", "age": 19},
#
# ]
#
# yeni_list = []
# for l in list:
#     if l["age"] > 18:
#         yeni_list.append(l)
# print(yeni_list)
from difflib import restore
from encodings.punycode import adapt
from queue import PriorityQueue

# user = {"username": "admin", "password": "12345"}
#
# logged = False
#
# while not logged:
#     username = input("Please enter your username: ")
#     password = input("Please enter your password: ")
#     if username == user["username"] and password == user["password"]:
#         logged = True
#         print("Welcome " + user["username"])
#     else:
#         print("Incorrect username or password")
# print(user["username"], user["password"])

# telebe = { # Nurlan -Key, v{ad-K, info2-v}
#     "Nurlan" : {"age": 16, "address" : "Baku"},
#     "Camal" : {"age": 17, "address" : "Moscow"},
#     "Kenan": {"age": 20, "address": "France"},
#     "Murad": {"age": 17, "address": "New York"}
#
# }
#
#
#
# for ad , info in telebe.items():
#     print(f"{ad}")
#     for yash , info2 in info.items():
#         print(f"{yash},{info2}")
#     print("________")
#
#
#     for list in telebe.values():
#         print(f"{list} ")
### ======================================================

# respomses = {
#     "u1" : {"username":"admin", "status": "success"},
#     "u2" : {"username":"admin", "status": "failed"},
#     "u3" : {"username":"admin", "status": "success"},
#     "u4" : {"username":"admin", "status": "failed"},
# }
#
# success = {}
# failed = {}
#
# for uid, info in respomses.items():
#     if info["status"] == "success":
#         success[uid] = info
#         print("elave edildi")
#     else:
#         failed[uid] = info
#         print("Kecmeyenler elave edildi")

############# =========== 13.02.2026 lesson4 ============############

# name = input("Adinizi daxil edin: ")
# age = input("yashinizi daxil edin: ")
#
# def salam_de(name):
#     return f"Salam {name}, Yash {age}"
#     # print("Salama", name )
#
# print(salam_de(name,age))
#

# reqemler = [1,2,3,4,5]
#
# def tapmaq (axtardigimiz_reqem):
#     if axtardigimiz_reqem > len(reqemler):
#         print("reqemler uzundur")
#     else:
#         print("reqemler kicikdir")
#     return "siz reqemi qeyd etdiniz"
# print(tapmaq(4))


# mehsul = {
#     "alma": {"qiymet": 20 , "cheki": 3.1,"stock": 17 },
#     "armud": {"qiymet": 12, "cheki": 4.4, "stock": 11},
#     "nar": {"qiymet": 32, "cheki": 5.5, "stock": 14},
#     "banan": {"qiymet": 11, "cheki": 6.1,"stock": 10},
#     "heyva": {"qiymet": 16, "cheki": 3.5,"stock": 19}
# }
#
#
#
# stock_melumati = {}
#
#
# for adlar, info in mehsul.items():
#     if info["stock"] > 10:
#         stock_melumati[adlar] = info["cheki"],info["qiymet"]
#
# print(stock_melumati)



# mushteri_daxil_edecek = int(input("musher daxil edeceyi qiymet: "))
#
# def mehsulda_axtarish(mehsul,kenardan_gelen):
#     stock_melumati = {}
#     for mehsulun_adi, mehsulun_infosu in mehsul.items():
#         if mehsulun_infosu["qiymet"] > kenardan_gelen:
#             stokdaki_melumat[mehsulun_adi] = mehsulun_infosu
#     if stock_melumati == {}
#         return "Stockda mehsul yoxdur"
#     return stokdaki_melumat
#
# print(mehsulda_axtarish,(mehsul,mushteri_daxil_edecek))



############# =========== 20.02.2026 lesson4 ============############

#
# # tupel examples
#
# sheher = ("Baki",)
# lc =(1234,)
#
#
# print(type(sheher))
# print(type(lc))
#
#
# umumi = ("Sheher", 1233, True, 99.99)
# litsll = ["Sheher", 1233, True, 99.99]
#
# yeni_tuple = tuple(litsll)
#
# print(yeni_tuple)
#



# # Sadə bir AI model konfiqurasiyası
# model_config = {
#     "model_name": "GPT-4",
#     "context_window": 128000,
#     "temperature": 0.7
# }
#
# # Məlumata müraciət (Index yox, Key ilə - Sürətli O(1))
# print(model_config["model_name"])  # Nəticə: GPT-4


# # Mətndən gələn xam sözlər (Təkrarlarla)
# raw_tokens = ["süni", "intellekt", "süni", "öyrənmə", "süni", "süni"]
#
# # Set-ə çevirmə (Təkrarlar avtomatik silinir)
# vocab = set(raw_tokens)
# print(vocab) # {'süni', 'intellekt', 'öyrənmə'}


# import tiktoken
#
#
# def compare_languages(text_en, text_az):
#     # GPT-4-ün istifadə etdiyi encoding sistemi: cl100k_base
#     enc = tiktoken.get_encoding("cl100k_base")
#
#     # Mətni token ID-lərinə çeviririk (Encoding)
#     tokens_en = enc.encode(text_en)
#     tokens_az = enc.encode(text_az)
#
#     print("-" * 40)
#     print(f"🇬🇧 İngilis: '{text_en}'")
#     print(f"   Token sayı: {len(tokens_en)}")
#     # Hər ID-nin qarşılığı olan mətn parçasını göstəririk
#     print(f"   Tokenlər: {[enc.decode_single_token_bytes(t).decode('utf-8', errors='replace') for t in tokens_en]}")
#
#     print("-" * 40)
#     print(f"🇦🇿 Azərbaycan: '{text_az}'")
#     print(f"   Token sayı: {len(tokens_az)}")
#     print(f"   Tokenlər: {[enc.decode_single_token_bytes(t).decode('utf-8', errors='replace') for t in tokens_az]}")
#     print("-" * 40)
#
#
# # Canlı Demo
# compare_languages(
#     "Hello, I am learning artificial intelligence",
#     "Salam, Mən süni intellekt öyrənirəm"
# )






















