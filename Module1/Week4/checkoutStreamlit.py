import streamlit as st

st.markdown("# Text Elements")

st.markdown("## Display Text")
code = '''
st.title("MY PROJECT")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("I love AI VIET NAM")
'''
st.code(code, language='python')

st.markdown("## Display string formatted as Markdown")
st.markdown("# Heading 1")
st.markdown("[AI VIETNAM](https://aivietnam.edu.vn/)")
st.markdown("""
1. Machine Learning
2. Deep Learning
""")
st.markdown("$\sqrt{2x+2}$")
st.latex("\sqrt{2x+2}")

def get_user_name():
    return 'Anh'

with st.echo():
    st.write("This code will be printed")
    def get_email():
        return "anh.nguyennhu2306@hcmut.edu.vn"
    user_name = get_user_name()
    email = get_email()
    st.write(user_name, email)

st.image("./images_videos/dog.jpeg")
st.audio("./images_videos/audio.mp4")
st.video("./images_videos/video.mp4")


agree = st.checkbox(
    "I agree", on_change=get_user_name
)
if agree:
    st.write("Hello World")

st.radio(
    "Your most favortite color: ",
    ['Yellow', 'Blue'],
    captions=['Vang', "Xanh"]
)


options = st.selectbox(
    "Your contact:",
    ("Email", "Home Phone", "Mobile Phone"),
)
st.write("Selected: ", options)

optionss = st.multiselect(
    "Your favorite colors",
    ["Green", "Yellow", "Red", "Blue", "Yellow", "Red"]
)
st.write("Your selected: ", optionss)

color= st.select_slider(
    "Your favorite color: ",
    options=["red", "orange", "violet"]
)
st.write("your option: ", color)

if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Goodbye")
st.link_button(
"Go to Google",
"https://www.google.com.vn/"
)

title = st.text_input(
"Movie title:", "Life of Brian"
)
st.write("The current movie title is", title)


if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


messages = st.container(height=200)
if prompt := st.chat_input("Say someting..."):
    st.session_state.chat_history.append(("user", prompt))
    response = f"Echo: {prompt}"
    st.session_state.chat_history.append(("assisstant", response))

with messages:
    for sender, message in st.session_state.chat_history:
        if sender == "user":
            st.chat_message("user").write(message)
        else:
            st.chat_message("assisstant").write(message)



number = st.number_input("Insert a number")
st.write("The current number is ",
number)


values = st.slider(
"Select a range of values",
0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

uploaded_files = st.file_uploader(
    "Choose files",
    accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename: ", uploaded_file.name)
    # st.write("Content: ", bytes_data)

with st.form("my_form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('First Name')
    l_name = col2.text_input('Last Name')
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("First Name: ", f_name,
        " - Last Name:", l_name)