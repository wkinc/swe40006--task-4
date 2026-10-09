import random
import sys

STUDENT = "BUILT BY CHUA WENG KIN - 106214072"



# Temp conversion (from Celsius to Fahrenheit, vice versa)
def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


def temperature_converter():
    while True:
        print("\n--- Temperature Converter ---")
        print("1) Celsius to Fahrenheit")
        print("2) Fahrenheit to Celsius")
        print("3) Back to main menu")
        choice = input("Choose 1-3: ").strip()

        if choice == "3":
            break
        elif choice in ("1", "2"):
            try:
                value = float(input("Enter the temperature: "))
            except ValueError:
                print("Error: please enter a number.")
                continue
            if choice == "1":
                print(f"{value} C = {c_to_f(value):.1f} F")
            else:
                print(f"{value} F = {f_to_c(value):.1f} C")
        else:
            print("Error: please choose 1, 2 or 3.")


# Guess the number game
def guessing_game():
    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number from 1 to 100.")
    secret = random.randint(1, 100)
    tries = 0
    while True:
        guess = input("Your guess (or 'q' to give up): ").strip()
        if guess.lower() == "q":
            print(f"The number was {secret}.")
            break
        try:
            guess = int(guess)
        except ValueError:
            print("Error: please enter a whole number.")
            continue
        if guess < 1 or guess > 100:
            print("Error: the number must be from 1 to 100.")
            continue
        tries += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You found it in {tries} tries.")
            break


#Count the amount of words you pasted in
def word_counter():
    print("\n--- Word Counter ---")
    text = input("Type or paste your text: ").strip()
    if not text:
        print("Error: the text is empty.")
        return

    words = text.split()
    clean = [w.strip(".,!?;:\"'()").lower() for w in words]
    clean = [w for w in clean if w]

    counts = {}
    for w in clean:
        counts[w] = counts.get(w, 0) + 1

    print(f"Words: {len(words)}")
    print(f"Characters (with spaces): {len(text)}")
    print(f"Characters (no spaces): {len(text.replace(' ', ''))}")
    print(f"Different words: {len(counts)}")

    top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Most common words:")
    for word, num in top:
        print(f"  {word}: {num}")


#demo (docker run --name cli-demo wkin/cli-app:1.0)
def demo():
    print("Multi-Tool App (demo mode)")
    print(STUDENT)

    print("\nTemperature examples:")
    print(f"100 C = {c_to_f(100):.1f} F")
    print(f"32 F = {f_to_c(32):.1f} C")

    print("\nWord counter example:")
    sample = "docker makes deployment easy and docker is fun"
    print(f'Text: "{sample}"')
    print(f"Words: {len(sample.split())}")

    print("\nGuessing game example:")
    print("Secret number is picked from 1 to 100 (play it in interactive mode).")
    print("Done.")

# main menu for navigation
def main_menu():
    print("=== Multi-Tool App ===")
    print(STUDENT)
    while True:
        print("\n--- Main Menu ---")
        print("1) Temperature Converter")
        print("2) Number Guessing Game")
        print("3) Word Counter")
        print("4) Quit")
        choice = input("Choose 1-4: ").strip()

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            guessing_game()
        elif choice == "3":
            word_counter()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    if sys.stdin.isatty():
        main_menu()
    else:
        demo()