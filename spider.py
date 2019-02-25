import urllib.request, json, sqlite3
from bs4 import BeautifulSoup


class MySpider:
    def openDB(self):
        self.con = sqlite3.connect('scenic.db')
        self.cursor = self.con.cursor()

    def initDB(self):
        try:
            self.cursor.execute("drop table scenic")
        except:
            pass
        self.cursor.execute("create table scenes (sName varchar(256) primary key,sType varchar(1024),"
                            "sSource varchar(1024),sLevel varchar(256),sTime varchar(256),sHotel varchar(1024))")

    def closeDB(self):
        self.con.commit()
        self.con.close()

    def insertDB(self, sName, sType, sSource, sLevel, sTime, sHotle):
        try:
            sql = "insert into secenic(sName,sType,sSource,sLevel,sTime,sHotel) values(?,?,?,?,?,?)"
            self.cursor.execute(sql, [sName, json.dumps(sType), json.dumps(sSource), sLevel, sTime, json.dumps(sHotel)])
        except:
            pass

    def spider(self,url):
        try:
            resp = urllib.request.urlopen(url)
            html = resp.read().decode()