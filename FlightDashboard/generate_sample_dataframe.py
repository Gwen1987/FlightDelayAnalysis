import pandas as pd

# Load the full dataframe
full_df = pd.read_csv('full_dataframe.csv', low_memory=False)

# Take a 10% random sample
sampled_df = full_df.sample(frac=0.1, random_state=42)

# Save the sampled dataframe to a new CSV file (optional)
sampled_df.to_csv('sampled_full_dataframe.csv', index=False)

print(f"Original size: {len(full_df)}, Sampled size: {len(sampled_df)}")