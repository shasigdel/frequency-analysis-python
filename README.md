# Frequency Analysis Python

## Overview

This project is a simple frequency analysis tool named **frequency-analysis-python** that helps users decrypt text by analyzing the frequency of characters in a given passage. The tool allows users to select between two predefined passages, calculates the frequency of each character, and provides functionality to swap the most frequent characters with user-defined replacements. This project is intended for educational purposes to demonstrate basic cryptography techniques like frequency analysis.

## Features

- **Frequency Calculation**: Analyze the frequency of each character in a passage, displaying both the count and percentage of occurrence.
- **Top Occurrence Replacement**: Automatically replace the top three most frequent characters with predefined replacements.
- **User-Defined Replacement**: Allow users to manually replace characters in the text, with restrictions on certain high-frequency characters.
- **File Input/Output**: The program reads from text files (`passage1.txt` and `passage2.txt`) and writes the modified text to `example.txt`.

## How It Works

1. **Select Passage**: The user is prompted to select between two passages (`passage1.txt` or `passage2.txt`). The selected passage is displayed for analysis.
2. **Frequency Analysis**: The program calculates and displays the frequency of each character in the selected passage, showing the count and percentage for each character.
3. **Automatic Replacement**: The program replaces the top three most frequent characters (`E`, `T`, `A`) with predefined replacements.
4. **Manual Replacement**: The user can then manually replace characters in the modified text, with restrictions on changing the characters `E`, `T`, and `A`.
5. **Save Modified Text**: The final modified text is saved to `example.txt`.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/frequency-analysis-python.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd frequency-analysis-python
   ```

3. **Place your passage files**:

   - Ensure you have two text files named `passage1.txt` and `passage2.txt` in the project directory.

4. **Run the program**:
   ```bash
   python main.py
   ```

## Usage

1. **Start the Program**:
   - Run the Python script `main.py`.
2. **Select a Passage**:

   - Input `1` or `2` to select the passage you want to analyze.

3. **View Frequency Analysis**:

   - The program will display the frequency analysis of the characters in the selected passage.

4. **Automatic Replacement**:

   - The program will automatically replace the top three most frequent characters with the predefined replacements.

5. **Manual Replacement**:

   - You can replace characters by entering the character you want to change and its replacement. Restrictions apply to `E`, `T`, and `A`.

6. **Save the Modified Text**:
   - The modified text is saved to `example.txt`.

## Example

Example of frequency analysis output:

```
E: 150 (12.50%)
T: 120 (10.00%)
A: 100 (8.33%)
...
```

## Future Enhancements

- **Custom Passage Input**: Allow users to input their custom text passages.
- **More Sophisticated Analysis**: Implement more advanced decryption techniques, such as bigram and trigram analysis.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any enhancements or bug fixes.
