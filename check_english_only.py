#!/usr/bin/env python3
import argparse
import sys
from typing import List, Tuple


def is_non_english(char: str) -> bool:
    """
    Check if a character is not a standard English character.
    Allows basic ASCII, common punctuation, and control characters.
    """
    # Basic ASCII range (0-127) includes English letters, numbers, and basic punctuation
    if ord(char) <= 127:
        return False

    # Additional allowed characters (em-dash, curly quotes, etc.)
    allowed_unicode = {
        "\u2013",  # en-dash
        "\u2014",  # em-dash
        "\u2018",  # left single quotation
        "\u2019",  # right single quotation
        "\u201C",  # left double quotation
        "\u201D",  # right double quotation
        "\u2026",  # ellipsis
    }

    return char not in allowed_unicode


def find_non_english_chars(file_path: str) -> List[Tuple[int, int, str]]:
    """
    Find non-English characters in the file.

    Returns:
        List of tuples (line_number, column_number, character)
    """
    results = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            for col_num, char in enumerate(line, 1):
                if is_non_english(char):
                    results.append((line_num, col_num, char))

    return results


def main(files: List[str]) -> int:
    """
    Main function to check files for non-English characters.

    Returns:
        int: 1 if errors found, 0 otherwise
    """
    found_errors = False

    for file_path in files:
        try:
            results = find_non_english_chars(file_path)
            if results:
                found_errors = True
                print(f"\n{file_path}:")
                for line_num, col_num, char in sorted(results):
                    print(
                        f"Line {line_num}, Column {col_num}: Found non-English char"
                        f"'{char}' (Unicode: U+{ord(char):04X})"
                    )
        except UnicodeDecodeError:
            print(f"Error: Unable to read {file_path} as UTF-8", file=sys.stderr)
            continue

    if found_errors:
        print(
            "\nError: Non-English characters found. Please use English characters only."
        )
        print("Note: This includes comments and strings. All text must be in English.")

    return 1 if found_errors else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check files for non-English characters"
    )
    parser.add_argument("files", nargs="*", help="Files to check")
    args = parser.parse_args()

    sys.exit(main(args.files))
