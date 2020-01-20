from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import InputRequired, DataRequired, Email


class InfoForm(FlaskForm):
    item = StringField('Item you want to buy', validators=[InputRequired()])
    cost = IntegerField('Cost', validators=[
                        InputRequired(message="Please enter the cost")])
    time = SelectField('Repayment time',
                       validators=[DataRequired()],
                       choices=[('3 months', '3 Months'),
                                ('6 months', '6 Months'),
                                ('12 months', '12 Months')])
    name = StringField('Enter your name',
                       validators=[InputRequired(message="Please enter your name as it appears in your ID")])
    national_id = StringField('Your NIDA ID number',
                              validators=[InputRequired()])
    user_address = StringField("Your address", validators=[
                               InputRequired(message="Please tell us your current address")])
    email = StringField("Your email",
                        validators=[InputRequired(), Email(message=("Enter valid email"))])
    phone = IntegerField("Enter your phone number", validators=[
                         InputRequired(message="Enter valid number")])
    birthday = StringField("Enter your birthdate", validators=[
                           InputRequired(message="enter your birthday")])
    status = SelectField('Marital status',
                         validators=[InputRequired(message="Please choose your status")],
                         choices=[('married', 'Married'),
                                  ('single', 'Single'),
                                  ('divorced', 'Divorced')])
    employer = StringField("Employer", validators=[InputRequired(
        message="Please fill the name of your employer")])
    address = StringField("Employer's address",
                          validators=[InputRequired(message="enter the address of your employer")])
    contract = StringField("Contract",
                           validators=[InputRequired(message="Please fill in the terms of your contract")])
    occupation = StringField("Occupation",
                             validators=[InputRequired(message="Please enter your occupation")])
    salary = IntegerField("Salary",
                          validators=[InputRequired(message="Please enter your salary")])
    loan = StringField("Any outstanding loan",
                       validators=[InputRequired(message="Please fill this in")])
    dependents = IntegerField("Any dependents",
                              validators=[InputRequired(message="Please fill this in")])
    expenditures = IntegerField("Expenditures",
                                validators=[InputRequired(message="please fill this in")])
