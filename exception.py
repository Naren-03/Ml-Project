from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os,sys

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])

def index():
    try:
        raise Exception("Testing Exception file") #Is a Error
    except Exception as e:
        var = CustomException(e,sys) #type:ignore
        logging.info(var.error_message)

    logging.info("We are testing our logging file")
    return "Hello World"

if __name__== "__main__":
    app.run(debug=True)