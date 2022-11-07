https://docs.google.com/document/d/1T_jdKenPBNGxwpshCwQiQqJpl8Sp_lSXuTGVjUHRBBo/edit?usp=sharing

> Create a program that outputs every combination of five 5 letter words. You must use 25 letters in the alphabet with no repeats.

## How I approach this problem

Looping over every word in the dictionary n^5 times will be slow.

Finding the least common words and starting there should be faster.

What are the most common letters? Why does this matter?

---

On second thought, I'm going to analyze existing code written by a data scientist, then make it readable.