from ..forms import SearchForm
from ..models import Job
from flask import render_template, request, redirect, url_for, Blueprint

JOB_PER_PAGE = 7

home = Blueprint('home', __name__)

@home.route("/en", methods=['GET', 'POST'])
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
        return redirect(url_for('home.result', title=title, location=location, page=1))
    elif request.method == "GET":
        return render_template("searcher.html", form=form)

@home.route('/en/<string:title>-jobs-in-<string:location>')
@home.route('/en/<int:page>/<string:title>-jobs-in-<string:location>')
def result(title, location, page=1):
    form = SearchForm()
    job_obj = Job()
    job_list = job_obj.get_job(title, location).paginate(page, JOB_PER_PAGE, False)
    return render_template("results.html", jobs=job_list, title=title.title(), location=location.title(), form=form)

# Finnish pages
@home.route('/', methods=['GET', 'POST'])
@home.route("/fi", methods=["GET", "POST"])
def searchFinnish():
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
        return redirect(url_for('home.resultFinnish', title=title, location=location, page=1))
    elif request.method == "GET":
        return render_template("searcher_finnish.html", form=form)


@home.route('/fi/<string:title>-jobs-in-<string:location>')
@home.route('/fi/<int:page>/<string:title>-jobs-in-<string:location>')
def resultFinnish(title, location, page=1):
    form = SearchForm()
    job_obj = Job()
    job_list = job_obj.get_job(title, location).paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsFinnish.html", jobs=job_list, title=title.title(), location=location.title(), form=form)

@home.route("/about")
def about():
    return render_template("about.html")
@home.route("/sitemap/page1")
def htmlSiteMap():
    return render_template("/sitemaps/sql_sitemap.html")
@home.route("/sitemap/page2")
def htmlSiteMap2():
    return render_template("/sitemaps/page2_sitemap.html")
