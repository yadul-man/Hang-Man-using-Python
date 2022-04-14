# Hang-Man-using-Python

This is a simple python project that uses Python to allow a user to play the game Hang Man.
It is a game of guessing the letters of a random word until all lives are over.

Logic:
<ol>
  <li> Program chooses a random word </li>
  <li> User enters a letter </li>
  <li> Letter is checked for occurence in string </li>
  <li> If found, user can proceed guessing </li>
  <li> Else total no. of lives is decreased </li>
</ol>

Correct guess:

```
ossified

Word: --------
Guess a letter (press - to exit): o

Correct guess.
Remaining lives: 6

Word: o-------
Guess a letter (press - to exit): i

Correct guess.
Letter already guessed. Try again.
Remaining lives: 6

Word: o--i-i--
Guess a letter (press - to exit): s

Correct guess.
Letter already guessed. Try again.
Remaining lives: 6

Word: ossi-i--
Guess a letter (press - to exit): d

Correct guess.
Letter already guessed. Try again.
Remaining lives: 6

Word: ossi-i-d
Guess a letter (press - to exit): f

Correct guess.
Letter already guessed. Try again.

Word: ossifi-d
Guess a letter (press - to exit): e

Correct guess.
Word successfully guessed.
```

Incorrect guess:

```
furry

Word: -----
Guess a letter (press - to exit): a
Incorrect guess.
Remaining lives: 5

Word: -----
Guess a letter (press - to exit): r

Correct guess.
Letter already guessed. Try again.
Remaining lives: 5

Word: --rr-
Guess a letter (press - to exit): d
Incorrect guess.
Remaining lives: 4

Word: --rr-
Guess a letter (press - to exit): c
Incorrect guess.
Remaining lives: 3

Word: --rr-
Guess a letter (press - to exit): m
Incorrect guess.
Remaining lives: 2

Word: --rr-
Guess a letter (press - to exit): p
Incorrect guess.
Remaining lives: 1

Word: --rr-
Guess a letter (press - to exit): l
Incorrect guess.
Game over.
```

