# Steps to follow:-
1. create a virtual environment
    ```python3 -m venv tutorial-env```
    
    
2. On the root folder and run:
    ```pip install -r requirements.txt```
    this will install all dependencies
    
    
3. Start the mongodb service
    ```sudo service mongodb start```
    
    
4. move to ScrapTask folder :
    ```cd ScrapTask```
    
    
5. run the pilot file:
    ```python3 scrapPilot.py```
    
    
6. Incase you want to drop all the collections
    ```python3 dropCollections.py```
