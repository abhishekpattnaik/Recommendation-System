# Steps to follow:-
1. create a virtual environment
    ```python3 -m venv tutorial-env```
    
    
2. On the root folder and run:
    ```pip install -r requirements.txt```
    this will install all dependencies
    
    
3. Start the mongodb service
    ```sudo service mongodb start```

    
4. The Django project is on main_training_project directory:
    ```cd main_training_project```

    
5. scrap the raw datas and save it into database :
    ```python3 manage.py scrap_the_db ```

    
6. get to run the server
    ```python3 manage.py runserver```

    