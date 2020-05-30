# https://unix.stackexchange.com/questions/110698/how-to-check-which-specific-processes-python-scripts-are-running
import psutil

def islemDurumKontrolu(islemAdi):
    """
    İşlem adına göre işlemin dönüş durumu.
    """
    islemDurumu = [ proc for proc in psutil.process_iter() if proc.name() == islemAdi ]

    if islemDurumu:
        for gecerliIslem in islemDurumu:
            print(f"id : {gecerliIslem.pid} | Ad : {gecerliIslem.name()} | Durum : {gecerliIslem.status()}")
    else:
        print("İşlem Adı Bulunamadı :", islemAdi)

# islemDurumKontrolu('chromium')

# islemDurumu = [ proc for proc in psutil.process_iter() if proc.status() != "sleeping"]
islemDurumu = [ proc for proc in psutil.process_iter() ]

veri = []
for gecerliIslem in islemDurumu:
    veri.append({
        "id" : gecerliIslem.pid,
        "Ad" : gecerliIslem.name(),
        "Durum" : gecerliIslem.status(),
    })


import pandas as pd
pandaVeri = pd.DataFrame(veri)

from tabulate import tabulate
gorselVeri = tabulate(pandaVeri, headers='keys', tablefmt='psql')
# print(gorselVeri)

import json
jsonVeri = json.loads(pandaVeri.to_json(orient='records'))
# print(jsonVeri)

anahtarlar = [ anahtar for anahtar in jsonVeri[0].keys() ]
# print(anahtarlar)

from proje import app
from flask import jsonify

@app.route('/islem')
def islem():
    return jsonify(jsonVeri)