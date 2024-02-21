import streamlit as st

# Title of the app
st.title('My Streamlit App')

# Add a header
st.header('Welcome to my app!')

# Add some text
st.write('This is a simple Streamlit app.')

# Add a sidebar
st.sidebar.header('Sidebar')
st.sidebar.write('This is the sidebar.')

# Add a slider widget
value = st.slider('Select a value', 0, 100, 50)

# Display the selected value
st.write(f'You selected: {value}')

# Add a button
if st.button('Click me'):
    st.write('Button clicked!')

# Add a file uploader
file = st.file_uploader('Upload a file', type=['csv', 'txt'])
if file is not None:
    st.write('File uploaded successfully!')
    st.write(file.read())  # Display file contents
