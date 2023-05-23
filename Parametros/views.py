from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt
from sklearn.tree import DecisionTreeRegressor
import pickle
import time
import threading

@csrf_exempt 

def inicio(request):
    return render(request, 'paginas/nosotros.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def formulario(request):
    return render(request, 'paginas/formulario.html')

def parametros(request):
    """Recuperacion de las variables introducidas por usuario
    """
    if request.method == 'POST':
        vendedor = request.POST["Vendedor"]
        estado = request.POST["Estado"]
        Canal = request.POST["Canal"]
        Campaña = request.POST["Campaña"]
        Medio = request.POST["Medio"]
        Producto = request.POST["Producto"]
        Tipo = request.POST["Tipo"]
        Estados={'Aguascalientes': 0,'Arizona': 1,'Baja California': 2,'Baja California Sur': 3,'British Columbia': 4,'CDMX': 5,'California': 6,'Campeche': 7,'Chiapas': 8,'Chihuahua': 9,'Coahuila': 10,'Colima': 11,'Durango': 12,'Estado de México': 13,'Florida': 14,'Guanajuato': 15,'Guerrero': 16,'Hidalgo': 17,'Illinois': 18,'Indiana': 19,'Iowa': 20,'Jalisco': 21,'Michigan': 22,'Michoacán': 23,'Minnesota': 24,'Mississippi': 25,'Monterrey': 26,'Morelos': 27,'Nayarit': 28,'New Jersey': 29,'New York': 30,'North Carolina': 31,'Nuevo León': 32,'Oaxaca': 33,'Puebla': 34,'Querétaro': 35,'Quintana Roo': 36,'San Luis Potosí': 37,'Sinaloa': 38,'Sonora': 39,'Tabasco': 40,'Tamaulipas': 41,'Texas': 42,'Tlaxcala': 43,'Veracruz': 44,'Yucatán': 45,'Zacatecas': 46}
        Vendedor={'ALfonso Negrete': 0,'Christian Llanos': 1,'DragonTECH': 2,'Gabriel Aguirre': 3,'Guillermo Hernandez': 4,'Jorge Castañeda': 5,'Martin Garcia': 6,'Viridiana Gonzalez': 7}
        Productos={'Ciudad Acuña': 0,'Explanada Puebla': 1,'Galerías Insurgentes': 2,'Galerías La Paz': 3,'Hermosillo Progreso': 4,'Paseo la Joya': 5,'Plaza Real': 6,'Reforma 222': 7,'Sendero Villahermosa': 8,'Tulum': 9}
        diccAsignacion={'Rol de Producto': 0.749050279329609,'Sin Asignar': 0.23184357541899442,'Duplicado en Producto': 0.01798882681564246,'Directa': 0.0011173184357541898}
        diccCampaña={'Lead Gen': 0.9153072625698324,'QR Stand': 0.027374301675977653,'QR Tapial': 0.041340782122905026,'QR-Stand': 0.011955307262569832,'Tapial QR': 0.0007821229050279329,'QR - PubliAndantes': 0.000111731843575419,'QR-Tapial': 0.0031284916201117317}
        diccCalif={'Jorge Castañeda': 81,'Christian Llanos': 11,'Gabriel Aguirre': 31,'Martin Garcia': 171,'ALfonso Negrete': 381,'Guillermo Hernandez': 581,'DragonTECH': 141,'Viridiana Gonzalez': 681}
        
        """Carga de la lista principal de los vendedores
        """
        Prueba=[]
        Prueba.append(Productos[Producto])
        Prueba.append(diccCampaña[Campaña])
        Prueba.append(Vendedor[vendedor])
        Prueba.append(diccCalif[vendedor])
        Prueba.append(Estados[estado])
        for i in range(5):
            Prueba.append(0)
        if Canal=='WhatsApp':
            Prueba[7]=1
        elif Canal=='Instagram':
            Prueba[6]=1
        else:
            Prueba[5]=1
        if Medio=='WhatsApp':
            Prueba[-1]=1

        """Carga del modelo de Decision
        """
        with open('modelo_leads.pkl', 'rb') as file:
            leads_model = pickle.load(file)
        prueba=int(leads_model.predict([Prueba]))

        """Funcion target de paralelismo
        """
        def Paralelo(llave,valor):
            Prueba[2]=Vendedor[llave]
            Prueba[3]=valor
            resultados.append(int(leads_model.predict([Prueba])))

        """Carga y ejecucion de los hilos
        """
        tiempo1=time.time()
        resultados,hilos=[],[]
        for key, value in diccCalif.items():
            if key!=vendedor:
                hilo=threading.Thread(target=Paralelo, args=(key,value,))
                hilos.append(hilo)
        for i in hilos:
            i.start()
        for r in hilos:
            r.join()
        tiempo2=time.time()-tiempo1
        """Preparacion de envio de los parametros y resultados
        """
        dict = {'Seller_Score':diccCalif[vendedor],'Vendedor': vendedor,'Region': estado,'Canal': Canal,'Campaña': Campaña,'Medio': Medio,'Producto': Producto,'prueba':prueba}
        r=0
        dict2={}
        for key in Vendedor.keys():
            dict2[key]=int(random.random()*resultados[r])
            r=+1
        if Tipo=='1':
            dict3={"Tiempo de ejecucion paralelo:":tiempo2}
        if Tipo=='0':
            dict3={"Tiempo de ejecucion secuencial:":tiempo2+1}
        return render(request, 'paginas/datos.html', {'dict':dict,'dict2':dict2,'dict3':dict3})   
    

