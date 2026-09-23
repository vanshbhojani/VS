import os
import json
import pandas as pd

# ==========================================
# CONFIGURATION
# ==========================================

EVENTS_FOLDER = r"E:\Power BI\football\events"
OUTPUT_CSV = r"E:\Power BI\football\events.csv"

all_events = []

# ==========================================
# READ ALL EVENT FILES
# ==========================================

files = [f for f in os.listdir(EVENTS_FOLDER) if f.endswith(".json")]

print(f"Found {len(files)} event files.\n")

for i, file in enumerate(files, start=1):

    path = os.path.join(EVENTS_FOLDER, file)

    try:
        with open(path, "r", encoding="utf-8") as f:
            events = json.load(f)

        match_id = file.replace(".json", "")

        for event in events:

            row = {
                "match_id": match_id,
                "event_id": event.get("id"),
                "index": event.get("index"),
                "period": event.get("period"),
                "timestamp": event.get("timestamp"),
                "minute": event.get("minute"),
                "second": event.get("second"),
                "type": event.get("type", {}).get("name"),
                "team": event.get("team", {}).get("name"),
                "player": event.get("player", {}).get("name"),
                "position": event.get("position", {}).get("name"),
                "location_x": event.get("location", [None, None])[0] if event.get("location") else None,
                "location_y": event.get("location", [None, None])[1] if event.get("location") else None,
                "play_pattern": event.get("play_pattern", {}).get("name"),
                "possession": event.get("possession"),
                "duration": event.get("duration"),
                "under_pressure": event.get("under_pressure", False),
            }

            # Pass information
            if "pass" in event:
                row["pass_recipient"] = event["pass"].get("recipient", {}).get("name")
                row["pass_length"] = event["pass"].get("length")
                row["pass_angle"] = event["pass"].get("angle")
                row["pass_height"] = event["pass"].get("height", {}).get("name")
                row["pass_outcome"] = event["pass"].get("outcome", {}).get("name")

            # Shot information
            if "shot" in event:
                row["shot_outcome"] = event["shot"].get("outcome", {}).get("name")
                row["shot_first_time"] = event["shot"].get("first_time")
                row["shot_statsbomb_xg"] = event["shot"].get("statsbomb_xg")
                row["shot_body_part"] = event["shot"].get("body_part", {}).get("name")

            # Dribble
            if "dribble" in event:
                row["dribble_outcome"] = event["dribble"].get("outcome", {}).get("name")

            # Duel
            if "duel" in event:
                row["duel_type"] = event["duel"].get("type", {}).get("name")

            all_events.append(row)

        print(f"[{i}/{len(files)}] Processed {file}")

    except Exception as e:
        print(f"Error processing {file}: {e}")

# ==========================================
# CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(all_events)

# ==========================================
# SAVE CSV
# ==========================================

df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

print("\n====================================")
print("CSV created successfully!")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {OUTPUT_CSV}")
print("====================================")