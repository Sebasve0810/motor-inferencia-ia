import json
import sys

# Asegurar UTF-8 en consola Windows (para imprimir el simbolo de check)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# ==========================================================
# PARTE 1: ESTRUCTURA DE DATOS (NO MODIFICAR)
# ==========================================================
class Regla:
    def __init__(self, id_regla, antecedentes, consecuente):
        self.id_regla = id_regla
        self.antecedentes = set(antecedentes)
        self.consecuente = consecuente

    def __str__(self):
        return f"{self.id_regla}: {' AND '.join(self.antecedentes)} -> {self.consecuente}"


class MotorInferencia:
    def __init__(self, ruta_kb):
        self.reglas = self.cargar_kb(ruta_kb)
        self.memoria_trabajo = set()
        self.traza = []  # Lista de tuplas (regla, es_objetivo)

    def cargar_kb(self, ruta):
        """Carga las reglas desde un archivo JSON."""
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            return [Regla(r.get('id'), r['antecedentes'], r['consecuente']) for r in datos['reglas']]
        except Exception as e:
            print(f"Error al cargar la Base de Conocimiento: {e}")
            return []

    # ==========================================================
    # PARTE 2: ALGORITMO DE ENCADENAMIENTO HACIA ADELANTE
    # ==========================================================
    def ejecutar_inferencia(self, hechos_iniciales, objetivo):
        """
        Encadenamiento hacia adelante hasta punto fijo.

        Entradas:
        - hechos_iniciales: lista de sintomas (ej. ["Fiebre", "Tos"])
        - objetivo: el diagnostico a verificar (ej. "Neumonia")

        Retorna:
        - True si el objetivo es consecuencia logica (KB |= objetivo).
        - False si se alcanza un punto fijo sin hallar el objetivo.
        """
        # 1. Inicializar memoria de trabajo y traza
        self.memoria_trabajo = set(hechos_iniciales)
        self.traza = []

        # Caso borde: el objetivo ya es un hecho de entrada
        if objetivo in self.memoria_trabajo:
            self._imprimir_traza(objetivo_alcanzado=True)
            return True

        # 2. Bucle hasta punto fijo
        hubo_cambios = True
        while hubo_cambios:
            hubo_cambios = False
            # 3. Recorrer cada regla
            for regla in self.reglas:
                # 4. Verificar si todos los antecedentes ya estan en memoria
                if regla.antecedentes.issubset(self.memoria_trabajo):
                    # Solo disparamos la regla si aporta un hecho nuevo
                    if regla.consecuente not in self.memoria_trabajo:
                        self.memoria_trabajo.add(regla.consecuente)
                        es_objetivo = (regla.consecuente == objetivo)
                        self.traza.append((regla, es_objetivo))
                        hubo_cambios = True

                        # Salida temprana al hallar el objetivo
                        if es_objetivo:
                            self._imprimir_traza(objetivo_alcanzado=True)
                            return True

        # 4. Punto fijo alcanzado sin encontrar el objetivo
        self._imprimir_traza(objetivo_alcanzado=False)
        return False

    # ==========================================================
    # PARTE 2b: TRAZA DE EXPLICACION
    # ==========================================================
    def _imprimir_traza(self, objetivo_alcanzado):
        """Imprime las reglas que se dispararon en orden cronologico."""
        if not self.traza:
            print("\n(No se activo ninguna regla — el objetivo ya estaba en los hechos o no se pudo derivar nada)")
            return

        print()  # linea en blanco antes de la traza
        for regla, es_objetivo in self.traza:
            # Reconstruimos los antecedentes ordenados para una salida estable
            antecedentes_str = ' AND '.join(sorted(regla.antecedentes))
            marca = "✓ OBJETIVO ALCANZADO" if es_objetivo else "✓ NUEVO"
            print(f"[{regla.id_regla}] {antecedentes_str} -> {regla.consecuente}  {marca}")


# ==========================================================
# PARTE 3: EJECUCION (PUEDEN MODIFICAR PARA PRUEBAS)
# ==========================================================
if __name__ == "__main__":
    # 1. Inicializar el motor con el archivo de reglas
    motor = MotorInferencia("base_conocimiento.json")

    # 2. Definir caso clinico de prueba
    sintomas = ["Fiebre", "Tos", "Dificultad_Respiratoria"]
    hipotesis = "Neumonia"

    print("--- Sistema Experto de Diagnostico ---")
    print(f"Sintomas iniciales: {sintomas}")
    print(f"Objetivo a verificar: {hipotesis}")

    # 3. Ejecutar Inferencia
    resultado = motor.ejecutar_inferencia(sintomas, hipotesis)

    # 4. Mostrar resultado
    print(f"\n¿Es consecuencia logica?: {resultado}")
