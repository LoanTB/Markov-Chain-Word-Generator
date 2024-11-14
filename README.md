# Markov Chain Word Generator

## Project Overview
The **Markov Chain Word Generator** is a Python-based tool designed to generate plausible words by analyzing character sequences in a user-provided source text. Leveraging Markov Chains and n-gram analysis, the generator constructs a probabilistic model of character transitions, which it uses to generate new words based on customizable parameters. This tool is ideal for creative applications, such as generating unique names, supporting creative writing, and serving as an educational resource in natural language processing (NLP).

## Features
- **Customizable N-Gram Context Length:** Allows users to control the length of the context for word generation, adjusting word complexity and coherence.
- **Probability Threshold for Creativity:** Users can set a probability threshold to balance between randomness and predictability in generated words.
- **Robust Error Handling:** Ensures smooth execution even with unusual inputs or configurations.
- **Interactive Command Line Interface:** A user-friendly CLI enables easy configuration, word generation, and display of output.

## Usage

### Prerequisites
- Python 3.x

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/LoanTB/Markov-Chain-Word-Generator.git
cd Markov-Chain-Word-Generator
```

### Running the Generator
Run the script using Python:
```bash
python3 word_generator.py
```

### Instructions
1. **Source Text File:** The program will prompt you for a file path to the text file you wish to use as a source for training. Ensure the file is in plain text format.
2. **Context Length:** Specify an integer for the n-gram length (e.g., 3 for trigrams). This value defines the length of character sequences used in the Markov model.
3. **Probability Threshold:** Set a probability between 0 and 1 for selecting the next character. Higher values increase adherence to common patterns in the text.
4. **Starting Sequence and Word Length:** For each word generated, enter a starting sequence and the desired word length. The program will output a new generated word.

### Example
```
Configuration:
Source text file for training: example.txt
Context length for training (E >= 1): 3
Probability threshold for character selection (0 < P <= 1): 0.8

Word Generation:
Start sequence (length >= 3): pro
Desired word length to generate: 8
Generated: program
```

## Code Structure

- **`load_text(file_path)`**: Loads and processes the source text.
- **`analyze_text(text, context_length)`**: Builds the statistical Markov model based on character sequences.
- **`generate_word(start_sequence, statistics, word_length, probability, context_length)`**: Generates words using the probabilistic model.
- **`main()`**: Manages program flow, user input, and error handling.

## License

This project is licensed under the Mozilla Public License 2.0 (MPL-2.0).

### Additional Note on Commercial Use
**Commercial use of this software or any derived works is prohibited without prior written permission from the original author.** For commercial licensing inquiries, please contact loan.tremoulet.breton@gmail.com.
