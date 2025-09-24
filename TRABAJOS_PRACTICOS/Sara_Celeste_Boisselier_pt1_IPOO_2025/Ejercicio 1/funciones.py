from collections import defaultdict

def jugadoresMasAltos(jugadores):
    max_altura = max(j.altura for j in jugadores)
    return [j.nombre for j in jugadores if j.altura == max_altura]

def equiposMasGanadores(equipos):
    max_ganados = max(e.partidos_ganados for e in equipos)
    return [e.nombre for e in equipos if e.partidos_ganados == max_ganados]

def jugadoresConMasPuntos(jugadores, n=10):
    jugadores_ordenador = sorted(jugadores, key=lambda j: j.puntos_totales, reverse=True)
    return [j.nombre for j in jugadores_ordenador[:n]]

def alturaPromedio(jugadores):
    alturas_por_equipo = defaultdict(list)
    for j in jugadores:
        alturas_por_equipo[j.equipo].append(j.altura)
    promedio_por_equipo = {equipo: sum(alturas)/len(alturas) for equipo, alturas in alturas_por_equipo.items()}
    return promedio_por_equipo

def jugadoresMasPuntosPeorEquipo(jugadores, equipos):
   max_perdidos = max(e.partidos_jugados - e.partidos_ganados for e in equipos)
   peores_equipos = [e.nombre for e in equipos if (e.partidos_jugados - e.partidos_ganados) == max_perdidos]
   jugadores_peores = [j for j in jugadores if j.equipo in peores_equipos]
   if not jugadores_peores:
       return []
   max_puntos = max(j.puntos_totales for j in jugadores_peores)
   return [j.nombre for j in jugadores_peores if j.puntos_totales == max_puntos]
