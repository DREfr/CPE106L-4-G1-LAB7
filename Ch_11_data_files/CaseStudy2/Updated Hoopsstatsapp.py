import pandas as pd
from hoopstatsview import HoopStatsView

def cleanStats(frame):
    """Ensures the basketball statistics DataFrame retains the makes-attempts format."""
    columns_to_keep = ["FG", "3PT", "FT"]  # Ensure these stay in the format 'makes-attempts'

    for col in columns_to_keep:
        if col in frame.columns:
            # Convert all values to strings to preserve the format
            frame[col] = frame[col].astype(str)

    return frame

def main():
    """Loads, cleans, and displays basketball statistics."""
    try:
        # Load CSV File
        frame = pd.read_csv("rawbrogdonstats.csv")  
        print("✅ CSV file loaded successfully!")

        # Clean dataset
        frame = cleanStats(frame)  
        print("✅ Data cleaned successfully!")
        
        # Print first few rows to verify format
        print(frame.head())

        # Save cleaned data
        frame.to_csv("cleanbrogdonstats.csv", index=False)  
        print("✅ Cleaned data saved to 'cleanbrogdonstats.csv'")

        # Display the stats in GUI
        HoopStatsView(frame)  
        print("✅ HoopStatsView launched successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
