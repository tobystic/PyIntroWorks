(reg(ex|ular\sexpressions?)) | (dd[0-9][0-9]) | 


regex
regular
regular expression


boundary
-----------
\b (for boundary - use both open and close. e,g if I want the first occurence of letter a alone \ba\b)  


negation
----------
^ to negate a single character or range e.g [a-d]lip will match clip and [^a-d] will not match clip but match flip  


anchor
-------
? use this to check occurence e.g flavou?r wil match flavour and flavour  


digit
------
\d will match digits e.g. \d{4} will match for four digits
\b\d{4}\b  will match four digits only and not other numbers that have more than four
/ \d{2,5} / will match a min of 2 digits and max of 5  


Alternation
-----------
/ I\slike\s(java|python) will match I like Java and also match I like Python

Or situation
(car|truck|bus|airplane|rocket)

I\slike\s(java|python\.com)+new will match I like python.comnew  


Multiple condition sample
-------------------------
((http|https):\/\/)(www.)?(ab\.com|test\.com|jwt\.ms)
this will search for any of the URIs in the list
