"""
Casos de prueba para el motor de inferencia (encadenamiento hacia adelante).

Cada caso define:
- una descripcion legible
- los sintomas iniciales
- el objetivo a verificar
- el resultado esperado (True / False)

Al ejecutar este archivo se imprime la traza de cada caso, el resultado y si
paso o fallo el assert. Al final se muestra un resumen.
"""

import sys
from proyecto_inferencia import MotorInferencia

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass


def ejecutar_caso(motor, numero, descripcion, sintomas, objetivo, esperado):
    """Ejecuta un caso de prueba y retorna True si paso."""
    print("\n" + "=" * 70)
    print(f"CASO {numero}: {descripcion}")
    print(f"Sintomas iniciales : {sintomas}")
    print(f"Objetivo           : {objetivo}")
    print(f"Resultado esperado : {esperado}")

    resultado = motor.ejecutar_inferencia(sintomas, objetivo)

    print(f"\nResultado obtenido : {resultado}")
    if resultado == esperado:
        print(">>> PASO <<<")
        return True
    else:
        print(">>> FALLO <<<")
        return False


def main():
    motor = MotorInferencia("base_conocimiento.json")
    print(f"Reglas cargadas: {len(motor.reglas)}")

    casos = [
        # ---------- CASOS QUE DEBEN RETORNAR True ----------
        (
            "Neumonia (cadena de 2 reglas: R1 -> R2)",
            ["Fiebre", "Tos", "Dificultad_Respiratoria"],
            "Neumonia",
            True,
        ),
        (
            "Pielonefritis (cadena de 3 reglas: R45 -> R46 -> R47)",
            ["Ardor_Orinar", "Orina_Turbia", "Fiebre", "Dolor_Lumbar"],
            "Pielonefritis",
            True,
        ),
        (
            "Dengue Hemorragico (cadena LARGA: R36 -> R37 -> R38 -> R39 -> R40, 5 reglas)",
            [
                "Fiebre", "Dolor_Articulaciones", "Sarpullido", "Dolor_Cabeza",
                "Sangrado_Encias", "Sangrado_Nasal",
            ],
            "Dengue_Hemorragico",
            True,
        ),
        (
            "Tuberculosis (cadena de 2: R15 -> R16)",
            ["Tos_Persistente", "Sudor_Nocturno", "Perdida_Peso"],
            "Tuberculosis",
            True,
        ),

        # ---------- CASOS QUE DEBEN RETORNAR False ----------
        (
            "Neumonia con sintomas insuficientes (falta Dificultad_Respiratoria)",
            ["Fiebre", "Tos"],
            "Neumonia",
            False,
        ),
        (
            "Malaria no derivable desde sintomas respiratorios basicos",
            ["Fiebre", "Tos", "Dolor_Cabeza"],
            "Malaria",
            False,
        ),
        (
            "Dengue Hemorragico sin sangrado (falta Sindrome_Hemorragico)",
            ["Fiebre", "Dolor_Articulaciones", "Sarpullido", "Dolor_Cabeza"],
            "Dengue_Hemorragico",
            False,
        ),
    ]

    pasados = 0
    fallidos = []
    for i, (desc, sintomas, obj, esp) in enumerate(casos, start=1):
        if ejecutar_caso(motor, i, desc, sintomas, obj, esp):
            pasados += 1
        else:
            fallidos.append((i, desc))

    print("\n" + "=" * 70)
    print(f"RESUMEN: {pasados}/{len(casos)} casos pasaron")
    if fallidos:
        print("Casos fallidos:")
        for num, desc in fallidos:
            print(f"  - Caso {num}: {desc}")
        sys.exit(1)
    else:
        print("Todos los casos pasaron correctamente.")
        sys.exit(0)


if __name__ == "__main__":
    main()
