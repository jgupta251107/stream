import streamlit as st

# Title of the app
st.title('Posture dtection jacket')

# Add a header
st.header('We'll crack your back!')

# Add some text
st.write('Analysis for posture')

# Add a sidebar
st.sidebar.header('Sidebar')
st.sidebar.write('sideBAR')

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
