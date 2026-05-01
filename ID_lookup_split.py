import pandas as pd
import os
import glob

folder = '/Users/saralunardelli/Downloads/Folder_Name/'
csv_files = glob.glob(os.path.join(folder, '*.csv'))

def process_and_split_csv(file_path):
    df = pd.read_csv(file_path, low_memory=False)

    # Filter rows where lickd_unique_track_id starts with 'XYZ'
    umg_filtered = df[df['lickd_unique_track_id'].str.startswith('XYZ', na=False)]

    # Split based on internal identifiers
    df_L1ckd = XYZ_filtered[XYZ_filtered['lickd_unique_track_id'].str.contains('L1ckd')]
    df_L2ck  = XYZ_filtered[XYZ_filtered['lickd_unique_track_id'].str.contains('L2ck')]
    df_L3ck  = XYZ_filtered[XYZ_filtered['lickd_unique_track_id'].str.contains('L3ck')]

    
    base_filename = os.path.splitext(os.path.basename(file_path))[0]

    output_dir = '/Users/saralunardelli/Downloads/output/'
    os.makedirs(output_dir, exist_ok=True)

    df_L1ckd.to_csv(f'{output_dir}{base_filename}_L1ckd.csv', index=False)
    df_L2ck.to_csv(f'{output_dir}{base_filename}_L2ck.csv', index=False)
    df_L3ck.to_csv(f'{output_dir}{base_filename}_L3ck.csv', index=False)

for csv_file in csv_files:
    process_and_split_csv(csv_file)

print("Processing complete!")
