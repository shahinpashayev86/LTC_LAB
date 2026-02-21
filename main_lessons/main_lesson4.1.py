import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 1️⃣ Word Embedding Matrix (Dictionary şəklində)
embedding_matrix = {
    "futbol": np.array([0.9, 0.8, 0.1, 0.0]),
    "oyun": np.array([0.8, 0.7, 0.2, 0.1]),
    "qapı": np.array([0.85, 0.75, 0.1, 0.1]),
    "qol": np.array([0.7, 0.6, 0.5, 0.4]),
    "iş": np.array([0.1, 0.2, 0.9, 0.8]),
    "sənəd": np.array([0.1, 0.1, 0.85, 0.9]),
    "imza": np.array([0.2, 0.2, 0.95, 0.85])
}


# 2️⃣ Cümlə vektoru hesablayan funksiya
def sentence_vector(sentence):
    words = sentence.lower().split()
    vectors = []

    for word in words:
        if word in embedding_matrix:
            vectors.append(embedding_matrix[word])

    if len(vectors) == 0:
        return None

    return np.mean(vectors, axis=0).reshape(1, -1)


# 3️⃣ Referans kontekstlər
football_context = sentence_vector("futbol oyun qapı qol")
work_context = sentence_vector("iş sənəd imza qol")

# 4️⃣ Test 1
input_sentence1 = "Mən bu gün futbol oyununda qapı qol"
vec1 = sentence_vector(input_sentence1)

sim_football1 = cosine_similarity(vec1, football_context)
sim_work1 = cosine_similarity(vec1, work_context)

print("Test 1 nəticə:")
if sim_football1 > sim_work1:
    print("Cavab: Qardaş 10 qol zərbəsi vurmaq lap yaxşı göstəricidir.")
else:
    print("Cavab: Bir gün işdə 100 sənədə qol çəkmək ciddi məsuliyyət deməkdir.")

# 5️⃣ Test 2
input_sentence2 = "Mən bu gün iş sənəd qol"
vec2 = sentence_vector(input_sentence2)

sim_football2 = cosine_similarity(vec2, football_context)
sim_work2 = cosine_similarity(vec2, work_context)

print("\nTest 2 nəticə:")
if sim_football2 > sim_work2:
    print("Cavab: Qardaş 10 qol zərbəsi vurmaq lap yaxşı göstəricidir.")
else:
    print("Cavab: Bir gün işdə 100 sənədə qol çəkmək ciddi məsuliyyət deməkdir.")
