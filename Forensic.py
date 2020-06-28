hair = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
face = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eyes = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}

suspects = {"Eva": ["blonde", "oval", "blue", "female"],
            "Larisa": ["brown", "oval", "brown", "female"],
            "Matej": ["black", "oval", "blue", "male"],
            "Miha": ["brown", "square", "green", "male"]}


with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

items = []

def investigate(i):
    for x in i:
        if i[x] in dna:
            items.append(x)

investigate(hair)
investigate(face)
investigate(eyes)
investigate(gender)

for y in suspects:
    if suspects[y] == items:
        print(y + " ist dringend tatverdächtigt.")