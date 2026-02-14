blacklist_dict = {"silah": 0.9, "qan": 0.83, "bomba": 0.81, "axmaq": 0.5}

user_prompt = input("Sorğunuzu daxil edin: ").lower()
toxicity_score = 0.5
found = False

for word, score in blacklist_dict.items():
    if word in user_prompt:
        if toxicity_score >= score:
            print(f"KRİTİK BLOK: '{word}' sözü aşkarlandı (Limit: {score}, Sizin Skor: {toxicity_score})")
            found = True
            break

if not found:
    print(f"UĞURLU SORĞU: '{user_prompt}' qəbul edildi.")



