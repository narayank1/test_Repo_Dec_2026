from flask import Flask, render_template
app = Falsk(name)

@app.route('/')
def hello_world():
return render_teplate('index.html')

@app.route('/health')
def health():
return 'Server is up and running'
