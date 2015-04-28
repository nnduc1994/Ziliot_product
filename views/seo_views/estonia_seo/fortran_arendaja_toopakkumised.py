from ....models import Job, JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = JobEstonia()

@EESEO1.route('/fortran-arendaja-toopakkumised-tallinn')
def fortran_toopakkumised1(page=1):

    job_list = job_obj.get_job("fortran arendaja ", "tallinn").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran arendaja", location="tallinn")
	
@EESEO1.route('/fortran-arendaja-toopakkumised-tartus')
def fortran_toopakkumised2(page=1):

    job_list = job_obj.get_job("fortran arendaja", "tartus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran arendaja", location="tartus")
	
@EESEO1.route('/fortran-arendaja-toopakkumised-narva')
def fortran_toopakkumised3(page=1):

    job_list = job_obj.get_job("fortran arendaja", "narva").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran arendaja", location="narva")
	
@EESEO1.route('/fortran-arendaja-toopakkumised-parnu')
def fortran_toopakkumised4(page=1):

    job_list = job_obj.get_job("fortran arendaja", "parnu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran arendaja", location="parnu")