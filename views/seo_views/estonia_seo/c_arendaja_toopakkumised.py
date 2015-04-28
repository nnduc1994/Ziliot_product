from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()


@EESEO1.route('/c-arendaja-toopakkumised-tallinn')
def c_toopakkumised1(page=1):

    job_list = job_obj.get_job("c arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c arendaja", location="tallinn")
	
@EESEO1.route('/c-arendaja-toopakkumised-tartus')
def c_toopakkumised2(page=1):

    job_list = job_obj.get_job("c arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c arendaja", location="tartus")
	
@EESEO1.route('/c-arendaja-toopakkumised-narva')
def c_toopakkumised3(page=1):

    job_list = job_obj.get_job("c arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c arendaja", location="narva")
	
@EESEO1.route('/c-arendaja-toopakkumised-parnu')
def c_toopakkumised4(page=1):

    job_list = job_obj.get_job("c arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c arendaja", location="parnu")