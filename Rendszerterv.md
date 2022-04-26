## 1. Rendszer célja

A rendszer egy Elearning weblap. A funkciók amiket meg kell valósítanunk azok a regisztráció tanulóknak és diákoknak. Az oldal csak regisztráció és belépés után lesz elérhető. Azt hogy valaki tanár lehessen az admin tudja csak módosítani. A tanároknak lehetőségük van kurzusokat hozzáadni, szerkeszteni, törölni. A tanárok tanulókat tudnak hozzáadni a kurzusokhoz. A tanár gombra kattintva kilistázzuk a tanárokat, illetve a tanulók gombra kilistázzuk a tanulókat. A profil gomba kattintva megjelenik az adott tanuló vagy tanár felhasználó neve, az hogy tanár vagy diák, illetve a csatlakozás időpontja. A tanulóknak lehetőséget biztosítunk a tanárok és a kurzusok értékelésére.

## 2. Projektterv

1. Projektszerepkörök:
  * Termék tulajdonos: Husi (teljes csapat)
2. Projektmunkások és felelősségek:
  * Backend munkálatok: Csapat tagjai
  * Frontend munkálatok: Csapat tagjai Feladatuk: adatbázis létrehozása az adatok tárolásához, megfelelő funkciók elkészítése az oldal megfelelő működésének érdekében, felhasználói   felület kialakítása.
3. Ütemterv:
  1. Követelmény specifikáció
  2. Funkcionális specifikáció
  3. Rendszerterv
  4. Adatbázis kialakítása
  5. Backend funkciók elkészítése
  6. Frontend design megtervezése
  7. Felhasználói felület kialakítása

## 3. Üzleti folyamatok modellje

![Üzleti modell](../Dokumentacio/Képek/Umodell.PNG)

## 4. Követelmények

**Funkcionális követelmények**
  - **Tanárok, tanulók adatainak tárolása**
  - **Tanárok, tanulók tudják változtatni adataikat**
  - **Kurzusok tárolása**
  - **Reszponzív webes alapú megjelenítés**
  - **Adminisztrátor tudja szerkeszteni, hogy ki tanuló illetve ki tanár**
  - **A tanárok képesek kurzusokat hozzáadni, törölni, szerkeszteni**
  - **A tanulók képesek megtekinteni a kurzusokat**

  **Nem funkcionális követelmények**
  - **A Tanárok, tanulók nem férnek hozzá egymás adataihoz**


## 5. Funkcionális terv

  **Rendszerszereplők:**
  - **Adminisztrátor**
  - **Tanuló**
  - **Tanár**

  **Rendszerhasználati esetek és lefutásaik:**
  - **Adminisztrátor**
    - **Képes felhasználókat törölni**
    - **Tudja módosítani a felhasználók jelszavát és adatait is**
    - **Látja az összes regisztrált felhasználót**
    - **Módosítani tudja a kurzusokat**
    - **Teljes hozzáférése van a rendszerhez**
  - **Tanár**
    - **Kurzusokat tud hozzáadni, törölni, módosítani**
    - **Módosíthatja a saját adatait**
    - **Módosíthatja jelszavát**
    - **Tanulókat tud hozzárendelni kurzusokhoz**
  - **Tanuló**
    - **Módosíthatja a saját adatait**
    - **Módosíthatja jelszavát**
    - **Meg tudja tekinteni a kurzusokat**
    - **Értékelést tud küldeni tanárokról és kurzusokról**
    

  - **Menü-hierarchiák:**
    - **Bejelentkezés**
    - **Regisztráció**
    - **Főoldal**

    - **Bejelentkezés után:**
      - **Tanárok/tanulók listája:** kizárólag admin joggal rendelkező felhasználóknak
      - **Kurzus módosítás/hozzáadása/szerkesztése:** Tanárok és admin joggal rendelkező felhasználóknak

      - **Kurzusok**
      - **Profil**
      - **Kijelentkezés**

## 6. Fizikai környezet
  - **Az alkalmazás csak web platformra készül.**
  - **Nincsenek megvásárolt komponensek.**
  - **Fejlesztői eszközök:**
    - **Pycharm**
    - **Notepad++**


## 7. Architekturális terv

A rendszerhez szükség van egy adatbázis szerverre, ebben az esetben Sqlite-ot használunk, ebbe visszük fel a tanulók, tanárok, kurzusok listáját. A backend django alapú. A bootstrap, a CSS keretrendszer felel a reszponzív webdesign-ért.

## 8. Adatbázis terv

**DSL**
```
class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    registration_date = models.DateField()
    num_of_published_courses = models.IntegerField()
    num_of_enrolled_students = models.IntegerField()
    average_review_rating = models.FloatField()
    num_of_reviews = models.IntegerField()


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    registration_date = models.DateField()
    num_of_courses_enrolled = models.IntegerField()
    num_of_courses_completed = models.IntegerField()


class Course(models.Model):
    course_title = models.CharField(max_length=200)
    course_brief = models.CharField(max_length=4000)
    instructor_id = models.IntegerField()
    num_of_chapters = models.IntegerField()

    def get_absolute_url(self):
        return reverse('course-list')


class CourseChapter(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=100)


class Enrollment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()


class ContentType(models.Model):
    content_type = models.CharField(max_length=20)


class CourseChapterContent(models.Model):
    course_chapter_id = models.ForeignKey(CourseChapter, on_delete=models.CASCADE)
    content_type_id = models.ForeignKey(ContentType, on_delete=models.CASCADE)


class LearningProgress(models.Model):
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    course_chapter_content_id = models.ForeignKey(CourseChapterContent, on_delete=models.CASCADE)
    status = models.CharField(max_length=1)


class Feedback(models.Model):
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    rating_score = models.IntegerField()
    feedback_text = models.CharField(max_length=4000)
    submission_date = models.DateField()




```
**UML**
<br>
![Adatbázis terv](../Dokumentacio/Képek/Adatbázis.PNG)

## 9. Implementációs terv

A webes felület HTML, CSS és python nyelven fog készülni. A különböző technológiákat amennyire lehet, külön fájlokba írva készítjük el, úgy csatoljuk egymáshoz. Így átláthatóbb, könnyebben változtatható és bővíthető lesz. tanulók, tanárok, kurzusok listáját egy Sqlite adatbázisban fogjuk tárolni. A reszponzív webdesign-t Bootstrap-pel fogjuk biztosítani.

## 10. Tesztterv

Az alább leírt tesztelések célja a rendszer és funkcióinak teljes körű vizsgálata, ellenőrzése a megfelelő működés érdekében.

Linkek, gombok tesztelése: a teszt célja a weboldalon megjelenő linkek és gombok megfelelő működésének ellenőrzése.
A weboldal és az adatbázis kapcsolatának vizsgálata: fel kell tudnia tölteni az adatbázist a megfelelő adatokkal és vissza kell tudnia adni azokat. Törlési, hozzáadási, módosítási műveletek tesztelése. A jelszavak megfelelő tárolásának ellenőrzése, vagyis minden jelszó titkosításának (hashelésének) ellenőrzése.
Hibás, hiányos adatok esetén adott hibaüzenetek ellenőrzése.
Kiléptető rendszer tesztelése, egy nap után ki kell jelentkeztetnie a felhasználót.
A weboldal helyes működésének ellenőrzése különböző böngészőkben pl. Firefox, Google Chrome…

## 11. Telepítési terv

1. Python telepítése
2. Django telepítése
2. Sqlite telepítése
3. Forráskód importálása
4. Sqlite importálása

1. Webserver bérlése
2. Forráskód Importálása
3. Adatbázis importálása

## 12. Karbantartási terv

A tanulók értékelés formájában tudják jelenteni a felmerűlő funkcionális hibákat és az adminok tudják javítani. <br>
A javított hibák egy oldalon Changelog vagy hír formában meg fognak jelenni visszajelzésként a felhasználók felé, az új funkciók / frissítésekkel együtt.
