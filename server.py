from flask import Flask, request, render_template
from converter import convert_currency
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/convert")
def convert():
  try:
    amount = float(request.args.get('amount'))
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    result = convert_currency(amount, from_currency, to_currency)
    if result['result'] != 'success':
      return render_template("error.html", message=result.get("error-type", "Unknown error"))
    return render_template("result.html", amount=amount, from_currency=from_currency, to_currency=to_currency, converted=result["conversion_result"], rate=result["conversion_rate"])
  except Exception as e:
    return render_template("error.html", message=str(e))

if __name__ == "__main__":  
  serve(app, host="0.0.0.0", port=8000)