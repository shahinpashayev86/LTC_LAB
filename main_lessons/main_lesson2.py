blacklist_dict = {"silah": 0.95, "qan": 0.83, "bomba": 0.75, "axmaq": 0.5  }

user_prompt = input("sorgunuzu daxil edin: ")

if user_prompt in blacklist_dict:
    print("Daxil elediyiniz soz qadağandır")
else:
    print("ugurlu sorğu")

