class StringManipulator:
    def reverse_words(self, text):
        words = text.split(' ')
        reversed_words = words[::-1]
        reversed_text = ' '.join(reversed_words)
        return reversed_text

if __name__ == "__main__":
    manipulator = StringManipulator()
    input_text = "I am groot. I am Groot"
    output_text = manipulator.reverse_words(input_text)
    print(f"in: {input_text}")
    print(f"out: {output_text}")
