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
translation ={
    'hausa':hausa,
}
language = input("enter what language; (hausa): ")
word = input("enter the english word you want to translate: ")
if language in translation:
    lang = translation[language]
    if word in lang:
        print("Translation:", lang[word])
    else:
        print("the word is not found")
else:
    print("the language is not found")