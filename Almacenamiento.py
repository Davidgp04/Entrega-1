try:
    calles=[]
    archivo=open('calles_de_medellin_con_acoso.csv','r',encoding='utf8')
    for line in archivo:
        line=line.replace('\n','')
        line=line.split(';')
        calles.append(line)
    print(calles[1])
except Exception as e:
    print(f'ocurrió un error {e}')
finally:
    archivo.close()
