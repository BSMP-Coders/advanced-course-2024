import streamlit as st  
import glob  
  
# Function to load and display images  
def load_image():  
    # Use glob to find all PNG files in the 'logos' directory  
    images_files = glob.glob("logos/*.png")  
      
    # Display the number of images found  
    st.write("Number of images found:", len(images_files))  
      
    # Loop through the list of image files  
    for image_file in images_files:  
        # Display each image  
        st.image(image_file, use_column_width=True)  
          
        # Write the file name under the image  
        st.write("File name:", image_file)  
          
    # Return the list of image files  
    return images_files  
          
# Main title of the page  
st.title("Demo Image Grid Display")  
  
# Explain the purpose of the app  
st.write("This app demonstrates how to load and display a grid of images from a directory.")  
  
# Call the function to load and display images  
image_files = load_image()  
  
# Explain what the returned value represents  
st.write("The `load_image` function returns a list of file paths for the images displayed above.")  
