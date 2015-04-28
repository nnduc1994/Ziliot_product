from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/sql-arendaja-toopakkumised-tallinn')
def sql_toopakkumised1(page=1):

    job_list = job_obj.get_job("sql arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql arendaja", location="tallinn")
	
@EESEO1.route('/sql-arendaja-toopakkumised-tartus')
def sql_toopakkumised2(page=1):

    job_list = job_obj.get_job("sql arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql arendaja", location="tartus")
	
@EESEO1.route('/sql-arendaja-toopakkumised-narva')
def sql_toopakkumised3(page=1):

    job_list = job_obj.get_job("sql arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql arendaja", location="narva")
	
@EESEO1.route('/sql-arendaja-toopakkumised-parnu')
def sql_toopakkumised4(page=1):

    job_list = job_obj.get_job("sql arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql arendaja", location="parnu")