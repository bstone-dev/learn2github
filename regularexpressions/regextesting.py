"""
 awesome website! https://regexr.com/
regex is a way to search through a string of text
regex is defined between forward slashes, like this: /cat/g

expression flags:
the "g" after /cat/ is a global search. It tries matching everything / all.
without G it just matches the first one.
"i" will be case insensitive

/e/g matches one e
/e+/g matches one or more e
/e+a?/g ? makes the thing optional. a? is effectively optional, so this is all "e" and all "ea"
/ea*/g * match 0 or more. In this example it would match any e, or ea. * is like ? and + combined
/.at/g . is a wildcard. It matches anything at all except a new line.
/t../g would match t and any two other characters, but not a new line.
/\./g \ cancels out anything after it. \. matches any periods. .\. would match anything and then a period.
/\w/g \w matches any character \W matches any not character
/\s/g \s matches any space, \S is any not space
/\w{4}/g matches any four digit long or more words. /\w\{4,5}/ would match any word between 4 and 5 characters.
/[fc]at/g [fc] matches any of the two characters. [A-Z] would be any capital letters. [a-z] would be any lower case characters
/[a-zA-Z]at/g would include either of the ranges so all lower and upper characters ending in at.
/(t|T)/g | is like an or, so match lowercase t or uppercase T
/(t|T)he/g would give you anything which is The or the.
/t|The/g would give you either t or The
/(t|T){2,3}he/g will match 2 to 3 of the preceeding character group.
/(a|r|t){2,3}) would match at, art, tar etc.
/re{2,3}/ would only match ree or re, as the bracket only affects the preceeding thing unless it's in ()
/^T/g ^ matches just the first character in a line.
/^T/gm the m expression makes it multiline, so all Ts that are the first character in a line would match.
$ matches the end of a statement. /\.$/g would match the period at the end of a line.

/(?<=[tT]he)./g ?<= is a positive look behind. It matches after a pattern. 
So whatever is defined after the = within the () will count

For my purposes I want everything after G
/(?<=G)./g would get the blank space after G, for instance.

/(?<=G).+-?.?[0-9]{1,4}.lb/


"""

# What i'll need to pull forklift data at work: /(?<=G\s+)-?\s?[0-9]{1,4}.lb/


print('\n'+'Hello World'+'\n')
