import streamlit as st
from pymongo import MongoClient
from link.final import final
try:
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['Hacknuthon']
    collection = db['HF_Questions']
except Exception as e:
    st.error(f"Error connecting to MongoDB: {e}")

# Title for the dashboard
st.title("Current Query")

# Input message and add button
col1, col2 = st.columns([1, 1])
input_message = col1.text_input("Enter Question")
col2.write(" ")
col2.write(" ")
add_button = col2.button("Add Question To DB")

if add_button and input_message:
    try:
        # Check if the question already exists
        existing_question = collection.find_one({"question": input_message})
        if existing_question:
            st.warning("Question already exists!")
        else:
            # Add the message to MongoDB
            collection.insert_one({"question": input_message})
            st.success("Question added to DB!")
    except Exception as e:
        st.error("Error adding message to DB")
st.write("---------------------------------------------------")
# Display table with questions and delete buttons
st.header("Questions in DB")
questions = collection.find({}, {"_id": 0, "question": 1})

for question in questions:
    col3, col4 = st.columns([1, 1])
    col3.write(question["question"])
    delete_button = col4.button("Delete", key=f"delete_{question['question']}")  # Unique key for each button

    if delete_button:
        try:
            # Delete the question from MongoDB
            collection.delete_one({"question": question["question"]})
            st.success(f"Deleted: {question['question']}")
            # Refresh the page after deletion
            st.experimental_rerun()
        except Exception as e:
            st.error("Error deleting message from DB")
st.write("-------------------------------------------")

# Display "Generate Video" button if database is not empty
if collection.count_documents({}) > 0:
    generate_video_button = st.button("Generate Video")
    if generate_video_button:
        first_question = collection.find_one({}, {"_id": 0, "question": 1})
        if first_question:
            out=final(first_question["question"])
            if out=="Synced video downloaded successfully!":
                st.success("Video Generated and store successfully")
            else:
                st.warning("There is some Error ",out)    