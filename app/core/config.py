from dotenv import load_dotenv
import os

load_dotenv()#Load Environment Variable from .env file

class Setting:
    DATABASE_URL=os.getenv("DATABASE_URL")

settings=Setting()    #Create an instance of class to access
    