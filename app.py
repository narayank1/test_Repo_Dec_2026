# this is the test file to test the code and ggithub actions.
# checking the linting flask test and run 
from flask import Flask, render_template
app = Falsk(name)

@app.route('/')
def hello_world():
return render_teplate('index.html')

@app.route('/health')
def health():
return 'Server is up and running'
