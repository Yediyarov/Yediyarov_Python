## Task 1

#### How to Run

1. Make sure you have Python 3 installed.
2. Clone or download this repository.
3. Run the script from your terminal:

```bash
python3 main.py
```

Follow the prompts to:

- Enter a number → prints "Hello" if greater than 7
- Enter a name → prints "Hello, John" if name is John, otherwise "There is no such name"
- Enter a list of integers → prints the elements that are multiples of 3

#### Example Run

```
Enter a number: 9
Hello
Enter a name: John
Hello, John
Enter integers separated by commas (e.g., 1,3,6,8,9,12): 1,3,6,8,9,12
Multiples of 3: [3, 6, 9, 12]
```

## Task 2 – Bracket Sequence Analysis
Given sequence: [((())()(())]]
Is it correct?

Original:
```[ ( ( ( ) ) ( ) ( ( ) ) ] ]```

Positions (1-indexed):
```1:[ 2:( 3:( 4:( 5:) 6:) 7:( 8:) 9:( 10:( 11:) 12:) 13:] 14:]```

Balanced brackets must:
- Have matching opening and closing brackets
- Be closed in the correct order

#### Final answer
Is the given sequence correct? No.


Minimal one-char fixes that work:

```
[((())()(()))] ← change pos13 ] → )

[[((())()(())]] ← change pos2 ( → [
```
