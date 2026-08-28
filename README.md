## Funciones investigadas

* **`head()`**: Esta función nos permite visualizar las primeras filas de un DataFrame (por defecto muestra las primeras 5). Es muy útil para darle una vista previa rápida a los datos, verificar el nombre de las columnas y asegurarnos de que la estructura del archivo se cargó correctamente.

* **`info()`**: Muestra un resumen general de la estructura del DataFrame. Nos entrega información sobre el número total de filas y columnas, los nombres de cada columna, el tipo de dato que contiene cada una (enteros, flotantes, texto, etc.) y la cantidad de valores no nulos que existen, lo que ayuda a identificar rápidamente si faltan datos.

* **`shape`**: A diferencia de las demás, no es una función sino una propiedad/atributo del DataFrame que devuelve una tupla con las dimensiones del conjunto de datos en formato `(filas, columnas)`. Nos sirve para conocer al instante el tamaño total de nuestro dataset sin procesar todo el contenido.

* **`isnull().sum()`**: Es la combinación de dos métodos que nos permite contar cuántos valores nulos o faltantes (`NaN`) existen en cada columna del DataFrame. `isnull()` detecta qué celdas están vacías devolviendo `True` o `False`, y `.sum()` suma todos esos valores verdaderos para darnos el total exacto de datos faltantes por columna.

* **`Numero de Filas y Columnas`**: (891,12)

* **`Columnas con valores vacios y cantidad`**:
<<<<<<< HEAD
=======
| Columnas    | Valores Vacios |
|-------------|----------------|
| PassengerId |        0       |
| Survived    |        0       |
| Pclass      |        0       |
| Name        |        0       |
| Sex         |        0       |
| Age         |       177      |
| SibSp       |        0       |
| Parch       |        0       |
| Ticket      |        0       |
| Fare        |        0       |
| Cabin       |       687      |
| Embarked    |        2       |

>>>>>>> 74de18eb96aba0be048c8576862edf81163bde1d
| `PassengerId` | 0 |
| `Survived` | 0 |
| `Pclass` | 0 |
| `Name` | 0 |
| `Sex` | 0 |
| `Age` | 177 |
| `SibSp` | 0 |
| `Parch` | 0 |
| `Ticket` | 0 |
| `Fare` | 0 |
| `Cabin` | 687 |
| `Embarked` | 2 |

* **`¿Qué hace fillna()?`**:

La función fillna() de Pandas sirve para reemplazar los valores vacíos o nulos (NaN) de un DataFrame.

En este proyecto se utilizó para completar los valores faltantes de la columna Age utilizando el promedio de las edades:

df["Age"] = df["Age"].fillna(df["Age"].mean())

De esta manera, los valores que estaban vacíos en Age son reemplazados por el promedio de las edades disponible

* **`¿Qué hace drop()?`**:
La función drop() de Pandas sirve para eliminar filas o columnas de un DataFrame.

En este proyecto se utilizó para eliminar la columna Cabin, debido a que contiene una gran cantidad de valores vacíos:

df = df.drop("Cabin", axis=1)

El parámetro axis=1 indica que se desea eliminar una columna. Si se utilizara axis=0, se eliminarían filas.

* **`¿Cuantos pasajeros sobrevivieron vs no sobrevivieron?`**:
| Sobrevivieron | No sobrevivieron |
|-----------|-----------|
|    342    |    549    |


* **`¿Qué hace value_counts()?`**:

La función value_counts() de Pandas sirve para contar cuántas veces aparece cada valor diferente en una columna.

En este proyecto se utilizó sobre la columna Survived para conocer cuántos pasajeros sobrevivieron y cuántos no sobrevivieron:

df["Survived"].value_counts()

El resultado muestra:

* `0`: cantidad de pasajeros que **no sobrevivieron**. -_-
* `1`: cantidad de pasajeros que **sobrevivieron**.
