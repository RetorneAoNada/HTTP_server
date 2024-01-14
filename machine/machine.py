import time
import data_manager
import json

f = open('C:/Users/USER/Desktop/Python/machine/count.txt','r')
count = int(f.read())
f.close()

# folder path
cache_path = r'C:/Users/USER/Desktop/Python/machine/cache'
url = "http://127.0.0.1:5000/login"
cache = 0
# Iterate directory

cache = data_manager.cache_check(cache_path)

while(True):
    #Se a máquina tem espaço para operar
    if(cache < 10):    
        data_manager.update(url, cache) # Isso previne falhas de iteração

        #Maquina trabalhando#
        time.sleep(5)

        #Cria dados como dicionário em python, com data e hora
        seconds = time.time()
        local_time = time.ctime(seconds)
        data = data_manager.data(count, local_time, 1, 1.1, 'Teste')

        #Cria espaço no cache para o dado
        f = open("cache/data"+str(cache+1)+".json" , "x")
        f.close()

        #Passa os dados para o cache
        f = open("cache/data"+str(cache+1)+".json" , "w")
        f.write(json.dumps(data._data))
        f.close()
        
        #Computa um dado produzido com sucesso
        count += 1    
        f = open('C:/Users/USER/Desktop/Python/machine/count.txt','w')
        f.write(str(count))
        f.close()

    #Se é necessário enviar dados e limpar o cache antes de retornar as operações
    else:
        data_manager.update(url, cache)
    
    #Avalia a "Memória" do cache
    cache = data_manager.cache_check(cache_path)


