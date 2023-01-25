# Setup
* Get python dev headers:

```bash
sudo apt-get install python3-dev
```

```bash
sudo apt-get install -y libkrb5-dev
```

* Create virtual env

```bash
cd <root-project-dir>
python3 -m venv .venv
which python # should output .venv python executable
```

* Activate virtual env

```bash
source .venv/bin/activate
```

* Install dependencies:

```bash
pip install -r requirements.txt
```

* Run server

```bash
python manage.py runserver
```