# Caesar Cypher

## Description
This is a Python implementation of a Caesar Cipher, a simple substitution cipher used to encode and decode messages by shifting characters in the alphabet by a specified number of positions.

## Features
- Encrypts and decrypts messages using the Caesar Cipher technique.
- Supports a continuous loop to allow users to restart the program after each operation.
- Includes a stylish ASCII art logo for a fun and engaging user experience.

## How to Use
1. Run the `Cypher.py` file in your terminal or Python IDE.
2. Follow the prompts:
   - Type "encode" to encrypt a message or "decode" to decrypt a message.
   - Enter your message.
   - Enter the shift value (integer).
3. The program will output the encoded or decoded text.

## Example
### Input:

Type 'encode' to encrypt, type 'decode' to decrypt: encode Type your message: hello Type the shift number: 3

### Output:

The encoded text is 'khoor'.


## Requirements
- Python 3.7 or higher
- The `art.py` file must be present in the same directory for the ASCII art to display.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Zar1717/caesar-cypher.git
2. Navigate to the project folder:
   ```bash
   cd caesar-cypher
3. Run the program:
   ```bash
   python Cypher.py


Notes:

- The alphabet list is extended to handle shifts that wrap around the end of the alphabet.
- Spaces are included as valid characters for encoding and decoding.

Future Improvements:

- Add support for uppercase letters and special characters.
- Implement error handling for invalid inputs.
- Create a graphical user interface (GUI) version.

