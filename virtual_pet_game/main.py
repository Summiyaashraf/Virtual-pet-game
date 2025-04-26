import streamlit as st
from game import Game

def main():
    st.set_page_config(page_title="🐾 Virtual Pet Game", page_icon="🐶", layout="centered")

    st.markdown(
        """
        <h1 style='text-align: center; color: #ff69b4;'>🐾 Welcome to Virtual Pet Game 🐾</h1>
        <p style='text-align: center; font-size:18px;'>Take care of your adorable little friend!</p>
        <hr style="border: 1px solid #f0a6ca;">
        """,
        unsafe_allow_html=True
    )

    pet_name = st.text_input("💬 Enter a name for your pet:")
    if pet_name:
        game = Game(pet_name)
        pet = game.get_pet()

        st.markdown(f"<h2 style='color: #6a0dad;'>🐾 {pet.name}'s Current Status 🐾</h2>", unsafe_allow_html=True)

        with st.container():
            st.info(f"🍖 Hunger: `{pet.hunger}/10`")
            st.success(f"🧼 Cleanliness: `{pet.cleanliness}/10`")
            st.warning(f"🎈 Mood: `{pet.mood}/10`")

        st.write("## ✨ Actions ✨")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🍔 Feed"):
                pet.feed()
                st.success(f"Yay! {pet.name} has been fed! 🥰")

        with col2:
            if st.button("🎮 Play"):
                pet.play()
                st.balloons()
                st.success(f"{pet.name} is playing happily! 🎉")

        with col3:
            if st.button("🛁 Clean"):
                pet.clean()
                st.success(f"{pet.name} is squeaky clean! ✨")

        st.markdown(f"<h2 style='color: #ff6347;'>📈 Updated Status 📈</h2>", unsafe_allow_html=True)
        with st.container():
            st.info(f"🍖 Hunger: `{pet.hunger}/10`")
            st.success(f"🧼 Cleanliness: `{pet.cleanliness}/10`")
            st.warning(f"🎈 Mood: `{pet.mood}/10`")

        st.markdown(
            """
            <hr style="border: 1px solid #f0a6ca;">
            <p style='text-align: center; color: grey; font-size:14px;'>🐾 A little love and a lot of code by Summiya 🐾</p>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
