# Inside-test
## FASTAPI CRUD application.
REST API application.<br>

### Stack of technologies:<br>
-Python >= 3.9<br>
-FastApi<br>
-Database: SQLite<br>
-linter: Black<br>

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.
The key features are: fast to code, based on the open standards for APIs,
very high performance, minimize code duplication.

### Basic functionality:<br>
1.Web REST API<br>
2.Getting list of some messages from the database.<br>
3.Creating new messages.<br>
4.Registr a new user. <br>
5.Authenticate user from database.

### APIs endpoints:<br>
| requests | url | description  |
| ------- | --- | --- |
| GET | /messages/{username}/ | get history ofmessages |
| POST | /messages/ | creates a new messagess |


## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/Inside-test <br>
$ cd Inside-test<br>

### Create virtualenv:<br>
$ virtualenv venv<br>
$ source venv/bin/activate<br>


### Dependency:
$ pip install -r requirements.txt<br>

### Run the sample server:<br>
$ uvicorn app.main:app --reload <br>



### API from the browser:
You can work on the API directly in your browser.<br>
You will see the automatic interactive API documentation (provided by Swagger UI).
http://127.0.0.1:8000/docs <br>


### Examples:<br>

![Screenshot](https://github.com/SparklingAcidity/Inside-test/blob/main/im_for_readme/1.png) <br>
![Screenshot](https://github.com/SparklingAcidity/Inside-test/blob/main/im_for_readme/2.png)<br><br>
or http://127.0.0.1:8000/redoc
![Screenshot](https://github.com/SparklingAcidity/Inside-test/blob/main/im_for_readme/3.png)
