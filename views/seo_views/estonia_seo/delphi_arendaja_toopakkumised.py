from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()


@EESEO1.route('/delphi-arendaja-toopakkumised-tallinn')
def delphi_toopakkumised1(page=1):

    job_list = job_obj.get_job("delphi arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi arendaja", location="tallinn")
	
@EESEO1.route('/delphi-arendaja-toopakkumised-tartus')
def delphi_toopakkumised2(page=1):

    job_list = job_obj.get_job("delphi arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi arendaja", location="tartus")
	
@EESEO1.route('/delphi-arendaja-toopakkumised-narva')
def delphi_toopakkumised3(page=1):

    job_list = job_obj.get_job("delphi arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi arendaja", location="narva")
	
@EESEO1.route('/delphi-arendaja-toopakkumised-parnu')
def delphi_toopakkumised4(page=1):

    job_list = job_obj.get_job("delphi arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi arendaja", location="parnu")