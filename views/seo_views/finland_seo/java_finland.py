from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PAGE = 7

java = Blueprint('java', __name__)
job_obj = Job()



####################################################################


@java.route('/java_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "java" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def java_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="espoo")

@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def java_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="tampere")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def java_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="vantaa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def java_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="turku")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def java_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="oulu")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def java_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lahti")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def java_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kuopio")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def java_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="jyvvaskyla")

@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def java_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="pori")

@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def java_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lappeenranta")	
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def java_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="vaasa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def java_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kotka")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def java_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="joensuu")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def java_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="hameenlinna")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def java_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="porvoo")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def java_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="mikkeli")

@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def java_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="hyvinkaa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def java_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="nurmijarvi")

@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def java_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="jarvenpaa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def java_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="rauma")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def java_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lohja")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def java_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="karleby")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def java_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kajaani")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def java_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="rovaniemi")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def java_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="tuusula")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def java_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kirkkonummi")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def java_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="seinajoki")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def java_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kerava")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def java_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kouvola")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def java_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="imatra")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def java_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="nokia")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def java_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="savonlinna")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def java_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="riihimaki")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def java_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="vihti")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def java_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="salo")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def java_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kangasala")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def java_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="raisio")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def java_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="karhula")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def java_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kemi")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def java_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="iisalmi")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def java_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="varkaus")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def java_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="raahe")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def java_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="ylojarvi")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def java_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="hamina")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def java_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kaarina")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def java_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="tornio")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def java_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="heinola")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def java_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="hollola")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def java_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="valkeakoski")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def java_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="siilinjarvi")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def java_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kuusankoski")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def java_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="sibbo")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def java_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="jakostad")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def java_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lempaala")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def java_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="mantsala")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def java_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="forssa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def java_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kuusamo")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def java_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="haukipudas")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def java_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="korsholm")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def java_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="laukaa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def java_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="anjala")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def java_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="uusikaupunki")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def java_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="janakkala")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def java_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="pirkkala")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def java_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def java_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="jamsa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def java_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="jamsa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def java_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="vammala")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def java_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="nastola")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def java_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="orimattila")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def java_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kauhajoki")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def java_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="ekenas")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def java_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kempele")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def java_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lapua")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def java_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lieksa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def java_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="naantali")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def java_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="aanekoski")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def java_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="ylivieska")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def java_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kontiolahti")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def java_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kankaanpaa")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def java_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="ulvila")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def java_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="pieksamaki")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def java_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kiiminki")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def java_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="pargas")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def java_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="nurmo")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def java_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="ilmajoki")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def java_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="liperi")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def java_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="keuruu")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def java_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="leppavirta")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def java_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kurikka")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def java_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="nivala")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def java_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="joutseno")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def java_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="pedersore")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def java_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="sotkamo")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def java_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kuhmo")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def java_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="paimio")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def java_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="saarijarvi")
	
@java.route('/java-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def java_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="helsinki")


	 
##############################################
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-espoo')
def java_ohjelmistosuunnittelija_tyopaikat2(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="espoo")

@java.route('/java-ohjelmistosuunnittelija-tyopaikat-tampere')
def java_ohjelmistosuunnittelija_tyopaikat3(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="tampere")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-vantaa')
def java_ohjelmistosuunnittelija_tyopaikat4(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="vantaa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-turku')
def java_ohjelmistosuunnittelija_tyopaikat5(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="turku")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-oulu')
def java_ohjelmistosuunnittelija_tyopaikat6(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="oulu")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-lahti')
def java_ohjelmistosuunnittelija_tyopaikat7(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lahti")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kuopio')
def java_ohjelmistosuunnittelija_tyopaikat8(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kuopio")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-jyvvaskyla')
def java_ohjelmistosuunnittelija_tyopaikat9(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="jyvvaskyla")

@java.route('/java-ohjelmistosuunnittelija-tyopaikat-pori')
def java_ohjelmistosuunnittelija_tyopaikat10(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="pori")

@java.route('/java-ohjelmistosuunnittelija-tyopaikat-lappeenranta')
def java_ohjelmistosuunnittelija_tyopaikat11(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lappeenranta")	
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-vaasa')
def java_ohjelmistosuunnittelija_tyopaikat12(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="vaasa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kotka')
def java_ohjelmistosuunnittelija_tyopaikat13(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kotka")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-joensuu')
def java_ohjelmistosuunnittelija_tyopaikat14(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="joensuu")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-hameenlinna')
def java_ohjelmistosuunnittelija_tyopaikat15(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="hameenlinna")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-porvoo')
def java_ohjelmistosuunnittelija_tyopaikat16(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="porvoo")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-mikkeli')
def java_ohjelmistosuunnittelija_tyopaikat17(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="mikkeli")

@java.route('/java-ohjelmistosuunnittelija-tyopaikat-hyvinkaa')
def java_ohjelmistosuunnittelija_tyopaikat18(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="hyvinkaa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-nurmijarvi')
def java_ohjelmistosuunnittelija_tyopaikat19(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="nurmijarvi")

@java.route('/java-ohjelmistosuunnittelija-tyopaikat-jarvenpaa')
def java_ohjelmistosuunnittelija_tyopaikat20(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="jarvenpaa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-rauma')
def java_ohjelmistosuunnittelija_tyopaikat21(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="rauma")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-lohja')
def java_ohjelmistosuunnittelija_tyopaikat22(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lohja")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-karleby')
def java_ohjelmistosuunnittelija_tyopaikat23(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="karleby")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kajaani')
def java_ohjelmistosuunnittelija_tyopaikat24(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kajaani")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-rovaniemi')
def java_ohjelmistosuunnittelija_tyopaikat25(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="rovaniemi")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-tuusula')
def java_ohjelmistosuunnittelija_tyopaikat26(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="tuusula")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kirkkonummi')
def java_ohjelmistosuunnittelija_tyopaikat27(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kirkkonummi")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-seinajoki')
def java_ohjelmistosuunnittelija_tyopaikat28(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="seinajoki")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kerava')
def java_ohjelmistosuunnittelija_tyopaikat29(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kerava")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kouvola')
def java_ohjelmistosuunnittelija_tyopaikat30(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kouvola")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-imatra')
def java_ohjelmistosuunnittelija_tyopaikat31(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="imatra")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-nokia')
def java_ohjelmistosuunnittelija_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="nokia")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-savonlinna')
def java_ohjelmistosuunnittelija_tyopaikat32(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="savonlinna")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-riihimaki')
def java_ohjelmistosuunnittelija_tyopaikat33(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="riihimaki")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-vihti')
def java_ohjelmistosuunnittelija_tyopaikat34(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="vihti")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-salo')
def java_ohjelmistosuunnittelija_tyopaikat35(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="salo")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kangasala')
def java_ohjelmistosuunnittelija_tyopaikat36(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kangasala")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-raisio')
def java_ohjelmistosuunnittelija_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="raisio")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-karhula')
def java_ohjelmistosuunnittelija_tyopaikat37(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="karhula")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kemi')
def java_ohjelmistosuunnittelija_tyopaikat38(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kemi")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-iisalmi')
def java_ohjelmistosuunnittelija_tyopaikat39(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="iisalmi")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-varkaus')
def java_ohjelmistosuunnittelija_tyopaikat40(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="varkaus")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-raahe')
def java_ohjelmistosuunnittelija_tyopaikat41(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="raahe")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-ylojarvi')
def java_ohjelmistosuunnittelija_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="ylojarvi")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-hamina')
def java_ohjelmistosuunnittelija_tyopaikat42(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="hamina")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kaarina')
def java_ohjelmistosuunnittelija_tyopaikat43(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kaarina")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-tornio')
def java_ohjelmistosuunnittelija_tyopaikat44(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="tornio")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-heinola')
def java_ohjelmistosuunnittelija_tyopaikat45(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="heinola")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-hollola')
def java_ohjelmistosuunnittelija_tyopaikat46(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="hollola")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-valkeakoski')
def java_ohjelmistosuunnittelija_tyopaikat47(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="valkeakoski")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-siilinjarvi')
def java_ohjelmistosuunnittelija_tyopaikat48(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="siilinjarvi")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kuusankoski')
def java_ohjelmistosuunnittelija_tyopaikat49(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kuusankoski")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-sibbo')
def java_ohjelmistosuunnittelija_tyopaikat50(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="sibbo")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-jakostad')
def java_ohjelmistosuunnittelija_tyopaikat51(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="jakostad")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-lempaala')
def java_ohjelmistosuunnittelija_tyopaikat52(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lempaala")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-mantsala')
def java_ohjelmistosuunnittelija_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="mantsala")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-forssa')
def java_ohjelmistosuunnittelija_tyopaikat53(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="forssa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kuusamo')
def java_ohjelmistosuunnittelija_tyopaikat54(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kuusamo")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-haukipudas')
def java_ohjelmistosuunnittelija_tyopaikat55(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="haukipudas")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-korsholm')
def java_ohjelmistosuunnittelija_tyopaikat56(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="korsholm")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-laukaa')
def java_ohjelmistosuunnittelija_tyopaikat57(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="laukaa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-anjala')
def java_ohjelmistosuunnittelija_tyopaikat58(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="anjala")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-uusikaupunki')
def java_ohjelmistosuunnittelija_tyopaikat59(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="uusikaupunki")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-janakkala')
def java_ohjelmistosuunnittelija_tyopaikat60(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="janakkala")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-pirkkala')
def java_ohjelmistosuunnittelija_tyopaikat61(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="pirkkala")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-lansi-turunmaa')
def java_ohjelmistosuunnittelija_tyopaikat62(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-jamsa')
def java_ohjelmistosuunnittelija_tyopaikat63(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="jamsa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-jamsa')
def java_ohjelmistosuunnittelija_tyopaikat64(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="jamsa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-vammala')
def java_ohjelmistosuunnittelija_tyopaikat65(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="vammala")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-nastola')
def java_ohjelmistosuunnittelija_tyopaikat66(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="nastola")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-orimattila')
def java_ohjelmistosuunnittelija_tyopaikat67(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="orimattila")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kauhajoki')
def java_ohjelmistosuunnittelija_tyopaikat68(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kauhajoki")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-ekenas')
def java_ohjelmistosuunnittelija_tyopaikat69(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="ekenas")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kempele')
def java_ohjelmistosuunnittelija_tyopaikat70(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kempele")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-lapua')
def java_ohjelmistosuunnittelija_tyopaikat71(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lapua")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-lieksa')
def java_ohjelmistosuunnittelija_tyopaikat72(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="lieksa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-naantali')
def java_ohjelmistosuunnittelija_tyopaikat73(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="naantali")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-aanekoski')
def java_ohjelmistosuunnittelija_tyopaikat74(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="aanekoski")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-ylivieska')
def java_ohjelmistosuunnittelija_tyopaikat75(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="ylivieska")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kontiolahti')
def java_ohjelmistosuunnittelija_tyopaikat76(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kontiolahti")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kankaanpaa')
def java_ohjelmistosuunnittelija_tyopaikat77(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kankaanpaa")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-ulvila')
def java_ohjelmistosuunnittelija_tyopaikat78(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="ulvila")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-pieksamaki')
def java_ohjelmistosuunnittelija_tyopaikat79(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="pieksamaki")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kiiminki')
def java_ohjelmistosuunnittelija_tyopaikat80(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kiiminki")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-pargas')
def java_ohjelmistosuunnittelija_tyopaikat81(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="pargas")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-nurmo')
def java_ohjelmistosuunnittelija_tyopaikat82(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="nurmo")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-ilmajoki')
def java_ohjelmistosuunnittelija_tyopaikat83(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="ilmajoki")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-liperi')
def java_ohjelmistosuunnittelija_tyopaikat84(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="liperi")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-keuruu')
def java_ohjelmistosuunnittelija_tyopaikat85(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="keuruu")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-leppavirta')
def java_ohjelmistosuunnittelija_tyopaikat86(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="leppavirta")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kurikka')
def java_ohjelmistosuunnittelija_tyopaikat87(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kurikka")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-nivala')
def java_ohjelmistosuunnittelija_tyopaikat88(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="nivala")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-joutseno')
def java_ohjelmistosuunnittelija_tyopaikat89(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="joutseno")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-pedersore')
def java_ohjelmistosuunnittelija_tyopaikat90(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="pedersore")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-sotkamo')
def java_ohjelmistosuunnittelija_tyopaikat91(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="sotkamo")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-kuhmo')
def java_ohjelmistosuunnittelija_tyopaikat92(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="kuhmo")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-paimio')
def java_ohjelmistosuunnittelija_tyopaikat93(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="paimio")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-saarijarvi')
def java_ohjelmistosuunnittelija_tyopaikat94(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="saarijarvi")
	
@java.route('/java-ohjelmistosuunnittelija-tyopaikat-helsinki')
def java_ohjelmistosuunnittelija_tyopaikat95(page=1):

    job_list = job_obj.get_job("java ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java ohjelmistosuunnittelija", location="helsinki")


####################################################################

##############################################
@java.route('/java-software-developer-jobs-espoo')
def java_software_developer2(page=1):

    job_list = job_obj.get_job("java software developer", "espoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="espoo")

@java.route('/java-software-developer-jobs-tampere')
def java_software_developer3(page=1):

    job_list = job_obj.get_job("java software developer", "tampere").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="tampere")
	
@java.route('/java-software-developer-jobs-vantaa')
def java_software_developer4(page=1):

    job_list = job_obj.get_job("java software developer", "vantaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="vantaa")
	
@java.route('/java-software-developer-jobs-turku')
def java_software_developer5(page=1):

    job_list = job_obj.get_job("java software developer", "turku").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="turku")
	
@java.route('/java-software-developer-jobs-oulu')
def java_software_developer6(page=1):

    job_list = job_obj.get_job("java software developer", "oulu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="oulu")
	
@java.route('/java-software-developer-jobs-lahti')
def java_software_developer7(page=1):

    job_list = job_obj.get_job("java software developer", "lahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="lahti")
	
@java.route('/java-software-developer-jobs-kuopio')
def java_software_developer8(page=1):

    job_list = job_obj.get_job("java software developer", "kuopio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kuopio")
	
@java.route('/java-software-developer-jobs-jyvvaskyla')
def java_software_developer9(page=1):

    job_list = job_obj.get_job("java software developer", "jyvvaskyla").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="jyvvaskyla")

@java.route('/java-software-developer-jobs-pori')
def java_software_developer10(page=1):

    job_list = job_obj.get_job("java software developer", "pori").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="pori")

@java.route('/java-software-developer-jobs-lappeenranta')
def java_software_developer11(page=1):

    job_list = job_obj.get_job("java software developer", "lappeenranta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="lappeenranta")	
	
@java.route('/java-software-developer-jobs-vaasa')
def java_software_developer12(page=1):

    job_list = job_obj.get_job("java software developer", "vaasa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="vaasa")
	
@java.route('/java-software-developer-jobs-kotka')
def java_software_developer13(page=1):

    job_list = job_obj.get_job("java software developer", "kotka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kotka")
	
@java.route('/java-software-developer-jobs-joensuu')
def java_software_developer14(page=1):

    job_list = job_obj.get_job("java software developer", "joensuu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="joensuu")
	
@java.route('/java-software-developer-jobs-hameenlinna')
def java_software_developer15(page=1):

    job_list = job_obj.get_job("java software developer", "hameenlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="hameenlinna")
	
@java.route('/java-software-developer-jobs-porvoo')
def java_software_developer16(page=1):

    job_list = job_obj.get_job("java software developer", "porvoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="porvoo")
	
@java.route('/java-software-developer-jobs-mikkeli')
def java_software_developer17(page=1):

    job_list = job_obj.get_job("java software developer", "mikkeli").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="mikkeli")

@java.route('/java-software-developer-jobs-hyvinkaa')
def java_software_developer18(page=1):

    job_list = job_obj.get_job("java software developer", "hyvinkaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="hyvinkaa")
	
@java.route('/java-software-developer-jobs-nurmijarvi')
def java_software_developer19(page=1):

    job_list = job_obj.get_job("java software developer", "nurmijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="nurmijarvi")

@java.route('/java-software-developer-jobs-jarvenpaa')
def java_software_developer20(page=1):

    job_list = job_obj.get_job("java software developer", "jarvenpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="jarvenpaa")
	
@java.route('/java-software-developer-jobs-rauma')
def java_software_developer21(page=1):

    job_list = job_obj.get_job("java software developer", "rauma").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="rauma")
	
@java.route('/java-software-developer-jobs-lohja')
def java_software_developer22(page=1):

    job_list = job_obj.get_job("java software developer", "lohja").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="lohja")
	
@java.route('/java-software-developer-jobs-karleby')
def java_software_developer23(page=1):

    job_list = job_obj.get_job("java software developer", "karleby").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="karleby")
	
@java.route('/java-software-developer-jobs-kajaani')
def java_software_developer24(page=1):

    job_list = job_obj.get_job("java software developer", "kajaani").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kajaani")
	
@java.route('/java-software-developer-jobs-rovaniemi')
def java_software_developer25(page=1):

    job_list = job_obj.get_job("java software developer", "rovaniemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="rovaniemi")
	
@java.route('/java-software-developer-jobs-tuusula')
def java_software_developer26(page=1):

    job_list = job_obj.get_job("java software developer", "tuusula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="tuusula")
	
@java.route('/java-software-developer-jobs-kirkkonummi')
def java_software_developer27(page=1):

    job_list = job_obj.get_job("java software developer", "kirkkonummi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kirkkonummi")
	
@java.route('/java-software-developer-jobs-seinajoki')
def java_software_developer28(page=1):

    job_list = job_obj.get_job("java software developer", "seinajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="seinajoki")
	
@java.route('/java-software-developer-jobs-kerava')
def java_software_developer29(page=1):

    job_list = job_obj.get_job("java software developer", "kerava").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kerava")
	
@java.route('/java-software-developer-jobs-kouvola')
def java_software_developer30(page=1):

    job_list = job_obj.get_job("java software developer", "kouvola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kouvola")
	
@java.route('/java-software-developer-jobs-imatra')
def java_software_developer31(page=1):

    job_list = job_obj.get_job("java software developer", "imatra").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="imatra")
	
@java.route('/java-software-developer-jobs-nokia')
def java_software_developer32_1(page=1):

    job_list = job_obj.get_job("java software developer", "nokia").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="nokia")
	
@java.route('/java-software-developer-jobs-savonlinna')
def java_software_developer32(page=1):

    job_list = job_obj.get_job("java software developer", "savonlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="savonlinna")
	
@java.route('/java-software-developer-jobs-riihimaki')
def java_software_developer33(page=1):

    job_list = job_obj.get_job("java software developer", "riihimaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="riihimaki")
	
@java.route('/java-software-developer-jobs-vihti')
def java_software_developer34(page=1):

    job_list = job_obj.get_job("java software developer", "vihti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="vihti")
	
@java.route('/java-software-developer-jobs-salo')
def java_software_developer35(page=1):

    job_list = job_obj.get_job("java software developer", "salo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="salo")
	
@java.route('/java-software-developer-jobs-kangasala')
def java_software_developer36(page=1):

    job_list = job_obj.get_job("java software developer", "kangasala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kangasala")
	
@java.route('/java-software-developer-jobs-raisio')
def java_software_developer37_1(page=1):

    job_list = job_obj.get_job("java software developer", "raisio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="raisio")
	
@java.route('/java-software-developer-jobs-karhula')
def java_software_developer37(page=1):

    job_list = job_obj.get_job("java software developer", "karhula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="karhula")
	
@java.route('/java-software-developer-jobs-kemi')
def java_software_developer38(page=1):

    job_list = job_obj.get_job("java software developer", "kemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kemi")
	
@java.route('/java-software-developer-jobs-iisalmi')
def java_software_developer39(page=1):

    job_list = job_obj.get_job("java software developer", "iisalmi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="iisalmi")
	
@java.route('/java-software-developer-jobs-varkaus')
def java_software_developer40(page=1):

    job_list = job_obj.get_job("java software developer", "varkaus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="varkaus")
	
@java.route('/java-software-developer-jobs-raahe')
def java_software_developer41(page=1):

    job_list = job_obj.get_job("java software developer", "raahe").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="raahe")
	
@java.route('/java-software-developer-jobs-ylojarvi')
def java_software_developer42_1(page=1):

    job_list = job_obj.get_job("java software developer", "ylojarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="ylojarvi")
	
@java.route('/java-software-developer-jobs-hamina')
def java_software_developer42(page=1):

    job_list = job_obj.get_job("java software developer", "hamina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="hamina")
	
@java.route('/java-software-developer-jobs-kaarina')
def java_software_developer43(page=1):

    job_list = job_obj.get_job("java software developer", "kaarina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kaarina")
	
@java.route('/java-software-developer-jobs-tornio')
def java_software_developer44(page=1):

    job_list = job_obj.get_job("java software developer", "tornio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="tornio")
	
@java.route('/java-software-developer-jobs-heinola')
def java_software_developer45(page=1):

    job_list = job_obj.get_job("java software developer", "heinola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="heinola")
	
@java.route('/java-software-developer-jobs-hollola')
def java_software_developer46(page=1):

    job_list = job_obj.get_job("java software developer", "hollola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="hollola")
	
@java.route('/java-software-developer-jobs-valkeakoski')
def java_software_developer47(page=1):

    job_list = job_obj.get_job("java software developer", "valkeakoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="valkeakoski")
	
@java.route('/java-software-developer-jobs-siilinjarvi')
def java_software_developer48(page=1):

    job_list = job_obj.get_job("java software developer", "siilinjarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="siilinjarvi")
	
@java.route('/java-software-developer-jobs-kuusankoski')
def java_software_developer49(page=1):

    job_list = job_obj.get_job("java software developer", "kuusankoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kuusankoski")
	
@java.route('/java-software-developer-jobs-sibbo')
def java_software_developer50(page=1):

    job_list = job_obj.get_job("java software developer", "sibbo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="sibbo")
	
@java.route('/java-software-developer-jobs-jakostad')
def java_software_developer51(page=1):

    job_list = job_obj.get_job("java software developer", "jakostad").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="jakostad")
	
@java.route('/java-software-developer-jobs-lempaala')
def java_software_developer52(page=1):

    job_list = job_obj.get_job("java software developer", "lempaala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="lempaala")
	
@java.route('/java-software-developer-jobs-mantsala')
def java_software_developer52_1(page=1):

    job_list = job_obj.get_job("java software developer", "mantsala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="mantsala")
	
@java.route('/java-software-developer-jobs-forssa')
def java_software_developer53(page=1):

    job_list = job_obj.get_job("java software developer", "forssa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="forssa")
	
@java.route('/java-software-developer-jobs-kuusamo')
def java_software_developer54(page=1):

    job_list = job_obj.get_job("java software developer", "kuusamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kuusamo")
	
@java.route('/java-software-developer-jobs-haukipudas')
def java_software_developer55(page=1):

    job_list = job_obj.get_job("java software developer", "haukipudas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="haukipudas")
	
@java.route('/java-software-developer-jobs-korsholm')
def java_software_developer56(page=1):

    job_list = job_obj.get_job("java software developer", "korsholm").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="korsholm")
	
@java.route('/java-software-developer-jobs-laukaa')
def java_software_developer57(page=1):

    job_list = job_obj.get_job("java software developer", "laukaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="laukaa")
	
@java.route('/java-software-developer-jobs-anjala')
def java_software_developer58(page=1):

    job_list = job_obj.get_job("java software developer", "anjala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="anjala")
	
@java.route('/java-software-developer-jobs-uusikaupunki')
def java_software_developer59(page=1):

    job_list = job_obj.get_job("java software developer", "uusikaupunki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="uusikaupunki")
	
@java.route('/java-software-developer-jobs-janakkala')
def java_software_developer60(page=1):

    job_list = job_obj.get_job("java software developer", "janakkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="janakkala")
	
@java.route('/java-software-developer-jobs-pirkkala')
def java_software_developer61(page=1):

    job_list = job_obj.get_job("java software developer", "pirkkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="pirkkala")
	
@java.route('/java-software-developer-jobs-lansi-turunmaa')
def java_software_developer62(page=1):

    job_list = job_obj.get_job("java software developer", "lansi-turunmaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="lansi-turunmaa")
	
@java.route('/java-software-developer-jobs-jamsa')
def java_software_developer63(page=1):

    job_list = job_obj.get_job("java software developer", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="jamsa")
	
@java.route('/java-software-developer-jobs-jamsa')
def java_software_developer64(page=1):

    job_list = job_obj.get_job("java software developer", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="jamsa")
	
@java.route('/java-software-developer-jobs-vammala')
def java_software_developer65(page=1):

    job_list = job_obj.get_job("java software developer", "vammala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="vammala")
	
@java.route('/java-software-developer-jobs-nastola')
def java_software_developer66(page=1):

    job_list = job_obj.get_job("java software developer", "nastola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="nastola")
	
@java.route('/java-software-developer-jobs-orimattila')
def java_software_developer67(page=1):

    job_list = job_obj.get_job("java software developer", "orimattila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="orimattila")
	
@java.route('/java-software-developer-jobs-kauhajoki')
def java_software_developer68(page=1):

    job_list = job_obj.get_job("java software developer", "kauhajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kauhajoki")
	
@java.route('/java-software-developer-jobs-ekenas')
def java_software_developer69(page=1):

    job_list = job_obj.get_job("java software developer", "ekenas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="ekenas")
	
@java.route('/java-software-developer-jobs-kempele')
def java_software_developer70(page=1):

    job_list = job_obj.get_job("java software developer", "kempele").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kempele")
	
@java.route('/java-software-developer-jobs-lapua')
def java_software_developer71(page=1):

    job_list = job_obj.get_job("java software developer", "lapua").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="lapua")
	
@java.route('/java-software-developer-jobs-lieksa')
def java_software_developer72(page=1):

    job_list = job_obj.get_job("java software developer", "lieksa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="lieksa")
	
@java.route('/java-software-developer-jobs-naantali')
def java_software_developer73(page=1):

    job_list = job_obj.get_job("java software developer", "naantali").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="naantali")
	
@java.route('/java-software-developer-jobs-aanekoski')
def java_software_developer74(page=1):

    job_list = job_obj.get_job("java software developer", "aanekoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="aanekoski")
	
@java.route('/java-software-developer-jobs-ylivieska')
def java_software_developer75(page=1):

    job_list = job_obj.get_job("java software developer", "ylivieska").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="ylivieska")
	
@java.route('/java-software-developer-jobs-kontiolahti')
def java_software_developer76(page=1):

    job_list = job_obj.get_job("java software developer", "kontiolahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kontiolahti")
	
@java.route('/java-software-developer-jobs-kankaanpaa')
def java_software_developer77(page=1):

    job_list = job_obj.get_job("java software developer", "kankaanpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kankaanpaa")
	
@java.route('/java-software-developer-jobs-ulvila')
def java_software_developer78(page=1):

    job_list = job_obj.get_job("java software developer", "ulvila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="ulvila")
	
@java.route('/java-software-developer-jobs-pieksamaki')
def java_software_developer79(page=1):

    job_list = job_obj.get_job("java software developer", "pieksamaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="pieksamaki")
	
@java.route('/java-software-developer-jobs-kiiminki')
def java_software_developer80(page=1):

    job_list = job_obj.get_job("java software developer", "kiiminki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kiiminki")
	
@java.route('/java-software-developer-jobs-pargas')
def java_software_developer81(page=1):

    job_list = job_obj.get_job("java software developer", "pargas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="pargas")
	
@java.route('/java-software-developer-jobs-nurmo')
def java_software_developer82(page=1):

    job_list = job_obj.get_job("java software developer", "nurmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="nurmo")
	
@java.route('/java-software-developer-jobs-ilmajoki')
def java_software_developer83(page=1):

    job_list = job_obj.get_job("java software developer", "ilmajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="ilmajoki")
	
@java.route('/java-software-developer-jobs-liperi')
def java_software_developer84(page=1):

    job_list = job_obj.get_job("java software developer", "liperi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="liperi")
	
@java.route('/java-software-developer-jobs-keuruu')
def java_software_developer85(page=1):

    job_list = job_obj.get_job("java software developer", "keuruu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="keuruu")
	
@java.route('/java-software-developer-jobs-leppavirta')
def java_software_developer86(page=1):

    job_list = job_obj.get_job("java software developer", "leppavirta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="leppavirta")
	
@java.route('/java-software-developer-jobs-kurikka')
def java_software_developer87(page=1):

    job_list = job_obj.get_job("java software developer", "kurikka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kurikka")
	
@java.route('/java-software-developer-jobs-nivala')
def java_software_developer88(page=1):

    job_list = job_obj.get_job("java software developer", "nivala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="nivala")
	
@java.route('/java-software-developer-jobs-joutseno')
def java_software_developer89(page=1):

    job_list = job_obj.get_job("java software developer", "joutseno").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="joutseno")
	
@java.route('/java-software-developer-jobs-pedersore')
def java_software_developer90(page=1):

    job_list = job_obj.get_job("java software developer", "pedersore").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="pedersore")
	
@java.route('/java-software-developer-jobs-sotkamo')
def java_software_developer91(page=1):

    job_list = job_obj.get_job("java software developer", "sotkamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="sotkamo")
	
@java.route('/java-software-developer-jobs-kuhmo')
def java_software_developer92(page=1):

    job_list = job_obj.get_job("java software developer", "kuhmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="kuhmo")
	
@java.route('/java-software-developer-jobs-paimio')
def java_software_developer93(page=1):

    job_list = job_obj.get_job("java software developer", "paimio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="paimio")
	
@java.route('/java-software-developer-jobs-saarijarvi')
def java_software_developer94(page=1):

    job_list = job_obj.get_job("java software developer", "saarijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="saarijarvi")
	
@java.route('/java-software-developer-jobs-helsinki')
def java_software_developer95(page=1):

    job_list = job_obj.get_job("java software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="java software developer", location="helsinki")


####################################################################

