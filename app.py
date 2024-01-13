import streamlit as st
import codes

st.set_page_config("C# Cheatsheet", layout='centered', page_icon='📖', initial_sidebar_state='auto')

def main():
    page = st.sidebar.selectbox("Choose a page", ["Basics", "Advance", "Examples"])
            
    if page == "Basics":
        for k, v in codes.basics.items():
            st.subheader(k)
            st.code(v[0], language='java')
            st.write(v[1])
            st.markdown("---")
    elif page == "Advance":
            st.write("No Advance code yet!")
    elif page == "Examples":
        for k, v in codes.examples.items():
            st.subheader(k)
            st.code(v[0], language='java')
            st.write(v[1])
            st.markdown("---")
        st.write("Copyright © 2024 Josuan. All rights reserved.")

if __name__ == '__main__':
    main()