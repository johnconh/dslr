### DSLR (Data Science Logistic Regression)
El proyecto DSLR consiste en implementar desde cero un modelo de clasificación multiclase usando regresión logística con gradiente descendente. Se sigue el enfoque "one-vs-all" para manejar múltiples clases (las cuatro casas de Hogwarts) y el modelo se entrena con características seleccionadas (como calificaciones en distintas materias). Finalmente, el modelo predice a qué casa pertenece un nuevo estudiante basado en sus calificaciones, utilizando los pesos obtenidos durante el entrenamiento.

Este proyecto refuerza varios conceptos clave en machine learning, como la regresión logística, gradiente descendente, y multiclase

**Preprocesamiento de Datos**
- ***Limpieza de datos:***  Antes de entrenar el modelo, necesitas asegurarte de que el conjunto de datos esté limpio. Esto implica eliminar o manejar valores faltantes. En este proyecto, puedes imputar valores faltantes con la mediana.
- ***Normalización:*** También es importante normalizar las características (calificaciones en diferentes asignaturas) para que todas las variables estén en la misma escala. Esto ayuda a que el algoritmo de gradiente descendente funcione de manera eficiente.

**Regresión Logística Multiclase (One-vs-All)**
- La regresión logística multiclase no se puede resolver directamente con la fórmula estándar de regresión logística (que es para problemas de clasificación binaria), así que se utiliza la técnica one-vs-all.
- En el enfoque one-vs-all, entrenas varios clasificadores binarios, uno para cada clase (cada casa de Hogwarts). Para cada clase, el modelo se entrena para distinguir si un estudiante pertenece a esa casa o no.

**Función de Costo y Gradiente Descendente**
- La función de costo mide el error del modelo, y en este proyecto se utiliza la función de costo logarítmica (log loss), la cual es adecuada para la regresión logística.
- Gradiente descendente es el algoritmo utilizado para minimizar esta función de costo. Se ajustan los pesos (thetas) del modelo en cada iteración, con el objetivo de encontrar los pesos que minimicen el error.

**Entrenamiendo del modelo**
- Implementas una función que entrena el modelo de regresión logística para cada clase usando el gradiente descendente. El entrenamiento devuelve los pesos óptimos para cada clase.
- Los pesos se almacenan para ser usados posteriormente en las predicciones.

**Prediccion**
- Una vez que el modelo ha sido entrenado, puedes utilizar los pesos obtenidos para hacer predicciones sobre nuevos datos (por ejemplo, del archivo dataset_test.csv). Para cada estudiante, el modelo calculará la probabilidad de que pertenezca a cada una de las casas de Hogwarts, y asignará la clase con la mayor probabilidad.