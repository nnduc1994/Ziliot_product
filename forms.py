from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, validators, DateField


class SearchForm(Form):
    title = StringField('Title')
    location = StringField('Location')
    search = SubmitField('Search')


class CreateWorkForm(Form):
    title = StringField('Job Title', [validators.DataRequired("Please enter job title")])
    location = StringField('Location', [validators.DataRequired("Please enter job location")])
    company_name = StringField('Company Name', [validators.DataRequired("Please enter company name")])
    description = TextAreaField('Job Description', [validators.DataRequired("Please enter some job description")])
    link = StringField('Link', [validators.DataRequired("Please enter link to job page")])
    expire_day = DateField('Expire Day', [validators.DataRequired("Please choose an expire day")])
    create = SubmitField('Create new job')