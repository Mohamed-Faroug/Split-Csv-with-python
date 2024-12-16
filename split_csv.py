import os
import csv

# Constants
MAX_SIZE = 1000000  # 1 MB in bytes
OUTPUT_PREFIX = "split_part"

def split_csv(input_file):
    """Split a CSV file into smaller parts."""
    part_number = 1
    total_files = 0
    current_size = 0
    header = None
    output_file = None
    writer = None

    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)  # Load all rows to process
        header = rows[0]  # First row as header

        # Start splitting
        for i, row in enumerate(rows):
            # Initialize new file if necessary
            if current_size == 0 or output_file is None:
                if output_file:
                    output_file.close()
                output_file_name = f"{OUTPUT_PREFIX}{part_number}_{os.path.splitext(os.path.basename(input_file))[0]}.csv"
                output_file = open(output_file_name, 'w', newline='', encoding='utf-8')
                writer = csv.writer(output_file)
                writer.writerow(header)  # Write header
                current_size = len(','.join(header).encode('utf-8')) + 1
                total_files += 1
                print(f"Created: {output_file_name}")

            # Calculate size of current row
            row_size = len(','.join(row).encode('utf-8')) + 1

            # Check if adding this row exceeds the size limit
            if current_size + row_size > MAX_SIZE:
                part_number += 1
                current_size = 0
                continue  # Write this row to the next file

            # Write the row to the current file
            writer.writerow(row)
            current_size += row_size

    if output_file:
        output_file.close()
    print(f"Finished processing {input_file}. Total files created: {total_files}.")

def process_all_csv_files():
    """Process all CSV files in the current directory."""
    total_files_created = 0
    for file in os.listdir('.'):
        if file.endswith('.csv'):
            print(f"Processing file: {file}")
            split_csv(file)
            total_files_created += 1
    print(f"All files processed. Total files created: {total_files_created}.")

if __name__ == "__main__":
    process_all_csv_files()
