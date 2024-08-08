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
  
# Layout: Use columns for song selection and number of songs  
col1, col2 = st.columns(2)  
  
# Select songs for the playlist in the first column  
with col1:  
    # Select artist    
    st.header("Step 1: Select an Artist")    
    selected_artist = st.radio("Choose an artist:", artists)    
    
    # Define the songs and album covers based on the selected artist using if statements    
    if selected_artist == "Michael Jackson":    
        songs = ["Billie Jean", "Thriller", "Beat It"]    
        album_covers = ["https://placehold.co/200x200.png"] * len(songs)  
    elif selected_artist == "Drake":    
        songs = ["God's Plan", "Hotline Bling", "In My Feelings"]    
        album_covers = ["https://placehold.co/200x200.png"] * len(songs)  
    elif selected_artist == "Kendrick Lamar":    
        songs = ["HUMBLE.", "DNA.", "Alright"]    
        album_covers = ["https://placehold.co/200x200.png"] * len(songs)  
    elif selected_artist == "Justin Timberlake":    
        songs = ["Cry Me a River", "Can't Stop the Feeling!", "Mirrors"]    
        album_covers = ["https://placehold.co/200x200.png"] * len(songs)  
    else:    
        songs = []    
        album_covers = []  
  
# Customize the playlist in the second column  
with col2:  
    # Customize the playlist  
    st.header("Step 2: Select Number of Songs")  
    num_songs = st.number_input("How many songs do you want in your playlist?", min_value=1, max_value=len(songs), value=1, step=1)  
      
    # Display selected artist's songs  
    if selected_artist:  
        st.write(f"You have selected **{selected_artist}**. The following songs will be added to your playlist:")  
        for i, song in enumerate(songs[:num_songs]):  
            st.write(f"{i+1}. {song}")  
    else:  
        st.write("No artist selected. Please choose an artist.")  
      
# Build the playlist  
st.header("Step 3: Build Your Playlist")  
button = st.button("Generate Playlist")  
  
if button:  
    st.write("Generating your custom playlist... 🎧")  
    playlist = []  
    for song in songs[:num_songs]:  
        playlist.append({"title": song, "cover": album_covers[songs.index(song)]})  
  
    st.write("Here is your custom playlist:")  
    for i, song in enumerate(playlist, 1):  
        st.write(f"{i}. {song['title']}")  
        st.image(song["cover"])  
