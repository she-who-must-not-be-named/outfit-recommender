import pandas as pd

def recommend_outfit(gender, weather, occasion):
    df = pd.read_csv("data/outfits.csv")
    match = df[
        (df["gender"].str.lower() == gender)
        & (df["weather"].str.lower() == weather)
        & (df["occasion"].str.lower() == occasion)
    ]
    if not match.empty:
        return match.iloc[0]["outfit"]
    return "No outfit found for given criteria."

