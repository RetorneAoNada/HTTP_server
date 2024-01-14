import os
import requests
import time

# Estrura dos dados a serem enviados
class data:
    def __init__(self,id = int ,time = str, d1 = int, d2 = float , d3 = str):
        self.id = id
        self.time = time
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self._data = {
        "id"    : str(self.id),
        "time"  : str(self.time),
        "d1"    : str(self.d1),
        "d2"    : str(self.d2),
        "d3"    : str(self.d3)
        }

# Checa a memória do cache (número de arquivos .json)
def cache_check(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count

#Essa função implementa um POST request e envia os arquivos do Cache encontrados para o site HTTP
def UPLOAD(url):
    for i in range(10):
        if os.path.exists("cache/data" + str(i+1) + ".json"):
            f = open("cache/data" + str(i+1) + ".json", 'rb')
            file = {'file' : f}
            r = requests.post(url, files=file)
            f.close()
    print('Updated')

#Essa função limpa o cache
def CLEAR():
    for i in range(10):
            if os.path.exists("cache/data" + str(i+1) + ".json"):
                os.remove("cache/data" + str(i+1) + ".json")
    print('cache cls')

########
# Por que a função update()?
########
# Essa função é o que caracteriza o administrador de dados, ela é excutada isoladamente (evitando erros de iteração)
# A ideia é em um momento isolado, fora da produção e tratamento dos dados, adicionar componentes ao banco de dados e remover os componentes do escopo local
# Isso é importante, pois ao iterar por uma lista, que tem sua memória atualizada durante a iteração, onde "atualizada" refere-se as ações de adição ou remoção de novas entidades à essa lista.
# Incorre em uma falha chamada "Iteration fault", que pode produzir: um resultado correto, um resultado errado no futuro, um resultado errado imediato ou um erro.
# Assim um administrador de dados é "implementado" para, em um momento seguro e somente nesse momento, efetuar a transferência e remoção dos dados salvos em escopo local
########
def update(url, cache = int):
    if cache == 0:
        pass

    else:
        #Testa a conexção com a Url
        try:
            page = requests.get(url)
            print("page status code:", page.status_code)
            
            #Funcionou, envia os dados
            UPLOAD(url)
            CLEAR()

        #Erro, tenta reconexão em 30 segundos
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
            print("trying to reconect in 30 seconds ...")
            time.sleep(30)
            #Tenta outra conexção
            try:
                page = requests.get(url)
                print(page.status_code)
                
                #Funcionou
                UPLOAD(url)
                CLEAR()

            #Erro novamente, volta a operar, para não perder eficiência na máquina
            except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
                print("conection error, moving to next iteration")
                pass
