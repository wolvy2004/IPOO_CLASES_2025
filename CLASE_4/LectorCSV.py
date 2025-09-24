import csv

class LectorCSV:
    

    def CSV_to_list(self, archivo:str)->list[str]:
        csv_to_list:list = []
        with open(archivo, newline='') as fichero:
            filas = csv.reader(fichero)
            for fila in filas:
                csv_to_list.append(fila)
        return csv_to_list
            
            