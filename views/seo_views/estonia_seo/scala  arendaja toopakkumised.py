from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/scala-arendaja-toopakkumised-tallinn')
def scala_toopakkumised1(page=1):

    job_list = job_obj.get_job("scala arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala arendaja", location="tallinn")
	
@EESEO1.route('/scala-arendaja-toopakkumised-tartus')
def scala_toopakkumised2(page=1):

    job_list = job_obj.get_job("scala arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala arendaja", location="tartus")
	
@EESEO1.route('/scala-arendaja-toopakkumised-narva')
def scala_toopakkumised3(page=1):

    job_list = job_obj.get_job("scala arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala arendaja", location="narva")
	
@EESEO1.route('/scala-arendaja-toopakkumised-parnu')
def scala_toopakkumised4(page=1):

    job_list = job_obj.get_job("scala arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala arendaja", location="parnu")