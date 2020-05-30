from proje import app
from flask import redirect, url_for
import psutil

@app.route('/sonlandir/<int:pid>')
def sonlandir(pid):

    p = psutil.Process(pid)
    p.kill()

    return redirect(url_for('anaSayfa'))