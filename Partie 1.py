import sqlite3 

def connect_db():
    try:
        conn = sqlite3.connect('dic_database.db')
        
        print("Base de données crée et correctement connectée à sqlite")
        
        conn.close()
        
        print("Connexion fermée")
        
    except sqlite3.Error as error:
        print("Erreur lors de la connexion à sqlite", error)

def create_table_db():
    try:
        conn = sqlite3.connect('dic_database.db')
        sql = '''CREATE TABLE DIC (
                      id_ept INTEGER PRIMARY KEY,
                      nom TEXT NOT NULL,
                      prenom TEXT NOT NULL,
                      departement TEXT NOT NULL,
                      niveau INTEGER NOT NULL,
                      telephone TEXT NOT NULL  
               );'''
        cur = conn.cursor()
        print("Connexion à sqlite réussie")
        cur.execute(sql)
        conn.commit()
        print("Table créée avec succés")
        cur.close()
        conn.close()
        print("Connexion fermée")
        
    except sqlite3.Error as error:
        print("Erreur lors de la création du table SQLite", error)

def save_db(*values):
    try:
        conn = sqlite3.connect('dic_database.db')
        cur = conn.cursor()
        print("Connexion réussie à SQLite")
        cur.execute("""
            INSERT INTO DIC (id_ept, nom, prenom, departement, niveau,telephone) VALUES(?, ?, ?, ?, ?, ?)""", values)
        conn.commit()
        print("Enregistrement inséré avec succès dans la table person")
        cur.close()
        conn.close()
        print("Connexion SQLite est fermée")
        
    except sqlite3.Error as error:
        print("Erreur lors de l'insertion dans la table person", error)

def get_db(id_w):
    values = {}
    try:
        conn = sqlite3.connect('dic_database.db')
        cur = conn.cursor()
        print("Connexion réussie à SQLite")
        
        cur.execute("SELECT * from DIC WHERE id_ept= :id_w", {"id_ept": id_w})
        for row in cursor:
            values[nom] = row[1]
            values[prenom] = row[2]
            values[departement] = row[3]
            values[niveau] = row[4]
            values[telephone] = row[5]
            
            print(values)
            
        cur.close()
        conn.close()
        print("Connexion SQLite est fermée")
        
    except sqlite3.Error as error:
        print("Erreur lors de la connexion à la table person", error)

def get_all_db():
    try :
        conn = sqlite3.connect('dic_database.db')
        cur = conn.cursor()
        print("Connexion réussie à SQLite")

        cur.execute("SELECT * FROM DIC")
        for row in cur:
            print("id_ept = "), row[0]
            print("nom = "), row[1]
            print("prenom = "), row[2]
            print("departement = "), row[3]
            print("niveau = "), row[4]
            print("telephone = "), row[5], "\n"

        cur.close()
        conn.close()
        print("Connexion SQLite est fermée")
        
    except sqlite3.Error as error:
        print("Erreur lors de la connexion à la table person", error)