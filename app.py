from flask import Flask, request, render_template
from api import get_api

flask_app = Flask(__name__)
flask_app.config["CACHE_TYPE"] = "null"

@flask_app.route('/', methods=['GET', 'POST'])
def crypto_cur():
    """
        SEND RESULT FROM API TO WEB PAGE
    """
    results = []
    if request.method == 'GET':
        print('GET METHOD OK')
        data = get_api()
        for x in data['data']:
            results.append(x)
        print('FOR FINISHED')
        # SORT BY ID
        sort_by = request.args.get('sort_by')
        reverse = request.args.get('reverse')
        if sort_by == 'price' or sort_by == 'percent_change_24h' or sort_by == 'percent_change_7d' or sort_by == 'market_cap' or sort_by == 'volume_24h' and reverse:
            results = sorted(results, key=lambda k: k['quote']['RON'][sort_by], reverse=int(reverse))
        
        elif sort_by and reverse:
            results = sorted(results, key=lambda k: k[sort_by], reverse=int(reverse))

        # SORT BY ID - FINISH
    return render_template("index.html", results=results, context=reverse)

if __name__ == '__main__':
    flask_app.run()