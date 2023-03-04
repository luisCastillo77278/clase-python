import pymysql

if __name__ == '__main__':

  connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='lc77278',
    db='coderhouse',
  )

  print('connection ready')


