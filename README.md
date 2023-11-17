## Required Python Version

Python version 3.10.6 or later is required for this project.

### Environment Setup

Create the virtual environment:

```bash
py.exe -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Environment Setup

### For running the project
Goto task folder using ```cd task``` command
Then run ```py.exe .\manage.py runserver```

### For coverage testing

Goto task folder using ```cd task``` command
Then run ```coverage run .\manage.py test``` and then run ```coverage report```

The json file of postman for testing the API endpoint is added. Import the json file to postman
