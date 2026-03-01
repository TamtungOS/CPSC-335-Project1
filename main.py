# Main.py script to execute the two algorithms
# Hector Mojica Arevalo
# Cj Rinaldi
# Project 1
import Algorithm1 as algo1
import Algorithm2 as algo2

def main():
    while True:
        print(f"""
Menu:
    1: Connecting Pairs of Persons
    2: Greedy Approach to Hamiltonian Problem
    3: Exit
            """)
        selection = int(input("Please make a selection from the menu: "))

        match selection:
            case 1: algo1.sort_couples()
            case 2: algo2.find_starting_city()
            case 3: break
            case _: print("Invalid Selection, please try again")

if __name__ == "__main__":
    main()