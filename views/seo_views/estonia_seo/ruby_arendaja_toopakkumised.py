from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/ruby-arendaja-toopakkumised-tallinn')
def ruby_toopakkumised1(page=1):

    job_list = job_obj.get_job("ruby arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby arendaja", location="tallinn")
	
@EESEO1.route('/ruby-arendaja-toopakkumised-tartus')
def ruby_toopakkumised2(page=1):

    job_list = job_obj.get_job("ruby arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby arendaja", location="tartus")
	
@EESEO1.route('/ruby-arendaja-toopakkumised-narva')
def ruby_toopakkumised3(page=1):

    job_list = job_obj.get_job("ruby arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby arendaja", location="narva")
	
@EESEO1.route('/ruby-arendaja-toopakkumised-parnu')
def ruby_toopakkumised4(page=1):

    job_list = job_obj.get_job("ruby arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby arendaja", location="parnu")