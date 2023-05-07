from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Location', validators=[DataRequired()])
    url = StringField(label='Url', validators=[DataRequired(), URL()])
    open_time = TimeField(label='Opening Time', validators=[DataRequired()])
    close_time = TimeField(label='Closing Time', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating', choices=[('☕'* _ )for _ in range(5)])
    wifi = SelectField(label='Wifi Rating', choices=[('💪' * _) for _ in range(5)])
    power = SelectField(label='Power Rating', choices=[('🔌' * _) for _ in range(5)])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', encoding='utf-8') as f:
            for field in form:
                if field.name == 'cafe':
                    f.write(f'\n {field.data}')
                else:
                    f.write(f', {field.data}')
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
