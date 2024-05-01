# 28. csapat - Blog | 3. beadandó


**Készítették:**

- Kárpáti Koppány   (AQ6K82)
- Molnár Balázs     (IPXKBK)
- Viszt Patrik      (PYAVM7)

## Használt nyelvek

**Kliens:** html, css, JavaScript

**Szerver:** Python 3.12

## Telepítés

A backend részhez használt könyvtárak:
- Flask
- Flask_CORS
- DateTime 
- SQLAlchemy
- MySQL Connector

```shell
    pip install flask
    pip install flask_cors
    pip install DateTime
    pip install sqlalchemy
    pip install mysql-connector-python
```

## Futtatás

Futtatáshoz a *server.py*-t szükséges elindítani. A frontend kezdőoldala az *index.html*. Adatbázis eléréséhez a XAMPP szükséges. Ezen belül a phpmyadmin és azon megtalálható *beadando* adatbázis. Jogosultak között kell szerepelnie egy *root* nevű felhasználónak jelszó nélkül, lokális eléréssel.

Az API eléréséhez a szerverrel a kliens a
```url
    http://127.0.0.1:5000
```
címen kommunikál.

Admin szerepköre az *admin* felhasználónak van. Jelszava: *1234*