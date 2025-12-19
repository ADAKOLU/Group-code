hausa = {
        "hello": "sannu",
        "water": "ruwa",
        "food": "abinci",
        "house": "gida",
        "school": "makaranta",
        "book": "littafi",
        "father": "uba",
        "mother": "uwa",
        "child": "yaro",
        "man": "namiji",
        "woman": "mace",
        "sun": "rana",
        "moon": "wata",
        "money": "kuɗi",
        "road": "hanya",
        "friend": "aboki",
        "love": "so",
        "work": "aiki",
        "sleep": "barci"
        "eat": "ci"
}
yoruba = {
    "man": "ọkùnrin",
    "woman": "obinrin",
    "sun": "oorun",
    "moon": "osupa",
    "money": "owo",
    "road": "opopona",
    "friend": "ọrẹ",
    "love": "ifẹ",
    "work": "iṣẹ",
    "sleep": "sun",
    "eat": "jẹ"
    "woman": "obinrin",
    "child": "ọmọ",
    "father": "baba",
    "mother": "iya",
    "friend": "ọrẹ",
    "teacher": "olukọ",
    "star": "irawọ",
    "water": "omi",
    "fire": "ina",
    "rain": "ojo",
    "love": "ifẹ",
    "happy": "ayọ",
    "sad": "ibanujẹ",
    "angry": "ibinu",   
}
igbo = {
        "house": "ulo",
        "money": "ego",
        "food": "nri",
        "water": "Mmiri",
        "cloth": "akwa",
        "hand": "aka",
        "leg": "ukwu",
        "head": "isi",
        "heart": "obi",
        "morning": "ututu",
        "evening": "angasi",
        "man": "nwoke",
        "woman": "nwaanyi",
        "child": "nwatakiri",
        "hunger": "aguu",
        "fire": "oku",
        "story": "akuko",
        "thanks you": "ekele",
        "what's up": "kedu",
}
translation ={
    'hausa':hausa,
    'youruba': yoruba
    'igbo': igbo
}
language = input("enter what language; (hausa / igbo): ")
word = input("enter the english word you want to translate: ")
language = input("Enter language (hausa / yoruba / igbo): ")
word = input("Enter the English word to translate: ")
if language in translation:
    lang = translation[language]
    if word in lang:
        print("Translation:", lang[word])
    else:
        print("the word is not found")
else:
    print("the language is not found")
        # English → Local Language dictionary
eng_to_local = {
    "good morning": "ite",
    "good afternoon": "ndo iko",
    "good evening": "mdo ididi",
    "how are you?": "nke nadi",
    "i love you": "avaduone",
    "let us go": "velido",
    "stand up": "titti",
    "sit down": "tuwo",
    "give me": "yinne",
    "water": "bayin",
    "plate": "ogbagala",
    "spoon": "ekor",
    "food": "kaji",
    "mother": "ené",
    "father": "edé",
    "nose": "jol",
    "hair": "kitulu",
    "teeth": "reraar",
    "tongue": "redaar",
    "mouth": "kamma"
}

# Automatically create Local → English dictionary
local_to_eng = {value: key for key, value in eng_to_local.items()}

print("1. English → Local Language")
print("2. Local Language → English")

choice = input("Choose translation direction (1 or 2): ")

word = input("Enter word or phrase: ").lower()

if choice == "1":
    if word in eng_to_local:
        print("Translation:", eng_to_local[word])
    else:
        print("Sorry, translation not found.")

elif choice == "2":
    if word in local_to_eng:
        print("Translation:", local_to_eng[word])
    else:
        print("Sorry, translation not found.")

else:
    print("Invalid choice.")

