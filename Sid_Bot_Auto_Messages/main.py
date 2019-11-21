import requests

import MySQLdb

import asyncio

from time import sleep
from time import time

from threading import Thread

import selenium.webdriver.support.ui as ui

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataBase:

    def __init__(self):

        hostName = "remotemysql.com"
        port = "3306"
        username = "nyBJDIUR9V"
        dataBasePassword = "IugtHsr0Bb"
        dataBaseName = "nyBJDIUR9V"

        self.dataBase = MySQLdb.connect(
                                        hostName,
                                        username,
                                        dataBasePassword,
                                        dataBaseName)

        self.cursor = self.dataBase.cursor()

    def dataBaseCursor(self):

        return self.cursor

    def runQuery(self, query, params):

        try:

            return self.cursor.execute(query, params)

        except:

            print ("Failed to Execute.")

            self.CloseDataBase()

    def CloseDataBase(self):

        self.dataBase.commit();

        self.cursor.close()

        self.dataBase.close()

class UserMisc:

    def UserAlreadyExistCheck(self, dataBase, username):

        query = "select username from Users where username = %s ;"

        params = (username)

        rows = dataBase.runQuery(query, params)

        if( rows > 0 ):

            return True

        elif( rows == 0 ):

            return False

    def AddUser(self, dataBase):

        try:

            username = input("Enter username:- ")

            password = input("Enter password:- ")

            if( UserMisc.UserAlreadyExistCheck(self, dataBase, username) == False ):

                query = "insert into Users(username, password) values(%s, %s)"

                params = (username, password)

                rows = dataBase.runQuery(query, params)

                if( rows == 1 ):

                    print("Added successfully.")

                else:

                    print("User Failed to Add.")

            else:

                print ("User Already Exist.")

        except:

            dataBase.CloseDataBase();

    def DeleteUser(self, dataBase):

        try:

            username = input("Enter username:- ")

            if( UserMisc.UserAlreadyExistCheck(self, dataBase, username) == True ):

                query = "delete from Users where username = %s"

                params = (username)

                dataBase.runQuery(query, params)

                print(rows)

                if( rows == 1 ):

                    print("Deleted successfully.")

                else:

                    print("User Failed to Delete.")

            else:

                print ("User doesn't Exist.")

        except:

            dataBase.CloseDataBase();

    def GetAllUsers(self, dataBase):

        try:

            query = "select username from Users"

            dataBase.runQuery(query, ())

            rows = dataBase.dataBaseCursor().fetchall();

            for row in rows:

                print (row[0])

        except:

            print ("Failed to Fetch All Users.")

            dataBase.close();

class SidCommands:

    async def MessageCommand(self, message, messageElement, sleepTimer):

        while True:

            try:

                await asyncio.sleep(sleepTimer)

                messageElement.send_keys(message)

            except Exception as e:

                print("Sid Command Message Failed :( ", messageElement, e)

    async def RunCommands(self, messageElement, loop):

        sidMessages = [
            "Sid work\nSid deposit all \n",
            "Sid ed\n",
            "Sid el\n",
            "Sid er\n",
            "Sid em\n"
        ]

        sidMessagesTime = [
            3700,
            2500,
            850,
            400,
            140
        ]

        tasks = [None] * len(sidMessages)

        for i in range( len(sidMessages) ):

            tasks[i] = loop.create_task(self.MessageCommand(sidMessages[i], messageElement, sidMessagesTime[i]))

        await asyncio.wait(tasks)

class Client:

    def LoginCheck(self):

        #email = input("Enter Email:- ")

        #password = input("Enter Password:- ")

        #channel = input("Enter Channel URL:- ")

        self.email = "xyz"                     #   Discord Email
  
        self.password= "xyz"                   #   Discord Password

        self.channel = "https://discordapp.com/channels/639929703913750540/639930033871519784"        # Channel link

    def Main(self):

        options = Options()

        commands = SidCommands()

        #options.add_argument("--incognito")

        options.add_argument("--headless")

        #options.add_argument("--window_size=1920,1080")

        #options.add_argument('--disable-gpu')       # for windows

        #driver = webdriver.Chrome(executable_path=r'D://LEARNING//PROGRAMING//DISCORD//CHROME DRIVER//chromedriver.exe', chrome_options=options)

        driver = webdriver.Chrome(executable_path="/home/ubuntu/DISCORD_BOT/CHROME_DRIVER/chromedriver", chrome_options=options)

        driver.get(self.channel)

        driver.implicitly_wait(10)

        driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(self.email)

        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(self.password)

        driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        try:

            driver.implicitly_wait(10)

            messageElement = driver.find_element_by_tag_name('textarea')

            try:

                loop = asyncio.get_event_loop()

                loop.run_until_complete(commands.RunCommands(messageElement, loop))

            except Exception as e:

                #dataBase.CloseDataBase()

                print("Failed at async -> ", e)

            finally:

                loop.close()

        except Exception as e:

            #dataBase.CloseDataBase()

            print("Failed at Main -> ", e)


    def __init__(self):

        self.LoginCheck()

        self.Main()


if __name__ == "__main__" :

    #dataBase = DataBase()

    #userMisc = UserMisc()

    #sidCommands = SidCommands()

    client = Client()

    #dataBase.CloseDataBase()
