# Regex Cheat Sheet

## Matching Characters/Digits

| Metacharacter | Match                                                                       |
| ------------- | --------------------------------------------------------------------------- |
| `.`           | Match **any** character (letter, digit, whitespace, everything).            |
| `\d`          | Match any digit from **0-9**.                                               |
| `\D`          | Match any character that's **not** a digit.                                 |
| `\w`          | Match **any letter** or **underscore** - equivalent to `[a-zA-Z_]`          |
| `\W`          | Match **any non-letter** or **underscore** - equivalent to `[^a-zA-Z_]`     |
| `[ ]`         | `[abc]` will match a **single** a,b or c letter                             |
| `^`           | Exclude the character inside `[ ]`. `[^a]` will exclude the letter a.       |
| `{ }`         | Match a specific repetition `.{2,6}` will match 2-6 of **any** character    |
| `+`           | Match any expression **1 or more** times. `[abc]+` (1 or more of any a,b,c) |
| `*`           | Match any expression **0 or more** times. `.*` (0 or more of **any** char)  |
| `?`           | Optional character. `files?` will match **file** and **files**.             |
| `\s`          | Match any whitespace, **space**`..` **tab**`\t` **newline**`(\n)`, etc.     |
| `\S`          | Match any non-whitespace character                                          |
| `^`           | Match a line that **begins** with expression ex. `^Mission`                 |
| `$`           | Match a line that **ends** with expression ex. `success$`                   |
| `( )`         | Capture Group - allows you to capture groups of characters                  |

## Escaping

To escape a "reserved" character, put a backslash in front of the character to match said character:

```
\\  Match slash
\.  Match period
```

## Example

```
function validateEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}
```
