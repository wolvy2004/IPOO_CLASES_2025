# analizador.py

import csv
from pathlib import Path
from collections import defaultdict
import sys
from modelos import Jugador, Equipo


class BasketballAnalyzer:
    def __init__(self, jugadores_file='2025-TR-jugadores.csv', equipos_file='2025-TR-equipos.csv'):
        self.jugadores = []
        self.equipos = {}
        self._load_data(jugadores_file, equipos_file)


    # --- Métodos de carga de datos ---

    def _load_data(self, jugadores_file, equipos_file):
        """Carga los datos de jugadores y equipos."""
        try:
            self.jugadores = self._load_jugadores(jugadores_file)
            self.equipos = self._load_equipos(equipos_file)
            print(f"Cargados {len(self.jugadores)} jugadores y {len(self.equipos)} equipos")
        except FileNotFoundError as e:
            print(f"Error: Archivo no encontrado - {e.filename}")
            sys.exit(1)


    def _load_jugadores(self, archivo):
        """Carga jugadores desde CSV usando el módulo csv estándar."""
        if not Path(archivo).exists():
            raise FileNotFoundError(None, "Archivo no encontrado", archivo)
        jugadores = []
        try:
            with open(archivo, 'r', encoding='utf-8', newline='') as file:
                reader = csv.reader(file)
                for row_num, row in enumerate(reader, 1):
                    if len(row) < 6:
                        print(f"Advertencia: Fila {row_num} incompleta: {row}")
                        continue
                    try:
                        jugadores.append(Jugador(
                            dni=row[4].strip(),
                            nombre_completo=row[0].strip(),
                            fecha_nacimiento=row[1].strip(),
                            altura=row[3].strip(),
                            equipo=row[2].strip(),
                            puntos_totales=row[5].strip()
                        ))
                    except (ValueError, TypeError, IndexError) as e:
                        print(f"Error procesando jugador en fila {row_num}: {row} - {e}")
            return jugadores
        except Exception as e:
            print(f"Error leyendo {archivo}: {e}")
            return []


    def _load_equipos(self, archivo):
        """Carga equipos desde CSV usando el módulo csv estándar."""
        if not Path(archivo).exists():
            raise FileNotFoundError(None, "Archivo no encontrado", archivo)
        equipos = {}
        try:
            with open(archivo, 'r', encoding='utf-8', newline='') as file:
                reader = csv.reader(file)
                for row_num, row in enumerate(reader, 1):
                    if len(row) < 4:
                        print(f"Advertencia: Fila {row_num} incompleta: {row}")
                        continue
                    try:
                        equipo = Equipo(
                            nombre=row[0].strip(),
                            ciudad=row[1].strip(),
                            partidos_jugados=row[2].strip(),
                            partidos_ganados=row[3].strip()
                        )
                        equipos[equipo.nombre.lower()] = equipo
                    except (ValueError, TypeError, IndexError) as e:
                        print(f"Error procesando equipo en fila {row_num}: {row} - {e}")
            return equipos
        except Exception as e:
            print(f"Error leyendo {archivo}: {e}")
            return {}


    # --- Métodos de análisis de datos ---

    def jugadores_mas_altos(self):
        """Encuentra los jugadores con mayor altura."""
        if not self.jugadores:
            return []
        max_altura = max(j.altura for j in self.jugadores)
        return [j.nombre_completo for j in self.jugadores if j.altura == max_altura]


    def equipos_mas_ganadores(self):
        """Encuentra los equipos con más victorias."""
        if not self.equipos:
            return []
        max_victorias = max(e.partidos_ganados for e in self.equipos.values())
        return [e.nombre for e in self.equipos.values() if e.partidos_ganados == max_victorias]


    def top_jugadores_puntos(self, limite=10):
        """Encuentra el top N de jugadores por puntos."""
        if not self.jugadores:
            return []
        jugadores_ordenados = sorted(
            self.jugadores,
            key=lambda x: (-x.puntos_totales, x.nombre_completo)
        )
        return [j.nombre_completo for j in jugadores_ordenados[:limite]]


    def altura_promedio_por_equipo(self):
        """Calcula la altura promedio por equipo usando collections."""
        if not self.jugadores:
            return {}
        alturas_por_equipo = defaultdict(list)
        for jugador in self.jugadores:
            alturas_por_equipo[jugador.equipo].append(jugador.altura)
        promedios = {}
        for equipo, alturas in alturas_por_equipo.items():
            promedio = sum(alturas) / len(alturas)
            promedios[equipo] = round(promedio, 2)
        return promedios


    def jugadores_mas_puntos_peor_equipo(self):
        """Obtiene una lista del jugador o jugadores con más puntos en el o los equipos con más partidos perdidos."""
        if not self.jugadores or not self.equipos:
            return []
        max_perdidos = max(e.partidos_perdidos for e in self.equipos.values())
        peores_equipos = {e.nombre.lower() for e in self.equipos.values() if e.partidos_perdidos == max_perdidos}
        jugadores_peores_equipos = [j for j in self.jugadores if j.equipo in peores_equipos]
        if not jugadores_peores_equipos:
            return []
        max_puntos = max(j.puntos_totales for j in jugadores_peores_equipos)
        mejores_jugadores = [j.nombre_completo for j in jugadores_peores_equipos if j.puntos_totales == max_puntos]
        return mejores_jugadores


    def estadisticas_adicionales(self):
        """Calcula estadísticas adicionales para el reporte."""
        if not self.jugadores:
            return {}
        alturas = [j.altura for j in self.jugadores]
        puntos = [j.puntos_totales for j in self.jugadores]
        return {
            'total_jugadores': len(self.jugadores),
            'altura_promedio_general': round(sum(alturas) / len(alturas), 2),
            'altura_minima': min(alturas),
            'altura_maxima': max(alturas),
            'puntos_promedio_general': round(sum(puntos) / len(puntos), 2),
            'puntos_minimos': min(puntos),
            'puntos_maximos': max(puntos),
            'total_equipos': len(self.equipos)
        }


    # --- Método de generación de reporte ---

    def generar_reporte(self):
        """Genera un reporte completo con todos los análisis."""
        print("=" * 60)
        print("REPORTE DE ANÁLISIS DE BASKETBALL")
        print("=" * 60)
        # Estadísticas generales
        stats = self.estadisticas_adicionales()
        if stats:
            print(f"\n📊 ESTADÍSTICAS GENERALES:")
            print(f"   • Total jugadores: {stats['total_jugadores']}")
            print(f"   • Total equipos: {stats['total_equipos']}")
            print(f"   • Altura promedio general: {stats['altura_promedio_general']}m")
            print(f"   • Puntos promedio general: {stats['puntos_promedio_general']}")
        # Jugadores más altos
        print(f"\n📏 JUGADORES MÁS ALTOS:")
        altos = self.jugadores_mas_altos()
        if altos:
            altura_maxima = max(j.altura for j in self.jugadores if j.nombre_completo in altos)
            for jugador in altos:
                print(f"   • {jugador} ({altura_maxima}m)")
        else:
            print("   ⚠️  No se encontraron jugadores")
        # Equipos más ganadores
        print(f"\n🏆 EQUIPOS MÁS GANADORES:")
        ganadores = self.equipos_mas_ganadores()
        if ganadores:
            max_victorias = max(e.partidos_ganados for e in self.equipos.values() if e.nombre in ganadores)
            for equipo in ganadores:
                equipo_obj = next(e for e in self.equipos.values() if e.nombre == equipo)
                print(f"   • {equipo} ({max_victorias} victorias - {equipo_obj.porcentaje_victoria}%)")
        else:
            print("   ⚠️  No se encontraron equipos")
        # Top 10 jugadores por puntos
        print(f"\n⭐ TOP 10 JUGADORES POR PUNTOS:")
        top_puntos = self.top_jugadores_puntos()
        for i, jugador in enumerate(top_puntos, 1):
            puntos = next(j.puntos_totales for j in self.jugadores if j.nombre_completo == jugador)
            equipo = next(j.equipo for j in self.jugadores if j.nombre_completo == jugador)
            print(f"   {i:2d}. {jugador} ({puntos} puntos - {equipo.title()})")
        # Altura promedio por equipo
        print(f"\n📊 ALTURA PROMEDIO POR EQUIPO:")
        promedios = self.altura_promedio_por_equipo()
        for equipo, promedio in sorted(promedios.items()):
            count = len([j for j in self.jugadores if j.equipo == equipo])
            print(f"   • {equipo.title()}: {promedio}m ({count} jugadores)")
        # Jugadores con más puntos en el peor equipo
        print(f"\n💪 JUGADORES CON MÁS PUNTOS EN EL/LOS EQUIPO/S CON MÁS PARTIDOS PERDIDOS:")
        # Mostrar información de contexto sobre los peores equipos
        if self.equipos:
            max_perdidos = max(e.partidos_perdidos for e in self.equipos.values())
            peores_equipos = [e for e in self.equipos.values() if e.partidos_perdidos == max_perdidos]
            print(f"   📊 Equipo(s) con más partidos perdidos ({max_perdidos}):")
            for equipo in peores_equipos:
                print(f"      • {equipo.nombre} ({equipo.partidos_ganados}G-{equipo.partidos_perdidos}P)")
        mejores_peores = self.jugadores_mas_puntos_peor_equipo()
        if mejores_peores:
            print(f"   🏀 Mejores anotadores en estos equipos:")
            for jugador in mejores_peores:
                jugador_obj = next(j for j in self.jugadores if j.nombre_completo == jugador)
                equipo_obj = next(e for e in self.equipos.values() if e.nombre.lower() == jugador_obj.equipo)
                print(f"      • {jugador} ({jugador_obj.puntos_totales} puntos - {equipo_obj.nombre})")
        else:
            print(f"   ⚠️  No se encontraron jugadores registrados en estos equipos")
        print("\n" + "=" * 60)