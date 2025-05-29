
from flask import Flask, send_file
import os
import subprocess


app = Flask(__name__)
@app.route('/<path:filename>')
def download_file(filename):
    file_path = os.path.join(os.getcwd(), filename)
    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404


subprocess.Popen("start cmd /k robocraft", shell=True)
print('wget http://0.0.0.0:8000 py')

print('wget http://0.0.0.0:1234/reactor.py reactor.py')
app.run(host='0.0.0.0', port=1234)


print('Натисніть cntr C, щоб завершити')



