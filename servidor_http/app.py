from flask import Flask, request, redirect
import json

app = Flask(__name__)

#Função que escreve no banco de dados
# !PROBLEMA, complexidade O(n^2), torna o processo de atualização, no tempo, mais devagar que a máquina
# .json não possui funções 
def write_json(new_data, index, filename, i):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data
        file_data[index].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = i)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        file = request.files['file']
        raw = file.read()
        data = json.loads(raw)
        write_json(data, 'data','data_base.json', 1)
        return redirect('http://localhost:5000/login', code=302)
    
    else:
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<h1>HOME</h1>
</form>
</body></html>"""
    

if __name__ == "__main__":
   app.run()
