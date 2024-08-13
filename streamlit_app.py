from openai import OpenAI
import base64
import streamlit as st
from PIL import Image
import io
import cv2

# Show title and description.
st.title("💬 Chatbot")


# Initialize the OpenAI client.
client = OpenAI()

# Create a session state variable to store the chat messages and images. 
# This ensures that the messages and images persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("image"):
            st.image(message["image"])

# Allow the user to upload an image.
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Display the uploaded image if available.
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Encode the image as base64
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode()
    
    st.session_state.messages.append({"role": "system",
                                      "content": "Professional Table Analyser, Reproduce the given table in HTML code",})
    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", 
                                      "content": "Please analyze the table in the attached image.",
                                      "image": image_base64})

    with st.chat_message("user"):
        st.markdown("Analyze the table in the image and provide the HTML code to reproduce")
        st.image(image)

    messages =[{"role": "system",
                    "content": "Professional Table Analyser, Reproduce the given table in HTML code",},
                {"role": "user", 
                "content": [{"Please analyze the table in the attached image."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },]
                }  
    ]

    # Generate a response using the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=messages,
        max_tokens=500
    )

    # Stream the response to the chat using `st.write_stream`, then store it in 
    # session state.
    with st.chat_message("assistant"):
        response = st.write_stream(response.choices[0].message.content)
    st.session_state.messages.append({"role": "assistant", "content": response})
