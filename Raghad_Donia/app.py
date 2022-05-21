from flask import Flask, request
import Donia_flask as Dondon
import Raghad_flask as Raghoda
import CCA as cca
import bfAttack_efficiency as BF
app = Flask(__name__)


@app.route("/raghad/sender/<msg>")
def Raghad(msg):
        return Raghoda.initRaghad(msg, reciever=False)

@app.route("/raghad/reciever/<genPQ>&<p>&<q>")
def RaghadReciever(genPQ,p,q):
        if(genPQ==1 or genPQ=="1"):
                return Raghoda.initRaghad("dummy",genPQ=True,p=p,q=q, reciever=True)
        else:
                return Raghoda.initRaghad("dummy",genPQ=False,p=p,q=q, reciever=True)

@app.route("/donia/sender/<msg>")
def Donia(msg):
        return Dondon.initDonia(msg, reciever=False)

@app.route("/donia/reciever/<genPQ>&<p>&<q>")
def DoniaReciever(genPQ,p,q):
        if(genPQ==1 or genPQ=="1"):
                return Dondon.initDonia("dummy",genPQ=True,p=p,q=q, reciever=True)
        else:
                return Dondon.initDonia("dummy",genPQ=False,p=p,q=q, reciever=True)

@app.route("/donia/keys/<genPQ>&<p>&<q>")
def DoniaKeys(genPQ,p,q):
        if(genPQ==1 or genPQ=="1"):
                return Dondon.getKeys(genPQ=True,p=p,q=q)
        else:
                return Dondon.getKeys(genPQ=False,p=p,q=q)

@app.route("/raghad/keys/<genPQ>&<p>&<q>")
def RaghadKeys(genPQ,p,q):
        if(genPQ==1 or genPQ=="1"):
                return Raghoda.getKeys(genPQ=True,p=p,q=q)
        else:
                return Raghoda.getKeys(genPQ=False,p=p,q=q)

@app.route("/attack/cca/init/raghad/<ind>")
def initCCA(ind):
        return Raghoda.initRaghadForAttack(ind);

@app.route("/attack/cca/<cipher>&<e>&<n>")
def AttackCCA(cipher,e,n):
        return cca.CCA_Flask(cipher,e,n);

@app.route("/attack/bf/<n>&<e>&<c>")
def AttackBF(n, e, c):
        return BF.mathematicalBFAttack(n, e, c);