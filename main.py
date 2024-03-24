# Import necessary libraries
import cv2
import streamlit as st
from datetime import datetime
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration

# Set the title of the Streamlit app
st.title('Motion Detector')

# Create a text input field for the user to enter location
location = st.text_input("Location (not required): ")

# Create a button that starts the camera when clicked
start = st.button('Start Camera')


class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        # Get the current date and time
        now = datetime.now()

        # Format the current day and time
        day = now.strftime("%A")
        timestamp = now.strftime("%H:%M:%S")

        # Convert the frame color from BGR to RGB
        img = cv2.cvtColor(frame.to_ndarray(), cv2.COLOR_BGR2RGB)

        # Add the location and day text to the frame
        cv2.putText(img=img, text=f"{location} {day}", org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0), thickness=2,
                    lineType=cv2.LINE_AA)

        # Add the timestamp text to the frame
        cv2.putText(img=img, text=str(timestamp), org=(50, 85),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

        return img


# Check if the start button has been clicked
if start:
    webrtc_streamer(key="example", video_processor_factory=VideoProcessor)
