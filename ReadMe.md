activate the virtual environment

```bash
source venv/bin/activate
```

install the requirements

```bash
pip install -r requirements.txt
```

run the server

```bash
python manage.py runserver
```

### Freeze package files

```bash
pip freeze > requirements.txt
```

### Collect static files

```bash
python manage.py collectstatic
```

### Install PostGIS

```bash
brew install postgis
```

#### Install GDAL, GEOS, PROJ

```bash
brew install gdal geos proj
```

#### Enable PostGIS

```bash
psql -U <your_username> -d <your_database>
CREATE EXTENSION postgis;
```
