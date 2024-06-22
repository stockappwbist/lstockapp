import yfinance as yf

def get_stock_info():
    ticker = "THYAO.IS"
    data = yf.download(ticker, end='2024-01-01')

    return data['Close'].iloc[-1]

# @app.route("/stock_info")
# def get_stock_information():
#     ticker = request.args.get('stock_name') + "." + "IS"
#     date_args = request.args.get('date_par')
#     user_price = request.args.get('user_price')
#     data = yf.download(ticker, end=date_args)
#     if not user_price:
#         return jsonify({'old_price': round(data['Close'].iloc[-1], 3)})
#
#     return jsonify({"msg": "Hello World"})