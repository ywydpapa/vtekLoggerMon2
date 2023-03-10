import json
from flask import Flask, jsonify, request, render_template, redirect , session

import dbconn
from dbconn import selectUsers
import pymysql
import datetime
import os
import psutil


db=None
cur=None
app = Flask(__name__)
app.secret_key = 'fsdfsfgsfdg3234'

@app.route('/')
def home():
    return render_template('./login/login.html')

@app.route('/subm/mnujson', methods=['GET'])
def mnujson():
    curr = datetime.datetime.now()
    datfr = ''
    datto = ''
    draw = request.args.get("draw")
    pageLength = request.args.get("length")
    
    if(request.args.get("whereplus") != None):
        wherecon = request.args.get("whereplus")
    else:
        wherecon = ''
    if datfr == '':
        datfr = curr - datetime.timedelta(minutes=5)
        datfr = datfr.strftime('%Y-%m-%d %H:%M')
    if datto == '':
        datto = curr.strftime('%Y-%m-%d %H:%M')
    resultlength = dbconn.fromtoTraffic(datfr, datto, str(wherecon))
    result = dbconn.fromtoTrafficLimit(datfr, datto, str(wherecon), draw, pageLength)
    resultData = {
        "data": result,
        "recordsTotal": len(resultlength),
        "recordsFiltered": len(resultlength),
    }
    return jsonify(resultData)

@app.route('/subm/mnu001', methods=['GET', 'POST'])
def mnu001f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        result = dbconn.fromtoTraffic(datfr, datto, str(wherecon))
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu001.html', result = result, cond = cond)
    else:
        datfr = ''
        datto = ''
        wherecon = ''
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        result = dbconn.fromtoTraffic(datfr, datto, str(wherecon))
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu001.html", result = result, cond = cond)

@app.route('/subm/mnu002', methods=['GET', 'POST'])
def mnu002f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu002.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu002.html", result = result, cond = cond)
    
@app.route('/subm/mnu003', methods=['GET', 'POST'])
def mnu003f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu003.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu003.html", result = result, cond = cond)
    
@app.route('/subm/mnu004', methods=['GET', 'POST'])
def mnu004f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu004.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu004.html", result = result, cond = cond)
    
@app.route('/subm/mnu005', methods=['GET', 'POST'])
def mnu005f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu005.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu005.html", result = result, cond = cond)
    
@app.route('/subm/mnu006', methods=['GET', 'POST'])
def mnu006f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu006.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu006.html", result = result, cond = cond)
    
@app.route('/subm/mnu007', methods=['GET', 'POST'])
def mnu007f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu007.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu007.html", result = result, cond = cond)
    
@app.route('/subm/mnu008', methods=['GET', 'POST'])
def mnu008f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu008.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu008.html", result = result, cond = cond)
    
@app.route('/subm/mnu009', methods=['GET', 'POST'])
def mnu009f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu009.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu009.html", result = result, cond = cond)
    
@app.route('/subm/mnu010', methods=['GET', 'POST'])
def mnu010f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu010.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu010.html", result = result, cond = cond)
    
@app.route('/subm/mnu011', methods=['GET', 'POST'])
def mnu011f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu011.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu011.html", result = result, cond = cond)
    
@app.route('/subm/mnu012', methods=['GET', 'POST'])
def mnu012f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu012.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu012.html", result = result, cond = cond)
    
@app.route('/subm/mnu013', methods=['GET', 'POST'])
def mnu013f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu013.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu013.html", result = result, cond = cond)
    
@app.route('/subm/mnu014', methods=['GET', 'POST'])
def mnu014f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu014.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu014.html", result = result, cond = cond)
    
@app.route('/subm/mnu015', methods=['GET', 'POST'])
def mnu015f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu015.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu015.html", result = result, cond = cond)

@app.route('/subm/mnu016', methods=['GET', 'POST'])
def mnu016f():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./subm/mnu016.html', result = result, cond = cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=5)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr,datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu016.html", result = result, cond = cond)

@app.route('/subm/cpu')  # ??????
def cpustat():
    pid = os.getpid()
    py = psutil.Process(pid)
    cpu_usage = os.popen("ps aux | grep " + str(pid) + " | grep -v grep | awk '{print $3}'").read()
    cpu_usage = cpu_usage.replace("\n", "")
    memory_usage = round(py.memory_info()[0] / 2. ** 30, 2)
    return render_template("stat/dashcpu.html", result_cpu = cpu_usage,result_mem = memory_usage )
@app.route('/subm/disk')  # ??????
def diskstat():
    result_disk = psutil.disk_usage(os.getcwd())
    return render_template("stat/dashdisk.html", result=result_disk)

@app.route('/subm/network')  # ??????
def networkstat():
    db = pymysql.connect(host='192.168.1.45', user='swcore', password='core2020', db='logger', charset='utf8')
    cur = db.cursor()
    sql = "select * from hBefore order by d002 desc limit 200"
    cur.execute(sql)
    result = cur.fetchall()
    db.close()
    return render_template("stat/dashnetwork.html", result=result)

@app.route('/monmain', methods=['GET','POST'])  # ??????
def okhome():
    curr = datetime.datetime.now()
    if request.method == 'GET':
        datfr = ''
        datto = ''
        wherecon = ''
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=2)
            datfr = datfr.strftime('%Y-%m-%d %H:%M')
        if datto == '':
            datto = curr.strftime('%Y-%m-%d %H:%M')
        print(datfr)
        print(datto)
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template('./stat/indexStart.html', result=result, cond=cond)
    else:
        datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
        datto = request.form.get('dateto') + " " + request.form.get('timeto')
        wherecon = request.form.get('whereplus')
        if wherecon != '':
            wherecon = wherecon
        if datfr == '':
            datfr = curr - datetime.timedelta(minutes=2)
        if datto == '':
            datto = curr
        print(wherecon)
        result = dbconn.fromtoTraffic(datfr, datto, wherecon)
        cond = dbconn.menuSet("TRAF")
        return render_template("./stat/indexStart.html", result=result, cond=cond)
@app.route('/menuset')
def menuset():

    db = pymysql.connect(host='192.168.1.45', user='swcore', password='core2020', db='logger', charset='utf8')
    cur = db.cursor()
    sql1 = "select activeMenu,menuTitle,useYN,sortCust from menuCustom where menuNo = 'TRAF' and attrib not like '%XXX%'"
    cur.execute(sql1)
    cond = cur.fetchall()
    db.close()
    return render_template("menu/menuAdmin.html", cond=cond)

@app.route('/updatemenu', methods=['GET','POST'])
def updatemenu():
    formtotal = request.form
    db = pymysql.connect(host='192.168.1.45', user='swcore', password='core2020', db='logger', charset='utf8')
    cur = db.cursor()
    mtitles = formtotal.getlist('mtitle')
    mkeys = formtotal.getlist('mkey')
    muses = formtotal.getlist('muse')
    msorts = formtotal.getlist('msort')
    for i in range(len(mkeys)):
        val01 = mtitles[i]
        val02 = muses[i]
        val03 = msorts[i]
        val04 = mkeys[i]
        sql1 = "update menuCustom set menuTitle = %s , useYN = %s , sortCust = %s where menuNo = 'TRAF' and activeMenu = %s"
        cur.execute(sql1, (val01, val02, val03, val04))
    db.commit()
    sql2 = "select activeMenu,menuTitle,useYN,sortCust from menuCustom where menuNo = 'TRAF' and attrib not like '%XXX%'"
    cur.execute(sql2)
    cond = cur.fetchall()
    db.close()
    return render_template("menu/menuAdmin.html", cond=cond)

@app.route('/dashmain')  # ??????
def searchSel():
    db = pymysql.connect(host='192.168.1.45', user='swcore', password='core2020', db='logger', charset='utf8')
    cur = db.cursor()
    sql = "select * from dayservice"
    cur.execute(sql)
    result_service = cur.fetchall()
    sql = "select * from areafrom"
    cur.execute(sql)
    result_area = cur.fetchall()
    db.close()
    return render_template("stat/dashinit.html", result=result_service, area = result_area)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('./login/login.html')
    else:
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        row = selectUsers(uid, upw)
        if row:
            session['userNo'] = row['userNo']
            session['userName'] = row['userName']
            session['userRole'] = row['userRole']
            return redirect('/dashmain')
        else:
            return '''
                <script>
                    // ????????? 
                    alert("????????? ??????, ?????? ???????????????")
                    // ?????????????????? ??????
                    history.back()
                </script>
            '''

@app.route('/logout')
def logout():
    session.clear()
    return render_template('./login/login.html')

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
