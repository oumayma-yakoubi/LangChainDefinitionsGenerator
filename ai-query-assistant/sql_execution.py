from langchain.sql_database import SQLDatabase 


## Connect to MySql DB
db_user = "root"
db_password = "root"
db_host = "localhost"
db_name = "classicmodels"

mysql_uri = 'mysql+mysqlconnector://'+db_user+':'+db_password+'@'+db_host+':3306/'+db_name

db = SQLDatabase.from_uri(mysql_uri)

def get_schema(db):
    return db.get_table_info()
