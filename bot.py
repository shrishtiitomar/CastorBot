!pip3 install requests
import sqlite3


class DBHelper:

    def _init_(self, dbname="todo.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS items (description text, owner text)"
        itemidx = "CREATE INDEX IF NOT EXISTS itemIndex ON items (description ASC)" 
        ownidx = "CREATE INDEX IF NOT EXISTS ownIndex ON items (owner ASC)"
        self.conn.execute(tblstmt)
        self.conn.execute(itemidx)
        self.conn.execute(ownidx)
        self.conn.commit()

    def add_item(self, item_text, owner):
        stmt = "INSERT INTO items (description, owner) VALUES (?, ?)"
        args = (item_text, owner)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text, owner):
        stmt = "DELETE FROM items WHERE description = (?) AND owner = (?)"
        args = (item_text, owner )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self, owner):
        stmt = "SELECT description FROM items WHERE owner = (?)"
        args = (owner, )
        return [x[0] for x in self.conn.execute(stmt, args)]
      
import json
import requests
import time
import urllib
import urllib3

db = DBHelper()


TOKEN ="5982049866:AAE2osRhTatA7181H2dzhVGDnV5x4Vk-M20"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

items=['Samsung','Vivo','OnePlus','Apple','Redmi','Oppo']
Samsung=['SamsungGalaxy','Samsung Galaxy A23','Samsung Galaxy Z Fold4' ]
Redmi=['Redmi A1+','Redmi Note 12 Pro']
Vivo=['Vivo Y21G','Vivo Y2207']
Oppo=['Oppo A78','Oppo Reno8']
OnePlus=['OnePlus 10R','OnePlus 10 Pro']
Apple=['Apple iPhone 13','Apple iPhone 14 Pro Max']

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def handle_updates(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        items=['Samsung','Vivo','OnePlus','Apple','Redmi','Oppo']
        model_name_list=['Samsung Galaxy A03','Redmi A1+','Vivo Y21G','Oppo A78','Redmi Note 12 Pro','Samsung galaxy A23','OnePlus 10R','Apple iPhone 13','Apple iPhone 14 Pro Max']
        Samsung=['Samsung Galaxy A03','Samsung Galaxy A23','Samsung Galaxy Z Fold4' ]
        Redmi=['Redmi A1+','Redmi Note 12 Pro']
        Vivo=['Vivo Y21G','Vivo Y2207']
        Oppo=['Oppo A78','Oppo Reno8']
        OnePlus=['OnePlus 10R','OnePlus 10 Pro']
        Apple=['Apple iPhone 13','Apple iPhone 14 Pro Max']
        if text == "/done":
            keyboard = build_keyboard(items)
            send_message("Which brand do you prefer?", chat, keyboard)
        elif text == "/start":
            send_message("Hello!Thanks for connecting.We are here to pick the perfect smartphone match for you.Press /done to view the available brands.Press /pay to make payments.", chat)
        elif text== "/pay":
            send_message("We accept payments through Debit/Credi or Cash on Delievery.",chat)
            keyboard = build_keyboard(['Debit/Credit Card','Cash on Delievery'])
            send_message("Choose a payment option",chat,keyboard)
        elif text == "Debit/Credit Card":
            send_message("Pay on the following link:",chat)
            send_message("https://retail.onlinesbi.sbi/retail/login.htm",chat)
            time.sleep(1)
            send_message("Processing....",chat)
            time.sleep(1)
            send_message("Redirecting....",chat)
            time.sleep(1)
            send_message("Payment received.",chat)
            time.sleep(1)
            send_message("Order successfully placed.",chat)
            send_message("Thank you for visiting!",chat)
            #send(gif=urllib3.urlopen('http://www.reactiongifs.us/wp-content/uploads/2014/08/popcorn_indiana_jones.gif').read())
            
        elif text == "Cash on Delievery":
            send_message("Pay 7249 rupees to the delivery partner.",chat)
            send_message("Order successfully placed.",chat)
            send_message("Thank you for visiting!",chat)

        elif text == "Bluetooth version?":
          send_message("Bluetooth version for this device is 5.0.",chat)
        
        elif text == "How many sims can be inserted?":
          send_message("Device is DUAL sim.",chat)
        
        elif text == "Which Data Generation does it support?":
          send_message("Device supports 4th Generation.",chat)
        
        elif text == "Warranty Period?":
          send_message("Device has Warranty Period of 12 Months.",chat)

        elif text in Apple:
          if text is "Apple iPhone 14 Pro Max":
            send_message("""
            Model_name: Apple iPhone 14 Pro Max
            Color: Deep Purple,Red,White,Smooth Black
            RAM: 6 GB""", chat)
        

        if text=='Apple iPhone 13':
            send_message("""Model_name: Apple iPhone 13
            Color: Pink, Starlight White,Midnight,Red
            RAM: 6 GB
            Internal Storage: 128 GB
            Display: 6.1 inches SuperRetina XDR OLED
            Battery: 5000 mAh Lithium ion
            Price: Rs 62,990
            Rear Main Camera: 12 MP+12 MP(DUAL CAMERA)
            Selfie Camera: 12 MP
            Weight: 173 g
            Platform: iOS 15
            Processor: Hexa-Core
            Brightness: 1200 NITS
            Resolution: 2520x1170 
            Units: 6 """,chat)

        if text=='Redmi Note 12 Pro':
            send_message("""Model_name:Redmi Note 12 Pro
            Color:Black
            RAM: 6GB
            Internal Storage: 128 GB
            Display: 6.57 inches AMOLED
            Battery:5000 mAh Lithium ion
            Price: Rs. 25,000
            Rear Main Camera: 50 MP+8MP+2 MP(TRIPLE CAMERA)
            Selfie Camera: 13MP
            Weight: 198 g
            Platform: Android 13
            Processor: Ouad-Core,2.6 GHz
            Brightness: 900NITS
            Resolution: 1800x720
            Units: 8 """,chat)
        
        if text=='Redmi A1+':
            send_message("""Model_name:Redmi A1+
            Color:Black
            RAM: 6GB
            Internal Storage: 128 GB
            Display: 6.57 inches AMOLED
            Battery:5000 mAh Lithium ion
            Price: Rs. 25,000
            Rear Main Camera:8 MP +8MP(DUAL CAMERA)
            Selfie Camera: 5MP
            Weight: 192 g
            Platform: Android 12
            Processor: Ouad-Core,2 GHz
            Brightness: 400NITS
            Resolution: 1600x720
            Units: 10 """,chat)

        if text=='Vivo Y21G':
            send_message("""Model_name:Vivo Y21G
            Color:Black
            RAM: 6GB
            Internal Storage: 128 GB
            Display: 6.51 inches  HD+ Halo
            Battery:5000 mAh Lithium ion
            Price: Rs. 25,000
            Rear Main Camera: 13 MP+2 MP(DUAL CAMERA)
            Selfie Camera: 8MP
            Weight: 198 g
            Platform: Android 13
            Processor: Ouad-Core,2 GHz
            Data Generation: 4G
            Brightness: 600NITS
            Resolution: 1600x720
            Units: 10 """,chat)
        
        if text=='Vivo Y2007':
            send_message("""Model_name:Vivo Y2207
            Color:Black
            RAM: 6GB
            Internal Storage: 128 GB
            Display: 6.51 inches  HD+ Halo
            Battery: 5000 mAh with 18W Fast Charging
            Price: Rs. 16,499
            Rear Main Camera:  50MP + 2MP Dual Rear & 8 MP Front Camera
            Selfie Camera: 8MP
            Weight: 197 g
            Platform: Android 13
            Processor: Ouad-Core,2 GHz
            Brightness: 800NITS
            Resolution: 1600x720
            Units: 10 """,chat)
          
        if text=='Samsung Galaxy Z Fold4':
            send_message("""Model_name:Samsung Galaxy Z Fold4
            Color: Beiege, Black, White
            RAM:12 GB
            Internal Storage: 256 GB
            Display: 7.6 inches Dynamic AMOLED 2X
            Battery:7700 mAh Lithium ion
            Price: Rs. 1,54,999
            Rear Main Camera:50 MP+12 MP+10 MP(TRIPLE CAMERA)
            Selfie Camera: 10 MP+4 MP
            Weight: 263 g
            Platform: Android 12
            Processor: Octa-Core,3.18 GHz
            Brightness: 2000 NITS
            Resolution: 1016x908
            Units: 4 """,chat)
       
     
   if text == 'SamsungGalaxy':
            send_message("""
            Model_name:Samsung Galaxy A03
            Rear Main Camera:48 MP+2MP(DUAL CAMERA)""",chat)

        elif text =="Samsung Galaxy A23":
            send_message("""Model_name:Samsung Galaxy A23
            Color: Orange
            RAM: 8 GB
            Internal Storage: 128 GB
            Display: 6.6 inches TFT LCD
            Battery:5000 mAh Lithium ion
            Price: Rs. 19,999
            Rear Main Camera:50 MP+2MP+ 2 MP + 5 MP(QUAD CAMERA)
            Selfie Camera: 8 MP
            Weight: 195 g
            Platform: Android 12
            Processor: Octa-Core,2.4 GHz
            Brightness: 900 NITS
            Resolution: 2408x1080
            Units: 8 """,chat)

        if text=='One Plus 10R':
            send_message("""Model_name:One Plus 10R
            Color:Sierra Black
            RAM: 12 GB
            Internal Storage: 256 GB
            Display: 6.7 inches FluidOLED
            Battery:5000 mAh Lithium ion
            Price: Rs. 36,999
            Rear Main Camera:50 MP+8MP+2 MP(TRIPLE CAMERA)
            Selfie Camera: 16 MP
            Weight: 186 g
            Platform: Android 12
            Processor: Octa-Core,2 GHz
            Brightness: 900 NITS
            Resolution: 2412x1080
            Units: 6 """,chat)
        
        if text=='One Plus 10 Pro':
            send_message("""
            Model_name:One Plus 10 Pro 
            Color: Emerald Forest
            RAM: 12 GB
            Internal Storage: 256 GB
            Display: 6.7 inches Fluid AMOLED with LTPO
            Battery:5000 mAh Lithium ion
            Price: Rs. 66,999
            Rear Main Camera:50 MP+8MP+2 MP(TRIPLE CAMERA)
            Selfie Camera: 16 MP
            Weight: 186 g
            Platform: Oxygen OS based on Android 12
            Processor: Octa-Core,2 GHz
            Brightness: 2000 NITS
            Resolution: 2412x1080
            Units: 6 """,chat)

        if text=='Oppo A78':
            send_message("""Model_name:Oppo A78
            Color: Grey,Black, White, Blue
            RAM:6 GB
            Internal Storage: 128 GB
            Display: 6.56 inches HD+
            Battery:5000 mAh Lithium ion
            Price: Rs. 25,000
            Rear Main Camera:50 MP+12 MP+10 MP(TRIPLE CAMERA)
            Selfie Camera: 50 MP+2MP(DUAL CAMERA)
            Weight: 196 g
            Platform: Android 13
            Processor: Octa-Core,2.6 GHz
            Brightness: 900 NITS
            Resolution: 1800x720
            Units: 4 """,chat)

        if text=='Oppo Reno8':
            send_message("""
            Model_name: Oppo Reno8
            Color: Shimmer Black
            RAM: 8GB
            Internal Storage: 128 GB
            Display: 16.33 cm (6.43 inch) Full HD
            Battery: 4500 mAh Lithium ion
            Price: Rs. 29,499
            Rear Main Camera: 50MP + 8MP + 2MP
            Selfie Camera: 32 MP
            Weight: 179 g
            Platform: Android 12.0
            Processor: Mediatek Dimensity 1300 Processor
            Data Generation: 5G
            Brightness: 950 NITS
            Resolution: 1080 x 2412
            Units: 10 """,chat)


        elif text in items:
          if text=='Samsung':
            send_message("""
            Model Name: Samsung Galaxy A03
            Color:Black
            RAM: 4GB
            Internal Storage:32 GB
            Display:6.5 inches PLS TFT LCD
            Battery: 5000 mAh Lithium ion
            Price:7,249
            Units:10""",chat)
            send_message("""
            Model Name: Samsung Galaxy A23
            Color:Orange
            RAM: 6GB
            Internal Storage:128 GB
            Display: 6.6 inches TFT LCD
            Battery: 5000 mAh Lithium ion
            Price:19,999
            Units:10""",chat)
            send_message("""
            Model Name: Samsung Galaxy Z Fold4 
            Color:Beige
            RAM: 12GB
            Internal Storage:256 GB
            Display:7.6 inches Dynamic AMOLED 2X
            Battery: 5000 mAh Lithium ion
            Price:154,999
            Units:10
            """,chat)
            
            keyboard = build_keyboard(Samsung)
            send_message("Which model  would you prefer?",chat,keyboard)
            time.sleep(2)
            send_message("""Let me tell you some cool features:
            1.It has Light Sensor and  Proximity Sensor.
            2.RAM expansion to 8GB.
            3.High Power Accelerometer.
            4.5 MP Front Camera
            5.48 MP+2MP Dual Camera
            """, chat)

        if text=='Oppo':
            send_message("""
            Model Name:Oppo A78
            Color:Grey
            RAM: 6 GB
            Internal Storage: 128 GB
            Display: 6.56 inches HD+ 
            Battery:  5000 mAh Lithium ion
            Price: 18,999
            Units: 10 """,chat)
            send_message("""
            Model_name: Oppo Reno8
            Color: Shimmer Black
            RAM: 8GB
            Internal Storage: 128 GB
            Display: 16.33 cm (6.43 inch) Full HD
            Battery: 4500 mAh Lithium ion
            Price: Rs. 29,499
            Units:10""",chat)
            keyboard = build_keyboard(Oppo)
            send_message("Which model  would you prefer?",chat,keyboard)


            
        
        if text=='Vivo':
            send_message("""
            Model Name:Vivo Y21G
            Color:Black
            RAM: 4GB
            Internal Storage: 64 GB
            Display: 6.51 inches  HD+ Halo
            Battery: 5000 mAh Lithium ion
            Price: 13,499
            Units: 10 """,chat)

            send_message("""
            Model_name:Vivo Y2207
            Color:Black
            RAM: 6GB
            Internal Storage: 128 GB
            Display: 6.51 inches  HD+ Halo
            Battery: 5000 mAh with 18W Fast Charging
            Price: Rs. 16,499
            Units:10""",chat)
            
            keyboard = build_keyboard(Vivo)
            send_message("Which model  would you prefer?",chat,keyboard)
        
        if text=='OnePlus':
            send_message("""
            Model Name:One Plus 10R
            Color: Sierra Black
            RAM: 12 GB
            Internal Storage: 256 GB
            Display: 6.7 inches FluidOLED
            Battery:  5000 mAh Lithium ion
            Price: 36,999
            Units: 10 """,chat)

            send_message("""
            Model_name:One Plus 10 Pro 5G
            Color: Emerald Forest
            RAM: 12 GB
            Internal Storage: 256 GB
            Display: 6.7 inches Fluid AMOLED with LTPO
            Battery:5000 mAh Lithium ion
            Price: Rs. 66,999
            Units:6
            """,chat)
            
            keyboard = build_keyboard(OnePlus)
            send_message("Which model would you prefer?",chat,keyboard)
        if text=='Redmi':
            send_message("""
            Model Name:Redmi A1+
            Color:Black
            RAM: 3GB
            Internal Storage: 32GB
            Display: 6.52 inches HD+
            Battery:5000 mAh Lithium ion
            Price: Rs.8,499
            Units: 10 """,chat)
            send_message("""
            Model_name:Redmi Note 12 Pro
            Color:Black
            RAM: 6GB
            Internal Storage: 128 GB
            Display: 6.57 inches AMOLED
            Battery:5000 mAh Lithium ion
            Price: Rs. 25,000
            Units:8 """,chat)

            
            keyboard = build_keyboard(Redmi)
            send_message("Which model  would you prefer?",chat,keyboard)
            
        if text == 'Apple':
          send_message("""
          Model Name: Apple iPhone 13
          Color: Pink, Starlight White,Midnight,Red
          RAM: 6GB
          Internal Storage: 128 GB
          Display: 6.1 inches SuperRetina XDR OLED
          Battery: 5000 mAh Lithium ion
          Price: Rs 62,990
          Units: 6""", chat)

          send_message("""
          Model Name: Apple iPhone 14 Pro Max
          Color: Deep Purple,Red,White,Smooth Black
          RAM: 6GB
          Internal Storage: 256 GB
          Display: 6.7 inches OLED
          Battery: 6000 mAh Lithium ion
          Price: Rs 1,39,000
          Units: 4""", chat)
          
          keyboard = build_keyboard(Apple)
          send_message("Which model  would you prefer?",chat,keyboard)
   
    
    
    

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)
 def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)


def main():
    db.setup()
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)


if _name_ == '_main_':
    main()
