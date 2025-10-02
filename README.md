# COMP 163 – Assignment 5


### Why I used each loop
- **Challenge 1 (Collatz / while):** I went with a `while` because I don’t know ahead of time how many steps it takes to reach 1. The loop just keeps going until the condition is met.  
- **Challenge 2 (Prime / for):** A `for` loop made sense here since I know exactly what numbers I need to test (2 through n-1). It’s a set range.  
- **Challenge 3 (Table / nested loops):** The table is basically rows and columns, so I needed two loops. The outer loop handles rows, and the inner loop handles each column in that row.  

### How it works (quick rundown)
- **Collatz:** Start with the given number. If it’s even, cut it in half; if it’s odd, do `3n + 1`. Keep repeating until the number becomes 1, and count how many steps it took.  
- **Prime check:** Test every number from 2 up to n-1. If any divide evenly, then the number isn’t prime. If none do, then it’s prime.  
- **Table:** First print the header row (1 through 10). Then loop through rows 1–10, and for each row, multiply it by every column number. The formatting keeps it lined up like a grid.  

### AI help
I used AI to help me with formatting the code and README so it looked cleaner, but I made sure the logic and final code worked the way I wanted.  

python3 BryantClarke_assignment_5.py
