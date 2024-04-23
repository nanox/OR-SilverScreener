from pulp import LpProblem, LpVariable, LpBinary, lpSum, LpMaximize, LpStatus

# Define el problema de programacion lineal entera
prob = LpProblem("ProgramacionCine", LpMaximize)

# Definir las semanas y películas disponibles
semanas = [1, 2, 3, 4]  # Cuatro semanas
peliculas = range(1, 7)  # Seis películas

'''# Duración máxima de cada película en semanas
duracion_maxima = {1: 2, 2: 3, 3: 1, 4: 2, 5: 3, 6: 3}'''

# Variables de decisión
x = LpVariable.dicts("programa", 
 [(i, j, k) for i in peliculas for j in semanas for k in range(1, 5)], 
                     0, 1, LpBinary)   # cat="Binary"

# Restricciones

# Solo un programa para la película 1
prob += lpSum(x[(1, j, k)] for j in semanas for k in range(1, 5)) == 1

# Solo un programa para la película 5
prob += lpSum(x[(5, j, k)] for j in semanas for k in range(1, 5)) == 1

# Restricción para limitar el número de películas en la semana 1
prob += lpSum(x[(i, 1, k)] for i in peliculas for k in range(1, 5)) <= 2

# Restricción para limitar el número de películas en la semana 3
prob += lpSum(x[(i, 3, k)] for i in peliculas for k in range(1, 5)) <= 2


# Función objetivo: maximizar el número total de películas programadas
funcion_objetivo = 0
funcion_objetivo += lpSum(x[(i, j, k)] for i in peliculas for j in semanas for k in range(1, 3))
prob.objective = funcion_objetivo

# Resolver el problema
prob.solve()

# Imprimir resultados
print("Estado:", LpStatus[prob.status])
print("Número total de funciones programadas:", prob.objective.value())

print('\n================= Solución PuLP ===================')
print("Programación:")
for i in peliculas:
    for j in semanas:
        for k in range(1, 5):
            if x[(i, j, k)].value() == 1:
                print(f"Película {i} programada a partir de la semana {j}, se proyecta por {k} semana(s).")

print('=======================================================')