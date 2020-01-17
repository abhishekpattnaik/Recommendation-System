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



# Overview of project :-
    This project recommends user most similar documents based on his/her likes on urls.It is mainly focused on the concept of
    TF-IDF.In information retrieval, tf–idf or TFIDF, short for term frequency–inverse document frequency, is a numerical
    statistic that is intended to reflect how important a word is to a document in a collection or corpus.It is often used as a
    weighting factor in searches of information retrieval, text mining, and user modeling. The tf–idf value increases 
    proportionally to the number of times a word appears in the document and is offset by the number of documents in the corpus 
    that contain the word, which helps to adjust for the fact that some words appear more frequently in general.
    
# Flow :-
    1. Superuser should be who can access to basic functionality of the project(Super user will have access to generate 
    recommended urls for the sub users)
    2. Sub user or app user is created who can hit like(actually by hitting like means it passes the doc id corresponding to
    the url liked by him)
    3. This liked urls uid will be updated on the appuser's model and will be proccessed on by the approval of super user's 
    permission.
    4. Now if app user opens the page then he will see the recommended list based on TF-IDF funcionalities
    
# Database details :-
    For this project we have used mongoDB and to connect it with Django,
    djongo tool is used as the bridge between them.
    
    Engine:- Djongo
    Database name:- main_project_DB
    Collections :- 
        i) urls(This will have all the urls name, title, uid)
        ii) urls_data(This is similar to urls' collection but additionally this will 
            have the dictionary for word count)
        iii) tf-idf(This will have weight for each word according to the document)
        
    
