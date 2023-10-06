from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.INFO,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/')
def blog():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return "Welcome to the Logging App"


if __name__ == '__main__':
    app.run(debug=True)
