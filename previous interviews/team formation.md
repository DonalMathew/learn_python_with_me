![[Pasted image 20241205185500.png]]

```python
def max_teams(n, m):
    max_teams = 0
    
    # Iterate through possible numbers of experienced players in the team
    for exp in range(1, 4):  # exp can be 1, 2, or 3
        fresh = 4 - exp      # Calculate the corresponding number of freshers
        
        # Check if we can form a team with this distribution
        if n >= exp and m >= fresh:
            # Calculate how many teams can be formed with this distribution
            teams = min(n // exp, m // fresh)
            max_teams += teams
            
            # Update remaining players after forming teams
            n -= teams * exp
            m -= teams * fresh
            
    return max_teams

# Example usage
n = int(input("Enter the number of experienced players: "))
m = int(input("Enter the number of freshers: "))
result = max_teams(n, m)
print("Maximum number of teams that can be formed:", result)

```