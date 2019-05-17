import argparse
import os
import re
import pymysql
import glob

class DBHelper:
  conn = None
  def __init__(self):
    self.db_connect()
  def db_connect(self):
    self.conn = pymysql.connect(host="localhost", user="root", password="1234", db="maratron", charset="utf8")
  def db_disconnect(self):
    if self.conn:
      self.conn.close()
  def selectAll(self):
    with self.conn.cursor() as cur:
        sql = "select * from tts_maratron"
        cur.execute(sql)
        rows = cur.fetchall()
    return rows
  def insert(self, category, author, title, contents, audio, thumnail):
    with self.conn.cursor() as cur:
      sql = """
            insert into tts_maratron(category, author, title, contents, audio, thumnail) 
            values(%s,%s,%s,%s,%s,%s)
            """
      cur.execute(sql,(category, author, title, contents, audio, thumnail))
    self.conn.commit()

def read_file():
  fileList = glob.glob(os.path.join('audiobooks', '*.*'))
  print ('file category title author title')
  for file in fileList:
    ext=os.path.splitext(file)
    if(ext[1]=='.txt') :
      with open(file, encoding='utf-8') as f:
        data = f.read()
      parts = data.strip().split('|')
      category=parts[0]
      title=parts[1]
      author=parts[2]
      text=parts[3]
      print('{:30}{:10}{:10}{:10}{:20}'.format(file, category, title, author, text[:20]))

def insert_data(db) :
  db.insert('영어','Yoon Dongju','There is no tomorrow','contents/Tomorrow.txt','audio/Tomorrow.wav','thumnail/img1.png')
  db.insert('영어','Shawn Achor','The happy secret to better work','contents/Secret.txt','audio/Secret.wav','thumnail/img2.png')
  db.insert('영어','Jim Holt','Why does the universe exist?','contents/Universe.txt','audio/Universe.wav','thumnail/img3.png')
  db.insert('한국어','법정스님','무소유','contents/무소유.txt','audio/무소유.wav','thumnail/img4.png')
  db.insert('한국어','리차드도킨스','이기적 유전자','contents/이기적유전자.txt','audio/이기적유전자.wav','thumnail/img5.png')
  db.insert('한국어','전래동화','호랑이와 곶감','contents/호랑이.txt','audio/호랑이.wav','thumnail/img6.png')

def main():
  read_file()
  db = DBHelper()
  insert_data(db)
  rows = db.selectAll()
  for row in rows:
    print (row)
  db.db_disconnect()

if __name__ == '__main__':
  main()