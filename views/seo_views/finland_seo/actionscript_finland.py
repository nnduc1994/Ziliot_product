from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

actionscript = Blueprint('actionscript', __name__)
job_obj = Job()



####################################################################


@actionscript.route('/actionscript_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "actionscript" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def actionscript_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="espoo")

@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def actionscript_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="tampere")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def actionscript_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="vantaa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def actionscript_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="turku")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def actionscript_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="oulu")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def actionscript_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="lahti")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def actionscript_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kuopio")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def actionscript_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="jyvvaskyla")

@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def actionscript_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="pori")

@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def actionscript_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="lappeenranta")	
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def actionscript_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="vaasa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def actionscript_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kotka")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def actionscript_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="joensuu")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def actionscript_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="hameenlinna")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def actionscript_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="porvoo")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def actionscript_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="mikkeli")

@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def actionscript_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="hyvinkaa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def actionscript_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="nurmijarvi")

@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def actionscript_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="jarvenpaa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def actionscript_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="rauma")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def actionscript_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="lohja")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def actionscript_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="karleby")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def actionscript_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kajaani")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def actionscript_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="rovaniemi")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def actionscript_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="tuusula")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def actionscript_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kirkkonummi")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def actionscript_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="seinajoki")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def actionscript_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kerava")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def actionscript_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kouvola")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def actionscript_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="imatra")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def actionscript_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="nokia")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def actionscript_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="savonlinna")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def actionscript_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="riihimaki")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def actionscript_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="vihti")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def actionscript_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="salo")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def actionscript_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kangasala")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def actionscript_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="raisio")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def actionscript_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="karhula")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def actionscript_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kemi")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def actionscript_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="iisalmi")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def actionscript_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="varkaus")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def actionscript_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="raahe")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def actionscript_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="ylojarvi")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def actionscript_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="hamina")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def actionscript_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kaarina")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def actionscript_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="tornio")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def actionscript_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="heinola")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def actionscript_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="hollola")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def actionscript_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="valkeakoski")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def actionscript_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="siilinjarvi")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def actionscript_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kuusankoski")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def actionscript_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="sibbo")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def actionscript_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="jakostad")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def actionscript_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="lempaala")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def actionscript_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="mantsala")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def actionscript_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="forssa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def actionscript_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kuusamo")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def actionscript_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="haukipudas")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def actionscript_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="korsholm")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def actionscript_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="laukaa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def actionscript_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="anjala")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def actionscript_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="uusikaupunki")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def actionscript_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="janakkala")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def actionscript_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="pirkkala")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def actionscript_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def actionscript_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="jamsa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def actionscript_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="jamsa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def actionscript_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="vammala")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def actionscript_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="nastola")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def actionscript_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="orimattila")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def actionscript_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kauhajoki")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def actionscript_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="ekenas")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def actionscript_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kempele")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def actionscript_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="lapua")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def actionscript_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="lieksa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def actionscript_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="naantali")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def actionscript_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="aanekoski")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def actionscript_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="ylivieska")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def actionscript_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kontiolahti")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def actionscript_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kankaanpaa")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def actionscript_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="ulvila")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def actionscript_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="pieksamaki")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def actionscript_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kiiminki")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def actionscript_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="pargas")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def actionscript_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="nurmo")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def actionscript_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="ilmajoki")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def actionscript_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="liperi")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def actionscript_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="keuruu")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def actionscript_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="leppavirta")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def actionscript_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kurikka")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def actionscript_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="nivala")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def actionscript_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="joutseno")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def actionscript_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="pedersore")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def actionscript_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="sotkamo")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def actionscript_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="kuhmo")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def actionscript_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="paimio")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def actionscript_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="saarijarvi")
	
@actionscript.route('/actionscript-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def actionscript_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("actionscript ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@actionscript.route('/actionscript-software-developer-jobs-espoo')
def actionscript_software_developer2(page=1):

    job_list = job_obj.get_job("actionscript software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="espoo")

@actionscript.route('/actionscript-software-developer-jobs-tampere')
def actionscript_software_developer3(page=1):

    job_list = job_obj.get_job("actionscript software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="tampere")
	
@actionscript.route('/actionscript-software-developer-jobs-vantaa')
def actionscript_software_developer4(page=1):

    job_list = job_obj.get_job("actionscript software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="vantaa")
	
@actionscript.route('/actionscript-software-developer-jobs-turku')
def actionscript_software_developer5(page=1):

    job_list = job_obj.get_job("actionscript software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="turku")
	
@actionscript.route('/actionscript-software-developer-jobs-oulu')
def actionscript_software_developer6(page=1):

    job_list = job_obj.get_job("actionscript software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="oulu")
	
@actionscript.route('/actionscript-software-developer-jobs-lahti')
def actionscript_software_developer7(page=1):

    job_list = job_obj.get_job("actionscript software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="lahti")
	
@actionscript.route('/actionscript-software-developer-jobs-kuopio')
def actionscript_software_developer8(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kuopio")
	
@actionscript.route('/actionscript-software-developer-jobs-jyvvaskyla')
def actionscript_software_developer9(page=1):

    job_list = job_obj.get_job("actionscript software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="jyvvaskyla")

@actionscript.route('/actionscript-software-developer-jobs-pori')
def actionscript_software_developer10(page=1):

    job_list = job_obj.get_job("actionscript software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="pori")

@actionscript.route('/actionscript-software-developer-jobs-lappeenranta')
def actionscript_software_developer11(page=1):

    job_list = job_obj.get_job("actionscript software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="lappeenranta")	
	
@actionscript.route('/actionscript-software-developer-jobs-vaasa')
def actionscript_software_developer12(page=1):

    job_list = job_obj.get_job("actionscript software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="vaasa")
	
@actionscript.route('/actionscript-software-developer-jobs-kotka')
def actionscript_software_developer13(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kotka")
	
@actionscript.route('/actionscript-software-developer-jobs-joensuu')
def actionscript_software_developer14(page=1):

    job_list = job_obj.get_job("actionscript software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="joensuu")
	
@actionscript.route('/actionscript-software-developer-jobs-hameenlinna')
def actionscript_software_developer15(page=1):

    job_list = job_obj.get_job("actionscript software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="hameenlinna")
	
@actionscript.route('/actionscript-software-developer-jobs-porvoo')
def actionscript_software_developer16(page=1):

    job_list = job_obj.get_job("actionscript software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="porvoo")
	
@actionscript.route('/actionscript-software-developer-jobs-mikkeli')
def actionscript_software_developer17(page=1):

    job_list = job_obj.get_job("actionscript software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="mikkeli")

@actionscript.route('/actionscript-software-developer-jobs-hyvinkaa')
def actionscript_software_developer18(page=1):

    job_list = job_obj.get_job("actionscript software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="hyvinkaa")
	
@actionscript.route('/actionscript-software-developer-jobs-nurmijarvi')
def actionscript_software_developer19(page=1):

    job_list = job_obj.get_job("actionscript software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="nurmijarvi")

@actionscript.route('/actionscript-software-developer-jobs-jarvenpaa')
def actionscript_software_developer20(page=1):

    job_list = job_obj.get_job("actionscript software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="jarvenpaa")
	
@actionscript.route('/actionscript-software-developer-jobs-rauma')
def actionscript_software_developer21(page=1):

    job_list = job_obj.get_job("actionscript software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="rauma")
	
@actionscript.route('/actionscript-software-developer-jobs-lohja')
def actionscript_software_developer22(page=1):

    job_list = job_obj.get_job("actionscript software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="lohja")
	
@actionscript.route('/actionscript-software-developer-jobs-karleby')
def actionscript_software_developer23(page=1):

    job_list = job_obj.get_job("actionscript software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="karleby")
	
@actionscript.route('/actionscript-software-developer-jobs-kajaani')
def actionscript_software_developer24(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kajaani")
	
@actionscript.route('/actionscript-software-developer-jobs-rovaniemi')
def actionscript_software_developer25(page=1):

    job_list = job_obj.get_job("actionscript software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="rovaniemi")
	
@actionscript.route('/actionscript-software-developer-jobs-tuusula')
def actionscript_software_developer26(page=1):

    job_list = job_obj.get_job("actionscript software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="tuusula")
	
@actionscript.route('/actionscript-software-developer-jobs-kirkkonummi')
def actionscript_software_developer27(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kirkkonummi")
	
@actionscript.route('/actionscript-software-developer-jobs-seinajoki')
def actionscript_software_developer28(page=1):

    job_list = job_obj.get_job("actionscript software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="seinajoki")
	
@actionscript.route('/actionscript-software-developer-jobs-kerava')
def actionscript_software_developer29(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kerava")
	
@actionscript.route('/actionscript-software-developer-jobs-kouvola')
def actionscript_software_developer30(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kouvola")
	
@actionscript.route('/actionscript-software-developer-jobs-imatra')
def actionscript_software_developer31(page=1):

    job_list = job_obj.get_job("actionscript software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="imatra")
	
@actionscript.route('/actionscript-software-developer-jobs-nokia')
def actionscript_software_developer32_1(page=1):

    job_list = job_obj.get_job("actionscript software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="nokia")
	
@actionscript.route('/actionscript-software-developer-jobs-savonlinna')
def actionscript_software_developer32(page=1):

    job_list = job_obj.get_job("actionscript software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="savonlinna")
	
@actionscript.route('/actionscript-software-developer-jobs-riihimaki')
def actionscript_software_developer33(page=1):

    job_list = job_obj.get_job("actionscript software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="riihimaki")
	
@actionscript.route('/actionscript-software-developer-jobs-vihti')
def actionscript_software_developer34(page=1):

    job_list = job_obj.get_job("actionscript software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="vihti")
	
@actionscript.route('/actionscript-software-developer-jobs-salo')
def actionscript_software_developer35(page=1):

    job_list = job_obj.get_job("actionscript software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="salo")
	
@actionscript.route('/actionscript-software-developer-jobs-kangasala')
def actionscript_software_developer36(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kangasala")
	
@actionscript.route('/actionscript-software-developer-jobs-raisio')
def actionscript_software_developer37_1(page=1):

    job_list = job_obj.get_job("actionscript software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="raisio")
	
@actionscript.route('/actionscript-software-developer-jobs-karhula')
def actionscript_software_developer37(page=1):

    job_list = job_obj.get_job("actionscript software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="karhula")
	
@actionscript.route('/actionscript-software-developer-jobs-kemi')
def actionscript_software_developer38(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kemi")
	
@actionscript.route('/actionscript-software-developer-jobs-iisalmi')
def actionscript_software_developer39(page=1):

    job_list = job_obj.get_job("actionscript software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="iisalmi")
	
@actionscript.route('/actionscript-software-developer-jobs-varkaus')
def actionscript_software_developer40(page=1):

    job_list = job_obj.get_job("actionscript software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="varkaus")
	
@actionscript.route('/actionscript-software-developer-jobs-raahe')
def actionscript_software_developer41(page=1):

    job_list = job_obj.get_job("actionscript software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="raahe")
	
@actionscript.route('/actionscript-software-developer-jobs-ylojarvi')
def actionscript_software_developer42_1(page=1):

    job_list = job_obj.get_job("actionscript software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="ylojarvi")
	
@actionscript.route('/actionscript-software-developer-jobs-hamina')
def actionscript_software_developer42(page=1):

    job_list = job_obj.get_job("actionscript software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="hamina")
	
@actionscript.route('/actionscript-software-developer-jobs-kaarina')
def actionscript_software_developer43(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kaarina")
	
@actionscript.route('/actionscript-software-developer-jobs-tornio')
def actionscript_software_developer44(page=1):

    job_list = job_obj.get_job("actionscript software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="tornio")
	
@actionscript.route('/actionscript-software-developer-jobs-heinola')
def actionscript_software_developer45(page=1):

    job_list = job_obj.get_job("actionscript software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="heinola")
	
@actionscript.route('/actionscript-software-developer-jobs-hollola')
def actionscript_software_developer46(page=1):

    job_list = job_obj.get_job("actionscript software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="hollola")
	
@actionscript.route('/actionscript-software-developer-jobs-valkeakoski')
def actionscript_software_developer47(page=1):

    job_list = job_obj.get_job("actionscript software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="valkeakoski")
	
@actionscript.route('/actionscript-software-developer-jobs-siilinjarvi')
def actionscript_software_developer48(page=1):

    job_list = job_obj.get_job("actionscript software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="siilinjarvi")
	
@actionscript.route('/actionscript-software-developer-jobs-kuusankoski')
def actionscript_software_developer49(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kuusankoski")
	
@actionscript.route('/actionscript-software-developer-jobs-sibbo')
def actionscript_software_developer50(page=1):

    job_list = job_obj.get_job("actionscript software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="sibbo")
	
@actionscript.route('/actionscript-software-developer-jobs-jakostad')
def actionscript_software_developer51(page=1):

    job_list = job_obj.get_job("actionscript software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="jakostad")
	
@actionscript.route('/actionscript-software-developer-jobs-lempaala')
def actionscript_software_developer52(page=1):

    job_list = job_obj.get_job("actionscript software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="lempaala")
	
@actionscript.route('/actionscript-software-developer-jobs-mantsala')
def actionscript_software_developer52_1(page=1):

    job_list = job_obj.get_job("actionscript software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="mantsala")
	
@actionscript.route('/actionscript-software-developer-jobs-forssa')
def actionscript_software_developer53(page=1):

    job_list = job_obj.get_job("actionscript software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="forssa")
	
@actionscript.route('/actionscript-software-developer-jobs-kuusamo')
def actionscript_software_developer54(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kuusamo")
	
@actionscript.route('/actionscript-software-developer-jobs-haukipudas')
def actionscript_software_developer55(page=1):

    job_list = job_obj.get_job("actionscript software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="haukipudas")
	
@actionscript.route('/actionscript-software-developer-jobs-korsholm')
def actionscript_software_developer56(page=1):

    job_list = job_obj.get_job("actionscript software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="korsholm")
	
@actionscript.route('/actionscript-software-developer-jobs-laukaa')
def actionscript_software_developer57(page=1):

    job_list = job_obj.get_job("actionscript software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="laukaa")
	
@actionscript.route('/actionscript-software-developer-jobs-anjala')
def actionscript_software_developer58(page=1):

    job_list = job_obj.get_job("actionscript software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="anjala")
	
@actionscript.route('/actionscript-software-developer-jobs-uusikaupunki')
def actionscript_software_developer59(page=1):

    job_list = job_obj.get_job("actionscript software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="uusikaupunki")
	
@actionscript.route('/actionscript-software-developer-jobs-janakkala')
def actionscript_software_developer60(page=1):

    job_list = job_obj.get_job("actionscript software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="janakkala")
	
@actionscript.route('/actionscript-software-developer-jobs-pirkkala')
def actionscript_software_developer61(page=1):

    job_list = job_obj.get_job("actionscript software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="pirkkala")
	
@actionscript.route('/actionscript-software-developer-jobs-lansi-turunmaa')
def actionscript_software_developer62(page=1):

    job_list = job_obj.get_job("actionscript software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="lansi-turunmaa")
	
@actionscript.route('/actionscript-software-developer-jobs-jamsa')
def actionscript_software_developer63(page=1):

    job_list = job_obj.get_job("actionscript software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="jamsa")
	
@actionscript.route('/actionscript-software-developer-jobs-jamsa')
def actionscript_software_developer64(page=1):

    job_list = job_obj.get_job("actionscript software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="jamsa")
	
@actionscript.route('/actionscript-software-developer-jobs-vammala')
def actionscript_software_developer65(page=1):

    job_list = job_obj.get_job("actionscript software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="vammala")
	
@actionscript.route('/actionscript-software-developer-jobs-nastola')
def actionscript_software_developer66(page=1):

    job_list = job_obj.get_job("actionscript software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="nastola")
	
@actionscript.route('/actionscript-software-developer-jobs-orimattila')
def actionscript_software_developer67(page=1):

    job_list = job_obj.get_job("actionscript software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="orimattila")
	
@actionscript.route('/actionscript-software-developer-jobs-kauhajoki')
def actionscript_software_developer68(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kauhajoki")
	
@actionscript.route('/actionscript-software-developer-jobs-ekenas')
def actionscript_software_developer69(page=1):

    job_list = job_obj.get_job("actionscript software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="ekenas")
	
@actionscript.route('/actionscript-software-developer-jobs-kempele')
def actionscript_software_developer70(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kempele")
	
@actionscript.route('/actionscript-software-developer-jobs-lapua')
def actionscript_software_developer71(page=1):

    job_list = job_obj.get_job("actionscript software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="lapua")
	
@actionscript.route('/actionscript-software-developer-jobs-lieksa')
def actionscript_software_developer72(page=1):

    job_list = job_obj.get_job("actionscript software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="lieksa")
	
@actionscript.route('/actionscript-software-developer-jobs-naantali')
def actionscript_software_developer73(page=1):

    job_list = job_obj.get_job("actionscript software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="naantali")
	
@actionscript.route('/actionscript-software-developer-jobs-aanekoski')
def actionscript_software_developer74(page=1):

    job_list = job_obj.get_job("actionscript software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="aanekoski")
	
@actionscript.route('/actionscript-software-developer-jobs-ylivieska')
def actionscript_software_developer75(page=1):

    job_list = job_obj.get_job("actionscript software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="ylivieska")
	
@actionscript.route('/actionscript-software-developer-jobs-kontiolahti')
def actionscript_software_developer76(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kontiolahti")
	
@actionscript.route('/actionscript-software-developer-jobs-kankaanpaa')
def actionscript_software_developer77(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kankaanpaa")
	
@actionscript.route('/actionscript-software-developer-jobs-ulvila')
def actionscript_software_developer78(page=1):

    job_list = job_obj.get_job("actionscript software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="ulvila")
	
@actionscript.route('/actionscript-software-developer-jobs-pieksamaki')
def actionscript_software_developer79(page=1):

    job_list = job_obj.get_job("actionscript software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="pieksamaki")
	
@actionscript.route('/actionscript-software-developer-jobs-kiiminki')
def actionscript_software_developer80(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kiiminki")
	
@actionscript.route('/actionscript-software-developer-jobs-pargas')
def actionscript_software_developer81(page=1):

    job_list = job_obj.get_job("actionscript software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="pargas")
	
@actionscript.route('/actionscript-software-developer-jobs-nurmo')
def actionscript_software_developer82(page=1):

    job_list = job_obj.get_job("actionscript software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="nurmo")
	
@actionscript.route('/actionscript-software-developer-jobs-ilmajoki')
def actionscript_software_developer83(page=1):

    job_list = job_obj.get_job("actionscript software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="ilmajoki")
	
@actionscript.route('/actionscript-software-developer-jobs-liperi')
def actionscript_software_developer84(page=1):

    job_list = job_obj.get_job("actionscript software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="liperi")
	
@actionscript.route('/actionscript-software-developer-jobs-keuruu')
def actionscript_software_developer85(page=1):

    job_list = job_obj.get_job("actionscript software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="keuruu")
	
@actionscript.route('/actionscript-software-developer-jobs-leppavirta')
def actionscript_software_developer86(page=1):

    job_list = job_obj.get_job("actionscript software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="leppavirta")
	
@actionscript.route('/actionscript-software-developer-jobs-kurikka')
def actionscript_software_developer87(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kurikka")
	
@actionscript.route('/actionscript-software-developer-jobs-nivala')
def actionscript_software_developer88(page=1):

    job_list = job_obj.get_job("actionscript software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="nivala")
	
@actionscript.route('/actionscript-software-developer-jobs-joutseno')
def actionscript_software_developer89(page=1):

    job_list = job_obj.get_job("actionscript software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="joutseno")
	
@actionscript.route('/actionscript-software-developer-jobs-pedersore')
def actionscript_software_developer90(page=1):

    job_list = job_obj.get_job("actionscript software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="pedersore")
	
@actionscript.route('/actionscript-software-developer-jobs-sotkamo')
def actionscript_software_developer91(page=1):

    job_list = job_obj.get_job("actionscript software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="sotkamo")
	
@actionscript.route('/actionscript-software-developer-jobs-kuhmo')
def actionscript_software_developer92(page=1):

    job_list = job_obj.get_job("actionscript software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="kuhmo")
	
@actionscript.route('/actionscript-software-developer-jobs-paimio')
def actionscript_software_developer93(page=1):

    job_list = job_obj.get_job("actionscript software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="paimio")
	
@actionscript.route('/actionscript-software-developer-jobs-saarijarvi')
def actionscript_software_developer94(page=1):

    job_list = job_obj.get_job("actionscript software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="saarijarvi")
	
@actionscript.route('/actionscript-software-developer-jobs-helsinki')
def actionscript_software_developer95(page=1):

    job_list = job_obj.get_job("actionscript software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="actionscript software developer", location="helsinki")


####################################################################

