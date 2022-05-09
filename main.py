
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./ciphers/index.html')

@app.route('/game')
def game():
    return render_template('./ciphers/game.html')


@app.route('/start')
def start():
    return render_template('./ciphers/s-game.html')

@app.route('/numeric')
def numeric():
    x=0
    return render_template('./numbers/n1.html')

@app.route('/n2',methods=['post'])
def n2():
    answer = request.form['answer']
    if answer == '10100111':
     
        return render_template('./numbers/n2.html')
    else:
        return render_template('./numbers/n1.html')


@app.route('/n3',methods=['post'])
def n3():
    answer = request.form['answer']
    if answer == '21':
     
        return render_template('./numbers/n3.html')
    else:
        return render_template('./numbers/n2.html')


@app.route('/n4',methods=['post'])
def n4():
    answer = request.form['answer']
    if answer == '106':
     
        return render_template('./numbers/n4.html')
    else:
        return render_template('./numbers/n3.html')

@app.route('/n5',methods=['post'])
def n5():
    answer = request.form['answer']
    if answer == '142':
         
        return render_template('./numbers/n5.html')
    else:
        return render_template('./numbers/n4.html')

@app.route('/n6',methods=['post'])
def n6():
    answer = request.form['answer']
    if answer == '200':
        
        return render_template('./numbers/n6.html')
    else:
        return render_template('./numbers/n5.html')

@app.route('/n7',methods=['post'])
def n7():
    answer = request.form['answer']
    if answer == '54945':
         
        return render_template('./numbers/n7.html')
    else:
        return render_template('./numbers/n6.html')

@app.route('/n8',methods=['post'])
def n8():
    answer = request.form['answer']
    if answer == '5.125':
         
        return render_template('./numbers/n8.html')
    else:
        return render_template('./numbers/n7.html')

@app.route('/win',methods=['post'])
def win():
    answer = request.form['answer']
    if answer == '1000000.00101':
         
        return render_template('./ciphers/winner.html')
    else:
        return render_template('./numbers/n8.html')

#security game---------------------------------------------------
@app.route('/sec')
def sec():
    return render_template('./h&s/h1.html')

@app.route('/h2',methods=['post'])
def h2():
    answer = request.form['answer']
    if answer == 'IPv6':
        return render_template('./h&s/h2.html')
    else:
        return render_template('./h&s/h1.html')

@app.route('/h3',methods=['post'])
def h3():
    answer = request.form['answer']
    if answer == 'no':
        return render_template('./h&s/h3.html')
    else:
        return render_template('./h&s/h2.html')


@app.route('/h4',methods=['post'])
def h4():
    answer = request.form['answer']
    if answer == 'router':
        return render_template('./h&s/h4.html')
    else:
        return render_template('./h&s/h3.html')

@app.route('/h5',methods=['post'])
def h5():
    answer = request.form['answer']
    if answer == '2' or answer == '4':
        return render_template('./h&s/h5.html')
    else:
        return render_template('./h&s/h4.html')

@app.route('/h6',methods=['post'])
def h6():
    blank1 = request.form['blank1']

    if blank1 == 'Two-factor authentication (2FA)':
          return render_template('./h&s/h6.html')
    else:
        return render_template('./h&s/h5.html')

@app.route('/win1',methods=['post'])
def win1():
    answer = request.form['answer']
    if answer == 'all layers':
        return render_template('./ciphers/winner.html')
    else:
        return render_template('./h&s/h6.html')

#sniffing-------------------------------------------------------

@app.route('/sniff')
def sniff():
    return render_template('./sniffing/s1.html')

@app.route('/s2',methods=['post'])
def s2():
    answer = request.form['answer']
    if answer == '4':
        return render_template('./sniffing/s2.html')
    else:
        return render_template('./sniffing/s1.html')

@app.route('/s3',methods=['post'])
def ps():
    answer = request.form['answer']
    if answer == 'b':
        return render_template('./sniffing/s3.html')
    else:
        return render_template('./sniffing/s2.html')


@app.route('/s4',methods=['post'])
def s4():
    answer = request.form['answer']
    if answer == 'a':
        return render_template('./sniffing/s4.html')
    else:
        return render_template('./sniffing/s3.html')

@app.route('/s5',methods=['post'])
def s5():
    answer = request.form['answer']
    if answer == 'c':
        return render_template('./sniffing/s5.html')
    else:
        return render_template('./sniffing/s4.html')

@app.route('/s6',methods=['post'])
def s6():
    answer = request.form['answer']
    if answer == 'a':
        return render_template('./sniffing/s6.html')
    else:
        return render_template('./sniffing/s5.html')

@app.route('/win4',methods=['post'])
def win4():
    answer = request.form['answer']
    if answer == 'yes':
        return render_template('./ciphers/winner.html')
    else:
        return render_template('./sniffing/s6.html')

#p&a--------------------------------------------------------------


@app.route('/pa')
def pa():
    return render_template('./p&a/a1.html')

@app.route('/a2',methods=['post'])
def a2():
    answer = request.form['answer']
    if answer == 'firewall':
        return render_template('./p&a/a2.html')
    else:
        return render_template('./p&a/a1.html')

@app.route('/a3',methods=['post'])
def a3():
    answer = request.form['answer']
    if answer == '4':
        return render_template('./p&a/a3.html')
    else:
        return render_template('./p&a/a2.html')


@app.route('/a4',methods=['post'])
def a4():
    answer = request.form['answer']
    if answer == 'active':
        return render_template('./p&a/a4.html')
    else:
        return render_template('./p&a/a3.html')

@app.route('/a5',methods=['post'])
def a5():
    answer = request.form['answer']
    if answer == 'single sign on':
        return render_template('./p&a/a5.html')
    else:
        return render_template('./p&a/a4.html')

@app.route('/a6',methods=['post'])
def a6():
    answer = request.form['answer']
    if answer == 'passive':
        return render_template('./p&a/a6.html')
    else:
        return render_template('./p&a/a5.html')


@app.route('/a7',methods=['post'])
def a7():
    answer = request.form['answer']
    if answer == 'active':
        return render_template('./p&a/a7.html')
    else:
        return render_template('./p&a/a6.html')

@app.route('/a8',methods=['post'])
def a8():
    answer = request.form['answer']
    if answer == 'denial of service':
        return render_template('./p&a/a8.html')
    else:
        return render_template('./p&a/a7.html')

@app.route('/win5',methods=['post'])
def win5():
    answer = request.form['answer']
    if answer == '3':
        return render_template('./ciphers/winner.html')
    else:
        return render_template('./p&a/a8.html')

#phising----------------------------------------------------


@app.route('/phis')
def phis():
    return render_template('./phising/p1.html')

@app.route('/p2',methods=['post'])
def p2():
    answer = request.form['answer']
    if answer == '5':
        return render_template('./phising/p2.html')
    else:
        return render_template('./phising/p1.html')

@app.route('/p3',methods=['post'])
def p3():
    answer = request.form['answer']
    if answer == '1 and 2':
        return render_template('./phising/p3.html')
    else:
        return render_template('./phising/p2.html')


@app.route('/p4',methods=['post'])
def p4():
    answer = request.form['answer']
    if answer == 'b':
        return render_template('./phising/p4.html')
    else:
        return render_template('./phising/p3.html')

@app.route('/p5',methods=['post'])
def p5():
    answer = request.form['answer']
    if answer == '3':
        return render_template('./phising/p5.html')
    else:
        return render_template('./phising/p4.html')

@app.route('/p6',methods=['post'])
def p6():
    answer = request.form['answer']
    if answer == '3':
        return render_template('./phising/p6.html')
    else:
        return render_template('./phising/p5.html')

@app.route('/win3',methods=['post'])
def win3():
    answer = request.form['answer']
    if answer == 'true':
        return render_template('./ciphers/winner.html')
    else:
        return render_template('./phising/p6.html')

#cia-----------------------------------------------------------------------
@app.route('/cia')
def cia():
    return render_template('./cia/c1.html')

@app.route('/c2',methods=['post'])
def c2():
    answer = request.form['answer']
    if answer == 'I':
        return render_template('./cia/c2.html')
    else:
        return render_template('./cia/c1.html')

@app.route('/c3',methods=['post'])
def c3():
    answer = request.form['answer']
    if answer == 'A':
        return render_template('./cia/c3.html')
    else:
        return render_template('./cia/c2.html')


@app.route('/c4',methods=['post'])
def c4():
    answer = request.form['answer']
    if answer == 'true':
        return render_template('./cia/c4.html')
    else:
        return render_template('./cia/c3.html')

@app.route('/c5',methods=['post'])
def c5():
    answer = request.form['answer']
    if answer == '2':
        return render_template('./cia/c5.html')
    else:
        return render_template('./cia/c4.html')

@app.route('/win2',methods=['post'])
def win2():
    answer = request.form['answer']
    if answer == '2':
        return render_template('./ciphers/winner.html')
    else:
        return render_template('./cia/c5.html')
#cipher game----------------------------------------------

@app.route('/null',methods=['post'])
def null():
    answer = request.form['answer']
    if answer == 'monalisa':
        return render_template('./ciphers/game1.html')
    else:
        return render_template('./ciphers/game.html',message = "wrong answer")

@app.route('/pigpen',methods=['post'])
def pigpen():
    answer = request.form['answer']
    if answer == 'dancing man is crazy':
        return render_template('./ciphers/game2.html')
    else:
        return render_template('./ciphers/game1.html',message = "wrong answer")

@app.route('/dance',methods=['post'])
def dance():
    answer = request.form['answer']
    if answer == 'ronaldo is the best':
        return render_template('./ciphers/game3.html')
    else:
        return render_template('./ciphers/game2.html',message = "wrong answer")

@app.route('/vignere',methods=['post'])
def vignere():
    answer = request.form['answer']
    if answer == 'LAolylBt ohz h nvvk wvAluAphs pu jvtpun Flhyz':
        return render_template('./ciphers/game4.html')
    else:
        return render_template('./ciphers/game3.html',message = "wrong answer")
@app.route('/subs',methods=['post'])
def subs():
    answer = request.form['answer']
    if answer == 'Ethereum has a good potential in coming future':
        return render_template('./ciphers/game5.html')
    else:
        return render_template('./ciphers/game4.html',message = "wrong answer")

@app.route('/rail',methods=['post'])
def rail():
    answer = request.form['answer']
    if answer == 'you are genius':
        return render_template('./ciphers/winner.html')
    else:
        return render_template('./ciphers/game5.html',message = "wrong answer")



if(__name__) == '__main__':
    app.run(debug=True)