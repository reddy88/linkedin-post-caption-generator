import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


# Main app layout
def main():
    st.subheader("LinkedIn Post Generator:")

    # Create four columns for the dropdowns
    col1, col2, col3, col4 = st.columns(4)

    fs = FewShotPosts()
    fields = fs.get_fields()

    with col1:
        # Dropdown for Field
        selected_field = st.selectbox("Field", options=fields)

    with col2:
        # Dropdown for Topic (Tags)
        topics = fs.get_topics_by_field(selected_field)
        selected_tag = st.selectbox("Topic", options=topics)

    with col3:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col4:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)

    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_field, selected_length, selected_language, selected_tag)
        st.write(post)


# Run the app
if __name__ == "__main__":
    main()