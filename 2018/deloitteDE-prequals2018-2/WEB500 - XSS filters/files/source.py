from flask import Flask, request, Response, make_response, url_for
import string
import subprocess
import os
import re
import cgi
import urllib
flags = open('secret.txt').read().split()

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def index():
    return """<html><body>Solve various XSS challenges to gain points.<br>
        For each of these challenges try to trigger and alert with the string 'XSS' to prove you were able to inject script code<p>
        <table>
        <tr><th>Challenge</th><th>Points</th></tr>
        <tr><td><a href="xss1?name=hacker">XSS1</a></td><td>100</td></tr>
        <tr><td><a href="xss2?name=hacker">XSS2</a></td><td>100</td></tr>
        <tr><td><a href="xss3?name=hacker">XSS3</a></td><td>100</td></tr>
        <tr><td><a href="xss4">XSS4</a></td><td>100</td></tr>
        <tr><td><a href="xss5?name=hacker">XSS5</a></td><td>100</td></tr>
        </table>

        <p>We believe in Kerckhoff's principle so we provide the <a href="source">full source code</a><p>

        </body></html>"""

# Checks if you did a succesful injection using phantomjs this should not be what you attack, hopefully it's secure ;)
def check_xss(page,flag):
    proc = subprocess.Popen(["timeout","5","phantomjs", "check.js"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    fn = "static/" + os.urandom(16).encode('hex') + '.html'
    url = 'http://localhost/' + fn
    try:
        of = open(fn, 'w')
        of.write(page)
        of.close()
        proc.stdin.write(url)
        proc.stdin.close()
        result = proc.stdout.readline().strip()
    finally:
        os.unlink(fn)
    if result == 'XSS':
        data = '<br>Nice you triggered the right alert!<p>Have a flag as a reward: %s' % flag
    elif result:
        data = '<br>Seems like you did an alert with %s instead of XSS' % (cgi.escape(result))
    else:
        data = "<br>Doesn't seem you triggered an alert at all, try harder..."
    return data

@app.route('/xss1')
def xss1():
    msg = request.args.get('name','')
    msg = re.sub(r"""<[a-z/]""", "", msg, flags=re.IGNORECASE) # Remove HTML tags, i.e. everything starts with < followed by a-z or /
    msg = re.sub(r"""["']XSS["']""", "", msg, flags=re.IGNORECASE) # Remove the string "XSS" to make it a bit harder
    data = "Hello %s" % msg
    data += check_xss(data,flags[0])
    return data

@app.route('/xss2')
def xss2():
    msg = request.args.get('name','')
    blacklist = ['<', '>', '(',')']
    for word in blacklist:
        if word in msg.lower():
            return "Sorry you can't use %s" % word
    data = "<img src='%s'>" % msg
    data += check_xss(data,flags[1])
    response = make_response(data)
    response.headers["X-XSS-Protection"] = "0"
    return response

@app.route('/xss3')
def xss3():
    msg = request.args.get('name','')
    blacklist = ['script', 'on', 'style','(',')',"'"]
    for word in blacklist:
        if word in msg.lower():
            return "Sorry you can't use %s" % word
    data = """<form><input type=text name=name value="Hello %s"></form>""" % msg
    data += check_xss(data,flags[2])
    response = make_response(data)
    response.headers["X-XSS-Protection"] = "0"
    return response

@app.route('/xss4',methods=['GET', 'POST'])
def xss4():
    msg = request.form.get('name','')
    blacklist = string.lowercase + string.uppercase + string.digits + '<>'
    for word in blacklist:
        if word in msg:
            return "Sorry you can't use %s" % word
    data = "<form method=post><textarea name=name cols=50 rows=20></textarea><br><input type=submit></form>"
    data += """<script>name = "%s"; document.write('Hello '+name);</script>""" % msg
    data += check_xss(data,flags[3])
    response = make_response(data)
    response.headers["X-XSS-Protection"] = "0"
    return response

@app.route('/xss5')
def xss5():
    msg = request.args.get('name','')
    blacklist = "<>'" + string.uppercase
    for word in blacklist:
        if word in msg:
            return "Sorry you can't use %s" % word
    msg = msg.replace('"',r'\"')
    data = """<script>name = "%s"; document.write('Hello '+name);</script>""" % msg
    data += check_xss(data,flags[4])
    response = make_response(data)
    response.headers["X-XSS-Protection"] = "0"
    return response


@app.route('/source')
def source():
    s = open('chall.py').read()
    return Response(s,mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
