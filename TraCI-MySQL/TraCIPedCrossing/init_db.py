import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="eclipse-sumo",
  password="root"
)

def initialize_db():
    '''
    Method to initialize the MySQL "sumo" database and "pedestrian" table
    '''
    cursor = db.cursor()

    cursor.execute("SHOW DATABASES")

    databases = [database_tuple[0] for database_tuple in cursor.fetchall()]
        
    if 'sumo' not in databases:
        print("DB sumo doesn't exist... \n Creating it...")
        cursor.execute("CREATE DATABASE sumo")
    else:
        print("DB sumo already exists, skipping DB creation")

    cursor.execute("USE sumo")

    cursor.execute("SHOW TABLES")

    tables = [table_tuple[0] for table_tuple in cursor.fetchall()]

    if "pedestrian" not in tables:
        print("Table pedestrians doesn't exist... \n Creating it...")
        cursor.execute("CREATE TABLE pedestrian \
                        (id INT AUTO_INCREMENT PRIMARY KEY, \
                        num_pers INT NOT NULL, \
                        time TIMESTAMP NOT NULL)")
    else:
        print("Table pedestrian already exists, skipping table creation")


    db.commit()
    print("Finished DB initialization")