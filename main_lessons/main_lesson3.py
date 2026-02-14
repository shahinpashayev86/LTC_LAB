## ========================================================================================= ###
## ============================================ Task 1 ===================================== ###
## ========================================================================================= ###

### Task 1: Core Logic (Namizəd Filtrləmə Mühərriki)

# **Məqsəd:** `For` dövrü və `If` şərtləri ilə verilənlər bazasını analiz etmək.
#
# **Texniki Tapşırıq:**
#
# 1. `candidates` adlı list yaradın. İçərisində 5 ədəd dictionary olsun. Hər dictionary-də: `name` (str), `skills` (list), `experience_years` (int) olsun.
# 2. `qualified_candidates` adlı boş list yaradın.
# 3. `for` dövrü ilə bütün namizədləri analiz edin.
# 4. Dövr daxilində məntiq qurun:
#     - Əgər namizədin təcrübəsi 3 ildən çoxdursa **VƏ** "Python" bacarığı varsa, onu `qualified_candidates` siyahısına əlavə edin.
# 5. Sonda qəbul edilən namizədlərin adlarını ekrana çap edin.
print("\n Task1")

candidates = [
    {"name": "Aysel Məmmədova", "skills": ["Python", "SQL"], "experience_years": 5},
    {"name": "Eldar Əliyev", "skills": ["Java", "C++"], "experience_years": 4},
    {"name": "Leyla Həsənova", "skills": ["Python", "JavaScript"], "experience_years": 2},
    {"name": "Rəşad Quliyev", "skills": ["Python", "Docker"], "experience_years": 7},
    {"name": "Nigar Bağırova", "skills": ["HTML", "CSS"], "experience_years": 1}
]

qualified_candidates = []

for candidate in candidates:
    if candidate["experience_years"] > 3 and "Python" in candidate["skills"]:
        qualified_candidates.append(candidate)

print("Tələblərə cavab verən namizədlər:")
for qc in qualified_candidates:
    print(f" * {qc['name']}")

## ========================================================================================= ###
## ============================================ Task 2 ===================================== ###
## ========================================================================================= ###

### Task 2: Advanced (Resurs İdarəetməsi və Token Limiti)
#
# **Məqsəd:** `While` dövrü ilə real "AI Agent" məhdudiyyətlərini simulyasiya etmək.
#
# **Ssenari:** Siz API vasitəsilə CV-ləri analiz edirsiniz. Hər CV analizi 50 token xərcləyir. Sizin ümumi balansınız (limiti) 180 tokendir. Balans bitdikdə proses avtomatik dayanmalıdır, əks halda sistem xəta verəcək.
#
# **Texniki Tapşırıq:**
#
# 1. `token_balance = 180` və `cost_per_cv = 50` dəyişənlərini təyin edin.
# 2. `candidates` siyahısı üzərində `while` və ya `for` dövrü qurun.
# 3. Hər iterasiyada yoxlayın:
#     - **Şərt:** Əgər `token_balance` < `cost_per_cv` (balans çatmırsa):
#         - Ekrana "Xəbərdarlıq: Token balansı bitdi. Proses dayandırılır." yazın.
#         - `break` əmri ilə dövrü dərhal dayandırın.
#     - **Əməliyyat:** Əgər balans yetərlidirsə:
#         - Namizədin adını və "Analiz edildi" mesajını çap edin.
#         - Balansdan 50 token çıxın (`token_balance -= cost_per_cv`).
#         - Qalıq balansı göstərin.

print("\n Task2")

token_balance = 180
cost_per_cv = 50


candidates = ["Shahin", "Nazim", "Arzu", "Kənan"]
print(f"Balans: {token_balance} token\n")

print(f" Ne qeder vaxta while dowruyyede olmalidr:   {len(candidates)}")
index = 0
while index < len(candidates):
    candidate_name = candidates[index]

    if token_balance < cost_per_cv:
        print("---")
        print("Token balansı bitdi.")
        print(f"Çatışmayan token: {cost_per_cv - token_balance}  token")
        break

    token_balance =  token_balance - cost_per_cv
    print(f"Analiz edildi: {candidate_name}")
    print(f"Qalıq balans: {token_balance} token")

    index = index + 1