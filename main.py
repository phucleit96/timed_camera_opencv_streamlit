# Import necessary libraries
import cv2
import streamlit as st
from datetime import datetime

# Set the title of the Streamlit app
st.title('Motion Detector')

# Create a text input field for the user to enter their location
location = st.text_input("Location (not required): ")

# Create a button that starts the camera when clicked
start = st.button('Start Camera')

# Check if the start button has been clicked
if start:
    # Create an empty image placeholder in the Streamlit app
    streamlit_image = st.image([])

    # Start the camera
    camera = cv2.VideoCapture(0)

    # Continuously capture frames from the camera
    while True:
        # Get the current date and time
        now = datetime.now()

        # Format the current day and time
        day = now.strftime("%A")
        timestamp = now.strftime("%H:%M:%S")

        # Read a frame from the camera
        check, frame = camera.read()

        # Convert the frame color from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Add the location and day text to the frame

        cv2.putText(img=frame, text=f"{location} {day}", org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0), thickness=2,
                    lineType=cv2.LINE_AA)

        # Add the timestamp text to the frame
        cv2.putText(img=frame, text=str(timestamp), org=(50, 85),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

        # Display the frame in the Streamlit app
        streamlit_image.image(frame)