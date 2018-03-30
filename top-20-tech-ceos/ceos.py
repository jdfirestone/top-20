from flask import Flask, render_template
from modules import convert_to_dict

app = Flask(__name__)

ceos_list = convert_to_dict("ceos.csv")


@app.route('/')
def index():
    number_list = []
    name_list = []
    for ceo in ceos_list:
        number_list.append(ceo['number'])
        name_list.append(ceo['name'])
    pairs_list = zip(number_list, name_list)
    return render_template('index.html', pairs=pairs_list, the_title="Ceos Index")

@app.route('/ceo/<num>')
def detail(num):
    for ceo in ceos_list:
        if ceo['number'] == num:
            ceos_dict = ceo
            break
    return render_template('ceo.html', ceo=ceos_dict, ord=ord, the_title=ceos_dict['name'])

if __name__ == '__main__':
    app.run(debug=True)
