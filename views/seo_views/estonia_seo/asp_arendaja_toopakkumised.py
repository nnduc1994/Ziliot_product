from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/asp-arendaja-toopakkumised-tallinn')
def asp_toopakkumised1(page=1):

    job_list = job_obj.get_job("asp arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp arendaja", location="tallinn")
	
@EESEO1.route('/asp-arendaja-toopakkumised-tartus')
def asp_toopakkumised2(page=1):

    job_list = job_obj.get_job("asp arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp arendaja", location="tartus")
	
@EESEO1.route('/asp-arendaja-toopakkumised-narva')
def asp_toopakkumised3(page=1):

    job_list = job_obj.get_job("asp arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp arendaja", location="narva")
	
@EESEO1.route('/asp-arendaja-toopakkumised-parnu')
def asp_toopakkumised4(page=1):

    job_list = job_obj.get_job("asp arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp arendaja", location="parnu")