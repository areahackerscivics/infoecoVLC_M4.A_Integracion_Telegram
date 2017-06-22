#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
from apiai import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
respuesta = ''
def obtenerRespuesta(texto):
    respApiai = sendQuery(texto)
    if respApiai['status']['code'] == 200 and respApiai['result']['metadata']['webhookUsed'] == 'true':
        respuesta = buscarRespuestaWH(resp)
    else:
        respuesta = respApiai['result']['speech']

    return respuesta
