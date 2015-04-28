from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

cobol = Blueprint('cobol', __name__)
job_obj = Job()



####################################################################


@cobol.route('/cobol_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "cobol" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def cobol_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="espoo")

@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def cobol_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="tampere")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def cobol_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="vantaa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def cobol_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="turku")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def cobol_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="oulu")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def cobol_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="lahti")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def cobol_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kuopio")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def cobol_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="jyvvaskyla")

@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def cobol_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="pori")

@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def cobol_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="lappeenranta")	
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def cobol_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="vaasa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def cobol_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kotka")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def cobol_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="joensuu")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def cobol_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="hameenlinna")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def cobol_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="porvoo")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def cobol_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="mikkeli")

@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def cobol_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="hyvinkaa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def cobol_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="nurmijarvi")

@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def cobol_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="jarvenpaa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def cobol_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="rauma")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def cobol_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="lohja")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def cobol_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="karleby")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def cobol_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kajaani")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def cobol_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="rovaniemi")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def cobol_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="tuusula")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def cobol_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kirkkonummi")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def cobol_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="seinajoki")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def cobol_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kerava")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def cobol_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kouvola")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def cobol_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="imatra")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def cobol_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="nokia")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def cobol_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="savonlinna")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def cobol_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="riihimaki")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def cobol_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="vihti")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def cobol_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="salo")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def cobol_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kangasala")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def cobol_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="raisio")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def cobol_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="karhula")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def cobol_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kemi")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def cobol_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="iisalmi")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def cobol_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="varkaus")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def cobol_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="raahe")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def cobol_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="ylojarvi")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def cobol_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="hamina")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def cobol_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kaarina")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def cobol_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="tornio")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def cobol_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="heinola")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def cobol_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="hollola")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def cobol_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="valkeakoski")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def cobol_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="siilinjarvi")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def cobol_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kuusankoski")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def cobol_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="sibbo")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def cobol_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="jakostad")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def cobol_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="lempaala")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def cobol_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="mantsala")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def cobol_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="forssa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def cobol_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kuusamo")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def cobol_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="haukipudas")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def cobol_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="korsholm")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def cobol_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="laukaa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def cobol_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="anjala")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def cobol_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="uusikaupunki")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def cobol_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="janakkala")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def cobol_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="pirkkala")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def cobol_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def cobol_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="jamsa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def cobol_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="jamsa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def cobol_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="vammala")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def cobol_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="nastola")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def cobol_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="orimattila")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def cobol_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kauhajoki")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def cobol_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="ekenas")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def cobol_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kempele")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def cobol_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="lapua")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def cobol_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="lieksa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def cobol_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="naantali")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def cobol_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="aanekoski")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def cobol_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="ylivieska")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def cobol_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kontiolahti")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def cobol_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kankaanpaa")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def cobol_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="ulvila")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def cobol_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="pieksamaki")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def cobol_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kiiminki")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def cobol_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="pargas")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def cobol_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="nurmo")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def cobol_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="ilmajoki")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def cobol_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="liperi")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def cobol_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="keuruu")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def cobol_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="leppavirta")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def cobol_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kurikka")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def cobol_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="nivala")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def cobol_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="joutseno")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def cobol_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="pedersore")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def cobol_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="sotkamo")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def cobol_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="kuhmo")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def cobol_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="paimio")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def cobol_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="saarijarvi")
	
@cobol.route('/cobol-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def cobol_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("cobol ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@cobol.route('/cobol-software-developer-jobs-espoo')
def cobol_software_developer2(page=1):

    job_list = job_obj.get_job("cobol software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="espoo")

@cobol.route('/cobol-software-developer-jobs-tampere')
def cobol_software_developer3(page=1):

    job_list = job_obj.get_job("cobol software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="tampere")
	
@cobol.route('/cobol-software-developer-jobs-vantaa')
def cobol_software_developer4(page=1):

    job_list = job_obj.get_job("cobol software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="vantaa")
	
@cobol.route('/cobol-software-developer-jobs-turku')
def cobol_software_developer5(page=1):

    job_list = job_obj.get_job("cobol software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="turku")
	
@cobol.route('/cobol-software-developer-jobs-oulu')
def cobol_software_developer6(page=1):

    job_list = job_obj.get_job("cobol software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="oulu")
	
@cobol.route('/cobol-software-developer-jobs-lahti')
def cobol_software_developer7(page=1):

    job_list = job_obj.get_job("cobol software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="lahti")
	
@cobol.route('/cobol-software-developer-jobs-kuopio')
def cobol_software_developer8(page=1):

    job_list = job_obj.get_job("cobol software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kuopio")
	
@cobol.route('/cobol-software-developer-jobs-jyvvaskyla')
def cobol_software_developer9(page=1):

    job_list = job_obj.get_job("cobol software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="jyvvaskyla")

@cobol.route('/cobol-software-developer-jobs-pori')
def cobol_software_developer10(page=1):

    job_list = job_obj.get_job("cobol software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="pori")

@cobol.route('/cobol-software-developer-jobs-lappeenranta')
def cobol_software_developer11(page=1):

    job_list = job_obj.get_job("cobol software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="lappeenranta")	
	
@cobol.route('/cobol-software-developer-jobs-vaasa')
def cobol_software_developer12(page=1):

    job_list = job_obj.get_job("cobol software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="vaasa")
	
@cobol.route('/cobol-software-developer-jobs-kotka')
def cobol_software_developer13(page=1):

    job_list = job_obj.get_job("cobol software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kotka")
	
@cobol.route('/cobol-software-developer-jobs-joensuu')
def cobol_software_developer14(page=1):

    job_list = job_obj.get_job("cobol software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="joensuu")
	
@cobol.route('/cobol-software-developer-jobs-hameenlinna')
def cobol_software_developer15(page=1):

    job_list = job_obj.get_job("cobol software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="hameenlinna")
	
@cobol.route('/cobol-software-developer-jobs-porvoo')
def cobol_software_developer16(page=1):

    job_list = job_obj.get_job("cobol software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="porvoo")
	
@cobol.route('/cobol-software-developer-jobs-mikkeli')
def cobol_software_developer17(page=1):

    job_list = job_obj.get_job("cobol software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="mikkeli")

@cobol.route('/cobol-software-developer-jobs-hyvinkaa')
def cobol_software_developer18(page=1):

    job_list = job_obj.get_job("cobol software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="hyvinkaa")
	
@cobol.route('/cobol-software-developer-jobs-nurmijarvi')
def cobol_software_developer19(page=1):

    job_list = job_obj.get_job("cobol software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="nurmijarvi")

@cobol.route('/cobol-software-developer-jobs-jarvenpaa')
def cobol_software_developer20(page=1):

    job_list = job_obj.get_job("cobol software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="jarvenpaa")
	
@cobol.route('/cobol-software-developer-jobs-rauma')
def cobol_software_developer21(page=1):

    job_list = job_obj.get_job("cobol software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="rauma")
	
@cobol.route('/cobol-software-developer-jobs-lohja')
def cobol_software_developer22(page=1):

    job_list = job_obj.get_job("cobol software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="lohja")
	
@cobol.route('/cobol-software-developer-jobs-karleby')
def cobol_software_developer23(page=1):

    job_list = job_obj.get_job("cobol software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="karleby")
	
@cobol.route('/cobol-software-developer-jobs-kajaani')
def cobol_software_developer24(page=1):

    job_list = job_obj.get_job("cobol software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kajaani")
	
@cobol.route('/cobol-software-developer-jobs-rovaniemi')
def cobol_software_developer25(page=1):

    job_list = job_obj.get_job("cobol software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="rovaniemi")
	
@cobol.route('/cobol-software-developer-jobs-tuusula')
def cobol_software_developer26(page=1):

    job_list = job_obj.get_job("cobol software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="tuusula")
	
@cobol.route('/cobol-software-developer-jobs-kirkkonummi')
def cobol_software_developer27(page=1):

    job_list = job_obj.get_job("cobol software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kirkkonummi")
	
@cobol.route('/cobol-software-developer-jobs-seinajoki')
def cobol_software_developer28(page=1):

    job_list = job_obj.get_job("cobol software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="seinajoki")
	
@cobol.route('/cobol-software-developer-jobs-kerava')
def cobol_software_developer29(page=1):

    job_list = job_obj.get_job("cobol software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kerava")
	
@cobol.route('/cobol-software-developer-jobs-kouvola')
def cobol_software_developer30(page=1):

    job_list = job_obj.get_job("cobol software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kouvola")
	
@cobol.route('/cobol-software-developer-jobs-imatra')
def cobol_software_developer31(page=1):

    job_list = job_obj.get_job("cobol software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="imatra")
	
@cobol.route('/cobol-software-developer-jobs-nokia')
def cobol_software_developer32_1(page=1):

    job_list = job_obj.get_job("cobol software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="nokia")
	
@cobol.route('/cobol-software-developer-jobs-savonlinna')
def cobol_software_developer32(page=1):

    job_list = job_obj.get_job("cobol software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="savonlinna")
	
@cobol.route('/cobol-software-developer-jobs-riihimaki')
def cobol_software_developer33(page=1):

    job_list = job_obj.get_job("cobol software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="riihimaki")
	
@cobol.route('/cobol-software-developer-jobs-vihti')
def cobol_software_developer34(page=1):

    job_list = job_obj.get_job("cobol software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="vihti")
	
@cobol.route('/cobol-software-developer-jobs-salo')
def cobol_software_developer35(page=1):

    job_list = job_obj.get_job("cobol software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="salo")
	
@cobol.route('/cobol-software-developer-jobs-kangasala')
def cobol_software_developer36(page=1):

    job_list = job_obj.get_job("cobol software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kangasala")
	
@cobol.route('/cobol-software-developer-jobs-raisio')
def cobol_software_developer37_1(page=1):

    job_list = job_obj.get_job("cobol software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="raisio")
	
@cobol.route('/cobol-software-developer-jobs-karhula')
def cobol_software_developer37(page=1):

    job_list = job_obj.get_job("cobol software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="karhula")
	
@cobol.route('/cobol-software-developer-jobs-kemi')
def cobol_software_developer38(page=1):

    job_list = job_obj.get_job("cobol software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kemi")
	
@cobol.route('/cobol-software-developer-jobs-iisalmi')
def cobol_software_developer39(page=1):

    job_list = job_obj.get_job("cobol software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="iisalmi")
	
@cobol.route('/cobol-software-developer-jobs-varkaus')
def cobol_software_developer40(page=1):

    job_list = job_obj.get_job("cobol software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="varkaus")
	
@cobol.route('/cobol-software-developer-jobs-raahe')
def cobol_software_developer41(page=1):

    job_list = job_obj.get_job("cobol software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="raahe")
	
@cobol.route('/cobol-software-developer-jobs-ylojarvi')
def cobol_software_developer42_1(page=1):

    job_list = job_obj.get_job("cobol software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="ylojarvi")
	
@cobol.route('/cobol-software-developer-jobs-hamina')
def cobol_software_developer42(page=1):

    job_list = job_obj.get_job("cobol software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="hamina")
	
@cobol.route('/cobol-software-developer-jobs-kaarina')
def cobol_software_developer43(page=1):

    job_list = job_obj.get_job("cobol software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kaarina")
	
@cobol.route('/cobol-software-developer-jobs-tornio')
def cobol_software_developer44(page=1):

    job_list = job_obj.get_job("cobol software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="tornio")
	
@cobol.route('/cobol-software-developer-jobs-heinola')
def cobol_software_developer45(page=1):

    job_list = job_obj.get_job("cobol software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="heinola")
	
@cobol.route('/cobol-software-developer-jobs-hollola')
def cobol_software_developer46(page=1):

    job_list = job_obj.get_job("cobol software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="hollola")
	
@cobol.route('/cobol-software-developer-jobs-valkeakoski')
def cobol_software_developer47(page=1):

    job_list = job_obj.get_job("cobol software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="valkeakoski")
	
@cobol.route('/cobol-software-developer-jobs-siilinjarvi')
def cobol_software_developer48(page=1):

    job_list = job_obj.get_job("cobol software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="siilinjarvi")
	
@cobol.route('/cobol-software-developer-jobs-kuusankoski')
def cobol_software_developer49(page=1):

    job_list = job_obj.get_job("cobol software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kuusankoski")
	
@cobol.route('/cobol-software-developer-jobs-sibbo')
def cobol_software_developer50(page=1):

    job_list = job_obj.get_job("cobol software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="sibbo")
	
@cobol.route('/cobol-software-developer-jobs-jakostad')
def cobol_software_developer51(page=1):

    job_list = job_obj.get_job("cobol software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="jakostad")
	
@cobol.route('/cobol-software-developer-jobs-lempaala')
def cobol_software_developer52(page=1):

    job_list = job_obj.get_job("cobol software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="lempaala")
	
@cobol.route('/cobol-software-developer-jobs-mantsala')
def cobol_software_developer52_1(page=1):

    job_list = job_obj.get_job("cobol software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="mantsala")
	
@cobol.route('/cobol-software-developer-jobs-forssa')
def cobol_software_developer53(page=1):

    job_list = job_obj.get_job("cobol software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="forssa")
	
@cobol.route('/cobol-software-developer-jobs-kuusamo')
def cobol_software_developer54(page=1):

    job_list = job_obj.get_job("cobol software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kuusamo")
	
@cobol.route('/cobol-software-developer-jobs-haukipudas')
def cobol_software_developer55(page=1):

    job_list = job_obj.get_job("cobol software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="haukipudas")
	
@cobol.route('/cobol-software-developer-jobs-korsholm')
def cobol_software_developer56(page=1):

    job_list = job_obj.get_job("cobol software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="korsholm")
	
@cobol.route('/cobol-software-developer-jobs-laukaa')
def cobol_software_developer57(page=1):

    job_list = job_obj.get_job("cobol software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="laukaa")
	
@cobol.route('/cobol-software-developer-jobs-anjala')
def cobol_software_developer58(page=1):

    job_list = job_obj.get_job("cobol software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="anjala")
	
@cobol.route('/cobol-software-developer-jobs-uusikaupunki')
def cobol_software_developer59(page=1):

    job_list = job_obj.get_job("cobol software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="uusikaupunki")
	
@cobol.route('/cobol-software-developer-jobs-janakkala')
def cobol_software_developer60(page=1):

    job_list = job_obj.get_job("cobol software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="janakkala")
	
@cobol.route('/cobol-software-developer-jobs-pirkkala')
def cobol_software_developer61(page=1):

    job_list = job_obj.get_job("cobol software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="pirkkala")
	
@cobol.route('/cobol-software-developer-jobs-lansi-turunmaa')
def cobol_software_developer62(page=1):

    job_list = job_obj.get_job("cobol software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="lansi-turunmaa")
	
@cobol.route('/cobol-software-developer-jobs-jamsa')
def cobol_software_developer63(page=1):

    job_list = job_obj.get_job("cobol software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="jamsa")
	
@cobol.route('/cobol-software-developer-jobs-jamsa')
def cobol_software_developer64(page=1):

    job_list = job_obj.get_job("cobol software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="jamsa")
	
@cobol.route('/cobol-software-developer-jobs-vammala')
def cobol_software_developer65(page=1):

    job_list = job_obj.get_job("cobol software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="vammala")
	
@cobol.route('/cobol-software-developer-jobs-nastola')
def cobol_software_developer66(page=1):

    job_list = job_obj.get_job("cobol software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="nastola")
	
@cobol.route('/cobol-software-developer-jobs-orimattila')
def cobol_software_developer67(page=1):

    job_list = job_obj.get_job("cobol software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="orimattila")
	
@cobol.route('/cobol-software-developer-jobs-kauhajoki')
def cobol_software_developer68(page=1):

    job_list = job_obj.get_job("cobol software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kauhajoki")
	
@cobol.route('/cobol-software-developer-jobs-ekenas')
def cobol_software_developer69(page=1):

    job_list = job_obj.get_job("cobol software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="ekenas")
	
@cobol.route('/cobol-software-developer-jobs-kempele')
def cobol_software_developer70(page=1):

    job_list = job_obj.get_job("cobol software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kempele")
	
@cobol.route('/cobol-software-developer-jobs-lapua')
def cobol_software_developer71(page=1):

    job_list = job_obj.get_job("cobol software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="lapua")
	
@cobol.route('/cobol-software-developer-jobs-lieksa')
def cobol_software_developer72(page=1):

    job_list = job_obj.get_job("cobol software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="lieksa")
	
@cobol.route('/cobol-software-developer-jobs-naantali')
def cobol_software_developer73(page=1):

    job_list = job_obj.get_job("cobol software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="naantali")
	
@cobol.route('/cobol-software-developer-jobs-aanekoski')
def cobol_software_developer74(page=1):

    job_list = job_obj.get_job("cobol software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="aanekoski")
	
@cobol.route('/cobol-software-developer-jobs-ylivieska')
def cobol_software_developer75(page=1):

    job_list = job_obj.get_job("cobol software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="ylivieska")
	
@cobol.route('/cobol-software-developer-jobs-kontiolahti')
def cobol_software_developer76(page=1):

    job_list = job_obj.get_job("cobol software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kontiolahti")
	
@cobol.route('/cobol-software-developer-jobs-kankaanpaa')
def cobol_software_developer77(page=1):

    job_list = job_obj.get_job("cobol software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kankaanpaa")
	
@cobol.route('/cobol-software-developer-jobs-ulvila')
def cobol_software_developer78(page=1):

    job_list = job_obj.get_job("cobol software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="ulvila")
	
@cobol.route('/cobol-software-developer-jobs-pieksamaki')
def cobol_software_developer79(page=1):

    job_list = job_obj.get_job("cobol software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="pieksamaki")
	
@cobol.route('/cobol-software-developer-jobs-kiiminki')
def cobol_software_developer80(page=1):

    job_list = job_obj.get_job("cobol software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kiiminki")
	
@cobol.route('/cobol-software-developer-jobs-pargas')
def cobol_software_developer81(page=1):

    job_list = job_obj.get_job("cobol software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="pargas")
	
@cobol.route('/cobol-software-developer-jobs-nurmo')
def cobol_software_developer82(page=1):

    job_list = job_obj.get_job("cobol software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="nurmo")
	
@cobol.route('/cobol-software-developer-jobs-ilmajoki')
def cobol_software_developer83(page=1):

    job_list = job_obj.get_job("cobol software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="ilmajoki")
	
@cobol.route('/cobol-software-developer-jobs-liperi')
def cobol_software_developer84(page=1):

    job_list = job_obj.get_job("cobol software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="liperi")
	
@cobol.route('/cobol-software-developer-jobs-keuruu')
def cobol_software_developer85(page=1):

    job_list = job_obj.get_job("cobol software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="keuruu")
	
@cobol.route('/cobol-software-developer-jobs-leppavirta')
def cobol_software_developer86(page=1):

    job_list = job_obj.get_job("cobol software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="leppavirta")
	
@cobol.route('/cobol-software-developer-jobs-kurikka')
def cobol_software_developer87(page=1):

    job_list = job_obj.get_job("cobol software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kurikka")
	
@cobol.route('/cobol-software-developer-jobs-nivala')
def cobol_software_developer88(page=1):

    job_list = job_obj.get_job("cobol software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="nivala")
	
@cobol.route('/cobol-software-developer-jobs-joutseno')
def cobol_software_developer89(page=1):

    job_list = job_obj.get_job("cobol software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="joutseno")
	
@cobol.route('/cobol-software-developer-jobs-pedersore')
def cobol_software_developer90(page=1):

    job_list = job_obj.get_job("cobol software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="pedersore")
	
@cobol.route('/cobol-software-developer-jobs-sotkamo')
def cobol_software_developer91(page=1):

    job_list = job_obj.get_job("cobol software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="sotkamo")
	
@cobol.route('/cobol-software-developer-jobs-kuhmo')
def cobol_software_developer92(page=1):

    job_list = job_obj.get_job("cobol software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="kuhmo")
	
@cobol.route('/cobol-software-developer-jobs-paimio')
def cobol_software_developer93(page=1):

    job_list = job_obj.get_job("cobol software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="paimio")
	
@cobol.route('/cobol-software-developer-jobs-saarijarvi')
def cobol_software_developer94(page=1):

    job_list = job_obj.get_job("cobol software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="saarijarvi")
	
@cobol.route('/cobol-software-developer-jobs-helsinki')
def cobol_software_developer95(page=1):

    job_list = job_obj.get_job("cobol software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="cobol software developer", location="helsinki")


####################################################################

