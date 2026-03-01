## CJ Rinaldi & Hector Arevalo
## Algorithm 1: Greedy Algorithm

n = int(input("Enter number of couples: "))

arrangement = input("Enter seating arrangement (Ex. 0 2 1 3): ")

swaps = 0 ## Initialize the number of swaps to 0

row = arrangement.split() ## Splits the string into a list of strings
for i in range(len(row)):
    row[i] = int(row[i]) ## Converts list of strings into list of integers
            
for i in range(0, 2*n, 2): ## Loop through this list in steps of 2, starting from index 0
    start = row[i]
    if start % 2 == 0: ## If starting number is even, then the partner is the next number
        partner = start+1 
    else:
        partner = start-1 ## If starting number is odd, then the partner is the previous number
        
    if row[i + 1] == partner: ## If partners are already sitting next to each other, continue
        continue
    
    for j in range(i+2, 2*n): ## Loop through rest of list to find partner
        if row[j] == partner: ## If partner is found, swap numbers
            temp = row[i+1] ## Store number at i+1 in temp
            row[i+1] = row[j] ## Swap number at j with its partner at index i+1
            row[j] = temp ## Swap number in temp with j
            swaps = swaps + 1 ## Increment number of swaps by 1
            break
        
print(f"\nAfter {swaps}(s): {row}") ## Print final arrangement and number of swaps


