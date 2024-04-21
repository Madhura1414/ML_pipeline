from flask import Flask, request, render_template, jsonify
# Alternatively can use Django, FastAPI, or anything similar
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/predict', methods = ['POST', "GET"])


def predict_datapoint(): 
    if request.method == "GET": 
        return render_template("form.html")
    else: 
        data = CustomData(
            carat = float(request.form.get('trans_date_trans_time')),
            depth = float(request.form.get('cc_num')),
            table = float(request.form.get("merchant")), 
            x= float(request.form.get("category")), 
            y = float(request.form.get("amt")),
            z = float(request.form.get("first")), 
            cut = request.form.get("last"), 
            color = request.form.get("gender"), 
            clarity = request.form.get("street"),
            city = request.form.get('city'),
            state = request.form.get('state'),
            zip = int(request.form.get('zip')),
            lat = float(request.form.get('lat')),
            long = float(request.form.get('long')),
            city_pop = int(request.form.get('city_pop')),
            job = request.form.get('job'),
            dob = request.form.get('dob'),
            trans_num = request.form.get('trans_num'),
            unix_time = int(request.form.get('unix_time')),
            merch_lat= float(request.form.get('merch_lat')),
            merch_long=float(request.form.get('merch_long')),
            is_fraud=int(request.form.get('is_fraud')) 
        )
    new_data = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(new_data)

    results = round(pred[0],2)

    return render_template("results.html", final_result = results)

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", debug= True)

#http://127.0.0.1:5000/ in browser