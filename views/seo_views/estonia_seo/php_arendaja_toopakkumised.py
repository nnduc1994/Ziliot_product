from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/php-arendaja-toopakkumised-tallinn')
def php_toopakkumised1(page=1):

    job_list = job_obj.get_job("php arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php arendaja", location="tallinn")
	
@EESEO1.route('/php-arendaja-toopakkumised-tartus')
def php_toopakkumised2(page=1):

    job_list = job_obj.get_job("php arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php arendaja", location="tartus")
	
@EESEO1.route('/php-arendaja-toopakkumised-narva')
def php_toopakkumised3(page=1):

    job_list = job_obj.get_job("php arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php arendaja", location="narva")
	
@EESEO1.route('/php-arendaja-toopakkumised-parnu')
def php_toopakkumised4(page=1):

    job_list = job_obj.get_job("php arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php arendaja", location="parnu")