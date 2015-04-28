from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()


@EESEO1.route('/visual-basic-arendaja-toopakkumised-tallinn')
def visual_basic_toopakkumised1(page=1):

    job_list = job_obj.get_job("visual basic arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic arendaja", location="tallinn")
	
@EESEO1.route('/visual-basic-arendaja-toopakkumised-tartus')
def visual_basic_toopakkumised2(page=1):

    job_list = job_obj.get_job("visual basic arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic arendaja", location="tartus")
	
@EESEO1.route('/visual-basic-arendaja-toopakkumised-narva')
def visual_basic_toopakkumised3(page=1):

    job_list = job_obj.get_job("visual basic arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic arendaja", location="narva")
	
@EESEO1.route('/visual-basic-arendaja-toopakkumised-parnu')
def visual_basic_toopakkumised4(page=1):

    job_list = job_obj.get_job("visual basic arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic arendaja", location="parnu")