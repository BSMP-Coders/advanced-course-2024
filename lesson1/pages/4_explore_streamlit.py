import streamlit as st  
  
# Title of the app with an engaging emoji  
st.title("Explore Streamlit! 🚀")  
  
# Introduction text  
st.write(  
    "👋 Hey BSMP24 Coders! Get ready to be amazed by Streamlit, a powerful tool that lets you create "  
    "awesome web apps with ease. On this page, you'll find cool examples and resources that will inspire "  
    "you to build your own Streamlit masterpieces!"  
)  
  
# Link to Streamlit Gallery for inspiration  
st.markdown(  
    "🎨 Check out the [Streamlit Gallery](https://streamlit.io/gallery) to explore apps created by developers around the world!"  
)  
# Add an image with a caption  
st.image("https://pbs.twimg.com/media/GKYnqPTWAAAjDYr?format=jpg&name=small", caption="Explore Streamlit Gallery")    
# Caption with a link  
st.caption("https://share.streamlit.io/explore")


# Add a header for the video section with an engaging emoji  
st.header("Watch a Streamlit App in Action! 🎥")  
  
# Add the video  
video_url = "https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4"  
st.video(video_url)  
  
# Divider to separate sections  
st.markdown("---")  
  
# Markdown content for exploring Streamlit documentation and gallery  
st.subheader("Embark on Your Streamlit Journey 🌟")  
  
st.write(  
    "🧭 Ready to dive deeper? The Streamlit documentation is your map to treasure! "  
    "Start with the basics, explore interactive widgets, and learn how to create layouts. "  
    "Then, take a leap into the gallery to get inspired by other creators."  
)  
  
st.markdown(  
    "🔍 Explore the [Streamlit Docs](https://docs.streamlit.io/) and start crafting your own apps. "  
    "Don't forget to share your creations in the gallery!"  
)  

# Introduce Streamlit features with images organized in columns  
st.header("Discover Streamlit's Features 🦸‍♂️🦸‍♀️")  
col1, col2, col3 = st.columns(3)  
  
with col1:  
    st.image("https://user-images.githubusercontent.com/7164864/217936099-12c16f8c-7fe4-44b1-889a-1ac9ee6a1b44.png", caption="Input Widgets")  
    st.markdown("[Widgets Docs](https://docs.streamlit.io/develop/api-reference/widgets)")  
  
with col2:  
    st.image("https://user-images.githubusercontent.com/7164864/215110064-5eb4e294-8f30-4933-9563-0275230e52b5.gif", caption="Dataframes")  
    st.markdown("[Dataframes Docs](https://docs.streamlit.io/develop/api-reference/data/st.dataframe)")  
  
with col3:  
    st.image("https://user-images.githubusercontent.com/7164864/215174472-bca8a0d7-cf4b-4268-9c3b-8c03dad50bcd.gif", caption="Charts")  
    st.markdown("[Charts Docs](https://docs.streamlit.io/develop/api-reference/charts)")  
  
col4, col5, col6 = st.columns(3)  
with col4:  
    st.image("https://user-images.githubusercontent.com/7164864/217936149-a35c35be-0d96-4c63-8c6a-1c4b52aa8f60.png", caption="Layout")  
    st.markdown("[Layout Docs](https://docs.streamlit.io/develop/api-reference/layout)")  
  
with col5:  
    st.image("https://user-images.githubusercontent.com/7164864/215173883-eae0de69-7c1d-4d78-97d0-3bc1ab865e5b.gif", caption="Multi-page Apps")  
    st.markdown("[Multi-page Apps Docs](https://docs.streamlit.io/develop/concepts/multipage-apps)")  
  
with col6:  
    st.image("https://user-images.githubusercontent.com/7164864/215109229-6ae9111f-e5c1-4f0b-b3a2-87a79268ccc9.gif", caption="Fun")  
    st.markdown("[Gallery Fun](https://streamlit.io/gallery)")  
  
# Divider to separate sections  
st.markdown("---")  

# Encourage students to start coding  
st.subheader("Your Coding Quest Begins Now! 🚀")  
st.write(  
    "🎓 Learn by doing! Choose a concept, build a simple app, and keep adding features. "  
    "Step by step, you'll become a Streamlit pro. We believe in you!"  
)  
  
# Add a friendly sign-off  
st.markdown(  
    "👏 That's it for now! Keep exploring, keep asking questions, and most importantly, "  
    "keep coding. See you in the next lesson!"  
)  
  
# Divider to separate sections  
st.markdown("---")  
  
# Include a link to the Streamlit Community Forum for additional resources and support  
st.caption("🤝 Need help or want to connect with other coders? Visit the [Streamlit Community Forum](https://discuss.streamlit.io/).")  

st.markdown("""
- [StreamlitLand Adventure RPG](https://github.com/TomJohnH/streamlit-game) 👉 adventure.streamlit.app
- [Streamlit Dungeon Crawler](https://github.com/TomJohnH/streamlit-dungeon) 👉 dungeon.streamlit.app

""")
#- [Streamlit Demo: The Udacity Self-driving Car Image Browser](https://github.com/streamlit/demo-self-driving)