For this tiny challenge, we need to use a wordlist attack.
For that, we can use the nice program fcrackzip and the ___rockyou___ wordlist.

`fcrackzip -u -D -p rockyou.txt challenge.zip`

After a few seconds we got a match!
Password: budweiser

We extract the zip and get a file with the following content:
If you can read this you managed to crack the password of the zip file.

Here is a nice flag for you:
CTF{1aa4c84b1ff9f21ce476ff50c7d0fe74}