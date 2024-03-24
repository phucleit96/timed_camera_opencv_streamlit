import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        return frame

st.title('Webcam Live Feed')
st.markdown("Click on 'Start webcam' to start the live feed")

webrtc_streamer(key="example", video_processor_factory=VideoProcessor)