import streamlit as st
import codes

correct_password = "leonardo@231"  

def check_password(password):
    return password == correct_password

st.set_page_config("C# Cheatsheet", layout='centered', page_icon='📖', initial_sidebar_state='auto')

def main():
    password = st.sidebar.text_input("Enter password:", type="password")
    if st.sidebar.button("Sign in"):
        if check_password(password):
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
        else:
            st.warning("Incorrect password. Access denied.")

if __name__ == '__main__':
    main()