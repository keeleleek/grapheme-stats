# Simple grapheme statistics of text files

This is a simple Python program that reads a text file and outputs csv table with statistics of all graphemes encountered in that file.

It is meant for debugging different kinds of problems.

Graphemes are composed characters that can consist of one or more characters. For example the grapheme `õ` can be represented both as
`LATIN SMALL LETTER O WITH TILDE`
and
`LATIN SMALL LETTER O + COMBINING TILDE`.

## Output statistics

The output statistics file include the grapheme, count, number of codepoints, names of the codepoints. Here is an example output table which could be used for finding problems of double representations of the grapheme `õ`.

| grapheme | count | number of codepoints | codepoint names |
| --- | --- | --- | --- |
| õ | 3 | 1 | LATIN SMALL LETTER O WITH TILDE |
| õ | 1 | 2 | LATIN SMALL LETTER O; COMBINING TILDE |


## Usage

Run the program with the command `python grapheme-stats.py filename.txt`.
