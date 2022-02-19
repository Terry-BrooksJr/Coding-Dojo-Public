from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
  return """

  <h1>Adopt A  Pet</h1>
  <p>Browse through the links below to find your new furry friend:.</p>
  <ul>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/cats"><Cats</a</li>
    <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  """
@app.route('/animals/<pet_type>')
def animal(pet_type):
  results = []
  for animal in pet_type:
    results.append(f'<li>{{animal}}</li>')
  html = f"<h1>List of {pet_type}</h1>"
  return results + html

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)