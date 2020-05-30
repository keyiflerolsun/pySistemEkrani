from proje import app
from flask import Response
import json, time, psutil

def birimDonusturucu(bytes, sonEK="B"):
    """
    Baytları doğru biçimine ölçeklendirme
    örn:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    etken = 1024
    for birim in ["", "K", "M", "G", "T", "P"]:
        if bytes < etken:
            return f"{bytes:.2f} {birim}{sonEK}"
        bytes /= etken

@app.route('/anlik-veri')
def ram():
    def veriUretim():
        while True:
            svmem = psutil.virtual_memory()
            cpufreq = psutil.cpu_freq()
            sarjDurum = open("/sys/class/power_supply/BAT0/status", "r").readline().strip()
            sarjSeviye = open("/sys/class/power_supply/BAT0/capacity", "r").readline().strip()

            json_data = json.dumps({
                'ram_Boşta' : birimDonusturucu(svmem.available).split()[0],
                'ram_Kullanılan': birimDonusturucu(svmem.used).split()[0],
                'CPU_Maks': f"{cpufreq.max:.2f}",
                'CPU_Kullanılan' : f"{cpufreq.current:.2f}",
                'Şarj_Durum' : sarjDurum,
                'Şarj_Seviye' : sarjSeviye
                }, sort_keys=False, ensure_ascii=False)
            
            yield f"data: {json_data}\n\n"
            time.sleep(1)

    return Response(veriUretim(), mimetype='text/event-stream')