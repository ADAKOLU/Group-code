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








        # English → Local Language dictionary


