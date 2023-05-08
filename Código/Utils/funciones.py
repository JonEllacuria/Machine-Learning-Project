import pandas as pd

#Resultado(1-X-2)
def generar_resultados(jornada, completo):
    filas = []
    columnas = ['clas_local', '%_Saques_esquina_local_favor', '%_Saques_esquina_local_contra', 'goles_marcados_local', 'goles_recibidos_local', 'goles_esperados_local', 'goles_esperados_contra_local', 'posesion_media_local', '%_disparos_puerta_hechos_local', '%_disparos_puerta_recibidos_local', '%_pases_cruzados_hechos_local', '%_pases_cruzados_recibidos_local', 'tarjetas_cometidas_local', 'tarjetas_provocadas_local', 'clas_visitante', '%_Saques_esquina_visitante_favor', '%_Saques_esquina_visitante_contra', 'goles_marcados_visitante', 'goles_recibidos_visitante', 'goles_esperados_visitante', 'goles_esperados_contra_visitante', 'posesion_media_visitante', '%_disparos_puerta_hechos_visitante', '%_disparos_puerta_recibidos_visitante', '%_pases_cruzados_hechos_visitante', '%_pases_cruzados_recibidos_visitante', 'tarjetas_cometidas_visitante', 'tarjetas_provocadas_visitante']
    
    for partido in jornada:
        local, visitante, arbitro = partido
        local_info = completo[['clas_local', '%_Saques_esquina_local_favor','%_Saques_esquina_local_contra','goles_marcados_local','goles_recibidos_local','goles_esperados_local','goles_esperados_contra_local','posesion_media_local','%_disparos_puerta_hechos_local','%_disparos_puerta_recibidos_local','%_pases_cruzados_hechos_local','%_pases_cruzados_recibidos_local','tarjetas_cometidas_local','tarjetas_provocadas_local']][completo["Equipo_local"]==local].iloc[0]
        visitante_info = completo[['clas_visitante', '%_Saques_esquina_visitante_favor', '%_Saques_esquina_visitante_contra', 'goles_marcados_visitante',                               'goles_recibidos_visitante', 'goles_esperados_visitante', 'goles_esperados_contra_visitante', 'posesion_media_visitante',                               '%_disparos_puerta_hechos_visitante', '%_disparos_puerta_recibidos_visitante', '%_pases_cruzados_hechos_visitante',                               '%_pases_cruzados_recibidos_visitante', 'tarjetas_cometidas_visitante', 'tarjetas_provocadas_visitante']][completo["Equipo_visitante"] == visitante].iloc[0]
        partido_info = list(local_info) + list(visitante_info)
        filas.append(partido_info)

    columnas = ['clas_local', '%_Saques_esquina_local_favor', '%_Saques_esquina_local_contra', 'goles_marcados_local', 'goles_recibidos_local', 'goles_esperados_local', 'goles_esperados_contra_local', 'posesion_media_local', '%_disparos_puerta_hechos_local', '%_disparos_puerta_recibidos_local', '%_pases_cruzados_hechos_local', '%_pases_cruzados_recibidos_local', 'tarjetas_cometidas_local', 'tarjetas_provocadas_local', 'clas_visitante', '%_Saques_esquina_visitante_favor', '%_Saques_esquina_visitante_contra', 'goles_marcados_visitante', 'goles_recibidos_visitante', 'goles_esperados_visitante', 'goles_esperados_contra_visitante', 'posesion_media_visitante', '%_disparos_puerta_hechos_visitante', '%_disparos_puerta_recibidos_visitante', '%_pases_cruzados_hechos_visitante', '%_pases_cruzados_recibidos_visitante', 'tarjetas_cometidas_visitante', 'tarjetas_provocadas_visitante']
    df_kiniela = pd.DataFrame(filas, columns=columnas)
    df_kiniela = df_kiniela.reindex(columns=['clas_local', 'clas_visitante', '%_Saques_esquina_local_favor', '%_Saques_esquina_visitante_favor', '%_Saques_esquina_local_contra', '%_Saques_esquina_visitante_contra', 'goles_marcados_local', 'goles_marcados_visitante', 'goles_recibidos_local', 'goles_recibidos_visitante', 'goles_esperados_local', 'goles_esperados_visitante', 'goles_esperados_contra_local', 'goles_esperados_contra_visitante', 'posesion_media_local', 'posesion_media_visitante', '%_disparos_puerta_hechos_local', '%_disparos_puerta_hechos_visitante', '%_disparos_puerta_recibidos_local', '%_disparos_puerta_recibidos_visitante', '%_pases_cruzados_hechos_local', '%_pases_cruzados_hechos_visitante', '%_pases_cruzados_recibidos_local', '%_pases_cruzados_recibidos_visitante', 'tarjetas_cometidas_local', 'tarjetas_cometidas_visitante', 'tarjetas_provocadas_local', 'tarjetas_provocadas_visitante'])
    return df_kiniela

#Goles
def generar_goles_local(jornada,completo):
    filas = []

    for partido in jornada:
        local, visitante, arbitro = partido
        local_info = completo[['clas_local', 'goles_marcados_local',
                           'goles_esperados_local','%_disparos_puerta_hechos_local','%_pases_cruzados_hechos_local']][completo["Equipo_local"]==local].iloc[0]
    
        visitante_info = completo[['clas_visitante','goles_recibidos_visitante',
                               'goles_esperados_contra_visitante','%_disparos_puerta_recibidos_visitante','%_pases_cruzados_hechos_visitante',
                               '%_pases_cruzados_recibidos_visitante']][completo["Equipo_visitante"] == visitante].iloc[0]
    
    
        partido_info = list(local_info) + list(visitante_info)
    
        filas.append(partido_info)

    columnas = ['clas_local', 'goles_marcados_local',
                           'goles_esperados_local','%_disparos_puerta_hechos_local','%_pases_cruzados_hechos_local','clas_visitante',
                           'goles_recibidos_visitante',
                               'goles_esperados_contra_visitante','%_disparos_puerta_recibidos_visitante','%_pases_cruzados_hechos_visitante',
                               '%_pases_cruzados_recibidos_visitante']
    df_goles_local = pd.DataFrame(filas, columns=columnas)
    df_goles_local=df_goles_local.reindex(columns=['clas_local', 'clas_visitante','goles_marcados_local','goles_recibidos_visitante','goles_esperados_local',
          'goles_esperados_contra_visitante','%_disparos_puerta_hechos_local',
       '%_disparos_puerta_recibidos_visitante','%_pases_cruzados_hechos_local','%_pases_cruzados_recibidos_visitante'])
    return df_goles_local
    

def generar_goles_visitante(jornada,completo):
    filas = []

    for partido in jornada:
        local, visitante, arbitro = partido
        local_info = completo[['clas_local', 'goles_recibidos_local',
                           'goles_esperados_contra_local','%_disparos_puerta_recibidos_local',
                           '%_pases_cruzados_recibidos_local']][completo["Equipo_local"]==local].iloc[0]
    
        visitante_info = completo[['clas_visitante','goles_marcados_visitante',
                               'goles_esperados_visitante','%_disparos_puerta_hechos_visitante','%_pases_cruzados_hechos_visitante',]][completo["Equipo_visitante"] == visitante].iloc[0]
    
    
        partido_info = list(local_info) + list(visitante_info)
    
        filas.append(partido_info)

    columnas = ['clas_local', 'goles_recibidos_local',
                           'goles_esperados_contra_local','%_disparos_puerta_recibidos_local',
                           '%_pases_cruzados_recibidos_local','clas_visitante','goles_marcados_visitante',
                               'goles_esperados_visitante','%_disparos_puerta_hechos_visitante','%_pases_cruzados_hechos_visitante']
    df_goles_visitante = pd.DataFrame(filas, columns=columnas)
    df_goles_visitante=df_goles_visitante.reindex(columns=['clas_local', 'clas_visitante','goles_marcados_visitante','goles_recibidos_local','goles_esperados_visitante',
          'goles_esperados_contra_local','%_disparos_puerta_hechos_visitante',
       '%_disparos_puerta_recibidos_local','%_pases_cruzados_hechos_visitante','%_pases_cruzados_recibidos_local'])
    return df_goles_visitante

#Tarjetas
def generar_tarjetas_local(jornada,completo):
    filas = []
    for partido in jornada:
        local, visitante, arbitro = partido
        local_info = completo[['clas_local', 'faltas_cometidas_local',
                            'tarjetas_cometidas_local']][completo["Equipo_local"]==local].iloc[0]
        
        visitante_info = completo[['clas_visitante', 'faltas_provocadas_visitante',
                                'tarjetas_provocadas_visitante']][completo["Equipo_visitante"] == visitante].iloc[0]
        
        arbitro_info=completo[["Árbitro_sum_tarjetas_local","Árbitro_faltas_local"]][completo["Árbitro"] == arbitro].iloc[0]
        
        partido_info = list(local_info) + list(visitante_info) + list(arbitro_info)
        
        filas.append(partido_info)

    columnas = ['clas_local', 'faltas_cometidas_local',
                            'tarjetas_cometidas_local','clas_visitante', 'faltas_provocadas_visitante',
                                'tarjetas_provocadas_visitante',"Árbitro_sum_tarjetas_local","Árbitro_faltas_local"]
    df_tarjetas_local = pd.DataFrame(filas, columns=columnas)
    df_tarjetas_local=df_tarjetas_local.reindex(columns=["clas_local","clas_visitante","Árbitro_sum_tarjetas_local","faltas_cometidas_local","faltas_provocadas_visitante","tarjetas_cometidas_local",
             'Árbitro_faltas_local',"tarjetas_provocadas_visitante"])
    return df_tarjetas_local

def generar_tarjetas_visitante(jornada,completo):
    filas = []

    for partido in jornada:
        local, visitante, arbitro = partido
        local_info = completo[['clas_local', 'faltas_provocadas_local',
                            'tarjetas_provocadas_local']][completo["Equipo_local"]==local].iloc[0]
        
        visitante_info = completo[['clas_visitante', 'faltas_cometidas_visitante',
                                'tarjetas_cometidas_visitante']][completo["Equipo_visitante"] == visitante].iloc[0]
        
        arbitro_info=completo[["Árbitro_sum_tarjetas_visitante","Árbitro_faltas_visitante"]][completo["Árbitro"] == arbitro].iloc[0]
        
        partido_info = list(local_info) + list(visitante_info) + list(arbitro_info)
        
        filas.append(partido_info)

    columnas = ["clas_local","clas_visitante","Árbitro_sum_tarjetas_visitante","faltas_cometidas_visitante","faltas_provocadas_local","tarjetas_cometidas_visitante",
                'Árbitro_faltas_visitante',"tarjetas_provocadas_local"]
    df_tarjetas_visitante = pd.DataFrame(filas, columns=columnas)
    df_tarjetas_visitante=df_tarjetas_visitante.reindex(columns=["clas_local","clas_visitante","Árbitro_sum_tarjetas_visitante","faltas_cometidas_visitante","faltas_provocadas_local","tarjetas_cometidas_visitante",
             'Árbitro_faltas_visitante',"tarjetas_provocadas_local"])
    return df_tarjetas_visitante

#Corners
def generar_corners_local(jornada,completo):
    filas = []

    for partido in jornada:
        local, visitante, arbitro = partido
        local_info = completo[['clas_local', '%_Saques_esquina_local_favor',
                            'posesion_media_local','%_disparos_puerta_hechos_local','%_pases_cruzados_hechos_local']][completo["Equipo_local"]==local].iloc[0]
        
        visitante_info = completo[['clas_visitante', '%_Saques_esquina_visitante_contra',
                                '%_disparos_puerta_recibidos_visitante','%_pases_cruzados_recibidos_visitante']][completo["Equipo_visitante"] == visitante].iloc[0]
        
        
        partido_info = list(local_info) + list(visitante_info)
        
        filas.append(partido_info)

    columnas = ['clas_local', '%_Saques_esquina_local_favor',
                            'posesion_media_local','%_disparos_puerta_hechos_local','%_pases_cruzados_hechos_local','clas_visitante',
                            '%_Saques_esquina_visitante_contra','%_disparos_puerta_recibidos_visitante','%_pases_cruzados_recibidos_visitante']
    df_corners_local = pd.DataFrame(filas, columns=columnas)
    df_corners_local=df_corners_local.reindex(columns=['clas_local', 'clas_visitante', '%_Saques_esquina_local_favor','%_Saques_esquina_visitante_contra','posesion_media_local',
            '%_disparos_puerta_hechos_local','%_disparos_puerta_recibidos_visitante','%_pases_cruzados_hechos_local','%_pases_cruzados_recibidos_visitante'])
    return df_corners_local

def generar_corners_visitante(jornada,completo):
    filas = []

    for partido in jornada:
        local, visitante, arbitro = partido
        local_info = completo[['clas_local', '%_Saques_esquina_local_contra',
                            '%_disparos_puerta_recibidos_local','%_pases_cruzados_recibidos_local']][completo["Equipo_local"]==local].iloc[0]
        
        visitante_info = completo[['clas_visitante','%_Saques_esquina_visitante_favor',
                                'posesion_media_visitante','%_disparos_puerta_hechos_visitante','%_pases_cruzados_hechos_visitante']][completo["Equipo_visitante"] == visitante].iloc[0]
        
        
        partido_info = list(local_info) + list(visitante_info)
        
        filas.append(partido_info)

    columnas = ['clas_local', '%_Saques_esquina_local_contra',
                            '%_disparos_puerta_recibidos_local','%_pases_cruzados_recibidos_local','clas_visitante','%_Saques_esquina_visitante_favor',
                                'posesion_media_visitante','%_disparos_puerta_hechos_visitante','%_pases_cruzados_hechos_visitante']
    df_corners_visitante = pd.DataFrame(filas, columns=columnas)
    df_corners_visitante=df_corners_visitante.reindex(columns=['clas_local', 'clas_visitante', '%_Saques_esquina_visitante_favor','%_Saques_esquina_local_contra','posesion_media_visitante',
            '%_disparos_puerta_hechos_visitante','%_disparos_puerta_recibidos_local','%_pases_cruzados_hechos_visitante','%_pases_cruzados_recibidos_local'])
    return df_corners_visitante