def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

if __name__ == "__main__":
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter text: ").strip()
    shift = int(input("Enter shift amount: ").strip())
    print(f"Result: {caesar_cipher(text, shift, mode)}")