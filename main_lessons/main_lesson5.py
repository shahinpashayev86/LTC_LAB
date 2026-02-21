# Namizədlər bazası (Simulyasiya edilmiş JSON)
candidates = [
    {
        "name": "Ali Valiyev",
        "experience": 3,
        "skills": ["Python", "Django", "AI", "Python", "Git", "Debug", "Dancing"], # Diqqət: "Python" təkrarlanır
        "expected_salary": 1500
    },
    {
        "name": "Aysel Mammadova",
        "experience": 5,
        "skills": ["Java", "Spring", "Hibernate", "SQL", "Eating", "SQL","Dancing"], # "Eating" lazımsız bacarıqdır
        "expected_salary": 2500
    },
    {
        "name": "Samir Qasimov",
        "experience": 1,
        "skills": ["Python", "Pandas", "NumPy", "Matplotlib","Sleeping"],
        "expected_salary": 800
    }
]

# Vakansiya Tələbləri (Weights - Çəkilər)
# Bu bizim "Word_to_ID" və ya "Token_Score" lüğətimizdir.
vacancy_weights = {
    "Python": 50,
    "Django": 30,
    "SQL": 20,
    "AI": 100,
    "Git": 10,
    "Pandas": 40,
    "NumPy": 40
}

# Tələb olunan minimum şərtlər
min_experience = 2
min_score = 150

print("\n Tapşırıq 1: Unikal Bacarıqlar (Set istifadəsi)")

for candidate in candidates:
    unique_skills = set(candidate["skills"])
    print(candidate["name"], "---", unique_skills)
print("-" * 40)

print("\n Tapşırıq 2: 'Stop Words' Təmizliyi (Set fərqi)")
print("\n Tapşırıq 3: Xalların Hesablanması (Dictionary Lookup)")
print("\n" )

stop_words = {'Eating', 'Sleeping', 'Dancing'}
total_score = 0
for candidate in candidates:
    cleaned_skills = unique_skills.difference(stop_words)
    print(candidate["name"], "---", cleaned_skills)
    for skill in cleaned_skills: ### Tapşırıq 3: Xalların Hesablanması (Dictionary Lookup)
        if skill in vacancy_weights:
            total_score += vacancy_weights[skill]
        candidate["score"] = total_score
for candidate in candidates:
    print(candidate["name"], "-> Score:", candidate["score"])

shortlisted_candidates = []
rejected_candidates = []

print("-" * 40)
print("\n Tapşırıq 4: Qərarvermə Mexanizmi (Filtering)" )

for candidate in candidates:

    if candidate["experience"] >= min_experience and candidate["score"] >= min_score:
        shortlisted_candidates.append(candidate)
    else:
        rejected_candidates.append(candidate)

print("\n✅ Shortlisted Candidates:")
for c in shortlisted_candidates:
    print(c["name"], "| Score:", c["score"], "| Experience:", c["experience"])

print("\n❌ Rejected Candidates:")
for c in rejected_candidates:
    print(c["name"], "| Score:", c["score"], "| Experience:", c["experience"])