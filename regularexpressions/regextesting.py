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

/(?=at)./g ?= is a positive look ahead, anything before at counts.
/.(?!at)/g ?! is everything NOT ahead of at.

\d is digits

/\d{3}[ -]?\d{3}[ -]?\d{4}/gm - multiline search that could be used to get phone numbers with no, spaces or - delimiters

/(\d{3})[ -]?(\d{3})[ -]?(\d{4})/gm - parenthesis would capture what is in () and ignore the rest.

Doing a replace with $1$2$3 would take each group and put them one after another.

Group Naming:
/(?<areacode>\d{3})[ -]?(\d{3})[ -]?(\d{4})/gm

$areacode would pull the first group now called areacode in find and replace

/(?:(\+1)[] -])?(?<areacode>\d{3})[ -]?(\d{3})[ -]?(\d{4})/gm - the ?: would not capture



For my purposes I want everything after G
/(?<=G)./g would get the blank space after G, for instance.

/(?<=G)(.+-?.?\d{1,4}).?:(lb)/
$weight

without the lbs:
/(?<=G\s+)(?<weight>-?\s?\d{1,4})(?=\slb)/
"""

# What i'll need to pull forklift data at work: /(?<=G\s+)-?\s?[\d]{1,4}.lb/
#is just the first match. I need to find a way for it to pull the last match.


print('\n'+'Hello World'+'\n')
