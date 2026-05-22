# Proyecto Aplicativo 3 — Motor de Inferencia (Intro IA)

## Contexto del proyecto
Sistema experto de diagnóstico médico basado en **Encadenamiento hacia Adelante (Forward Chaining)**.
Curso: Introducción a la Inteligencia Artificial — Pontificia Universidad Javeriana.

## Estructura de archivos
```
proyecto-ia/
├── CLAUDE.md                  ← este archivo
├── proyecto_inferencia.py     ← motor de inferencia (esqueleto entregado por el profesor)
├── base_conocimiento.json     ← KB en JSON (debe tener mínimo 50 reglas al final)
└── test_casos.py              ← casos de prueba (por crear)
```

## Stack
- Python 3.x (sin librerías externas, solo `json` de la stdlib)
- Formato de KB: JSON plano

## Reglas del dominio (restricciones del enunciado)
1. **Cláusulas de Horn**: cada regla tiene N antecedentes unidos por AND y UN solo consecuente positivo.
2. **Sin ciclos**: no puede existir A→B y B→A (ni ciclos más largos).
3. **Alcanzabilidad**: toda regla debe poder activarse desde algún síntoma de entrada real.
4. **Mínimo 50 reglas** con interdependencia (hechos intermedios obligatorios).

## Algoritmo a implementar — ejecutar_inferencia()
```
ENTRADA: hechos_iniciales (lista), objetivo (string)
SALIDA:  True / False

1. memoria_trabajo = set(hechos_iniciales)
2. hubo_cambios = True
3. MIENTRAS hubo_cambios:
     hubo_cambios = False
     PARA CADA regla en self.reglas:
         SI regla.antecedentes ⊆ memoria_trabajo:
             SI regla.consecuente NO ESTÁ en memoria_trabajo:
                 memoria_trabajo.add(regla.consecuente)
                 hubo_cambios = True
                 registrar en traza de explicación
                 SI regla.consecuente == objetivo:
                     RETORNAR True
4. RETORNAR False   # punto fijo alcanzado sin encontrar objetivo
```

## Entregables requeridos
- [ ] `ejecutar_inferencia()` completamente implementada
- [ ] `base_conocimiento.json` con ≥ 50 reglas, auditadas lógicamente
- [ ] Traza de explicación impresa en consola (qué regla activó qué hecho)
- [ ] `test_casos.py` con mínimo 3 casos de prueba distintos (True y False)

## Convenciones de código
- Nombres de hechos en `Snake_Case` con mayúscula inicial: `Fiebre`, `Infeccion_Respiratoria`
- IDs de reglas: `R1`, `R2`, ... `R50`
- Comentarios en español
- No usar librerías externas

## Comportamiento esperado en consola
```
--- Sistema Experto de Diagnóstico ---
Síntomas iniciales: ['Fiebre', 'Tos', 'Dificultad_Respiratoria']
Objetivo a verificar: Neumonia

[R1] Fiebre AND Tos -> Infeccion_Respiratoria  ✓ NUEVO
[R2] Infeccion_Respiratoria AND Dificultad_Respiratoria -> Neumonia  ✓ OBJETIVO ALCANZADO

¿Es consecuencia lógica?: True
```
