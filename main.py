from flask import Flask, render_template
  
app = Flask(__name__)

JOB = [
  {
    'id': 1,
    'title': 'Data analyst',
    'location': 'Delhi, india',
    'Salary': 'Rs. 10, 00,000'
  },
  {
    'id': 2,
    'title': 'Data Science',
    'location': 'Delhi, india',
    'Salary': 'Rs. 10, 00,000'
  },
{
    'id': 3,
    'title': 'Forntend',
    'location': 'Delhi, india',
    'Salary': 'Rs. 10, 00,000'
  },
{
    'id': 4,
    'title': 'Html Deplpor',
    'location': 'Delhi, india',
    'Salary': 'Rs. 10, 00,000'
  }
]


@app.route('/')
def hello_world():
  return render_template('home.html', job=JOB)

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)