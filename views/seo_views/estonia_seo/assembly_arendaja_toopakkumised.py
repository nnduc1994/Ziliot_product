from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()
@EESEO1.route('/assembly-arendaja-toopakkumised-tallinn')
def assembly_toopakkumised1(page=1):

    job_list = job_obj.get_job("assembly arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly arendaja", location="tallinn")
	
@EESEO1.route('/assembly-arendaja-toopakkumised-tartus')
def assembly_toopakkumised2(page=1):

    job_list = job_obj.get_job("assembly arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly arendaja", location="tartus")
	
@EESEO1.route('/assembly-arendaja-toopakkumised-narva')
def assembly_toopakkumised3(page=1):

    job_list = job_obj.get_job("assembly arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly arendaja", location="narva")
	
@EESEO1.route('/assembly-arendaja-toopakkumised-parnu')
def assembly_toopakkumised4(page=1):

    job_list = job_obj.get_job("assembly arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly arendaja", location="parnu")