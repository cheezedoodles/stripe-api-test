# stripe-api-test

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements. (py v3.10.5)

```bash
python -m pip install -r requirements.txt
```
Make migrations via manage.py
```bash
python manage.py makemigrations
```
And migrate them to the database (currently sqlite3)
```bash
python manage.py migrate
```
In order to start the server use
```bash
python manage.py runserver
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
