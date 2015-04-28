
from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()


@EESEO1.route('/actionscript-arendaja-toopakkumised-tallinn')
def actionscript_toopakkumised1(page=1):

    job_list = job_obj.get_job("actionscript arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsEstonia.html", jobs=job_list, title="actionscript arendaja", location="tallinn")
	
@EESEO1.route('/actionscript-arendaja-toopakkumised-tartus')
def actionscript_toopakkumised2(page=1):

    job_list = job_obj.get_job("actionscript arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsEstonia.html", jobs=job_list, title="actionscript arendaja", location="tartus")
	
@EESEO1.route('/actionscript-arendaja-toopakkumised-narva')
def actionscript_toopakkumised3(page=1):

    job_list = job_obj.get_job("actionscript arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsEstonia.html", jobs=job_list, title="actionscript arendaja", location="narva")
	
@EESEO1.route('/actionscript-arendaja-toopakkumised-parnu')
def actionscript_toopakkumised4(page=1):

    job_list = job_obj.get_job("actionscript arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsEstonia.html", jobs=job_list, title="actionscript arendaja", location="parnu")