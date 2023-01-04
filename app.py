from flask import Flask, render_template
from dataset import main_projects, small_projects
from styles import style


app = Flask(__name__)


@app.route('/')
def main_page():
    content = {'main_projects': main_projects, 'small_projects': small_projects, 'style': style}
    return render_template('main_page.html', content=content)
    
