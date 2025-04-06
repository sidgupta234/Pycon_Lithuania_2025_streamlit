# Streamlit Exercise: Build a Song Lyrics Finder App

# 1. Import the necessary libraries
# (Hint: You'll need Streamlit and pandas)

# 2. Load your dataset
# Use pandas to read "subset_lyrics.csv" into a DataFrame

# 3. Create a Streamlit title
# Use st.title to display: "Song Lyrics Fetcher"

# 4. Create two side-by-side columns
# Use st.columns(2) to make col1 and col2

# 5. In col1: Add a subheader for the search box
# Then, create a selectbox to choose a song from the DataFrame
# (Hint: The options should come from the "Song_Performer" column)
# If a song is selected, extract the first row matching the choice

# 6. Split the selected "Song_Performer" string into song and performer
# (Assume the format is "Song - Performer")

# 7. In col2: Add a subheader for displaying lyrics
# Show the selected song name and performer nicely formatted
# Then display the corresponding lyrics using st.text()

# Run the app with: streamlit run your_script_name.py