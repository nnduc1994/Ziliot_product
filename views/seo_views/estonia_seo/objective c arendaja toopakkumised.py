
from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/objective-c-arendaja-toopakkumised-tallinn')
def objective_c_toopakkumised1(page=1):

    job_list = job_obj.get_job("objective c arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c arendaja", location="tallinn")
	
@EESEO1.route('/objective-c-arendaja-toopakkumised-tartus')
def objective_c_toopakkumised2(page=1):

    job_list = job_obj.get_job("objective c arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c arendaja", location="tartus")
	
@EESEO1.route('/objective-c-arendaja-toopakkumised-narva')
def objective_c_toopakkumised3(page=1):

    job_list = job_obj.get_job("objective c arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c arendaja", location="narva")
	
@EESEO1.route('/objective-c-arendaja-toopakkumised-parnu')
def objective_c_toopakkumised4(page=1):

    job_list = job_obj.get_job("objective c arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c arendaja", location="parnu")