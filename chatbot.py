import streamlit as st
import pandas as pd
from rapidfuzz import fuzz

# Load Excel file
df = pd.read_excel("data4.xlsx")

st.title("📍 Ask About a Location")
user_query = st.text_input("Enter location name:")

if user_query:
    df["score"] = df["Location"].apply(lambda x: fuzz.partial_ratio(user_query.lower(), str(x).lower()))
    best = df.sort_values(by="score", ascending=False).head(1)

    if not best.empty and best.iloc[0]["score"] > 70:
        row = best.iloc[0]

        st.markdown(f"**Location:** {row.get('Location', '')}")
        st.markdown(f"**Contract:** {row.get('Contract', '')}")

        
        signage = row.get("Signage", "")
        if pd.notna(signage) and signage.startswith("http"):
                st.markdown(f"**Signage:** [Click here]({signage})")
        else:
                st.markdown(f"**Signage:** {signage}")



        st.markdown(f"**Portal:** {row.get('Portal', '')}")
        st.markdown(f"**SALIK Status:** {row.get('SALIK Status', '')}")

        
       


    else:
        st.warning("❌ Location not found. Try another name.")
