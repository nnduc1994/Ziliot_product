
from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()
@EESEO1.route('/coldfusion-arendaja-toopakkumised-tallinn')
def coldfusion_toopakkumised1(page=1):

    job_list = job_obj.get_job("coldfusion arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion arendaja", location="tallinn")
	
@EESEO1.route('/coldfusion-arendaja-toopakkumised-tartus')
def coldfusion_toopakkumised2(page=1):

    job_list = job_obj.get_job("coldfusion arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion arendaja", location="tartus")
	
@EESEO1.route('/coldfusion-arendaja-toopakkumised-narva')
def coldfusion_toopakkumised3(page=1):

    job_list = job_obj.get_job("coldfusion arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion arendaja", location="narva")
	
@EESEO1.route('/coldfusion-arendaja-toopakkumised-parnu')
def coldfusion_toopakkumised4(page=1):

    job_list = job_obj.get_job("coldfusion arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion arendaja", location="parnu")