import streamlit as st
import pandas as pd

# Load your dataset
df = pd.read_csv("subset_lyrics.csv")

# Title
st.title("🎶 Song Lyrics Finder")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Search Song")
    
    song_choice = st.selectbox(
        "Start typing a song name...",
        options=df["Song_Performer"].unique()
    )
    if song_choice:
        selected = df[df["Song_Performer"] == song_choice].iloc[0]
        song, performer = selected['Song_Performer'].split(' - ', 1)

# Column 2: Display lyrics
with col2:
    st.subheader("Lyrics")
    if song_choice:
        st.markdown(f"**{song}** by *{performer}*")
        st.text(selected["Lyrics"])
