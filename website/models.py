from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, IntegerRangeField, SelectField
from wtforms.validators import DataRequired, Optional, NumberRange

class ProjectsForm (FlaskForm):
  project_ID = IntegerField (label = "Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  project_title = StringField (label = "Project Title",     validators = [DataRequired(message = "Please fill in this field")])
  project_starting_date = DateField (label = "Starting Date",     validators = [DataRequired(message = "Please fill in this field")])
  project_summary = StringField (label = "Project Summary",     validators = [DataRequired(message = "Please fill in this field")])
  project_due_date = DateField (label = "Due Date",     validators = [DataRequired(message = "Please fill in this field")])
  supervisor_executive_ID= IntegerField (label = "Supervisor Executive ID",     validators = [DataRequired(message = "Please fill in this field")])
  supervisor_researcher_ID= IntegerField (label = "Supervisor Researcher ID",     validators = [DataRequired(message = "Please fill in this field")])
  org_ID= IntegerField (label = "Organisation ID",     validators = [DataRequired(message = "Please fill in this field")])
  capital = IntegerField (label = "Capital",     validators = [DataRequired(message = "Please fill in this field")])
  programme_ID= IntegerField (label = "Financial Programme ID",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class ResearchersForm (FlaskForm):
  researcher_ID= IntegerField (label = "Reasercher ID",     validators = [DataRequired(message = "Please fill in this field")])
  first_name = StringField (label = " First Name", validators = [DataRequired(message = "Please fill in this field")])
  last_name = StringField (label = " Last Name", validators = [DataRequired(message = "Please fill in this field")])
  gender = StringField (label = "Gender", validators = [DataRequired(message = "Please fill in this field")])
  birth_date = DateField (label = "Date", validators = [DataRequired(message = "Please fill in this field")])
  org_ID= IntegerField (label = "Organisation ID",     validators = [DataRequired(message = "Please fill in this field")])
  employment_starting_date = DateField (label = "Date", validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class OrganizationsForm(FlaskForm):
  org_ID= IntegerField (label = "Organisation ID",     validators = [DataRequired(message = "Please fill in this field")])
  org_name = StringField (label = " Organisation Name", validators = [DataRequired(message = "Please fill in this field")])
  org_acronym = StringField (label = " Organisation Acronym", validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")


class Organization_AddressForm(FlaskForm):
  org_ID= IntegerField (label = "Organisation ID",     validators = [DataRequired(message = "Please fill in this field")])
  street = StringField (label = "Street", validators = [DataRequired(message = "Please fill in this field")])
  st_number = IntegerField (label = "Street", validators = [DataRequired(message = "Please fill in this field")])
  ZIP_code = IntegerField (label = "ZIP Code", validators = [DataRequired(message = "Please fill in this field")])
  city = StringField (label = "City", validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class Organization_TelephoneForm(FlaskForm):
  org_ID= IntegerField (label = "Organisation ID",     validators = [DataRequired(message = "Please fill in this field")])
  telephone = StringField (label = "Telephone", validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class Organization_TelephoneForm2(FlaskForm):
  org_ID= IntegerField (label = "Organisation ID",     validators = [DataRequired(message = "Please fill in this field")])
  telephone = StringField (label = "Telephone", validators = [DataRequired(message = "Please fill in this field")])
  new_telephone = StringField (label = "New Telephone", validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class CompanyForm(FlaskForm):
  company_ID= IntegerField (label = "Company ID",     validators = [DataRequired(message = "Please fill in this field")])
  capital = IntegerField (label = "Capital",     validators = [DataRequired(message = "Please fill in this field")])
  org_ID= IntegerField (label = "Organisation ID",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class UniversityForm(FlaskForm):
  university_ID= IntegerField (label = "University ID",     validators = [DataRequired(message = "Please fill in this field")])
  ministry_budget = IntegerField (label = "Ministry budget",     validators = [DataRequired(message = "Please fill in this field")])
  org_ID= IntegerField (label = "Organisation ID",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class Research_CenterForm(FlaskForm):
  research_center_ID= IntegerField (label = "Research Centre ID",     validators = [DataRequired(message = "Please fill in this field")])
  ministry_budget = IntegerField (label = "Ministry budget",     validators = [DataRequired(message = "Please fill in this field")])
  private_budget = IntegerField (label = "Private budget",     validators = [DataRequired(message = "Please fill in this field")])
  org_ID= IntegerField (label = "Organisation ID",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class HFRI_executivesForm(FlaskForm):
  executive_ID= IntegerField (label = "Executive ID",     validators = [DataRequired(message = "Please fill in this field")])
  executive_first_name = StringField (label = "Executive First Name",     validators = [DataRequired(message = "Please fill in this field")])
  executive_last_name = StringField (label = "Executive Last Name",     validators = [DataRequired(message = "Please fill in this field")])
  HFRI_department_ID= IntegerField (label = "HFRI Department ID",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class HFRI_departmentForm(FlaskForm):
  HFRI_department_ID= IntegerField (label = "HFRI department ID",     validators = [DataRequired(message = "Please fill in this field")])
  HFRI_department_name = StringField (label = " Department Name", validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class Financial_ProgrammeForm(FlaskForm):
  programme_ID= IntegerField (label = "Financial Programme ID",     validators = [DataRequired(message = "Please fill in this field")])
  HFRI_department_ID= IntegerField (label = "HFRI department ID",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class belongs_toForm(FlaskForm):
  scientific_field = StringField (label = "Scientific Field", validators = [DataRequired(message = "Please fill in this field")])
  project_ID = IntegerField (label = "Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class belongs_to2Form(FlaskForm):
  old_scientific_field = StringField (label = "Old Scientific Field", validators = [DataRequired(message = "Please fill in this field")])
  old_project_ID = IntegerField (label = "Old Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  scientific_field = StringField (label = "Scientific Field", validators = [DataRequired(message = "Please fill in this field")])
  project_ID = IntegerField (label = "Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class scientific_fieldForm(FlaskForm):
  scientific_field_name = StringField (label = "Scientific Field", validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class final_productForm(FlaskForm):
  product_ID= IntegerField (label = "Product ID",     validators = [DataRequired(message = "Please fill in this field")])
  product_title= StringField (label = "Title",     validators = [DataRequired(message = "Please fill in this field")])
  project_ID = IntegerField (label = "Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  product_summary = StringField (label = "Project Summary",     validators = [Optional()])
  product_due_date = DateField (label = "Due Date",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")
  
class evaluateForm(FlaskForm):
  researcher_ID= IntegerField (label = "Reasercher ID",     validators = [DataRequired(message = "Please fill in this field")])
  project_ID = IntegerField (label = "Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  grade = StringField (label = "Grade",     validators = [Optional()])
  evaluation_date = DateField (label = "Evaluation Date",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class evaluate2Form(FlaskForm):
  researcher_ID = IntegerField (label = "Reasercher ID",     validators = [DataRequired(message = "Please fill in this field")])
  project_ID = IntegerField (label = "Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  new_researcher_ID= IntegerField (label = "Reasercher ID",     validators = [DataRequired(message = "Please fill in this field")])
  new_project_ID = IntegerField (label = "Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  grade = StringField (label = "Grade",     validators = [Optional()])
  evaluation_date = DateField (label = "Evaluation Date",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class worksForm(FlaskForm):
  researcher_ID= IntegerField (label = "Reasercher ID",     validators = [DataRequired(message = "Please fill in this field")])
  project_ID = IntegerField (label = "Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")

class works2Form(FlaskForm):
  researcher_ID = IntegerField (label = "Reasercher ID",     validators = [DataRequired(message = "Please fill in this field")])
  project_ID = IntegerField (label = "Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  new_researcher_ID= IntegerField (label = "New Reasercher ID",     validators = [DataRequired(message = "Please fill in this field")])
  new_project_ID = IntegerField (label = "New Project ID",     validators = [DataRequired(message = "Please fill in this field")])
  submit = SubmitField("Submit")


  