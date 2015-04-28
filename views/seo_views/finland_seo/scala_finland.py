from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

scala = Blueprint('scala', __name__)
job_obj = Job()



####################################################################


@scala.route('/scala_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "scala" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def scala_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="espoo")

@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def scala_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="tampere")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def scala_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="vantaa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def scala_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="turku")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def scala_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="oulu")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def scala_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="lahti")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def scala_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kuopio")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def scala_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="jyvvaskyla")

@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def scala_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="pori")

@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def scala_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="lappeenranta")	
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def scala_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="vaasa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def scala_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kotka")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def scala_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="joensuu")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def scala_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="hameenlinna")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def scala_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="porvoo")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def scala_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="mikkeli")

@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def scala_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="hyvinkaa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def scala_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="nurmijarvi")

@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def scala_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="jarvenpaa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def scala_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="rauma")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def scala_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="lohja")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def scala_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="karleby")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def scala_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kajaani")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def scala_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="rovaniemi")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def scala_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="tuusula")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def scala_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kirkkonummi")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def scala_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="seinajoki")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def scala_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kerava")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def scala_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kouvola")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def scala_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="imatra")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def scala_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="nokia")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def scala_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="savonlinna")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def scala_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="riihimaki")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def scala_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="vihti")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def scala_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="salo")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def scala_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kangasala")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def scala_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="raisio")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def scala_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="karhula")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def scala_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kemi")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def scala_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="iisalmi")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def scala_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="varkaus")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def scala_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="raahe")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def scala_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="ylojarvi")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def scala_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="hamina")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def scala_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kaarina")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def scala_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="tornio")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def scala_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="heinola")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def scala_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="hollola")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def scala_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="valkeakoski")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def scala_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="siilinjarvi")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def scala_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kuusankoski")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def scala_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="sibbo")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def scala_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="jakostad")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def scala_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="lempaala")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def scala_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="mantsala")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def scala_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="forssa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def scala_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kuusamo")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def scala_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="haukipudas")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def scala_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="korsholm")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def scala_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="laukaa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def scala_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="anjala")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def scala_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="uusikaupunki")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def scala_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="janakkala")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def scala_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="pirkkala")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def scala_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def scala_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="jamsa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def scala_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="jamsa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def scala_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="vammala")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def scala_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="nastola")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def scala_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="orimattila")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def scala_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kauhajoki")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def scala_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="ekenas")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def scala_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kempele")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def scala_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="lapua")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def scala_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="lieksa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def scala_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="naantali")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def scala_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="aanekoski")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def scala_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="ylivieska")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def scala_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kontiolahti")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def scala_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kankaanpaa")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def scala_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="ulvila")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def scala_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="pieksamaki")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def scala_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kiiminki")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def scala_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="pargas")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def scala_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="nurmo")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def scala_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="ilmajoki")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def scala_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="liperi")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def scala_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="keuruu")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def scala_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="leppavirta")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def scala_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kurikka")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def scala_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="nivala")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def scala_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="joutseno")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def scala_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="pedersore")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def scala_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="sotkamo")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def scala_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="kuhmo")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def scala_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="paimio")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def scala_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="saarijarvi")
	
@scala.route('/scala-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def scala_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("scala ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@scala.route('/scala-software-developer-jobs-espoo')
def scala_software_developer2(page=1):

    job_list = job_obj.get_job("scala software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="espoo")

@scala.route('/scala-software-developer-jobs-tampere')
def scala_software_developer3(page=1):

    job_list = job_obj.get_job("scala software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="tampere")
	
@scala.route('/scala-software-developer-jobs-vantaa')
def scala_software_developer4(page=1):

    job_list = job_obj.get_job("scala software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="vantaa")
	
@scala.route('/scala-software-developer-jobs-turku')
def scala_software_developer5(page=1):

    job_list = job_obj.get_job("scala software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="turku")
	
@scala.route('/scala-software-developer-jobs-oulu')
def scala_software_developer6(page=1):

    job_list = job_obj.get_job("scala software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="oulu")
	
@scala.route('/scala-software-developer-jobs-lahti')
def scala_software_developer7(page=1):

    job_list = job_obj.get_job("scala software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="lahti")
	
@scala.route('/scala-software-developer-jobs-kuopio')
def scala_software_developer8(page=1):

    job_list = job_obj.get_job("scala software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kuopio")
	
@scala.route('/scala-software-developer-jobs-jyvvaskyla')
def scala_software_developer9(page=1):

    job_list = job_obj.get_job("scala software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="jyvvaskyla")

@scala.route('/scala-software-developer-jobs-pori')
def scala_software_developer10(page=1):

    job_list = job_obj.get_job("scala software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="pori")

@scala.route('/scala-software-developer-jobs-lappeenranta')
def scala_software_developer11(page=1):

    job_list = job_obj.get_job("scala software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="lappeenranta")	
	
@scala.route('/scala-software-developer-jobs-vaasa')
def scala_software_developer12(page=1):

    job_list = job_obj.get_job("scala software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="vaasa")
	
@scala.route('/scala-software-developer-jobs-kotka')
def scala_software_developer13(page=1):

    job_list = job_obj.get_job("scala software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kotka")
	
@scala.route('/scala-software-developer-jobs-joensuu')
def scala_software_developer14(page=1):

    job_list = job_obj.get_job("scala software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="joensuu")
	
@scala.route('/scala-software-developer-jobs-hameenlinna')
def scala_software_developer15(page=1):

    job_list = job_obj.get_job("scala software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="hameenlinna")
	
@scala.route('/scala-software-developer-jobs-porvoo')
def scala_software_developer16(page=1):

    job_list = job_obj.get_job("scala software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="porvoo")
	
@scala.route('/scala-software-developer-jobs-mikkeli')
def scala_software_developer17(page=1):

    job_list = job_obj.get_job("scala software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="mikkeli")

@scala.route('/scala-software-developer-jobs-hyvinkaa')
def scala_software_developer18(page=1):

    job_list = job_obj.get_job("scala software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="hyvinkaa")
	
@scala.route('/scala-software-developer-jobs-nurmijarvi')
def scala_software_developer19(page=1):

    job_list = job_obj.get_job("scala software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="nurmijarvi")

@scala.route('/scala-software-developer-jobs-jarvenpaa')
def scala_software_developer20(page=1):

    job_list = job_obj.get_job("scala software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="jarvenpaa")
	
@scala.route('/scala-software-developer-jobs-rauma')
def scala_software_developer21(page=1):

    job_list = job_obj.get_job("scala software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="rauma")
	
@scala.route('/scala-software-developer-jobs-lohja')
def scala_software_developer22(page=1):

    job_list = job_obj.get_job("scala software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="lohja")
	
@scala.route('/scala-software-developer-jobs-karleby')
def scala_software_developer23(page=1):

    job_list = job_obj.get_job("scala software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="karleby")
	
@scala.route('/scala-software-developer-jobs-kajaani')
def scala_software_developer24(page=1):

    job_list = job_obj.get_job("scala software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kajaani")
	
@scala.route('/scala-software-developer-jobs-rovaniemi')
def scala_software_developer25(page=1):

    job_list = job_obj.get_job("scala software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="rovaniemi")
	
@scala.route('/scala-software-developer-jobs-tuusula')
def scala_software_developer26(page=1):

    job_list = job_obj.get_job("scala software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="tuusula")
	
@scala.route('/scala-software-developer-jobs-kirkkonummi')
def scala_software_developer27(page=1):

    job_list = job_obj.get_job("scala software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kirkkonummi")
	
@scala.route('/scala-software-developer-jobs-seinajoki')
def scala_software_developer28(page=1):

    job_list = job_obj.get_job("scala software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="seinajoki")
	
@scala.route('/scala-software-developer-jobs-kerava')
def scala_software_developer29(page=1):

    job_list = job_obj.get_job("scala software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kerava")
	
@scala.route('/scala-software-developer-jobs-kouvola')
def scala_software_developer30(page=1):

    job_list = job_obj.get_job("scala software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kouvola")
	
@scala.route('/scala-software-developer-jobs-imatra')
def scala_software_developer31(page=1):

    job_list = job_obj.get_job("scala software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="imatra")
	
@scala.route('/scala-software-developer-jobs-nokia')
def scala_software_developer32_1(page=1):

    job_list = job_obj.get_job("scala software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="nokia")
	
@scala.route('/scala-software-developer-jobs-savonlinna')
def scala_software_developer32(page=1):

    job_list = job_obj.get_job("scala software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="savonlinna")
	
@scala.route('/scala-software-developer-jobs-riihimaki')
def scala_software_developer33(page=1):

    job_list = job_obj.get_job("scala software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="riihimaki")
	
@scala.route('/scala-software-developer-jobs-vihti')
def scala_software_developer34(page=1):

    job_list = job_obj.get_job("scala software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="vihti")
	
@scala.route('/scala-software-developer-jobs-salo')
def scala_software_developer35(page=1):

    job_list = job_obj.get_job("scala software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="salo")
	
@scala.route('/scala-software-developer-jobs-kangasala')
def scala_software_developer36(page=1):

    job_list = job_obj.get_job("scala software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kangasala")
	
@scala.route('/scala-software-developer-jobs-raisio')
def scala_software_developer37_1(page=1):

    job_list = job_obj.get_job("scala software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="raisio")
	
@scala.route('/scala-software-developer-jobs-karhula')
def scala_software_developer37(page=1):

    job_list = job_obj.get_job("scala software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="karhula")
	
@scala.route('/scala-software-developer-jobs-kemi')
def scala_software_developer38(page=1):

    job_list = job_obj.get_job("scala software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kemi")
	
@scala.route('/scala-software-developer-jobs-iisalmi')
def scala_software_developer39(page=1):

    job_list = job_obj.get_job("scala software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="iisalmi")
	
@scala.route('/scala-software-developer-jobs-varkaus')
def scala_software_developer40(page=1):

    job_list = job_obj.get_job("scala software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="varkaus")
	
@scala.route('/scala-software-developer-jobs-raahe')
def scala_software_developer41(page=1):

    job_list = job_obj.get_job("scala software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="raahe")
	
@scala.route('/scala-software-developer-jobs-ylojarvi')
def scala_software_developer42_1(page=1):

    job_list = job_obj.get_job("scala software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="ylojarvi")
	
@scala.route('/scala-software-developer-jobs-hamina')
def scala_software_developer42(page=1):

    job_list = job_obj.get_job("scala software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="hamina")
	
@scala.route('/scala-software-developer-jobs-kaarina')
def scala_software_developer43(page=1):

    job_list = job_obj.get_job("scala software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kaarina")
	
@scala.route('/scala-software-developer-jobs-tornio')
def scala_software_developer44(page=1):

    job_list = job_obj.get_job("scala software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="tornio")
	
@scala.route('/scala-software-developer-jobs-heinola')
def scala_software_developer45(page=1):

    job_list = job_obj.get_job("scala software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="heinola")
	
@scala.route('/scala-software-developer-jobs-hollola')
def scala_software_developer46(page=1):

    job_list = job_obj.get_job("scala software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="hollola")
	
@scala.route('/scala-software-developer-jobs-valkeakoski')
def scala_software_developer47(page=1):

    job_list = job_obj.get_job("scala software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="valkeakoski")
	
@scala.route('/scala-software-developer-jobs-siilinjarvi')
def scala_software_developer48(page=1):

    job_list = job_obj.get_job("scala software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="siilinjarvi")
	
@scala.route('/scala-software-developer-jobs-kuusankoski')
def scala_software_developer49(page=1):

    job_list = job_obj.get_job("scala software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kuusankoski")
	
@scala.route('/scala-software-developer-jobs-sibbo')
def scala_software_developer50(page=1):

    job_list = job_obj.get_job("scala software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="sibbo")
	
@scala.route('/scala-software-developer-jobs-jakostad')
def scala_software_developer51(page=1):

    job_list = job_obj.get_job("scala software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="jakostad")
	
@scala.route('/scala-software-developer-jobs-lempaala')
def scala_software_developer52(page=1):

    job_list = job_obj.get_job("scala software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="lempaala")
	
@scala.route('/scala-software-developer-jobs-mantsala')
def scala_software_developer52_1(page=1):

    job_list = job_obj.get_job("scala software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="mantsala")
	
@scala.route('/scala-software-developer-jobs-forssa')
def scala_software_developer53(page=1):

    job_list = job_obj.get_job("scala software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="forssa")
	
@scala.route('/scala-software-developer-jobs-kuusamo')
def scala_software_developer54(page=1):

    job_list = job_obj.get_job("scala software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kuusamo")
	
@scala.route('/scala-software-developer-jobs-haukipudas')
def scala_software_developer55(page=1):

    job_list = job_obj.get_job("scala software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="haukipudas")
	
@scala.route('/scala-software-developer-jobs-korsholm')
def scala_software_developer56(page=1):

    job_list = job_obj.get_job("scala software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="korsholm")
	
@scala.route('/scala-software-developer-jobs-laukaa')
def scala_software_developer57(page=1):

    job_list = job_obj.get_job("scala software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="laukaa")
	
@scala.route('/scala-software-developer-jobs-anjala')
def scala_software_developer58(page=1):

    job_list = job_obj.get_job("scala software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="anjala")
	
@scala.route('/scala-software-developer-jobs-uusikaupunki')
def scala_software_developer59(page=1):

    job_list = job_obj.get_job("scala software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="uusikaupunki")
	
@scala.route('/scala-software-developer-jobs-janakkala')
def scala_software_developer60(page=1):

    job_list = job_obj.get_job("scala software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="janakkala")
	
@scala.route('/scala-software-developer-jobs-pirkkala')
def scala_software_developer61(page=1):

    job_list = job_obj.get_job("scala software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="pirkkala")
	
@scala.route('/scala-software-developer-jobs-lansi-turunmaa')
def scala_software_developer62(page=1):

    job_list = job_obj.get_job("scala software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="lansi-turunmaa")
	
@scala.route('/scala-software-developer-jobs-jamsa')
def scala_software_developer63(page=1):

    job_list = job_obj.get_job("scala software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="jamsa")
	
@scala.route('/scala-software-developer-jobs-jamsa')
def scala_software_developer64(page=1):

    job_list = job_obj.get_job("scala software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="jamsa")
	
@scala.route('/scala-software-developer-jobs-vammala')
def scala_software_developer65(page=1):

    job_list = job_obj.get_job("scala software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="vammala")
	
@scala.route('/scala-software-developer-jobs-nastola')
def scala_software_developer66(page=1):

    job_list = job_obj.get_job("scala software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="nastola")
	
@scala.route('/scala-software-developer-jobs-orimattila')
def scala_software_developer67(page=1):

    job_list = job_obj.get_job("scala software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="orimattila")
	
@scala.route('/scala-software-developer-jobs-kauhajoki')
def scala_software_developer68(page=1):

    job_list = job_obj.get_job("scala software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kauhajoki")
	
@scala.route('/scala-software-developer-jobs-ekenas')
def scala_software_developer69(page=1):

    job_list = job_obj.get_job("scala software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="ekenas")
	
@scala.route('/scala-software-developer-jobs-kempele')
def scala_software_developer70(page=1):

    job_list = job_obj.get_job("scala software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kempele")
	
@scala.route('/scala-software-developer-jobs-lapua')
def scala_software_developer71(page=1):

    job_list = job_obj.get_job("scala software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="lapua")
	
@scala.route('/scala-software-developer-jobs-lieksa')
def scala_software_developer72(page=1):

    job_list = job_obj.get_job("scala software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="lieksa")
	
@scala.route('/scala-software-developer-jobs-naantali')
def scala_software_developer73(page=1):

    job_list = job_obj.get_job("scala software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="naantali")
	
@scala.route('/scala-software-developer-jobs-aanekoski')
def scala_software_developer74(page=1):

    job_list = job_obj.get_job("scala software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="aanekoski")
	
@scala.route('/scala-software-developer-jobs-ylivieska')
def scala_software_developer75(page=1):

    job_list = job_obj.get_job("scala software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="ylivieska")
	
@scala.route('/scala-software-developer-jobs-kontiolahti')
def scala_software_developer76(page=1):

    job_list = job_obj.get_job("scala software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kontiolahti")
	
@scala.route('/scala-software-developer-jobs-kankaanpaa')
def scala_software_developer77(page=1):

    job_list = job_obj.get_job("scala software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kankaanpaa")
	
@scala.route('/scala-software-developer-jobs-ulvila')
def scala_software_developer78(page=1):

    job_list = job_obj.get_job("scala software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="ulvila")
	
@scala.route('/scala-software-developer-jobs-pieksamaki')
def scala_software_developer79(page=1):

    job_list = job_obj.get_job("scala software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="pieksamaki")
	
@scala.route('/scala-software-developer-jobs-kiiminki')
def scala_software_developer80(page=1):

    job_list = job_obj.get_job("scala software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kiiminki")
	
@scala.route('/scala-software-developer-jobs-pargas')
def scala_software_developer81(page=1):

    job_list = job_obj.get_job("scala software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="pargas")
	
@scala.route('/scala-software-developer-jobs-nurmo')
def scala_software_developer82(page=1):

    job_list = job_obj.get_job("scala software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="nurmo")
	
@scala.route('/scala-software-developer-jobs-ilmajoki')
def scala_software_developer83(page=1):

    job_list = job_obj.get_job("scala software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="ilmajoki")
	
@scala.route('/scala-software-developer-jobs-liperi')
def scala_software_developer84(page=1):

    job_list = job_obj.get_job("scala software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="liperi")
	
@scala.route('/scala-software-developer-jobs-keuruu')
def scala_software_developer85(page=1):

    job_list = job_obj.get_job("scala software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="keuruu")
	
@scala.route('/scala-software-developer-jobs-leppavirta')
def scala_software_developer86(page=1):

    job_list = job_obj.get_job("scala software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="leppavirta")
	
@scala.route('/scala-software-developer-jobs-kurikka')
def scala_software_developer87(page=1):

    job_list = job_obj.get_job("scala software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kurikka")
	
@scala.route('/scala-software-developer-jobs-nivala')
def scala_software_developer88(page=1):

    job_list = job_obj.get_job("scala software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="nivala")
	
@scala.route('/scala-software-developer-jobs-joutseno')
def scala_software_developer89(page=1):

    job_list = job_obj.get_job("scala software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="joutseno")
	
@scala.route('/scala-software-developer-jobs-pedersore')
def scala_software_developer90(page=1):

    job_list = job_obj.get_job("scala software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="pedersore")
	
@scala.route('/scala-software-developer-jobs-sotkamo')
def scala_software_developer91(page=1):

    job_list = job_obj.get_job("scala software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="sotkamo")
	
@scala.route('/scala-software-developer-jobs-kuhmo')
def scala_software_developer92(page=1):

    job_list = job_obj.get_job("scala software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="kuhmo")
	
@scala.route('/scala-software-developer-jobs-paimio')
def scala_software_developer93(page=1):

    job_list = job_obj.get_job("scala software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="paimio")
	
@scala.route('/scala-software-developer-jobs-saarijarvi')
def scala_software_developer94(page=1):

    job_list = job_obj.get_job("scala software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="saarijarvi")
	
@scala.route('/scala-software-developer-jobs-helsinki')
def scala_software_developer95(page=1):

    job_list = job_obj.get_job("scala software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="scala software developer", location="helsinki")


####################################################################

