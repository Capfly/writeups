This challenge is about strings and numbers conversion in PHP.
At least the following values will work to represent the required number (and the length=5 constraint):
`02432` (we add a leading zero, note that it is not converted to Octal, because we convert from a STRING!)
`2432.` (we use a dot to get a length of 5 and the resulting float is valid as numeric type)
`+2432` (the + is a hidden, but valid character for numbers, we can use that, too)

We enter those values (?x=02432&y=2432.&z=+2432) and get the following output: CTF{c571e25978f76ee76da39af146c32314}