from ..forms import CreateWorkForm
from ..models import Job
from ..share import db, mail
from flask import render_template, request, Blueprint, flash
from flask_mail import Message

company = Blueprint('company', __name__)


@company.route("/create", methods=['GET', 'POST'])
def create_job():
    form = CreateWorkForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template("create_job.html", form=form)
        else:
            new_job = Job()
            new_job.title = form.title.data.lower() + "/ %s" % form.company_name.data
            new_job.link = form.link.data
            new_job.location = form.location.data.lower()
            new_job.description = form.description.data
            new_job.source = "company"
            new_job.sponsor = 1
            new_job.company_name = form.company_name.data
            new_job.expire_day = form.expire_day.data

            db.session.add(new_job)
            db.session.commit()

            msg = Message("New Job have been created", sender="ziliot.info@gmail.com", recipients=["info@ziliot.com"])
            msg.body = """
                New Job have been created by
                %s Company
                title : %s
                location : %s
                description : %s
            """ % (new_job.company_name, new_job.title, new_job.location, new_job.description)
            mail.send(msg)

            flash("Create Job Success")
            return render_template("create_job.html", form=form)

    if request.method == "GET":
        return render_template("create_job.html", form=form)