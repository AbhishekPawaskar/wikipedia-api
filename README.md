# WIKIPEDIA_API
### this microservice is build to host APIs endpoints that gives the word frequency of top N words and also give the same search result for same userId if exists.

##  Contents:
###  1. API endpoints Info
###  2. Setup & Usage
###  3. Request-Response Structure 
###  4. System

## 1. API endpoints Info

### There are two API endpoints 

### a. `/wiki-api/word-frequency-analysis` , where a user will give the `topic`, `N` & `userId`. this will deliver the results. 

### b. `/wiki-api/search-history` , where the user can provide their `userId` and the `topic` to see any past search history results associated with their account.

##  2. Setup & Usage:


```
# start docker desktop application, open a terminal/command prompt and navigate to this project and enter the following

$  docker-compose build

$  docker-compose up

```

#### You may use any tool to send requests to endpoint. Screenshot below displays usage of `ThunderClient` for both the endpoints.

##  3. Request-Response Structure:

### Kindly check the file 'src/datamodels/models.py'

## 4. System

### this is to display how this could integrate with entire system in general. (as future development)

