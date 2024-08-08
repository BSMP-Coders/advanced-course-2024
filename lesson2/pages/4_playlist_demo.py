import streamlit as st  
  
# Title of the Streamlit page  
st.title("Build Your Custom Playlist 🎶")  
  
# Introduction  
st.write("""  
Welcome to the Playlist Builder!   
Today, we will learn how to use `IF` statements, `lists`, and `loops` in Python by creating a fun and interactive playlist builder.   
Let's get started!  
""")  
  
# List of artists  
artists = ["Michael Jackson", "Drake", "Kendrick Lamar", "Justin Timberlake"]  
  
# Select artist  
st.header("Step 1: Select an Artist")  
selected_artist = st.radio("Choose an artist:", artists)  
  
# Define the songs based on the selected artist using if statements  
if selected_artist == "Michael Jackson":  
    songs = ["Billie Jean", "Thriller", "Beat It"]  
elif selected_artist == "Drake":  
    songs = ["God's Plan", "Hotline Bling", "In My Feelings"]  
elif selected_artist == "Kendrick Lamar":  
    songs = ["HUMBLE.", "DNA.", "Alright"]  
elif selected_artist == "Justin Timberlake":  
    songs = ["Cry Me a River", "Can't Stop the Feeling!", "Mirrors"]  
else:  
    songs = []  
  
# Customize the playlist  
st.header("Step 2: Customize Your Playlist")  
repeat_count = st.number_input("How many times do you want each song to repeat in your playlist?", min_value=1, max_value=10, value=1, step=1)  
  
# Display selected artist's songs  
if selected_artist:  
    st.write(f"You have selected **{selected_artist}**. The following songs will be added to your playlist:")  
    for song in songs:  
        st.write(f"- {song}")  
else:  
    st.write("No artist selected. Please choose an artist.")  
  
# Build the playlist  
st.header("Step 3: Build Your Playlist")  
button = st.button("Generate Playlist")  
  
if button:  
    st.write("Generating your custom playlist... 🎧")  
    playlist = []  
    for song in songs:  
        for _ in range(repeat_count):  
            playlist.append(song)  
  
    st.write("Here is your custom playlist:")  
    for i, song in enumerate(playlist, 1):  
        st.write(f"{i}. {song}")  
