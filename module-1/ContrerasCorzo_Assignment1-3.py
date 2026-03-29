# Name: Fernando Contreras Corzo
# Date: March 28, 2026
# Assignment: Module 1.3 - On the Wall

# Purpose: This program takes a user-defined number of bottles and counts down 
# the "Bottles of Beer" song lyrics using a custom function and loop.

def manage_beer_countdown(starting_bottles):
    """
    Takes an integer input and prints the song lyrics counting down to 1.
    Handles the grammar change from 'bottles' to 'bottle' for the final verse.
    """
    current_count = starting_bottles

    # Loop through the bottles until we hit zero
    while current_count > 0:
        if current_count > 1:
            # Standard verse for multiple bottles
            print(f"{current_count} bottles of beer on the wall, {current_count} bottles of beer.")
            
            # Look ahead to see if the next number needs singular or plural grammar
            next_count = current_count - 1
            word = "bottle" if next_count == 1 else "bottles"
            
            print(f"Take one down, pass it around, {next_count} {word} of beer on the wall.")
        else:
            # Special verse for the very last bottle
            print(f"{current_count} bottle of beer on the wall, {current_count} bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall!")
        
        # Print a blank line between verses for readability
        print()
        current_count -= 1


def main():
    """
    Main execution block: Handles user input and final program output.
    """
    # Ask the user for the starting number
    user_input = input("How many bottles of beer are on the wall? ")

    # Validate that the input is a number
    try:
        initial_bottles = int(user_input)

        if initial_bottles > 0:
            # Execute the countdown function
            manage_beer_countdown(initial_bottles)

            # Final reminder after returning from the function
            print("The wall is empty! Go buy more beer.")
        else:
            print("Please enter a number greater than 0 to start the song.")

    except ValueError:
        print("Error: Please enter a valid whole number.")

if __name__ == "__main__":
    main()