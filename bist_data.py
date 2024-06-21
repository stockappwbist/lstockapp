from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)


@app.route("/")
def r_hello_world():
    return jsonify({"msg": "Hello World"})


@app.route("/stock_info")
def get_stock_information():
    ticker = request.args.get('stock_name') + "." + "IS"
    date_args = request.args.get('date_par')
    user_price = request.args.get('user_price')
    data = yf.download(ticker, end=date_args)
    if not user_price:
        return jsonify({'old_price': round(data['Close'].iloc[-1], 3)})

    return jsonify({"msg": "Hello World"})


if __name__ == '__main__':
    app.run(debug=True)


