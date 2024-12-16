# CSV Splitter

This Python script splits large CSV files into smaller parts, ensuring that each part does not exceed a specified size (e.g., 1 MB). Each split file includes the original header for easier handling of the data.

## Features

- Processes all `.csv` files in the current directory.
- Splits files into smaller parts, each named sequentially (e.g., `split_part1_<original_filename>.csv`).
- Ensures each split file includes the header row from the original CSV.
- Configurable maximum file size.

## Requirements

- Python 3.6 or higher.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Mohamed-Faroug/Split-Csv-with-python.git
   ```
2. Navigate to the repository folder:
   ```bash
   cd Split-Csv-with-python   

## Usage

1. Place your `.csv` files in the same directory as the script.
2. Run the script:
   ```bash
   python split_csv.py
   ```

### Example

For a CSV file named `data.csv` with a size of 5 MB, the script will generate five smaller files:

- `split_part1_data.csv`
- `split_part2_data.csv`
- `split_part3_data.csv`
- `split_part4_data.csv`
- `split_part5_data.csv`

Each part will be approximately 1 MB in size, including the header.

## Configuration

The maximum file size is defined in the script as `MAX_SIZE`:

```python
MAX_SIZE = 1048576  # 1 MB in bytes
```

You can adjust this value as needed.

## Limitations

- The script assumes UTF-8 encoding for CSV files.
- The header is assumed to be the first row of the CSV file.
- All `.csv` files in the directory will be processed, so ensure no unrelated files are present.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
