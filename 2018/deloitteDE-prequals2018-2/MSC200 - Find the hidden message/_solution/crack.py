f = open("out.txt","r")
text = f.readline().strip()
words = text.split(" ")
out = ""
for word in words:
	out += word[0]

out = out.replace("zero","0")
out = out.replace("one","1")
out = out.replace("two","2")
out = out.replace("three","3")
out = out.replace("five","5")
out = out.replace("seven","7")
out = out.replace("nine","9")
out = out.replace("openbracket","{")
out = out.replace("closebracket","}")
out = out.replace("space"," ")
print(out)
