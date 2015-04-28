
from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/pascal-arendaja-toopakkumised-tallinn')
def pascal_toopakkumised1(page=1):

    job_list = job_obj.get_job("pascal arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal arendaja", location="tallinn")
	
@EESEO1.route('/pascal-arendaja-toopakkumised-tartus')
def pascal_toopakkumised2(page=1):

    job_list = job_obj.get_job("pascal arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal arendaja", location="tartus")
	
@EESEO1.route('/pascal-arendaja-toopakkumised-narva')
def pascal_toopakkumised3(page=1):

    job_list = job_obj.get_job("pascal arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal arendaja", location="narva")
	
@EESEO1.route('/pascal-arendaja-toopakkumised-parnu')
def pascal_toopakkumised4(page=1):

    job_list = job_obj.get_job("pascal arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal arendaja", location="parnu")