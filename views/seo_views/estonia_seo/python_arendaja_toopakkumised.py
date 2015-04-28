from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/python-arendaja-toopakkumised-tallinn')
def python_toopakkumised1(page=1):

    job_list = job_obj.get_job("python arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python arendaja", location="tallinn")
	
@EESEO1.route('/python-arendaja-toopakkumised-tartus')
def python_toopakkumised2(page=1):

    job_list = job_obj.get_job("python arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python arendaja", location="tartus")
	
@EESEO1.route('/python-arendaja-toopakkumised-narva')
def python_toopakkumised3(page=1):

    job_list = job_obj.get_job("python arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python arendaja", location="narva")
	
@EESEO1.route('/python-arendaja-toopakkumised-parnu')
def python_toopakkumised4(page=1):

    job_list = job_obj.get_job("python arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python arendaja", location="parnu")