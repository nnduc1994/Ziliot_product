from ..forms import SearchForm
from ..models import JobEstonia
from flask import render_template, request, redirect, url_for, Blueprint

JOB_PER_PAGE = 7

estonia = Blueprint('estonia', __name__)

@estonia.route("/en", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == "POST":
        if form.title.data == "":
            title = "all"
        else:
            title = form.title.data.lower().strip()
        if form.location.data == "":
            location = "everywhere"
        else:
            location = form.location.data.lower().strip()
        return redirect(url_for('estonia.result', title=title, location=location, page=1, lang="ee"))
    elif request.method == "GET":
        return render_template("searcher.html", form=form, lang="ee")

@estonia.route('/en/<string:title>-jobs-in-<string:location>')
@estonia.route('/en/<int:page>/<string:title>-jobs-in-<string:location>')
def result(title, location, page=1):
    form = SearchForm()
    job_obj = JobEstonia()
    job_list = job_obj.get_job(title, location).paginate(page, JOB_PER_PAGE, False)
    return render_template("results.html", jobs=job_list, title=title.title(), location=location.title(), form=form, lang="ee")

# Estonia pages
@estonia.route('/', methods=['GET', 'POST'])
@estonia.route("/ee", methods=["GET", "POST"])
def searchEstonia():
    form = SearchForm()
    if request.method == "POST":
        if form.title.data == "":
            title = "all"
        else:
            title = form.title.data.lower().strip()
        if form.location.data == "":
            location = "everywhere"
        else:
            location = form.location.data.lower().strip()
        return redirect(url_for('estonia.resultEstonia', title=title, location=location, page=1, lang="ee"))
    elif request.method == "GET":
        return render_template("searcher_estonia.html", form=form, lang="ee")


@estonia.route('/ee/<string:title>-jobs-in-<string:location>')
@estonia.route('/ee/<int:page>/<string:title>-jobs-in-<string:location>')
def resultEstonia(title, location, page=1):
    form = SearchForm()
    job_obj = JobEstonia()
    job_list = job_obj.get_job(title, location).paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsEstonia.html", jobs=job_list, title=title.title(), location=location.title(), form=form, lang="ee")

@estonia.route("/about")
def about():
    return render_template("about.html")
