# -*- coding: utf-8 -*-
# __author__ = 'WangChaoWei'
# __date__ = '2019/8/16 10:50'

from flask import Flask, url_for, redirect,request
from flask import render_template

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

app = Flask(__name__)

f1 = open('zhengxiang.txt', 'r')
lines = f1.readlines()
counts = len(lines)
lines = iter(lines)
next_line = ""
f1.close()
f2 = open('zhengxiang_true.txt', 'a+')
f3 = open('zhengxiang_false.txt', 'a+')

@app.route('/')
def index():
    global next_line
    if next_line == "":
        next_line = lines.next()
        next_line.decode("utf-8")

    return render_template('index.html', line=next_line, counts=counts)

@app.route('/true')
def true():
    line = request.args.get('line', '')
    f2.write(line)
    f2.flush()
    global counts
    counts -= 1
    global next_line
    next_line = ""
    return redirect(url_for('index'))


@app.route('/false')
def false():
    line = request.args.get('line', '')
    f3.write(line)
    f3.flush()
    global counts
    counts -= 1
    global next_line
    next_line = ""
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')