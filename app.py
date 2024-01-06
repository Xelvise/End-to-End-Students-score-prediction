from flask import Flask, render_template, request, jsonify
from src.pipeline.predict_pipeline import DataChannel, predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict-data', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    
    elif request.method == 'POST':
        data = DataChannel(
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = request.form.get('reading_score'),
            writing_score = request.form.get('writing_score')
        )
        df = data.switch_to_df()
        output = predict(df)
        return render_template('home.html', results=output[0])

# Creating an API endpoint url
@app.route('/api-predict', methods=['POST'])
def pred():
    dict = request.get_json()
    data = DataChannel(
        gender = dict['gender'],
        race_ethnicity = dict['ethnicity'],
        parental_level_of_education = dict['parental_level_of_education'],
        lunch = dict['lunch'],
        test_preparation_course = dict['test_preparation_course'],
        reading_score = dict['reading_score'],
        writing_score = dict['writing_score']
    )
    df = data.switch_to_df()
    output = predict(df)
    return jsonify({'maths_score': output[0]}), 200


if __name__ == '__main__':
    app.run(debug=True)