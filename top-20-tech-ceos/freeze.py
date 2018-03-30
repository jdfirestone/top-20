from flask_frozen import Freezer
# instead of routes, use the name of the file that runs YOUR Flask app
from ceos import app

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def detail():
        yield '/ceo/1'
        yield '/ceo/2'
        yield '/ceo/3'
        yield '/ceo/4'
        yield '/ceo/5'
        yield '/ceo/6'
        yield '/ceo/7'
        yield '/ceo/8'
        yield '/ceo/9'
        yield '/ceo/10'
        yield '/ceo/11'
        yield '/ceo/12'
        yield '/ceo/13'
        yield '/ceo/14'
        yield '/ceo/15'
        yield '/ceo/16'
        yield '/ceo/17'
        yield '/ceo/18'
        yield '/ceo/19'
        yield '/ceo/20'

if __name__ == '__main__':
    freezer.freeze()
