from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/cobol-arendaja-toopakkumised-tallinn')
def cobol_toopakkumised1(page=1):

    job_list = job_obj.get_job("cobol arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol arendaja", location="tallinn")
	
@EESEO1.route('/cobol-arendaja-toopakkumised-tartus')
def cobol_toopakkumised2(page=1):

    job_list = job_obj.get_job("cobol arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol arendaja", location="tartus")
	
@EESEO1.route('/cobol-arendaja-toopakkumised-narva')
def cobol_toopakkumised3(page=1):

    job_list = job_obj.get_job("cobol arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol arendaja", location="narva")
	
@EESEO1.route('/cobol-arendaja-toopakkumised-parnu')
def cobol_toopakkumised4(page=1):

    job_list = job_obj.get_job("cobol arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol arendaja", location="parnu")