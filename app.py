import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Game Progress Manager", page_icon="🎮", layout="wide")

# Header Details
current_date = datetime.now().strftime("%B %d, %Y")
st.title("🎮 Game Progress Manager")
st.markdown(f"### **Owner:** Gourav M Kulkarni | **Date:** {current_date}")
st.write("Manage your PC & PlayStation game reviews, track unfinished/leftover games, and explore upcoming releases for your wishlist.")

# Dataset Loading
@st.cache_data
def load_data():
    data = [
        # PC Played
        {"Title": "Battlefield 6", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.5, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/ar28v.jpg"},
        {"Title": "Call of Duty Black Ops 6 - Campaign", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.0, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/ar2g5.jpg"},
        {"Title": "Call of Duty Cold War - Campaign", "Platform": "PC", "Category": "Played & Finished", "Rating": 3.8, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1vbp.jpg"},
        {"Title": "Call of Duty Modern Warfare 2019 – Campaign", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.5, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1w6u.jpg"},
        {"Title": "Call of Duty Modern Warfare II 2022 – Campaign", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.0, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co5xgd.jpg"},
        {"Title": "Call of Duty Modern Warfare III 2023 – Campaign", "Platform": "PC", "Category": "Played & Finished", "Rating": 3.5, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co6wh5.jpg"},
        {"Title": "Call of Duty Vanguard - Campaign", "Platform": "PC", "Category": "Played & Finished", "Rating": 3.0, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co3una.jpg"},
        {"Title": "FIFA 23, FC 2025, FC 2026", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.0, "Status": "Active", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co5qep.jpg"},
        {"Title": "GTA 5 - Enhanced Edition", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.8, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co2lfa.jpg"},
        {"Title": "Lara Croft - Rise of the Tomb Raider", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.6, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1vbt.jpg"},
        {"Title": "Mafia - 2 Definitive Edition", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.2, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co2uzb.jpg"},
        {"Title": "Mafia - Old Country", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.5, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/ar2g5.jpg"},
        {"Title": "Mafia 1 Definitive Edition", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.7, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co2uz9.jpg"},
        {"Title": "Mortal Kombat X", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.3, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1rjg.jpg"},
        {"Title": "Spiderman Miles Morales", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.6, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co39v5.jpg"},
        {"Title": "Spiderman Remastered with DLC", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.9, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1x77.jpg"},
        {"Title": "The Last of Us Part 1", "Platform": "PC", "Category": "Played & Finished", "Rating": 5.0, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co5xbu.jpg"},
        {"Title": "The Last of Us Part 2", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.9, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co67xs.jpg"},
        {"Title": "First Light 007", "Platform": "PC", "Category": "Played & Finished", "Rating": 3.8, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/ar28v.jpg"},
        {"Title": "MW - 4", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.2, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1w6u.jpg"},
        {"Title": "Mortal Kombat 1", "Platform": "PC", "Category": "Played & Finished", "Rating": 4.4, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co67xs.jpg"},

        # PS4 Played
        {"Title": "Assassin's Creed Mirage", "Platform": "PS4", "Category": "Played & Finished", "Rating": 4.1, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co60mh.jpg"},
        {"Title": "Ghost of Tsushima", "Platform": "PS4", "Category": "Played & Finished", "Rating": 4.9, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co2gvu.jpg"},
        {"Title": "Mortal Kombat 11", "Platform": "PS4", "Category": "Played & Finished", "Rating": 4.5, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1w1z.jpg"},
        {"Title": "Uncharted Lost Legacy", "Platform": "PS4", "Category": "Played & Finished", "Rating": 4.6, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1vcd.jpg"},
        {"Title": "Uncharted Thieves End", "Platform": "PS4", "Category": "Played & Finished", "Rating": 4.9, "Status": "Completed", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1vcc.jpg"},

        # Leftover / Unfinished
        {"Title": "AC Valhalla – (Cross Saved)", "Platform": "Multi", "Category": "Leftover / Unfinished", "Rating": 3.0, "Status": "Dropped", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co2cnq.jpg"},
        {"Title": "Battlefield 3 – (PC)", "Platform": "PC", "Category": "Leftover / Unfinished", "Rating": 3.2, "Status": "Dropped", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1qsc.jpg"},
        {"Title": "Battlefield 4 – (PS4)", "Platform": "PS4", "Category": "Leftover / Unfinished", "Rating": 3.5, "Status": "Dropped", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1u2g.jpg"},
        {"Title": "Red Dead Redemption 2 – (PS4)", "Platform": "PS4", "Category": "Leftover / Unfinished", "Rating": 3.8, "Status": "Dropped", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1qrg.jpg"},
        {"Title": "Shadow of the Tomb Raider - Definitive Edition – (PS4)", "Platform": "PS4", "Category": "Leftover / Unfinished", "Rating": 3.4, "Status": "Dropped", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1vbt.jpg"},

        # Upcoming / Next 2 Years Wishlist
        {"Title": "1943 Rise of Hydra", "Platform": "PC/PS5", "Category": "Upcoming (Next 2 Years)", "Rating": 0.0, "Status": "Wishlist", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/ar28v.jpg"},
        {"Title": "AC Shadows", "Platform": "PC/PS5", "Category": "Upcoming (Next 2 Years)", "Rating": 0.0, "Status": "Wishlist", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co60mh.jpg"},
        {"Title": "GTA 6", "Platform": "PS5/PC", "Category": "Upcoming (Next 2 Years)", "Rating": 0.0, "Status": "Wishlist", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co2lfa.jpg"},
        {"Title": "Ghost of Yotei", "Platform": "PS5", "Category": "Upcoming (Next 2 Years)", "Rating": 0.0, "Status": "Wishlist", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co2gvu.jpg"},
        {"Title": "Spiderman 2", "Platform": "PS5/PC", "Category": "Upcoming (Next 2 Years)", "Rating": 0.0, "Status": "Wishlist", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co39v5.jpg"},
        {"Title": "Wolverine", "Platform": "PS5", "Category": "Upcoming (Next 2 Years)", "Rating": 0.0, "Status": "Wishlist", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/ar2g5.jpg"},
        {"Title": "Lara Croft - Legacy of Atlantis", "Platform": "PC/PS5", "Category": "Upcoming (Next 2 Years)", "Rating": 0.0, "Status": "Wishlist", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1vbt.jpg"},
        {"Title": "Lara Croft - Catalyst", "Platform": "PC/PS5", "Category": "Upcoming (Next 2 Years)", "Rating": 0.0, "Status": "Wishlist", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/co1vbt.jpg"},
        {"Title": "John Wick", "Platform": "PC/PS5", "Category": "Upcoming (Next 2 Years)", "Rating": 0.0, "Status": "Wishlist", "Thumbnail": "https://images.igdb.com/igdb/image/upload/t_1080p/ar28v.jpg"}
    ]
    return pd.DataFrame(data)

df = load_data()

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["🎮 Played & Finished", "⚠️ Leftover / Unfinished", "🚀 Upcoming (Next 2 Years)"])

with tab1:
    st.header("Played & Finished Games")
    filtered_df = df[df["Category"] == "Played & Finished"]
    for index, row in filtered_df.iterrows():
        cols = st.columns([1, 4])
        with cols[0]:
            st.image(row["Thumbnail"], width=120)
        with cols[1]:
            st.subheader(row["Title"])
            st.write(f"**Platform:** {row['Platform']} | **Rating:** {row['Rating']} / 5.0 | **Status:** {row['Status']}")
        st.divider()

with tab2:
    st.header("Leftover / Unfinished Games")
    st.write("Games that were started but won't be continued.")
    filtered_df = df[df["Category"] == "Leftover / Unfinished"]
    for index, row in filtered_df.iterrows():
        cols = st.columns([1, 4])
        with cols[0]:
            st.image(row["Thumbnail"], width=120)
        with cols[1]:
            st.subheader(row["Title"])
            st.write(f"**Platform:** {row['Platform']} | **Reason/Status:** Dropped / Leftover")
        st.divider()

with tab3:
    st.header("Upcoming Games (Next 2 Years Wishlist)")
    st.write("New game suggestions and upcoming titles to add to your to-be-played list.")
    filtered_df = df[df["Category"] == "Upcoming (Next 2 Years)"]
    for index, row in filtered_df.iterrows():
        cols = st.columns([1, 4])
        with cols[0]:
            st.image(row["Thumbnail"], width=120)
        with cols[1]:
            st.subheader(row["Title"])
            st.write(f"**Target Platform:** {row['Platform']} | **Status:** {row['Status']}")
            if st.button(f"Add to Wishlist / Track: {row['Title']}", key=row['Title']):
                st.success(f"Added {row['Title']} to your active watch list!")
        st.divider()