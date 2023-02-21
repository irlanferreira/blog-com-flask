import mysql.connector
import datetime, time

def conectar():
    try:
        con = mysql.connector.connect(host='localhost',user='root',password='04052005', database='blog')
    except:
        criar_db()
        con = mysql.connector.connect(host='localhost',user='root',password='04052005', database='blog')
    return con

def criar_db():
    con = mysql.connector.connect(host='localhost',user='root',password='04052005')
    cursor = con.cursor()
    cursor.execute('CREATE DATABASE blog')
    cursor.execute('USE blog')
    cursor.execute("""
    CREATE TABLE postagem(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(500) NOT NULL,
    horario VARCHAR(40) NOT NULL
    )
    """)
    con.commit()
    return True

def postar(texto, horario):
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO postagem (texto, horario) VALUES ('{texto}', '{horario}')")
        con.commit()
        return True
    except mysql.connector.Error as er:
        print(er)
        return False

def obter_posts(id=False):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM postagem {f"WHERE id = {id}" if id != False else ""}')
    fetch = cursor.fetchall()
    res = []
    for item in fetch:
        horario = datetime.datetime.fromtimestamp(float(item[2]))
        hora = f"{'0' if horario.hour < 10 else ''}{horario.hour}:{'0' if horario.minute < 10 else ''}{horario.minute}"
        data = f"{'0' if horario.day < 10 else ''}{horario.day}/{'0' if horario.month < 10 else ''}{horario.month}/{horario.year}"
        res.append({'id': item[0],'texto':item[1], 'hora':hora,'data':data})
    return res
