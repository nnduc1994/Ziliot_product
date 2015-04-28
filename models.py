from sqlalchemy import or_

from share import db

# Finland Database
class Job(db.Model):
    __table__ = db.Model.metadata.tables['job_finland']

    def get_job(self, title, location):

        if title == "all":
            query = self.query.filter(Job.location.contains(location)).order_by(Job.sponsor)
            return query
        elif location == "everywhere":
            return self.query.filter(or_(Job.title.contains(title.lower()),
                                         Job.description.contains(title))).order_by(Job.sponsor)
        else:
            return self.query.filter(or_(Job.title.contains(title.lower()), Job.description.contains(title)),
                                     Job.location.contains(location)).order_by(Job.sponsor)


# Estonia Database
class JobEstonia(db.Model):
    __table__ = db.Model.metadata.tables['job_estonia']

    def get_job(self, title, location):

        if title == "all":
            query = self.query.filter(JobEstonia.location.contains(location)).order_by(JobEstonia.sponsor)
            return query
        elif location == "everywhere":
            return self.query.filter(or_(JobEstonia.title.contains(title.lower()),
                                         JobEstonia.description.contains(title))).order_by(JobEstonia.sponsor)
        else:
            return self.query.filter(or_(JobEstonia.title.contains(title.lower()), JobEstonia.description.contains(title)),
                                     JobEstonia.location.contains(location)).order_by(JobEstonia.sponsor)