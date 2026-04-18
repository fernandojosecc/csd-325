"""
sitka_high_low_fc.py
Author: Fernando Contreras
Assignment: CSD-325 Module 4
Description: Reads Sitka weather data and displays a menu allowing the user
             to plot daily high temps (red), daily low temps (blue), or exit.
             The program loops until the user chooses to exit.
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


FILENAME = 'sitka_weather_2018_simple.csv'


def load_weather_data():
    """Read the CSV and return lists of dates, highs, and lows."""
    dates, highs, lows = [], [], []

    with open(FILENAME, newline='') as f:
        reader = csv.DictReader(f)  # Use DictReader to access columns by name

        for row in reader:
            current_date = datetime.strptime(row['DATE'].strip(), '%Y-%m-%d')
            dates.append(current_date)
            highs.append(int(row['TMAX'].strip()))
            lows.append(int(row['TMIN'].strip()))

    return dates, highs, lows


def plot_highs(dates, highs):
    """Plot daily high temperatures in red."""
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    plt.title("Daily High Temperatures - Sitka, AK 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def plot_lows(dates, lows):
    """Plot daily low temperatures in blue."""
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    plt.title("Daily Low Temperatures - Sitka, AK 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def display_menu():
    """Print the menu options to the screen."""
    print("\n--- Sitka Weather 2018 ---")
    print("H - View High Temperatures")
    print("L - View Low Temperatures")
    print("E - Exit")
    print("--------------------------")


def main():
    """Main loop: load data, show menu, handle user input until exit."""
    print("Welcome to the Sitka Weather Viewer!")

    # Load data once before the loop
    dates, highs, lows = load_weather_data()

    while True:
        display_menu()
        choice = input("Enter your choice (H, L, or E): ").strip().upper()

        if choice == 'H':
            plot_highs(dates, highs)
        elif choice == 'L':
            plot_lows(dates, lows)
        elif choice == 'E':
            print("\nThanks for using the Sitka Weather Viewer. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter H, L, or E.")


# Entry point
if __name__ == "__main__":
    main()