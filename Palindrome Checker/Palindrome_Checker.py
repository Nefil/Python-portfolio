def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(sentence):
    words = sentence.split()  
    palindromes = [word for word in words if is_palindrome(word.lower())] 
    return palindromes

if __name__ == "__main__":
    sentence = input("Enter a sentence: ").strip().lower()
    palindromes = find_palindromes(sentence)
    
    if palindromes:
        print("Palindromes found:", ", ".join(palindromes))
    else:
        print("No palindromes found in the sentence.")