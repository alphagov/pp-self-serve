
import config

from flask import Flask, render_template

from flask.ext.assets import Environment, Bundle


app = Flask(__name__)
app.debug = True

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('css/main.scss', filters='pyscss', output='css/main.css')
assets.register('scss_all', scss)

@app.route('/favicon.ico')
def favicon():
    return ''


@app.route('/static/<path:path>', methods=['GET'])
def static_files():
    return send_from_directory(config.STATIC_PATH, path)

# @app.route('/<path:path>', methods=['GET'])
@app.route('/', methods=['GET'])
# def render(path):
def render():
    return render_template('pp-self-serve.html',
        title='Hello, world!',
        content='Hello, world!',
        govuk_template_path='/static/govuk_template/')

if __name__ == '__main__':
    app.run()
