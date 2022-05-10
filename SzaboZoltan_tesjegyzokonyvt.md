# Teszt jegyzőkönyv
#### Készítette: WIP - Szabó Zoltán

Lépés | Funkció | Tesztelés leírása | Státusz | Megjegyzés | Aláírás | Időpont
--- | --- | --- | --- | --- | --- | --- 
1 | Új Kurzus rögzítése adminként felület megjelenése | Az oldal sikeresen megjelenik | Siker | - | Szabó Zoltán | 2021.12.12
2 | Új Kurzus rögzítése adminként | Helyes adatokkal ezek feltöltése | Siker | A kurzusokre válaszokat javasolt lenne szövegként is eltárolni | Szabó Zoltán | 2021.12.12
4 | kurzus felvétele az adatbázisba | Ezen az oldalon a megfelelő gombra kattintva eltárolja azt, hogy vannak új kérdőívek | Siker | - | Szabó Zoltán | 2021.12.12
5 | kurzusok megjelenítése | kurzusok megjelennek, minden kitöltendő kérdőívet olvashatóan, átláthatóan lehet értelmezni | Siker | - | Szabó Zoltán | 2021.12.12
6 | kurzusok megjelenítése kurzusütközés esetén | kurzusok megjelennek, minden megválaszolt kérdőívet olvashatóan, átláthatóan lehet értelmezni akkor is, ha kurzusütközés történik | Sikertelen | Egybe folyik a szöveg elválasztás nélkül | Szabó Zoltán | 2021.12.12
7 | kurzusok megjelenítése kurzusütközés esetén (új teszt) | kurzusok megjelennek, minden megválaszolt kérdőívet olvashatóan, átláthatóan lehet értelmezni akkor is, ha kurzusütközés történik | Sikeres | Egy [Enter] hiány volt] | Szabó Zoltán | 2021.12.12
8 | Regisztráció | A regisztrációs oldal megjelenik | Siker | - | Szabó Zoltán | 2021.12.12
9 | Regisztráció | A regisztráció rossz adatok esetén nem működik | Siker | - | Szabó Zoltán | 2021.12.12
10 | Regisztráció | Helyes adatok esetén, minden mező kitöltése esetén a regisztráció sikeres | Siker | - | Szabó Zoltán | 2021.12.12
11 | kurzus megválaszolás | A kurzus megválaszoló oldal megjelenik, listázza a kurzusokat | Sikertelen | A hibát az SQL kód helytelen szintaxisa okozta | Szabó Zoltán | 2021.12.12
12 | kurzus megválaszolás | A felhasználó sikeresen meg tudja válaszolni a kurzusokat | Siker | - | Szabó Zoltán | 2021.12.12
13 | Admin felület | A felhasználók hibamentesen vannak listázva | Sikertelen | A bejelentkezett admin felhasználót is kilistázta, hibás volt a lekérdezés | Szabó Zoltán | 2021.12.12
14 | Admin felület | A felhasználókat lehet törölni az adatbázisból | Siker | - | Szabó Zoltán | 2021.12.12
15 | Admin felület | Új témát, kérdőívet és kurzust lehet hozzáadni az adatbázishoz | Siker | - | Szabó Zoltán | 2021.12.12
16 | Oldal fejléc megjelenése | A fejléc reszponzív | Siker | - | Szabó Zoltán | 2021.12.12
17 | Oldal fejléc megjelenése | Adott oldalon levő menüpont osztály aktívvá tétele | Sikertelen | feltételeket kellett beletenni, hogy működjön | Szabó Zoltán | 2021.12.12
18 | Oldal fejléc megjelenése | Minden oldal elérhető ami a menüponton található | Siker | - | Szabó Zoltán | 2021.12.12
19 | Bejelentkezés | A bejelentkező oldal megjelenik | Siker | - | Szabó Zoltán | 2021.12.12
20 | Bejelentkezés | A bejelentkezés rossz adatok esetén nem működik | Siker | - | Szabó Zoltán | 2021.12.12
21 | Bejelentkezés | Helyes adatok esetén a bejelentkezés sikeres | Siker | - | Szabó Zoltán | 2021.12.12
22 | Bejelentkezés | Oldal betöltés sikertenel bejelentkezés után | Sikertelen | szintaktikai hiba miatt az oldal nem töltött be egy másikra | Szabó Zoltán | 2021.12.12
23 | Bejelentkezés | Bejelentkezés után a bejelentkező adatai elmentődnek | Siker | külön változókban van eltárolva a felhasználók adatai | Szabó Zoltán | 2021.12.12
24 | Új kurzus rögzítése adminként felület megjelenése | Az oldal sikeresen megjelenik | Siker | - | Szabó Zoltán | 2021.12.12
25 | Új kurzus rögzítése adminként helytelen adatokkal | Az adatok feltöltésének nem kellene teljesülnie helytelen adatokkal | Siker | Nem írja ki, hogy nem töltötte fel. Kiírhatná. | Szabó Zoltán | 2021.12.12
26 | Új kurzus rögzítése adminként helytelen adatokkal figyelmeztetés | Az adatok feltöltésének nem kellene teljesülnie helytelen adatokkal | Siker | Nem figyelmeztet, hogy nem töltött fel semmit | Szabó Zoltán | 2021.12.12
27 | kurzus felvétele az kurzusokbe | Ezen az oldalon a megfelelő gombra kattintva eltárolja az adatbázisban, hogy nekem van ilyen órám | Siker | - | Szabó Zoltán | 2021.12.12
28 | Megválaszolt kurzusok megjelenítése | kurzus megjelenik, minden megválaszolt kérdőívet olvashatóan, átláthatóan lehet értelmezni | Siker | - | Szabó Zoltán | 2021.12.12
29 | Megválaszolt kurzusok megjelenítése kurzusütközés esetén | kurzus megjelenik, minden megválaszolt kérdőívet olvashatóan, átláthatóan lehet értelmezni akkor is, ha kurzusütközés történik | Sikertelen | Egybe folyik a szöveg elválasztás nélkül | Szabó Zoltán | 2021.12.12
30 | Megválaszolt kurzusok megjelenítése kurzusütközés esetén (új teszt) | kurzusok megjelenik, minden megválaszolt kérdőívet olvashatóan, átláthatóan lehet értelmezni akkor is, ha kurzusütközés történik | Sikeres | Egy [Enter] hiány volt | Szabó Zoltán | 2021.12.12
31 | Tárgy törlése jogosultság nélkül | Az oldal nem jelenik meg az admin jog hiányában | Siker | - | Szabó Zoltán | 2021.12.13
32 | Tárgy törlése jogosultsággal | Az oldal megfelelően működik | Siker | - | Szabó Zoltán | 2021.12.13
33 | kurzus törlése a rendszerből, ami fel van véve az kurzusrendbe | SQL hiba | Sikertelen | A hibát a kapcsolótábla okozta, először onnan kell törölni | Szabó Zoltán | 2021.12.13
34 | kurzus törlése a rendszerből, ami fel van véve az kurzusrendbe | SQL hiba javítva | Siker | - | Szabó Zoltán | 2021.12.13
35 | Adott kurzus adatainak szerkesztése | A szerkesztés megfelelően működött | Siker | - | Szabó Zoltán | 2021.12.13
36 | Adott kurzus adatainak szerkesztése jogosultásgok nélkül | A szerkesztés menüpont nem elérhető felhasználóként| Siker | - | Szabó Zoltán | 2021.12.13
37 | Adott kurzus adatainak szerkesztése string tipusú idvel | Az oldal ellenőrizte, hogy a paraméterként kapott id int-e| Siker | - | Szabó Zoltán | 2021.12.13
38 | Adott kurzus adatainak szerkesztése negatív idvel | A negatív paraméter kezelve volt | Sikeres | Paraméter vizsgálattal könnyen megoldható | Szabó Zoltán | 2021.12.14
39 | Adott kurzus adatainak szerkesztése negatív idvel | A negatív számok vizsgálata hozzáadva a paraméterhez  | Siker | - | Szabó Zoltán | 2021.12.14
40 | Felhasználói adatok szerkesztése, jelszó változtatása | Jelszó változtatás | Siker | - | Szabó Zoltán | 2021.12.14 
41 | Felhasználói adatok szerkesztése, email változtatása | Email változtatás | Siker | Az email cím változtatás megtörtént, a régi email cím mező nem frissül | Szabó Zoltán | 2021.12.14 
42 | Register| Regisztráció hibás adatokkal várva az újratöltést a beírt adatokkal együtt| Sikeres | Az általam beírt felhasználónév vissza került a felhasználónév mezőbe sikertelen regisztráció során| Szabó Zoltán | 2022.05.09
44 | Register-> login| A sikeres regisztráció átirányít a login oldalra | Sikeres | | Szabó Zoltán| 2022.05.09
45 | Login regisztráció után| A sikeres regisztráció átirányít a login oldalra ezt követően a login oldalon a regisztrált felhasználónév megjelenik így azt nem kell beírni. | Sikeres | | Szabó Zoltán| 2022.05.09
