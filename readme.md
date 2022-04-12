# wordle
A command-line clone of Wordle

Answers are five letters long and six guesses are allowed.

Since this is command-line based the clues aren't coloured. A dot means the letter isn't there, a tilda means it is there but has been misplaced and the letter itself means it has been placed correctly.

The word list is an expanded version of the SOWPODS dictionary, ordered by the frequency of the word's usage. Words that are less frequently used than an arbitrary cutoff point (the OBSCURITY_THRESHOLD variable) are accepted as guesses but won't be given as correct answers.
