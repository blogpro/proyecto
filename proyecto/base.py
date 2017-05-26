# -*- encoding: utf-8 -*-
"""
Archivo de configuracion para 
Produccion
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#debug = False  
HOSTS = ['http://systab.herokuapp.com/','systab.herokuapp.com']

debug = True
# HOSTS = ['*']

#Bd Produccion
# HOST = 'ec2-54-225-201-25.compute-1.amazonaws.com'
# NAME = 'd8aecn4b0n19m3'
# USER = 'nnwgvgoklyndcu'
# PASSWORD = '3eyYWb0OMg9o5VNlkEa4QQPkpu'

#Bd desarrollo
HOST = 'localhost'
NAME = 'bdpro'
USER = 'postgres'
PASSWORD = ''

facebook_key = "1476656729277209"#Produccion
facebook_secret = "5c1f80475bcef95cef58f523ab14df27"#Produccion