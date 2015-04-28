from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/perl-arendaja-toopakkumised-tallinn')
def perl_toopakkumised1(page=1):

    job_list = job_obj.get_job("perl arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl arendaja", location="tallinn")
	
@EESEO1.route('/perl-arendaja-toopakkumised-tartus')
def perl_toopakkumised2(page=1):

    job_list = job_obj.get_job("perl arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl arendaja", location="tartus")
	
@EESEO1.route('/perl-arendaja-toopakkumised-narva')
def perl_toopakkumised3(page=1):

    job_list = job_obj.get_job("perl arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl arendaja", location="narva")
	
@EESEO1.route('/perl-arendaja-toopakkumised-parnu')
def perl_toopakkumised4(page=1):

    job_list = job_obj.get_job("perl arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl arendaja", location="parnu")