# Motor de Inferencia — Sistema Experto de Diagnóstico Médico

Sistema experto en **Python** que implementa **Encadenamiento hacia Adelante (Forward Chaining)** para diagnóstico médico. Dado un conjunto de síntomas iniciales y una hipótesis, el motor infiere si el diagnóstico es consecuencia lógica de la base de conocimiento.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-Expert_System-FF6B35?style=flat)
![Inference](https://img.shields.io/badge/Logic-Forward_Chaining-6f42c1?style=flat)

---

## Descripción

El motor carga una base de conocimiento en formato JSON (cláusulas de Horn) y aplica el algoritmo de encadenamiento hacia adelante hasta punto fijo para determinar si una hipótesis es derivable desde los hechos iniciales. Incluye una traza de explicación que detalla qué reglas se dispararon y en qué orden.

---

## Funcionalidades

- **Encadenamiento hacia adelante** hasta punto fijo con salida temprana al encontrar el objetivo
- **Base de conocimiento JSON** con 50+ reglas médicas en cláusulas de Horn
- **Traza de explicación** — muestra cada regla disparada con su resultado
- **Suite de tests** — casos de prueba cubriendo resultados positivos y negativos
- **Cero dependencias externas** — solo librería estándar de Python (`json`)

---

## Algoritmo

```
ENTRADA: hechos_iniciales (lista de síntomas), objetivo (diagnóstico a verificar)
SALIDA:  True si KB |= objetivo, False si se alcanza punto fijo sin encontrarlo

1. memoria_trabajo = set(hechos_iniciales)
2. MIENTRAS hubo_cambios:
     PARA CADA regla en base_conocimiento:
         SI antecedentes ⊆ memoria_trabajo Y consecuente ∉ memoria_trabajo:
             agregar consecuente a memoria_trabajo
             registrar en traza
             SI consecuente == objetivo → RETORNAR True
3. RETORNAR False  ← punto fijo sin objetivo
```

---

## Estructura del proyecto

```
motor-inferencia-ia/
├── proyecto_inferencia.py     # Motor de inferencia — clase MotorInferencia
├── base_conocimiento.json     # KB con 50+ reglas médicas (cláusulas de Horn)
├── test_casos.py              # Suite de casos de prueba
└── README.md
```

---

## Ejemplo de ejecución

```bash
python proyecto_inferencia.py
```

```
--- Sistema Experto de Diagnóstico ---
Síntomas iniciales: ['Fiebre', 'Tos', 'Dificultad_Respiratoria']
Objetivo a verificar: Neumonia

[R1] Fiebre AND Tos -> Infeccion_Respiratoria  ✓ NUEVO
[R2] Infeccion_Respiratoria AND Dificultad_Respiratoria -> Neumonia  ✓ OBJETIVO ALCANZADO

¿Es consecuencia lógica?: True
```

---

## Formato de la base de conocimiento

```json
{
  "reglas": [
    {
      "id": "R1",
      "antecedentes": ["Fiebre", "Tos"],
      "consecuente": "Infeccion_Respiratoria"
    },
    {
      "id": "R2",
      "antecedentes": ["Infeccion_Respiratoria", "Dificultad_Respiratoria"],
      "consecuente": "Neumonia"
    }
  ]
}
```

**Restricciones del dominio:**
- Cláusulas de Horn: N antecedentes AND → 1 consecuente positivo
- Sin ciclos en el grafo de inferencia
- Toda regla debe ser alcanzable desde síntomas reales de entrada

---

## Ejecutar los tests

```bash
python test_casos.py
```

---

## Autor

**Sebastián Velasquez**
Systems Engineering @ Pontificia Universidad Javeriana

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sebastian-velasquez-73662721a)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/Sebasve0810)

---

*Proyecto académico — Introducción a la Inteligencia Artificial | Ingeniería de Sistemas, Javeriana 2026*
