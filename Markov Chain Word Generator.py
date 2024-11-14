import random

def load_text(file_path):
    """
    Loads text from a file, replacing newline characters with spaces.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: The processed text content.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        text = " ".join(file.read().split("\n"))
    return text

def analyze_text(text, context_length):
    """
    Analyzes the text to build a statistical model based on n-grams.

    Args:
        text (str): The text to analyze.
        context_length (int): The length of the n-gram context.

    Returns:
        dict: A dictionary representing the statistical model.
    """
    statistics = {}
    for n in range(context_length):
        for i in range(len(text)):
            if i + n + 2 < len(text):
                context = text[i:i + n + 1]
                next_char = text[i + n + 1]
                if context not in statistics:
                    statistics[context] = {}
                if next_char in statistics[context]:
                    statistics[context][next_char] += 1
                else:
                    statistics[context][next_char] = 1
    return statistics

def generate_word(start_sequence, statistics, word_length, probability, context_length):
    """
    Generates a word based on the statistical model.

    Args:
        start_sequence (str): The starting sequence of characters.
        statistics (dict): The statistical model.
        word_length (int): The desired length of the generated word.
        probability (float): The probability threshold for selecting the next character.
        context_length (int): The length of the n-gram context.

    Returns:
        str: The generated word.
    """
    word = start_sequence
    for _ in range(word_length):
        context = word[-context_length:]
        if context not in statistics:
            break
        next_chars = statistics[context]
        max_count = 0
        selected_char = ""
        for char, count in next_chars.items():
            if count > max_count and random.random() < probability:
                max_count = count
                selected_char = char
        word += selected_char
    return word

def generate_word_no_space(start_sequence, statistics, word_length, probability, context_length):
    """
    Generates a word without including space characters based on the statistical model.

    Args:
        start_sequence (str): The starting sequence of characters.
        statistics (dict): The statistical model.
        word_length (int): The desired length of the generated word.
        probability (float): The probability threshold for selecting the next character.
        context_length (int): The length of the n-gram context.

    Returns:
        str: The generated word.
    """
    word = start_sequence
    while len(word) < word_length:
        context = word[-context_length:]
        if context not in statistics:
            break
        next_chars = statistics[context]
        max_count = 0
        selected_char = ""
        for char, count in next_chars.items():
            if count > max_count and random.random() < probability and char != " ":
                max_count = count
                selected_char = char
        word += selected_char
    return word

def display_banner():
    """
    Displays an ASCII art banner.
    """
    banner = """
,---.    ,---.    _______   .--.      .--.  .-_'''-.
|    \\  /    |   /   __  \\  |  |_     |  | '_( )_   \\
|  ,  \\/  ,  |  | ,_/  \\__) | _( )_   |  ||(_ o _)|  '
|  |\\_   /|  |,-./  )       |(_ o _)  |  |. (_,_)/___|
|  _( )_/ |  |\\  '_ '`)     | (_,_) \\ |  ||  |  .-----.
| (_ o _) |  | > (_)  )  __ |  |/    \\|  |'  \\  '-   .'
|  (_,_)  |  |(  .  .-'_/  )|  '  /\\  `  | \\  `-'`   |
|  |      |  | `-'`-'     / |    /  \\    |  \\        /
'--'      '--'   `._____.'  `---'    `---`   `'-...-'
"""
    print(banner)

def main():
    display_banner()
    print("Configuration:")
    source_file = input("Source text file for training: ")
    context_length = int(input("Context length for training (E >= 1): "))
    probability = float(input("Probability threshold for character selection (0 < P <= 1): "))
    print("\nWord Generation:\n")

    try:
        text_content = load_text(source_file)
        statistics = analyze_text(text_content, context_length)
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
        return

    while True:
        try:
            start_sequence = input(f"Start sequence (length >= {context_length}): ")
            if len(start_sequence) < context_length:
                print(f"Error: The start sequence must be at least {context_length} characters long.")
                continue
            desired_length = int(input("Desired word length to generate: "))
            generated_word = generate_word_no_space(start_sequence, statistics, desired_length, probability, context_length)
            print(f"Generated: {generated_word}\n")
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break
        except Exception:
            print("Error: The start sequence is unknown, the training text is too short, or the context length is too large.\n")

if __name__ == "__main__":
    main()
