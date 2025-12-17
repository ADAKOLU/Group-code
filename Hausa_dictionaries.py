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
translation ={
    'hausa':hausa,
    'youruba': yoruba
}
language = input("enter what language; (hausa): ")
word = input("enter the english word you want to translate: ")
language = input("Enter language (hausa / yoruba): ")
word = input("Enter the English word to translate: ")
if language in translation:
    lang = translation[language]
    if word in lang:
        print("Translation:", lang[word])
    else:
        print("the word is not found")
else:
    print("the language is not found")
