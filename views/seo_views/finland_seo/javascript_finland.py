from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

javascript = Blueprint('javascript', __name__)
job_obj = Job()



####################################################################


@javascript.route('/javascript_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "javascript" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def javascript_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="espoo")

@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def javascript_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="tampere")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def javascript_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="vantaa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def javascript_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="turku")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def javascript_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="oulu")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def javascript_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="lahti")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def javascript_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kuopio")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def javascript_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="jyvvaskyla")

@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def javascript_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="pori")

@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def javascript_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="lappeenranta")	
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def javascript_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="vaasa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def javascript_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kotka")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def javascript_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="joensuu")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def javascript_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="hameenlinna")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def javascript_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="porvoo")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def javascript_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="mikkeli")

@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def javascript_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="hyvinkaa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def javascript_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="nurmijarvi")

@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def javascript_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="jarvenpaa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def javascript_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="rauma")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def javascript_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="lohja")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def javascript_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="karleby")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def javascript_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kajaani")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def javascript_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="rovaniemi")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def javascript_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="tuusula")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def javascript_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kirkkonummi")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def javascript_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="seinajoki")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def javascript_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kerava")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def javascript_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kouvola")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def javascript_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="imatra")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def javascript_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="nokia")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def javascript_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="savonlinna")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def javascript_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="riihimaki")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def javascript_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="vihti")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def javascript_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="salo")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def javascript_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kangasala")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def javascript_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="raisio")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def javascript_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="karhula")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def javascript_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kemi")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def javascript_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="iisalmi")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def javascript_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="varkaus")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def javascript_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="raahe")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def javascript_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="ylojarvi")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def javascript_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="hamina")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def javascript_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kaarina")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def javascript_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="tornio")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def javascript_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="heinola")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def javascript_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="hollola")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def javascript_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="valkeakoski")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def javascript_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="siilinjarvi")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def javascript_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kuusankoski")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def javascript_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="sibbo")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def javascript_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="jakostad")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def javascript_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="lempaala")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def javascript_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="mantsala")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def javascript_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="forssa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def javascript_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kuusamo")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def javascript_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="haukipudas")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def javascript_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="korsholm")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def javascript_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="laukaa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def javascript_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="anjala")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def javascript_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="uusikaupunki")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def javascript_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="janakkala")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def javascript_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="pirkkala")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def javascript_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def javascript_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="jamsa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def javascript_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="jamsa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def javascript_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="vammala")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def javascript_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="nastola")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def javascript_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="orimattila")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def javascript_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kauhajoki")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def javascript_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="ekenas")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def javascript_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kempele")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def javascript_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="lapua")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def javascript_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="lieksa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def javascript_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="naantali")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def javascript_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="aanekoski")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def javascript_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="ylivieska")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def javascript_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kontiolahti")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def javascript_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kankaanpaa")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def javascript_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="ulvila")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def javascript_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="pieksamaki")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def javascript_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kiiminki")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def javascript_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="pargas")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def javascript_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="nurmo")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def javascript_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="ilmajoki")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def javascript_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="liperi")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def javascript_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="keuruu")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def javascript_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="leppavirta")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def javascript_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kurikka")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def javascript_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="nivala")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def javascript_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="joutseno")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def javascript_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="pedersore")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def javascript_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="sotkamo")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def javascript_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="kuhmo")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def javascript_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="paimio")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def javascript_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="saarijarvi")
	
@javascript.route('/javascript-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def javascript_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("javascript ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@javascript.route('/javascript-software-developer-jobs-espoo')
def javascript_software_developer2(page=1):

    job_list = job_obj.get_job("javascript software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="espoo")

@javascript.route('/javascript-software-developer-jobs-tampere')
def javascript_software_developer3(page=1):

    job_list = job_obj.get_job("javascript software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="tampere")
	
@javascript.route('/javascript-software-developer-jobs-vantaa')
def javascript_software_developer4(page=1):

    job_list = job_obj.get_job("javascript software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="vantaa")
	
@javascript.route('/javascript-software-developer-jobs-turku')
def javascript_software_developer5(page=1):

    job_list = job_obj.get_job("javascript software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="turku")
	
@javascript.route('/javascript-software-developer-jobs-oulu')
def javascript_software_developer6(page=1):

    job_list = job_obj.get_job("javascript software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="oulu")
	
@javascript.route('/javascript-software-developer-jobs-lahti')
def javascript_software_developer7(page=1):

    job_list = job_obj.get_job("javascript software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="lahti")
	
@javascript.route('/javascript-software-developer-jobs-kuopio')
def javascript_software_developer8(page=1):

    job_list = job_obj.get_job("javascript software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kuopio")
	
@javascript.route('/javascript-software-developer-jobs-jyvvaskyla')
def javascript_software_developer9(page=1):

    job_list = job_obj.get_job("javascript software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="jyvvaskyla")

@javascript.route('/javascript-software-developer-jobs-pori')
def javascript_software_developer10(page=1):

    job_list = job_obj.get_job("javascript software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="pori")

@javascript.route('/javascript-software-developer-jobs-lappeenranta')
def javascript_software_developer11(page=1):

    job_list = job_obj.get_job("javascript software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="lappeenranta")	
	
@javascript.route('/javascript-software-developer-jobs-vaasa')
def javascript_software_developer12(page=1):

    job_list = job_obj.get_job("javascript software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="vaasa")
	
@javascript.route('/javascript-software-developer-jobs-kotka')
def javascript_software_developer13(page=1):

    job_list = job_obj.get_job("javascript software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kotka")
	
@javascript.route('/javascript-software-developer-jobs-joensuu')
def javascript_software_developer14(page=1):

    job_list = job_obj.get_job("javascript software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="joensuu")
	
@javascript.route('/javascript-software-developer-jobs-hameenlinna')
def javascript_software_developer15(page=1):

    job_list = job_obj.get_job("javascript software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="hameenlinna")
	
@javascript.route('/javascript-software-developer-jobs-porvoo')
def javascript_software_developer16(page=1):

    job_list = job_obj.get_job("javascript software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="porvoo")
	
@javascript.route('/javascript-software-developer-jobs-mikkeli')
def javascript_software_developer17(page=1):

    job_list = job_obj.get_job("javascript software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="mikkeli")

@javascript.route('/javascript-software-developer-jobs-hyvinkaa')
def javascript_software_developer18(page=1):

    job_list = job_obj.get_job("javascript software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="hyvinkaa")
	
@javascript.route('/javascript-software-developer-jobs-nurmijarvi')
def javascript_software_developer19(page=1):

    job_list = job_obj.get_job("javascript software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="nurmijarvi")

@javascript.route('/javascript-software-developer-jobs-jarvenpaa')
def javascript_software_developer20(page=1):

    job_list = job_obj.get_job("javascript software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="jarvenpaa")
	
@javascript.route('/javascript-software-developer-jobs-rauma')
def javascript_software_developer21(page=1):

    job_list = job_obj.get_job("javascript software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="rauma")
	
@javascript.route('/javascript-software-developer-jobs-lohja')
def javascript_software_developer22(page=1):

    job_list = job_obj.get_job("javascript software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="lohja")
	
@javascript.route('/javascript-software-developer-jobs-karleby')
def javascript_software_developer23(page=1):

    job_list = job_obj.get_job("javascript software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="karleby")
	
@javascript.route('/javascript-software-developer-jobs-kajaani')
def javascript_software_developer24(page=1):

    job_list = job_obj.get_job("javascript software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kajaani")
	
@javascript.route('/javascript-software-developer-jobs-rovaniemi')
def javascript_software_developer25(page=1):

    job_list = job_obj.get_job("javascript software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="rovaniemi")
	
@javascript.route('/javascript-software-developer-jobs-tuusula')
def javascript_software_developer26(page=1):

    job_list = job_obj.get_job("javascript software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="tuusula")
	
@javascript.route('/javascript-software-developer-jobs-kirkkonummi')
def javascript_software_developer27(page=1):

    job_list = job_obj.get_job("javascript software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kirkkonummi")
	
@javascript.route('/javascript-software-developer-jobs-seinajoki')
def javascript_software_developer28(page=1):

    job_list = job_obj.get_job("javascript software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="seinajoki")
	
@javascript.route('/javascript-software-developer-jobs-kerava')
def javascript_software_developer29(page=1):

    job_list = job_obj.get_job("javascript software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kerava")
	
@javascript.route('/javascript-software-developer-jobs-kouvola')
def javascript_software_developer30(page=1):

    job_list = job_obj.get_job("javascript software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kouvola")
	
@javascript.route('/javascript-software-developer-jobs-imatra')
def javascript_software_developer31(page=1):

    job_list = job_obj.get_job("javascript software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="imatra")
	
@javascript.route('/javascript-software-developer-jobs-nokia')
def javascript_software_developer32_1(page=1):

    job_list = job_obj.get_job("javascript software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="nokia")
	
@javascript.route('/javascript-software-developer-jobs-savonlinna')
def javascript_software_developer32(page=1):

    job_list = job_obj.get_job("javascript software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="savonlinna")
	
@javascript.route('/javascript-software-developer-jobs-riihimaki')
def javascript_software_developer33(page=1):

    job_list = job_obj.get_job("javascript software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="riihimaki")
	
@javascript.route('/javascript-software-developer-jobs-vihti')
def javascript_software_developer34(page=1):

    job_list = job_obj.get_job("javascript software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="vihti")
	
@javascript.route('/javascript-software-developer-jobs-salo')
def javascript_software_developer35(page=1):

    job_list = job_obj.get_job("javascript software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="salo")
	
@javascript.route('/javascript-software-developer-jobs-kangasala')
def javascript_software_developer36(page=1):

    job_list = job_obj.get_job("javascript software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kangasala")
	
@javascript.route('/javascript-software-developer-jobs-raisio')
def javascript_software_developer37_1(page=1):

    job_list = job_obj.get_job("javascript software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="raisio")
	
@javascript.route('/javascript-software-developer-jobs-karhula')
def javascript_software_developer37(page=1):

    job_list = job_obj.get_job("javascript software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="karhula")
	
@javascript.route('/javascript-software-developer-jobs-kemi')
def javascript_software_developer38(page=1):

    job_list = job_obj.get_job("javascript software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kemi")
	
@javascript.route('/javascript-software-developer-jobs-iisalmi')
def javascript_software_developer39(page=1):

    job_list = job_obj.get_job("javascript software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="iisalmi")
	
@javascript.route('/javascript-software-developer-jobs-varkaus')
def javascript_software_developer40(page=1):

    job_list = job_obj.get_job("javascript software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="varkaus")
	
@javascript.route('/javascript-software-developer-jobs-raahe')
def javascript_software_developer41(page=1):

    job_list = job_obj.get_job("javascript software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="raahe")
	
@javascript.route('/javascript-software-developer-jobs-ylojarvi')
def javascript_software_developer42_1(page=1):

    job_list = job_obj.get_job("javascript software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="ylojarvi")
	
@javascript.route('/javascript-software-developer-jobs-hamina')
def javascript_software_developer42(page=1):

    job_list = job_obj.get_job("javascript software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="hamina")
	
@javascript.route('/javascript-software-developer-jobs-kaarina')
def javascript_software_developer43(page=1):

    job_list = job_obj.get_job("javascript software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kaarina")
	
@javascript.route('/javascript-software-developer-jobs-tornio')
def javascript_software_developer44(page=1):

    job_list = job_obj.get_job("javascript software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="tornio")
	
@javascript.route('/javascript-software-developer-jobs-heinola')
def javascript_software_developer45(page=1):

    job_list = job_obj.get_job("javascript software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="heinola")
	
@javascript.route('/javascript-software-developer-jobs-hollola')
def javascript_software_developer46(page=1):

    job_list = job_obj.get_job("javascript software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="hollola")
	
@javascript.route('/javascript-software-developer-jobs-valkeakoski')
def javascript_software_developer47(page=1):

    job_list = job_obj.get_job("javascript software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="valkeakoski")
	
@javascript.route('/javascript-software-developer-jobs-siilinjarvi')
def javascript_software_developer48(page=1):

    job_list = job_obj.get_job("javascript software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="siilinjarvi")
	
@javascript.route('/javascript-software-developer-jobs-kuusankoski')
def javascript_software_developer49(page=1):

    job_list = job_obj.get_job("javascript software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kuusankoski")
	
@javascript.route('/javascript-software-developer-jobs-sibbo')
def javascript_software_developer50(page=1):

    job_list = job_obj.get_job("javascript software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="sibbo")
	
@javascript.route('/javascript-software-developer-jobs-jakostad')
def javascript_software_developer51(page=1):

    job_list = job_obj.get_job("javascript software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="jakostad")
	
@javascript.route('/javascript-software-developer-jobs-lempaala')
def javascript_software_developer52(page=1):

    job_list = job_obj.get_job("javascript software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="lempaala")
	
@javascript.route('/javascript-software-developer-jobs-mantsala')
def javascript_software_developer52_1(page=1):

    job_list = job_obj.get_job("javascript software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="mantsala")
	
@javascript.route('/javascript-software-developer-jobs-forssa')
def javascript_software_developer53(page=1):

    job_list = job_obj.get_job("javascript software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="forssa")
	
@javascript.route('/javascript-software-developer-jobs-kuusamo')
def javascript_software_developer54(page=1):

    job_list = job_obj.get_job("javascript software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kuusamo")
	
@javascript.route('/javascript-software-developer-jobs-haukipudas')
def javascript_software_developer55(page=1):

    job_list = job_obj.get_job("javascript software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="haukipudas")
	
@javascript.route('/javascript-software-developer-jobs-korsholm')
def javascript_software_developer56(page=1):

    job_list = job_obj.get_job("javascript software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="korsholm")
	
@javascript.route('/javascript-software-developer-jobs-laukaa')
def javascript_software_developer57(page=1):

    job_list = job_obj.get_job("javascript software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="laukaa")
	
@javascript.route('/javascript-software-developer-jobs-anjala')
def javascript_software_developer58(page=1):

    job_list = job_obj.get_job("javascript software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="anjala")
	
@javascript.route('/javascript-software-developer-jobs-uusikaupunki')
def javascript_software_developer59(page=1):

    job_list = job_obj.get_job("javascript software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="uusikaupunki")
	
@javascript.route('/javascript-software-developer-jobs-janakkala')
def javascript_software_developer60(page=1):

    job_list = job_obj.get_job("javascript software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="janakkala")
	
@javascript.route('/javascript-software-developer-jobs-pirkkala')
def javascript_software_developer61(page=1):

    job_list = job_obj.get_job("javascript software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="pirkkala")
	
@javascript.route('/javascript-software-developer-jobs-lansi-turunmaa')
def javascript_software_developer62(page=1):

    job_list = job_obj.get_job("javascript software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="lansi-turunmaa")
	
@javascript.route('/javascript-software-developer-jobs-jamsa')
def javascript_software_developer63(page=1):

    job_list = job_obj.get_job("javascript software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="jamsa")
	
@javascript.route('/javascript-software-developer-jobs-jamsa')
def javascript_software_developer64(page=1):

    job_list = job_obj.get_job("javascript software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="jamsa")
	
@javascript.route('/javascript-software-developer-jobs-vammala')
def javascript_software_developer65(page=1):

    job_list = job_obj.get_job("javascript software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="vammala")
	
@javascript.route('/javascript-software-developer-jobs-nastola')
def javascript_software_developer66(page=1):

    job_list = job_obj.get_job("javascript software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="nastola")
	
@javascript.route('/javascript-software-developer-jobs-orimattila')
def javascript_software_developer67(page=1):

    job_list = job_obj.get_job("javascript software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="orimattila")
	
@javascript.route('/javascript-software-developer-jobs-kauhajoki')
def javascript_software_developer68(page=1):

    job_list = job_obj.get_job("javascript software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kauhajoki")
	
@javascript.route('/javascript-software-developer-jobs-ekenas')
def javascript_software_developer69(page=1):

    job_list = job_obj.get_job("javascript software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="ekenas")
	
@javascript.route('/javascript-software-developer-jobs-kempele')
def javascript_software_developer70(page=1):

    job_list = job_obj.get_job("javascript software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kempele")
	
@javascript.route('/javascript-software-developer-jobs-lapua')
def javascript_software_developer71(page=1):

    job_list = job_obj.get_job("javascript software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="lapua")
	
@javascript.route('/javascript-software-developer-jobs-lieksa')
def javascript_software_developer72(page=1):

    job_list = job_obj.get_job("javascript software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="lieksa")
	
@javascript.route('/javascript-software-developer-jobs-naantali')
def javascript_software_developer73(page=1):

    job_list = job_obj.get_job("javascript software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="naantali")
	
@javascript.route('/javascript-software-developer-jobs-aanekoski')
def javascript_software_developer74(page=1):

    job_list = job_obj.get_job("javascript software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="aanekoski")
	
@javascript.route('/javascript-software-developer-jobs-ylivieska')
def javascript_software_developer75(page=1):

    job_list = job_obj.get_job("javascript software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="ylivieska")
	
@javascript.route('/javascript-software-developer-jobs-kontiolahti')
def javascript_software_developer76(page=1):

    job_list = job_obj.get_job("javascript software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kontiolahti")
	
@javascript.route('/javascript-software-developer-jobs-kankaanpaa')
def javascript_software_developer77(page=1):

    job_list = job_obj.get_job("javascript software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kankaanpaa")
	
@javascript.route('/javascript-software-developer-jobs-ulvila')
def javascript_software_developer78(page=1):

    job_list = job_obj.get_job("javascript software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="ulvila")
	
@javascript.route('/javascript-software-developer-jobs-pieksamaki')
def javascript_software_developer79(page=1):

    job_list = job_obj.get_job("javascript software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="pieksamaki")
	
@javascript.route('/javascript-software-developer-jobs-kiiminki')
def javascript_software_developer80(page=1):

    job_list = job_obj.get_job("javascript software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kiiminki")
	
@javascript.route('/javascript-software-developer-jobs-pargas')
def javascript_software_developer81(page=1):

    job_list = job_obj.get_job("javascript software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="pargas")
	
@javascript.route('/javascript-software-developer-jobs-nurmo')
def javascript_software_developer82(page=1):

    job_list = job_obj.get_job("javascript software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="nurmo")
	
@javascript.route('/javascript-software-developer-jobs-ilmajoki')
def javascript_software_developer83(page=1):

    job_list = job_obj.get_job("javascript software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="ilmajoki")
	
@javascript.route('/javascript-software-developer-jobs-liperi')
def javascript_software_developer84(page=1):

    job_list = job_obj.get_job("javascript software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="liperi")
	
@javascript.route('/javascript-software-developer-jobs-keuruu')
def javascript_software_developer85(page=1):

    job_list = job_obj.get_job("javascript software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="keuruu")
	
@javascript.route('/javascript-software-developer-jobs-leppavirta')
def javascript_software_developer86(page=1):

    job_list = job_obj.get_job("javascript software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="leppavirta")
	
@javascript.route('/javascript-software-developer-jobs-kurikka')
def javascript_software_developer87(page=1):

    job_list = job_obj.get_job("javascript software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kurikka")
	
@javascript.route('/javascript-software-developer-jobs-nivala')
def javascript_software_developer88(page=1):

    job_list = job_obj.get_job("javascript software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="nivala")
	
@javascript.route('/javascript-software-developer-jobs-joutseno')
def javascript_software_developer89(page=1):

    job_list = job_obj.get_job("javascript software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="joutseno")
	
@javascript.route('/javascript-software-developer-jobs-pedersore')
def javascript_software_developer90(page=1):

    job_list = job_obj.get_job("javascript software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="pedersore")
	
@javascript.route('/javascript-software-developer-jobs-sotkamo')
def javascript_software_developer91(page=1):

    job_list = job_obj.get_job("javascript software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="sotkamo")
	
@javascript.route('/javascript-software-developer-jobs-kuhmo')
def javascript_software_developer92(page=1):

    job_list = job_obj.get_job("javascript software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="kuhmo")
	
@javascript.route('/javascript-software-developer-jobs-paimio')
def javascript_software_developer93(page=1):

    job_list = job_obj.get_job("javascript software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="paimio")
	
@javascript.route('/javascript-software-developer-jobs-saarijarvi')
def javascript_software_developer94(page=1):

    job_list = job_obj.get_job("javascript software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="saarijarvi")
	
@javascript.route('/javascript-software-developer-jobs-helsinki')
def javascript_software_developer95(page=1):

    job_list = job_obj.get_job("javascript software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="javascript software developer", location="helsinki")


####################################################################

