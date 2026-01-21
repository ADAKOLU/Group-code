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
ufia = {
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
idoma = {
        "cassava": "akpu",
        "good": "oma",
        "fire":  "oku",
        "spirit": "mmuo",
        "sit": "no",
        "goodness": "oma",
        "king": "eze",
        "mother": "nne",
        "father": "nna",
        "children": "umu",
        "land": "ala",
        "medicine": "ogwu",
        "money":"akwu",
        "journey": "ije",
        "time": "oge",
        "house": "ulo",
        "eye": "anya",
        "ear": "nti",
        "mouth": "onu",
        "hand": "aka",
}
translation ={
    'hausa':hausa,
    'youruba': yoruba,
    'igbo': igbo,
    'eng_to_local':eng_to_local,
    'idoma': idoma
}
language = input("enter what language; (hausa / igbo/yoruba / eng_to_local / idoma): ")
word = input("enter the english word you want to translate: ")

if language in translation:
    lang = translation.get(word, '')
    if word in lang:
        print("Translation:", lang[word])
    else:
        print("the word is not found")
else:
    print("the language is not found")

#streamlit version
import streamlit as st

choice = st.selectbox('language',['hausa','yoruba','igbo','ufia','idoma'])

hausa_dict = {
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
        "sleep": "barci",
        "eat": "ci"
}
igbo_dict = {
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
        "thanks_you": "ekele",
        "what's_up": "kedu",
}
yoruba_dict = {
       "woman":"obirin",
        "sun":"oorun",
        "sleep":"sun",
        "father":"baba",
        "joy":"ayo",
        "anger":"ibinu",
        "eat":"je",
        "Water":"omi",
        "work":"ise",
        "fire":"ina",
        "money":"owo",
}
idoma_dict = {
        "cassava": "akpu",
        "good": "oma",
        "fire":  "oku",
        "spirit": "mmuo",
        "sit": "no",
        "goodness": "oma",
        "king": "eze",
        "mother": "nne",
        "father": "nna",
        "children": "umu",
        "land": "ala",
        "medicine": "ogwu",
        "money":"akwu",
        "journey": "ije",
        "time": "oge",
        "house": "ulo",
        "eye": "anya",
        "ear": "nti",
        "mouth": "onu",
        "hand": "aka",
}
  ufia_dict = {
          "Good morning":"ite",
          "Good afternoon":"Ndo Iko",
          "Good evening":"Ndo Ididi",
          "How are you doing?":"Icholo-be?",
          "I love you":"Ava-gbudom",
          "Give me":"Yinne",
          "Water":"Bayin",
          "Spoon":"Ekor",
          "Mother":"ada",
          "Teeth":"Reraar",
          "Leg":"kotuwo",
  }          
          
          
def search_dictionary(word,dictionary):
        return dictionary.get(word,'word not found')
if choice == 'hausa':
        dictionary = hausa_dict
        your_word = st.text_input('Enter your word')
        st.button('search', on_click=lambda: st.title(search_dictionary(your_word.lower(),dictionary)))
if choice == 'igbo':
        dictionary = igbo_dict
        your_word = st.text_input('Enter your word')
        st.button('search', on_click=lambda: st.title(search_dictionary(your_word.lower(),dictionary)))
if choice == 'yoruba':
        dictionary = yoruba_dict
        your_word = st.text_input('Enter your word')
        st.button('search', on_click=lambda: st.title(search_dictionary(your_word.lower(),dictionary)))
if choice == 'ufia_dict'
         dictionary = ufia_dict
         your_word = st.text_input('Enter your word')
         st.button('search', on_click = lambda: st.title(search_dictionary(your_word.lower(),dictionary)))
 if choice == 'idoma'
         dictionary = idoma_dict
         your_word = st.text_input('Enter your word')
         st.button('search', on_click = lambda: st.title(search_dictionary(your_word.lower(),dictionary)))
        








        # English → Local Language dictionary


