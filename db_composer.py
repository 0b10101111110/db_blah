import mysql.connector


from os import listdir
from os.path import isfile, join
import csv


folder_var = '/'


from random import randint
import datetime
from time import sleep
from math import sqrt


# time vars
local_utc = 2
local_tz = datetime.timezone(datetime.timedelta(hours = local_utc))
local_date = datetime.datetime.now(local_tz).date()
local_date_str = local_date.strftime("%d_%m_%y")

countries = [
  {
    "country": "Senegal",
    "utc": 0,
    "currency": "USD"
  },
  {
    "country": "United Kingdom",
    "utc": 0,
    "currency": "GBP"
  },
  {
    "country": "France",
    "utc": 1,
    "currency": "EUR"
  },
  {
    "country": "Spain",
    "utc": 1,
    "currency": "EUR"
  },
  {
    "country": "Italy",
    "utc": 1,
    "currency": "EUR"
  },
  {
    "country": "Norway",
    "utc": 1,
    "currency": "NOK"
  },
  {
    "country": "Poland",
    "utc": 1,
    "currency": "PLN"
  },
  {
    "country": "Tunisia",
    "utc": 1,
    "currency": "TND"
  },
  {
    "country": "Sweden",
    "utc": 1,
    "currency": "SEK"
  },
  {
    "country": "Switzerland",
    "utc": 1,
    "currency": "CHF"
  },
  {
    "country": "Denmark",
    "utc": 1,
    "currency": "DKK"
  },
  {
    "country": "Netherlands",
    "utc": 1,
    "currency": "EUR"
  },
  {
    "country": "Czech Republic",
    "utc": 1,
    "currency": "CZK"
  },
  {
    "country": "Greece",
    "utc": 2,
    "currency": "EUR"
  },
  {
    "country": "Egypt",
    "utc": 2,
    "currency": "EGP"
  },
  {
    "country": "Cyprus",
    "utc": 2,
    "currency": "EUR"
  },
  {
    "country": "Latvia",
    "utc": 2,
    "currency": "EUR"
  },
  {
    "country": "Romania",
    "utc": 2,
    "currency": "RON"
  },
  {
    "country": "Turkey",
    "utc": 2,
    "currency": "TRY"
  },
  {
    "country": "Finland",
    "utc": 2,
    "currency": "EUR"
  },
  {
    "country": "South Africa",
    "utc": 2,
    "currency": "ZAR"
  },
  {
    "country": "Ukraine",
    "utc": 2,
    "currency": "UAH"
  },
  {
    "country": "Estonia",
    "utc": 2,
    "currency": "EUR"
  },
  {
    "country": "Saudi Arabia",
    "utc": 3,
    "currency": "SAR"
  },
  {
    "country": "Ethiopia",
    "utc": 3,
    "currency": "ETB"
  },
  {
    "country": "Russia",
    "utc": 4,
    "currency": "RUB"
  },
  {
    "country": "Pakistan",
    "utc": 5,
    "currency": "PKR"
  },
  {
    "country": "India",
    "utc": 6,
    "currency": "INR"
  },
  {
    "country": "Thailand",
    "utc": 7,
    "currency": "THB"
  },
  {
    "country": "Vietnam",
    "utc": 7,
    "currency": "VND"
  },
  {
    "country": "China",
    "utc": 8,
    "currency": "CNY"
  },
  {
    "country": "Japan",
    "utc": 9,
    "currency": "JPY"
  },
  {
    "country": "Australia",
    "utc": 10,
    "currency": "AUD"
  },
  {
    "country": "Argentina",
    "utc": 3,
    "currency": "ARS"
  },
  {
    "country": "Dominican Republic",
    "utc": -4,
    "currency": "DOP"
  },
  {
    "country": "Ecuador",
    "utc": -5,
    "currency": "USD"
  },
  {
    "country": "USA",
    "utc": -5,
    "currency": "USD"
  },
  {
    "country": "Canada",
    "utc": -6,
    "currency": "CAD"
  }
]

crypto = [ "BTC", "ETH", "USDT" ] 

def get_rand_fiat():
    return countries[randint(0, len(countries) - 1)]["currency"]

def get_rand_crypto():
    return crypto[randint(0, len(crypto) - 1)]

def get_rand_dt(tz_var):
    dt = None
    dt = datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day, randint(9, 17), randint(0, 59), randint(0, 59), 0, datetime.timezone(datetime.timedelta(hours = tz_var)))
    #print(dt.astimezone(datetime.timezone(datetime.timedelta(hours = local_utc))).date())
    #print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours = local_utc))).date())
    while (dt.astimezone(datetime.timezone(datetime.timedelta(hours = local_utc))).date() != datetime.datetime.now(local_tz).date()):
        dt = datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day, randint(9, 17), randint(0, 59), randint(0, 59), 0).astimezone(datetime.timezone(datetime.timedelta(hours = tz_var)))
    return dt
    

def percent_count(sum):
    if (sum >= 1850000):
        return 0.3
    if (sum >= 1650000):
        return 0.4
    if (sum >= 1500000):
        return 0.5
    if (sum >= 1350000):
        return 0.6
    if (sum >= 1150000):
        return 0.7
    if (sum >= 1000000):
        return 0.8
    if (sum >= 850000):
        return 0.9
    if (sum >= 650000):
        return 1
    if (sum >= 500000):
        return 1.1
    if (sum >= 430000):
        return 1.3
    if (sum >= 360000):
        return 1.4
    if (sum >= 300000):
        return 1.5
    if (sum >= 250000):
        return 1.6
    if (sum >= 200000):
        return 1.7
    if (sum >= 170000):
        return 1.8
    if (sum >= 130000):
        return 1.9
    if (sum >= 100000):
        return 2
    if (sum >= 92000):
        return 2.1
    if (sum >= 840000):
        return 2.2
    if (sum >= 760000):
        return 2.3
    if (sum >= 680000):
        return 2.4
    if (sum >= 600000):
        return 2.5
    if (sum >= 65000):
        return 2.6
    if (sum >= 50000):
        return 2.7
    if (sum >= 44000):
        return 2.8
    if (sum >= 38000):
        return 2.9
    if (sum >= 32000):
        return 3
    if (sum >= 26000):
        return 3.1
    if (sum >= 20000):
        return 3.2
    
    

class Operation: 
    def __init__(self, id, swaptype, sum, percent, profit, country, datetime, utc):
        self.id = id
        self.swaptype = swaptype
        self.sum = sum
        self.percent = percent
        self.profit = profit
        self.country = country
        self.datetime = datetime
        self.utc = utc


class Database:
    def __init__(self):
        # main vars init
        self.full_sum = None
        self.amount_of_operations = None

        self.database = []
    
    def check_csv(self):
        f_exists = False
        onlyfiles = [f for f in listdir(csv_path) if isfile(join(csv_path, f))]
        for x in onlyfiles:
            if x == f'{local_date}.csv':
              f_exists = True
        return f_exists

    def upload_from_csv(self):
      with open(f"{csv_path}{folder_var}{local_date_str}.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
          self.database.append(Operation(int(row[0]), row[2], int(row[3]), float(row[4]), int(row[5]), row[6], datetime.datetime.fromisoformat(row[1]), int(row[7])))


      

    def upload_to_csv(self):
      with open(f"{csv_path}{folder_var}{local_date_str}.csv", 'w', newline='', encoding='utf-8') as file:
        csvwriter = csv.writer(file)
        for row in db.database:
          csvwriter.writerow([row.id, row.datetime, f"{row.swaptype}", row.sum, row.percent, row.profit, row.country, row.utc])

    def db_connect(self):
      self.db_connection = mysql.connector.connect (
        host="127.0.0.1",
        user="root",
        password="root",
        database="operations"
      )
      self.db_cursor = self.db_connection.cursor()


    def check_table(self):
      exists = False
      self.db_cursor.execute("show tables")
      for x in self.db_cursor.fetchall():
        if x[0] == local_date_str:
            exists = True
            break
      return exists

    def create_table(self):
      self.db_cursor.execute(f"create table {local_date_str} (id integer, date_time datetime(6), swaptype varchar(11), sum integer, percent float, profit integer, country varchar(30), utc integer)")
    
    def upload_next(self):
          x = self.database[0]
          while x.datetime > datetime.datetime.now(local_tz):
              sleep(5)
          self.db_cursor.execute(f"select id from {local_date_str} where id = {x.id}")
          id = self.db_cursor.fetchall()
          if id == []:
              self.db_cursor.execute(f"insert into {local_date_str} (id, date_time, swaptype, sum, percent, profit, country, utc) values ({x.id}, '{x.datetime.strftime('%Y-%m-%d %H:%M:%S')}', '{x.swaptype}', {x.sum}, {x.percent}, {x.profit}, '{x.country}', {x.utc})")
              self.db_connection.commit()
          del self.database[0]
          sleep(5)



    #def db_upload(self):


    def get_sum_state(self):
        x = randint(1, self.all_sums)
        if (x <= self.three_zero):
            self.three_zero-=1
            self.all_sums-=1
            return 1
        elif (x > self.three_zero + self.zero_zero):
            self.all_sums-=1
            self.two_zero-=1
            return 3
        else:
            self.all_sums-=1
            self.zero_zero-=1
            return 2

    def get_swaptype_state(self):
        x = randint(1, self.all_swaptypes)
        self.all_swaptypes-=1
        if (x <= self.crypro_fiat):
            self.crypro_fiat-=1
            return 1
        elif (x > self.crypro_fiat + self.fiat_crypto):
            self.crypto_crypto-=1
            return 3
        else:
            self.fiat_crypto-=1
            return 2

    def fill_with_rand(self):
        
        self.full_sum = randint(5000000, 10000000)

        self.amount_of_operations = round(80 * self.full_sum / 10000000)

        self.lower_number = 20000
        self.higher_number = 2000000
        self.difference = self.higher_number - self.lower_number

        self.all_swaptypes = self.amount_of_operations
        self.crypro_fiat = round(self.all_swaptypes / 3)
        self.fiat_crypto = round(self.all_swaptypes / 3)
        self.crypto_crypto = self.all_swaptypes - self.crypro_fiat - self.fiat_crypto

        # # sum types amount in percent
        self.all_sums = 100
        self.three_zero = randint(35, 45)
        self.zero_zero = randint(25, 35)
        self.two_zero = self.all_sums - self.three_zero - self.zero_zero

        # convert sum types amout in percent to raw amount
        self.all_sums = self.amount_of_operations
        self.three_zero = round(self.amount_of_operations * self.three_zero / 100)
        self.zero_zero = round(self.amount_of_operations * self.zero_zero / 100)
        self.two_zero = self.amount_of_operations - self.three_zero - self.zero_zero

        self.stayed_sum = self.full_sum - (self.amount_of_operations * self.lower_number)
        
        dt = None

        

        # filling database array with lines
        for i in range(self.amount_of_operations):

            # sum generation
            if (self.difference > self.stayed_sum):
                self.difference = self.stayed_sum

            modifier = 10

            
            x_sum = (100 - ((randint(1, 100**modifier))**(1/modifier))) * self.difference / 100

            x_sum = round(x_sum)
            
            
            sum_state = self.get_sum_state()

            if (sum_state == 1):
                x_sum -= x_sum % 1000
            
            if (sum_state == 2):
                x_sum -= x_sum % 1
            
            if (sum_state == 3):
                x_sum -= x_sum % 100

            self.stayed_sum -= x_sum
            

            # random datetime generation
            percent = percent_count(x_sum + 20000)
            profit = round((x_sum + 20000) * percent / 100)
            country = countries[randint(0, len(countries) - 1)]
            dt = get_rand_dt(country["utc"])
            currency_x = get_rand_crypto()
            currency_y = get_rand_crypto()
            swaptype = self.get_swaptype_state()
            while (currency_x == currency_y):
                currency_y = get_rand_crypto()
            if (swaptype == 1):
                swaptype = f'{currency_x} - {country["currency"]}'
            if (swaptype == 2):
                swaptype = f'{country["currency"]} - {currency_x}'
            if (swaptype == 3):
                swaptype = f'{currency_x} - {currency_y}'


            # putting created variables into class in array 
            self.database.append(Operation(0, swaptype, x_sum + 20000, percent, profit, country["country"], dt, country["utc"]))
        
        self.database[self.amount_of_operations - 1].sum += self.stayed_sum

    def print(self):
        for i in self.database:
            print(i.id, "\t", "{:10}".format(i.sum), "\t", f"\t{i.percent}%", "\t", i.profit, "\t", i.swaptype, "\t", i.datetime.time(), "\t", i.datetime.date(), "\t", f'UTC{i.utc:+3}', "\t", "{:17}".format(i.country))

    def sort(self):
        self.database = sorted(self.database, key=lambda Operation: Operation.datetime)
        for i in range(self.amount_of_operations):
            self.database[i].id = i
        
            
while True:
        
        


  
  csv_path = '.'
  local_utc = 2





  local_tz = datetime.timezone(datetime.timedelta(hours = local_utc))
  local_date = datetime.datetime.now(local_tz).date()
  local_date_str = local_date.strftime("%d_%m_%y")


  db = Database()
  if db.check_csv() == False:
    db.fill_with_rand()
    db.sort()
    db.upload_to_csv()
  else:
    db.upload_from_csv()
  #db.print()
  db.db_connect()
  if db.check_table() == False:
    db.create_table()

  while db.database != []:
      db.upload_next()


  while local_date == datetime.datetime.now(local_tz).date():
      sleep(60)
  

