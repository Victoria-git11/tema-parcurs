# Documentatie tema de parcurs
<br><br>
## Delimart Alexiana Cristina Victoria

<br><br><br><br><br><br><br><br><br><br><br><br>

# Documentatie pentru exercitiul `1`

## 1. **Dependente necesare Inainte de rularea programului**

Acest program este scris In limbajul **Python** si nu necesita nicio biblioteca externa. Tot ce ai nevoie este un mediu In care sa rulezi Python, cum ar fi:

 - **Python instalat pe calculator**  
   - Se descarca Python de pe [site-ul oficial Python](https://www.python.org/downloads/).
   - Se verifica instalarea deschizand terminalul (Command Prompt pe Windows sau Terminal pe macOS/Linux) si tastand:  
     ```bash
     python --version
     ```  
     Sau, daca a fost instalat Python 3:  
     ```bash
     python3 --version
     ```

 - **Editor de cod** (optional)  
   - Poate fi folosit orice editor de cod precum **Visual Studio Code**, **PyCharm**, **Sublime Text** sau chiar un editor de text simplu precum **Notepad**.

---

<br><br>

## 2. **Explicatia codului**

### **Clasa `Employee`**

Aceasta este clasa de baza pentru angajati.

- **Atribute**:  
  - `everyone`: lista care stocheaza toate instantele create din `Employee` si `Manager`, folosita pentru a parcurge mai rapid angajatii si managerii printr-un `for` la afisare.  
  - `emp_count`: variabila de clasa care tine evidenta numarului total de angajati, creeata pentru ultimul subpunct.

- **Metoda `__init__`**:  
  Constructorul clasei initializeaza `name`, `salary` si `department` pentru fiecare angajat si adauga angajatul In lista `everyone`. De asemenea, creste numarul total de angajati (`emp_count`).

- **Metoda `display_employee`**:  
  Aceasta metoda afiseaza departamentul angajatului. In contextul problemei, deoarece `X = 8` si <br>`8 % 3 = 2`, metoda afiseaza doar departamentul.

### **Clasa `Manager`**

Aceasta este o subclasa a clasei `Employee`.

- **Atribute**:    
  - `mgr_count`: variabila de clasa care tine evidenta numarului total de manageri.

- **Metoda `__init__`**:  
  Constructorul clasei `Manager` apeleaza constructorul clasei parinte `Employee` folosind `super()`. Fiecare instanta noua de `Manager` creste numarul total de manageri (`mgr_count`).

### **Crearea obiectelor**

- **8 obiecte de tip `Manager`** sunt create cu nume, salariu si departament specifice (subpunctul b), lucru indicat In cerinta problemei.  
- **2 obiecte de tip `Employee`** sunt create cu nume, salariu si departament specifice, pentru a putea observa diferenta dintre `mgr_count` si `emp_count`.

### **Afisarea datelor**

- **Bucla `for`** parcurge lista `everyone` si apeleaza metoda `display_employee` pentru fiecare angajat. Dupa afisarea managerilor, afisarea angajatilor este separata de un `print("\n   Employees:")`.

- Se afiseaza numarul total de manageri si numarul total de angajati folosind variabilele `mgr_count` si `emp_count`.

---

<br><br>

## 3. **Cum se ruleaza codul**

**Se salveaza codul Intr-un fisier `.py`**

**Se deschide terminalul**  
    Se navigheaza la folderul unde ai salvat fisierul folosind comanda `cd`. De exemplu:  

```bash
    cd C:\Users\NumeleTau\Desktop
```
**Se ruleaza codul**    
    Se introduce comanda
```bash
    python employee.py
```

Sau, daca este folosit Python 3:   
```bash
    python3 employee.py
```

**Rezultat asteptat**    
    Programul va afisa departamentele pentru toti managerii si angajatii, urmate de numarul total de manageri si angajati. Exemplu de rezultat:

```yaml
        Managers:
    Human Resources
    IT
    Design
    Contabilitate
    Publicitate
    Fizica Cuantica
    Relatii clienti
    Contabilitate
    
        Employees:
    Human Resources
    IT

        Numarul de manageri este: 8
        Numarul total de angajati este: 10
```

<br><br><br><br><br><br>


# Testarea codului `employee.py`

## 1. **Dependente necesare Inainte de rularea testelor**

Pentru a rula testele, este nevoie sa fie instalat **`pytest`**. Aceasta este o biblioteca Python pentru testarea automata.
    
**Instalarea `pytest`**  
   Daca nu este instalat `pytest`, poti sa-l instalezi folosind pip. In terminal, ruleaza comanda:  
   ```bash
   pip install pytest
   ```

**II. Verificarea instalarii**  
   Se verifica instalarea tastand:  
   ```bash
   pytest --version
   ```

---

## 2. **Structura fisierelor**

Pentru a rula corect testele, fisierele au fost organizate astfel:

```
proiect/
│-- employee.py       # Codul principal
|-- test_employee.py  # Fisierul de testare
```

---

## 3. **Explicatia codului de testare**

### **Importurile si configurarea**

```python
import pytest
from employee import Employee, Manager
```

- **Importam** clasele `Employee` si `Manager` din fisierul `employee.py`.
- **`pytest`** este biblioteca folosita pentru testare.

**Fixture: `reset_employees_and_managers`**

```python
@pytest.fixture
def reset_employees_and_managers():
    Employee.everyone = []
    Employee.emp_count = 0
    Manager.mgr_count = 0
```

- **Fixture-ul `reset_employees_and_managers`** reseteaza starile claselor `Employee` si `Manager` Inainte de fiecare test, asigurand ca testele sunt independente.

---
<br>

### **I. Testarea crearii unui `Employee`**

```python
def test_employee_creation(reset_employees_and_managers):
    emp1 = Employee("Ana", 3000, "HR")
    assert emp1.name == "Ana"
    assert emp1.salary == 3000
    assert emp1.department == "HR"
    assert Employee.emp_count == 1
    assert emp1 in Employee.everyone
```

- **Testam** daca un obiect `Employee` este creat corect cu nume, salariu si departament specificate.
- **Verificam** ca:
  - `emp1` are valorile corecte pentru `name`, `salary`, si `department`.
  - `emp_count` a fost incrementat.
  - `emp1` a fost adaugat In lista `everyone`.

---
<br>

### **II. Testarea crearii unui `Manager`**

```python
def test_manager_creation(reset_employees_and_managers):
    mgr1 = Manager("George", 50000, "IT")
    assert mgr1.name == "George"
    assert mgr1.salary == 50000
    assert mgr1.department == "IT"
    assert Manager.mgr_count == 1
    assert Employee.emp_count == 1
    assert mgr1 in Employee.everyone
```

- **Testam** daca un obiect `Manager` este creat corect.
- **Verificam** ca:
  - `mgr1` are numele, salariul si departamentul corecte.
  - `mgr_count` este incrementat.
  - `emp_count` este incrementat deoarece `Manager` mosteneste din `Employee`.
  - `mgr1` apare In lista `everyone`.

---
<br>

### **III. Testarea metodei `display_employee`**

```python
def test_display_employee(capsys, reset_employees_and_managers):
    emp1 = Employee("Mihai", 4000, "Design")
    emp1.display_employee()
    captured = capsys.readouterr()
    assert captured.out == "Design\n"
```

- **Testam** metoda `display_employee` pentru un obiect `Employee`.
- **Folosim `capsys`** pentru a captura output-ul afisat.
- **Verificam** ca output-ul este `Design` urmat de o linie noua.

---
<br>

### **IV. Testarea numarului total de angajati si manageri**

```python
def test_total_counts(reset_employees_and_managers):
    mgr1 = Manager("Andrei", 60000, "Finance")
    mgr2 = Manager("Maria", 70000, "HR")
    emp1 = Employee("Elena", 4500, "IT")
    assert Manager.mgr_count == 2
    assert Employee.emp_count == 3
```

- **Testam** daca numarul total de manageri si angajati este corect dupa crearea mai multor obiecte.
- **Verificam** ca:
  - `mgr_count` este `2` pentru manageri.
  - `emp_count` este `3` pentru totalul angajatilor.

---

## 4. **Cum se ruleaza testele**

  - **Se navigheaza la directorul proiectului**  
   ```bash
   cd proiect
   ```

   - **Se ruleaza testele cu `pytest`**  
   ```bash
   pytest test_employee.py
   ```

   - **Rezultat asteptat**  
   ```
   ======================= test session starts =======================
   collected 4 items

   test_employee.py ....

   ======================= 4 passed in 0.03s =========================
   ```
   
   <br><br><br><br>

# Documentatie pentru exercitiul `2`  

## Pasi necesari Inainte de rularea aplicatiei

### Instalare pachete Python
Pentru a rula aplicatia, asigurati-va ca aveti instalate urmatoarele pachete Python:
- `pandas` pentru manipularea datelor
- `plotly` pentru generarea graficelor interactive
- `flask` pentru crearea serverului web

Puteti instala aceste pachete folosind comanda:
```bash
pip install pandas plotly flask
```

### Structura fisierelor proiectului
Asigurati-va ca proiectul contine urmatoarele fisiere si directoare:
```
project/
│
├── app.py
├── templates/
│   └── index.html
├── static/
└── data.csv (optional)
```

## Descrierea codului principal `app.py`

### Importurile necesare
In aceasta sectiune, se aduc toate bibliotecile esentiale pentru functionarea aplicatiei:
- **`os`**: Permite manipularea cailor de fisiere si gestionarea fisierelor pe sistemul local.
- **`pandas`**: Biblioteca utilizata pentru citirea si manipularea datelor din fisierul CSV.
- **`plotly.graph_objects`**: Modulul folosit pentru a crea grafice interactive.
- **`flask`**: Framework web utilizat pentru crearea aplicatiei, gestionarea rutelor si a cererilor HTTP.

### Initializarea aplicatiei Flask
```python
app = Flask(__name__)
dir = os.path.join(app.root_path, 'static')
```
- **`Flask(__name__)`**: Creeaza o instanta a aplicatiei Flask, punctul central al aplicatiei web.
- **`os.path.join(app.root_path, 'static')`**: Defineste un director pentru fisierele statice generate de aplicatie, cum ar fi graficele HTML.

### Functionalitatea principala
Ruta principala (`@app.route("/")`) gestioneaza:
1. **Incarcarea fisierului CSV**: Utilizatorul poate Incarca un fisier utilizand formularul HTML.
2. **Citirea datelor**: Dupa Incarcare, fisierul este salvat local si citit folosind `pandas.read_csv`.
3. **Generarea graficelor**:
   - Se utilizeaza functii dedicate pentru a crea graficele pentru toate valorile, primele X valori si ultimele Y valori.
   - Graficele sunt salvate In format HTML In directorul `static`.
4. **Returnarea raspunsului**: Se trimite un sablon HTML (`index.html`) care include graficele generate.

```python
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["csv_file"]
        if file:
            filepath = os.path.join("data.csv")
            file.save(filepath)
            df = pd.read_csv(filepath)
            
            # Generarea graficelor
            fig1 = plot_all_values(df)
            fig2 = plot_first_X_values(df)
            fig3 = plot_last_Y_values(df)

            # Salvarea graficelor
            fig1.write_html(os.path.join(dir, "plot1.html"))
            fig2.write_html(os.path.join(dir, "plot2.html"))
            fig3.write_html(os.path.join(dir, "plot3.html"))

            return render_template("index.html", plot1="static/plot1.html", plot2="static/plot2.html", plot3="static/plot3.html")
    return render_template("index.html")
```

### Functiile de generare a graficelor
Fiecare functie de generare a graficelor utilizeaza biblioteca `plotly.graph_objects`.

#### Functia `plot_all_values`
```python
def plot_all_values(df):
    fig = go.Figure()
    for column in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name=column))
    fig.update_layout(title="Toate Valorile", xaxis_title="Index", yaxis_title="Values")
    return fig
```
Aceasta functie:
- Creeaza un obiect `Figure`.
- Adauga o trasare (`Scatter`) pentru fiecare coloana din DataFrame-ul CSV, reprezentand valorile coloanelor pe axa Y si indexul pe axa X.
- Seteaza titlul graficului si etichetele axelor.

#### Functia `plot_first_X_values`
```python
def plot_first_X_values(df):
    fig = go.Figure()
    for column in df.columns:
        fig.add_trace(go.Scatter(x=df.head(8).index, y=df.head(8)[column], mode='lines', name=column))
    fig.update_layout(title="Primele X Valori", xaxis_title="Index", yaxis_title="Values")
    return fig
```
Aceasta functie:
- Filtreaza primele 8 randuri ale DataFrame-ului folosind `df.head(8)`.
- Creeaza un grafic similar cu cel pentru toate valorile, dar include doar primele randuri.

#### Functia `plot_last_Y_values`
```python
def plot_last_Y_values(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.tail(24).index, y=df.tail(24)['Durata'], mode='lines', name="Durata"))
    fig.add_trace(go.Scatter(x=df.tail(24).index, y=df.tail(24)['Puls'], mode='lines', name="Puls"))
    fig.update_layout(title="Ultimele Y Valori", xaxis_title="Index", yaxis_title="Values")
    return fig
```
Aceasta functie:
- Selecteaza ultimele 24 de randuri din DataFrame (`df.tail(24)`).
- Adauga trasari separate pentru coloanele `Durata` si `Puls`.
- Configureaza titlul si etichetele.

### Pornirea aplicatiei
```python
if __name__ == "__main__":
    app.run(debug=True)
```
- Aplicatia Flask este pornita In modul **debug**, ceea ce permite detectarea automata a modificarilor si afisarea erorilor In detaliu.

### Descrierea sablonului `index.html`

Pagina HTML este construita astfel Incat sa Indeplineasca urmatoarele functionalitati:

1. **Afisarea unui formular pentru Incarcarea fisierului CSV**
   ```html
   <form action="/" method="post" enctype="multipart/form-data">
       <input type="file" name="csv_file" accept=".csv" required>
       <input type="submit" value="Upload and Plot">
   </form>
   ```
   - **`<form>`**: Definitia unui formular care trimite date catre ruta principala (`/`).
   - **`method="post"`**: Specifica metoda HTTP utilizata (POST pentru trimiterea fisierelor).
   - **`enctype="multipart/form-data"`**: Permite trimiterea fisierelor binare (CSV).
   - **`<input type="file">`**: Adauga un selector de fisiere.
   - **`<input type="submit">`**: Creeaza un buton pentru trimiterea formularului.

2. **Afisarea graficelor generate**
   Graficele sunt afisate doar daca acestea exista, folosind sintaxa Jinja2 pentru conditionare.

   #### Afisarea graficului pentru toate valorile
   ```html
   {% if plot1 %}
       <h2>Toate Valorile</h2>
       <iframe src="{{ plot1 }}" width="100%" height="600px"></iframe>
   {% endif %}
   ```
   - **`{% if plot1 %}`**: Verifica daca exista o cale catre primul grafic.
   - **`<h2>`**: Titlul sectiunii.
   - **`<iframe>`**: Un cadru HTML care afiseaza graficul generat. Parametrii `width` si `height` controleaza dimensiunea.

   #### Afisarea graficului pentru primele X valori
   ```html
   {% if plot2 %}
       <h2>Primele X Valori</h2>
       <iframe src="{{ plot2 }}" width="100%" height="600px"></iframe>
   {% endif %}
   ```
   Functionalitate similara cu cea pentru `plot1`, dar afiseaza graficul cu primele X valori.

   #### Afisarea graficului pentru ultimele Y valori
   ```html
   {% if plot3 %}
       <h2>Ultimele Y Valori</h2>
       <iframe src="{{ plot3 }}" width="100%" height="600px"></iframe>
   {% endif %}
   ```
   Urmeaza aceeasi structura, afisand al treilea grafic.

3. **Structura generala**
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>CSV Plotter</title>
   </head>
   <body>
       <h1>Upload CSV File</h1>
       ...
   </body>
   </html>
   ```
   - **`<html>`**: Specifica Inceputul documentului HTML.
   - **`<head>`**: Contine metadatele paginii, inclusiv titlul si setarile de codificare.
   - **`<body>`**: Sectiunea vizibila a paginii unde se definesc formularul si graficele.

## Rularea aplicatiei
Pentru a rula aplicatia, executati comanda:
```bash
python app.py
```

Accesati [http://127.0.0.1:5000](http://127.0.0.1:5000) In browserul dvs. pentru a utiliza aplicatia.

---
<br><br>

# Referinte

### Referintele recomandate in tema

- https://www.w3schools.com/python/pandas/default.asp
- https://www.w3schools.com/python/matplotlib_intro.asp
- calp.python.extras de la Files > Class.Materials
- https://code.visualstudio.com/docs/python/tutorial-flask
- https://github.com/microsoft/python-sample-vscode-flask-tutorial
- https://github.com/crchende/ppyan2
- https://code.visualstudio.com/docs/python/tutorial-django
- https://www.w3schools.com/django/index.php
- https://code.visualstudio.com/docs/python/testing
- https://www.tutorialspoint.com/pytest/index.htm

### Markdown

- https://gist.github.com/allysonsilva/85fff14a22bbdf55485be947566cc09e
- https://blog.markdowntools.com/posts/using-nested-lists-and-sub-bullets-in-markdown

### Plotly
- https://stackoverflow.com/questions/63012167/plot-using-go-scatter-with-entire-dataframe
- https://plotly.com/python/graph-objects/

### Passing data from flask to HTML
 - https://stackoverflow.com/questions/51669102/how-to-pass-data-to-html-page-using-flask
