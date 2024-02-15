import random

def main():
    while True:
        target_word = input("Enter the target word: ").lower()
        generated_word = ""

        while target_word not in generated_word:
            generated_word += random.choice('abcdefghijklmnopqrstuvwxyz')

        print("Target word '{}' generated!".format(target_word))
        print("It took {} letters to form the target word.".format(len(generated_word)))

        choice = input("Do you want to enter another word? (yes/no): ").lower()
        if choice != "yes":
            break

if __name__ == "__main__":
    main()
