Required python version 3.10.6 or later

# Commands

For creating the environment
py.exe -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

For running the project
Goto task folder using cd task command
then run py.exe .\manage.py runserver

For coverage testing
Goto task folder using cd task command
then run coverage run .\manage.py test and then run coverage report
