 

def get_input(word_type: str, hint: str = "") -> str:
    """Get non-empty user input for a word type with an optional hint."""
    while True:
        user_input = input(f"Enter a {word_type} {hint}: ").strip()
        if user_input:
            return user_input
        print("Please enter a non-empty word!")

def choose_story():
    """Let user pick a story template."""
    print("\nChoose a story:")
    print("1. Epic Adventure")
    print("2. Galactic Voyage")
    choice = input("Enter 1 or 2: ").strip()
    return choice

def generate_story(choice: str, noun1: str, verb1: str, adjective: str, noun2: str, verb2: str):
    """Generate the chosen story with user inputs."""
    if choice == "1":
        story = f"""
In a faraway kingdom, a {adjective} {noun1} loved to {verb1} near the legendary {noun2}.
One day, the {noun1} found the {noun2} in a hidden cave and {verb2} bravely.
"Why did you {verb2}?" asked the {noun2}, amazed.
The {adjective} {noun1} said, "To protect our land!"
They teamed up to {verb1} and became heroes of the kingdom.
        """
    else:  # Default to Sci-Fi
        story = f"""
Aboard a starship, the {adjective} Captain {noun1} planned to {verb1} toward the mysterious {noun2}.
An alien {noun2} appeared and {verb2} with the crew!
"Why did you {verb2}?" asked Captain {noun1}.
"To join your mission!" replied the {noun2}.
They {verb1}ed together, forging a galactic legend.
        """
    return story.strip()

def main():
    """Run the Mini Story Maker game."""
    print("Welcome to Mini Story Maker!")

    while True:
        # Choose story
        choice = choose_story()
        if choice not in ["1", "2"]:
            print("Invalid choice, defaulting to Epic Adventure.")
            choice = "1"

        # Get user inputs
        noun1 = get_input("noun", "(e.g., knight or astronaut)")
        verb1 = get_input("verb", "(present tense, e.g., run or explore)")
        adjective = get_input("adjective", "(e.g., brave or coward)")
        noun2 = get_input("noun", "(e.g., dragon or planet)")
        verb2 = get_input("verb", "(past tense, e.g., fought or explored)")

        # Generate and show story
        story = generate_story(choice, noun1, verb1, adjective, noun2, verb2)
        print("\n=== Your Story ===\n")
        print(story)

        # Replay?
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()