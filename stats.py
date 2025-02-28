def count_words(getting_numbers_out):
    import re
    words = re.findall(r'\S+', getting_numbers_out)
    words_count = len(words)
    return words_count

def yanking_my_pizzle(text: str) -> dict:
    text = text.lower()
    char_count = {}  
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

def sort_char_counts(char_count: dict) -> list:
    filtered_chars = {char: count for char, count in char_count.items() if char.isalpha()}
    sorted_chars = sorted(filtered_chars.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_chars