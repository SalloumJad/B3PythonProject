import re
from flask import Flask
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import ast
from flask_mysqldb import MySQL
import pymysql

app = Flask(__name__)

api = Api(app)


# Connexion à MySQL
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="DB_B3_Python" 
)

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS titles")

cursor.execute("CREATE TABLE titles(title VARCHAR(255) NOT NULL)")

cursor.execute("INSERT INTO titles(title) VALUES('title1')")
cursor.execute("INSERT INTO titles(title) VALUES('title2')")
cursor.execute("INSERT INTO titles(title) VALUES('title3')")
cursor.execute("INSERT INTO titles(title) VALUES('title4')")
cursor.execute("INSERT INTO titles(title) VALUES('title5')")

# charger les données depuis le CSV directement (fonctionne mais la BDD reste vide à la fin)
#cursor.execute("LOAD DATA INFILE 'C:/Users/jadsa/Desktop/Jad/Ynov/Cours/B3/Python/Cours/result.csv' INTO TABLE titles FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '/n' IGNORE 1 ROWS")

cursor.execute("SELECT * FROM titles")

result = cursor.fetchall()

print(result)

db.close()


class Titles(Resource):
    def get(self, id):
        self.data = pd.read_csv('result.csv')
        self.data = self.data.to_dict()
        # retourner le data
        return {'self.data': self.data}, 200
        #return {'get': str(id)}

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('title', required=True)

        args = parser.parse_args()

        data = pd.DataFrame({
            'Unnamed: 0' : args['title']
        })

        return {'put': str(id)}
    
    def delete(self, id):
        db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="DB_B3_Python" 
        )

        cursor = db.cursor()
        cursor.execute("DELETE FROM titles WHERE title=%s", id)
        cursor.execute("SELECT * FROM titles")
        result = cursor.fetchall()
        print(result)
        db.close()
        return {'delete': str(id)}

    def post(self, id):
        
        return request.json

api.add_resource(Titles, '/<id>') 

t = Titles()
t.get(1)
t.delete(1)

if __name__ == '__main__':
    app.run()