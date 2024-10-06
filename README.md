Picoyap on keskustelusovellusprojektini web-ohjelmointikurssia varten. Se koostuu "femtoyapeista" eli keskustelualueista, joilla on eri aiheet. Femtoyapit koostuvat ketjuista, ja ketjut puolestaan koostuvat viesteistä. (Ohjelman sisäisesti aion myös varmaan käyttää ketjusta nimitystä "attoyap" ja viestistä "zeptoyap".) Käyttäjät ovat joko peruskäyttäjiä tai ylläpitäjiä. Tässä vielä sovellukseen suunnitteilla olevista ominaisuuksista pari listaa:

Varmasti tulevat:
- sovelluksen etusivulla on lista femtoyapeista, ja kussakin näkyy ketjujen ja viestien lukumäärät sekä uusimman viestin ajankohta
- käyttäjä voi luoda uuden tunnuksen
- käyttäjä voi kirjautua sisään ja ulos
- käyttäjä voi luoda femtoyapiin uuden ketjun antamalla ketjulle otsikon ja aloitusviestin
- käyttäjä voi luoda ketjuun uuden viestin
- käyttäjä voi muokata ja poistaa omia ketjuja ja viestejä
- käyttäjä voi etsiä kaikki viestit, joiden osana on antamansa sana
- ylläpitäjä voi lisäksi lisätä ja poistaa femtoyapeja
- ylläpitäjä voi luoda salaisen femtoyapin ja määrittää, keillä on pääsy kyseiseen femtoyapiin.

Ehkä:
- käyttäjän hakusana voi ottaa huomioon taivutetut muodot viestien hakemisessa
- käyttäjä voi hakea viestejä myös viestin lähettäjän ja ajankohdan perusteella.

-------------------------------

OHJEET TESTAAMISEEN:

Sovellusta ei voi testata Fly.io-palvelussa. Tässä ohjeet paikalliseen testaamiseen: 

git clone https://github.com/jannesoukka/picoyap.git
cd picoyap/
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install flask sql-alchemy
pip install psycopg2-binary
pip install python-dotenv

luo .env tiedosto jossa määrittelet ympäristömuuttujat (niitä on kaksi: SECRET_KEY ja DATABASE_URL)

suorita myös seuraavat komennot ennen ohjelman suorittamista:
psql
create database picoyap;
\q
psql -d picoyap < schema.sql
psql -d picoyap < seed.sql

-------------------------------

PÄIVITYS 22.9.2024:

- tilanne: Sovellus on oikeastaan alkutekijöissään. Se toki pyörittää; se ei siis heitä virhettä. Etusivun ja Femtoyapin sivupohjat ovat toiminnassa. Etusivulla on lista Femtoyapeista, ja niitä voi klikata, jotta niihin pääsee.

-------------------------------

PÄIVITYS 06.10.2024:

- tilanne: Sovellus on hyvässä vaiheessa mutta ei suinkaan viimeistelyä vaille valmis. 

toiminnallisuuksia toistaiseksi:
- sovelluksen etusivulla on lista femtoyapeista, ja kussakin näkyy ketjujen ja viestien lukumäärät sekä uusimman viestin ajankohta
- käyttäjä voi luoda uuden tunnuksen
- käyttäjä voi kirjautua sisään ja ulos
- käyttäjä voi luoda femtoyapiin uuden ketjun antamalla ketjulle otsikon ja aloitusviestin
- käyttäjä voi luoda ketjuun (attoyapiin) uuden viestin (zeptoyapin)

ei vielä:
- käyttäjä voi muokata ja poistaa omia ketjuja ja viestejä
- käyttäjä voi etsiä kaikki viestit, joiden osana on antamansa sana
- ylläpitäjä voi lisäksi lisätä ja poistaa femtoyapeja
- ylläpitäjä voi luoda salaisen femtoyapin ja määrittää, keillä on pääsy kyseiseen femtoyapiin.