# Instalacja głównych komponentów 

## Instalacja Javy 

Aby odwzorować "docelowe" środowisko potrzebujemy Javy (JDK) w wersji 11.X. Dla przykładu:
```
https://adoptium.net/temurin/releases/?version=11&arch=x64&package=jdk&os=windows
```

## Instalacja Sparka 

Potrzebujemy Apache Spark 3.5.X dla Apache Hadoop 3.3
```
https://spark.apache.org/downloads.html
```

Pakiet wskazanego oprogramowania pobieramy i rozpakowujemy np. do katalogu 
```
C:\Programy\spark-3.5.2-bin-hadoop3
```

## Instalacja Apache Hadoop

a.	`winutils` (w przypadku środowiska *Windows*)
```
https://github.com/cdarlint/winutils
```

b.	*Apache Hadoop 3.3.6* (w przypadku środowiska *Linux*)
```
https://hadoop.apache.org/releases.html
```

Pakiet wskazanego oprogramowania pobieramy i rozpakowujemy np. do katalogu 
```
C:\Programy\winutils\hadoop-3.3.6
```

## Zmienne środowiskowe 

Dla wszystkich powyższych składników definiujemy zmienne środowiskowe:

- `JAVA_HOME` (np. `C:\Program Files\Eclipse Adoptium\jdk-11.0.24.8-hotspot`)
- `SPARK_HOME` (np. `C:\Programy\spark-3.5.2-bin-hadoop3`)
- `HADOOP_HOME` (np. `C:\Programy\winutils\hadoop-3.3.6`)


Dodatkowo do zmiennej `PATH` dodajemy 

- `%JAVA_HOME%\bin`
- `%HADOOP_HOME%\bin`
- `%SPARK_HOME%\bin`

# Python

Instalujemy Pythona w wersji odpowiedniej dla naszego Sparka np. 3.11.8

## Sprawdzenie 

Koniecznie sprawdzamy dostępność zainstalowanych komponentów

Dla przykładu:
```
C:\Users\kjankiewicz>where java
C:\Program Files\Eclipse Adoptium\jdk-11.0.24.8-hotspot\bin\java.exe

C:\Users\kjankiewicz>where hadoop
C:\Programy\winutils\hadoop-3.3.6\bin\hadoop
C:\Programy\winutils\hadoop-3.3.6\bin\hadoop.cmd

C:\Users\kjankiewicz>where pyspark
C:\Programy\spark-3.5.2-bin-hadoop3\bin\pyspark
C:\Programy\spark-3.5.2-bin-hadoop3\bin\pyspark.cmd

C:\Users\kjankiewicz>py --version
Python 3.11.9
```

# Konfiguracja wirtualnego środowiska

1. Utwórz katalog dla naszych projektów dla przykładu 

```
mkdir C:\Projekty\BigDataKJCourses\SparkProjectsNoGCP
```

2. W terminalu przejdź do tego katalogu 

```
cd C:\Projekty\BigDataKJCourses\SparkProjectsNoGCP
```

3. Utwórz wirtualne środowisko, aby za jego pomocą zarządzać potrzebnymi zależnościami. Spowoduje to utworzenie katalogu `venv` w bieżącym katalogu, gdzie przechowywane będą wszystkie zależności.

```
python -m venv venv
```

4. Aktywuj wirtualne środowisko:

```
.\venv\Scripts\activate
```

5. Dokonaj akualizacji pakietu `pip`

```
python.exe -m pip install --upgrade pip
```

6. Następnie, zainstaluj wymagane pakiety. 

```
pip install pyspark
```

# Visual Studio Code

## Konfiguracja 

Po utworzeniu i aktywowaniu wirtualnego środowiska, *VS Code* automatycznie je wykryje, wystarczy, że otworzysz w nim utworzony katalog zawierający wirtualne środowisko. 
Jeśli jednak chcesz ręcznie wskazać środowisko:
* Otwórz paletę poleceń (*Ctrl+Shift+P*) i wpisz `Python: Select Interpreter`.
* Wybierz odpowiedni interpreter z listy (*VS Code* powinien pokazać ścieżkę do utworzonego wirtualnego środowiska).
* W przypadku otwierania nowego projektu w przyszłości, pamiętaj, aby ponownie aktywować wirtualne środowisko i wskazać je w *VS Code*.

## Uruchomienie pierwszego programu

1. Utwórz w otwartym przed chwilą katalogu nowy plik Pythona np.: `MyFirst.py`

2. Wprowadź do niego poniższy kod. W założeniu, w katalogu `C:\Programy\spark-3.5.2-bin-hadoop3` został rozpakowany *Apache Spark*

```
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.json("C:\Programy\spark-3.5.2-bin-hadoop3\examples/src/main/resources/people.json")
# Displays the content of the DataFrame to stdout
df.show()

spark.stop()
```

3. Uruchom nasz pierwszy program.

# Notatnik Jupyter w ramach Visual Studio Code

## Konfiguracja

1. Mając aktywne środowisko wirtualne dodaj kolejny pakiet 

```
pip install ipykernel
```

## Uruchomienie 

1. Utwórz w *VS Code* nowy plik będący notatnikiem Jupyter np: `MyFirst.ipynb`

2. W pierwszym paragrafie wprowadź poniższy kod 

```
from pyspark.sql import SparkSession
```

3. Uruchom go

4. Możesz  wprowadzić kolejne paragrafy 

```
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
```

```
df = spark.read.json("C:\Programy\spark-3.5.2-bin-hadoop3\examples/src/main/resources/people.json")
```

```
df.show()
```

5. Pamiętaj, że w czasie gdy sesja Sparka jest aktywna, dostępny jest jej interfejs sieciowy 
```
# Uzyskanie adresu interfejsu webowego
spark_ui_url = spark.sparkContext.uiWebUrl

print(f"Spark UI is available at: {spark_ui_url}")
```

# Finał 

1. Aby wyjść z aktywowanego wirtualnego środowiska venv w Pythonie, wystarczy wpisać w terminalu poniższe polecenie:

```
deactivate
```