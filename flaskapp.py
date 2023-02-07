
from flask import Flask
from collections import Counter

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello from Flask! i promise im almost there professor'

@app.route('/countme/<input_str>')
def count_me(input_str):
  input_counter = Counter(input_str)
  response = []
  for letter, count in input_counter.most_common():
    response.append('"{}": {}'.format(letter, count))
  return '<br>'.join(response)

if __name__ == '__main__':
  app.run()