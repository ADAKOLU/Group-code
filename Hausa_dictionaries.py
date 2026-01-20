import streamlit as st

choice = st.selectbox('language','hausa','yoruba','idoma','eng_to_local','igbo')

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
        "sleep": "barci"
        "eat": "ci"
}
def search_dictionary(word,dictionary):
        return dictionary[word]
if choice == 'hausa':
        dictionary = hausa_dict
        your_word = st.text_input('Enter your word')
        st.button('search', on_click=lambda: st.title(search_dictionary(your_word.lower(),dictionary)))







        # English → Local Language dictionary


