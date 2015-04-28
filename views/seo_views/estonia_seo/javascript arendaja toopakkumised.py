from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/javascript-arendaja-toopakkumised-tallinn')
def javascript_toopakkumised1(page=1):

    job_list = job_obj.get_job("javascript arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript arendaja", location="tallinn")
	
@EESEO1.route('/javascript-arendaja-toopakkumised-tartus')
def javascript_toopakkumised2(page=1):

    job_list = job_obj.get_job("javascript arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript arendaja", location="tartus")
	
@EESEO1.route('/javascript-arendaja-toopakkumised-narva')
def javascript_toopakkumised3(page=1):

    job_list = job_obj.get_job("javascript arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript arendaja", location="narva")
	
@EESEO1.route('/javascript-arendaja-toopakkumised-parnu')
def javascript_toopakkumised4(page=1):

    job_list = job_obj.get_job("javascript arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript arendaja", location="parnu")