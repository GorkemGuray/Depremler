from flask import Flask,render_template,redirect,url_for
import requests
from bs4 import BeautifulSoup as bs


app = Flask(__name__)
app.secret_key="deprem.gorkem.co"



@app.route('/')
def index():
    r = requests.get('http://www.koeri.boun.edu.tr/scripts/lst0.asp')
    soup = bs(r.content, 'html.parser')
    pre = soup.select_one('pre').text

    liste = [x.strip() for x in pre.split('\n')]
    liste=liste[7:-2]
    liste2=[]

    depremler={}

    for i in liste:
        liste2.append(list(filter(None,i.split(' '))))
    
    for i in liste2:
        del i[5]
        del i[6]
        del i[-1]

    for i in liste2:
        temp = i[6:]
        del i[6:]
        s = ''.join(temp)
        c = s.split('(')
        if len(c)==1:
            i.append("yok")
            i.append(c[0])
        else:
            i.append(c[0])
            i.append(c[1].rstrip(')'))
    


    for i in range(len(liste2)):
        depremler[i]={"tarih":liste2[i][0],
                    "saat":liste2[i][1],
                    "enlem":liste2[i][2],
                    "boylam":liste2[i][3],
                    "derinlik":liste2[i][4],
                    "buyukluk":float(liste2[i][5]),
                    "yer-aciklama":liste2[i][6],
                    "yer":liste2[i][7]
     
        }

    length = len(depremler)


    return  render_template("index.html",depremler=depremler,length=length)

if __name__ == '__main__':
    app.run(debug=True)