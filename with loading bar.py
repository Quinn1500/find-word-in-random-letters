import random
import sys
import time

def main():
    while True:
        target_word = input("Enter the target word: ").lower()
        generated_word = ""

        loading_dots = ''
        while target_word not in generated_word:
            generated_word += generate_substring(target_word, len(generated_word))
            loading_dots = loading_animation(loading_dots)
            sys.stdout.write('\rGenerating word' + loading_dots)
            sys.stdout.flush()
            time.sleep(0.1)  # Adjusted sleep time

        print("\nTarget word '{}' generated!".format(target_word))
        print("It took {} letters to form the target word.".format(len(generated_word)))

        choice = input("Do you want to enter another word? (yes/no): ").lower()
        if choice != "yes":
            break

def generate_substring(target_word, current_length):
    # Generate a substring of the target word
    return target_word[current_length:min(current_length + 10, len(target_word))]

def loading_animation(dots):
    if len(dots) < 3:
        dots += '.'
    else:
        dots = ''
    return dots

if __name__ == "__main__":
    main()
