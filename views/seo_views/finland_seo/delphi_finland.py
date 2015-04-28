from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

delphi = Blueprint('delphi', __name__)
job_obj = Job()



####################################################################


@delphi.route('/delphi_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "delphi" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def delphi_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="espoo")

@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def delphi_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="tampere")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def delphi_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="vantaa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def delphi_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="turku")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def delphi_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="oulu")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def delphi_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="lahti")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def delphi_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kuopio")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def delphi_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="jyvvaskyla")

@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def delphi_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="pori")

@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def delphi_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="lappeenranta")	
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def delphi_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="vaasa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def delphi_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kotka")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def delphi_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="joensuu")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def delphi_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="hameenlinna")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def delphi_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="porvoo")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def delphi_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="mikkeli")

@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def delphi_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="hyvinkaa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def delphi_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="nurmijarvi")

@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def delphi_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="jarvenpaa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def delphi_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="rauma")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def delphi_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="lohja")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def delphi_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="karleby")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def delphi_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kajaani")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def delphi_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="rovaniemi")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def delphi_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="tuusula")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def delphi_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kirkkonummi")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def delphi_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="seinajoki")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def delphi_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kerava")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def delphi_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kouvola")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def delphi_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="imatra")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def delphi_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="nokia")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def delphi_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="savonlinna")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def delphi_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="riihimaki")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def delphi_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="vihti")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def delphi_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="salo")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def delphi_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kangasala")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def delphi_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="raisio")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def delphi_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="karhula")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def delphi_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kemi")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def delphi_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="iisalmi")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def delphi_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="varkaus")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def delphi_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="raahe")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def delphi_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="ylojarvi")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def delphi_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="hamina")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def delphi_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kaarina")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def delphi_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="tornio")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def delphi_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="heinola")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def delphi_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="hollola")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def delphi_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="valkeakoski")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def delphi_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="siilinjarvi")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def delphi_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kuusankoski")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def delphi_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="sibbo")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def delphi_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="jakostad")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def delphi_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="lempaala")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def delphi_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="mantsala")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def delphi_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="forssa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def delphi_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kuusamo")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def delphi_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="haukipudas")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def delphi_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="korsholm")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def delphi_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="laukaa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def delphi_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="anjala")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def delphi_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="uusikaupunki")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def delphi_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="janakkala")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def delphi_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="pirkkala")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def delphi_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def delphi_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="jamsa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def delphi_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="jamsa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def delphi_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="vammala")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def delphi_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="nastola")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def delphi_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="orimattila")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def delphi_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kauhajoki")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def delphi_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="ekenas")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def delphi_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kempele")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def delphi_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="lapua")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def delphi_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="lieksa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def delphi_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="naantali")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def delphi_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="aanekoski")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def delphi_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="ylivieska")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def delphi_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kontiolahti")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def delphi_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kankaanpaa")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def delphi_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="ulvila")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def delphi_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="pieksamaki")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def delphi_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kiiminki")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def delphi_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="pargas")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def delphi_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="nurmo")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def delphi_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="ilmajoki")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def delphi_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="liperi")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def delphi_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="keuruu")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def delphi_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="leppavirta")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def delphi_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kurikka")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def delphi_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="nivala")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def delphi_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="joutseno")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def delphi_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="pedersore")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def delphi_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="sotkamo")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def delphi_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="kuhmo")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def delphi_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="paimio")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def delphi_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="saarijarvi")
	
@delphi.route('/delphi-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def delphi_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("delphi ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@delphi.route('/delphi-software-developer-jobs-espoo')
def delphi_software_developer2(page=1):

    job_list = job_obj.get_job("delphi software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="espoo")

@delphi.route('/delphi-software-developer-jobs-tampere')
def delphi_software_developer3(page=1):

    job_list = job_obj.get_job("delphi software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="tampere")
	
@delphi.route('/delphi-software-developer-jobs-vantaa')
def delphi_software_developer4(page=1):

    job_list = job_obj.get_job("delphi software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="vantaa")
	
@delphi.route('/delphi-software-developer-jobs-turku')
def delphi_software_developer5(page=1):

    job_list = job_obj.get_job("delphi software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="turku")
	
@delphi.route('/delphi-software-developer-jobs-oulu')
def delphi_software_developer6(page=1):

    job_list = job_obj.get_job("delphi software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="oulu")
	
@delphi.route('/delphi-software-developer-jobs-lahti')
def delphi_software_developer7(page=1):

    job_list = job_obj.get_job("delphi software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="lahti")
	
@delphi.route('/delphi-software-developer-jobs-kuopio')
def delphi_software_developer8(page=1):

    job_list = job_obj.get_job("delphi software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kuopio")
	
@delphi.route('/delphi-software-developer-jobs-jyvvaskyla')
def delphi_software_developer9(page=1):

    job_list = job_obj.get_job("delphi software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="jyvvaskyla")

@delphi.route('/delphi-software-developer-jobs-pori')
def delphi_software_developer10(page=1):

    job_list = job_obj.get_job("delphi software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="pori")

@delphi.route('/delphi-software-developer-jobs-lappeenranta')
def delphi_software_developer11(page=1):

    job_list = job_obj.get_job("delphi software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="lappeenranta")	
	
@delphi.route('/delphi-software-developer-jobs-vaasa')
def delphi_software_developer12(page=1):

    job_list = job_obj.get_job("delphi software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="vaasa")
	
@delphi.route('/delphi-software-developer-jobs-kotka')
def delphi_software_developer13(page=1):

    job_list = job_obj.get_job("delphi software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kotka")
	
@delphi.route('/delphi-software-developer-jobs-joensuu')
def delphi_software_developer14(page=1):

    job_list = job_obj.get_job("delphi software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="joensuu")
	
@delphi.route('/delphi-software-developer-jobs-hameenlinna')
def delphi_software_developer15(page=1):

    job_list = job_obj.get_job("delphi software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="hameenlinna")
	
@delphi.route('/delphi-software-developer-jobs-porvoo')
def delphi_software_developer16(page=1):

    job_list = job_obj.get_job("delphi software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="porvoo")
	
@delphi.route('/delphi-software-developer-jobs-mikkeli')
def delphi_software_developer17(page=1):

    job_list = job_obj.get_job("delphi software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="mikkeli")

@delphi.route('/delphi-software-developer-jobs-hyvinkaa')
def delphi_software_developer18(page=1):

    job_list = job_obj.get_job("delphi software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="hyvinkaa")
	
@delphi.route('/delphi-software-developer-jobs-nurmijarvi')
def delphi_software_developer19(page=1):

    job_list = job_obj.get_job("delphi software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="nurmijarvi")

@delphi.route('/delphi-software-developer-jobs-jarvenpaa')
def delphi_software_developer20(page=1):

    job_list = job_obj.get_job("delphi software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="jarvenpaa")
	
@delphi.route('/delphi-software-developer-jobs-rauma')
def delphi_software_developer21(page=1):

    job_list = job_obj.get_job("delphi software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="rauma")
	
@delphi.route('/delphi-software-developer-jobs-lohja')
def delphi_software_developer22(page=1):

    job_list = job_obj.get_job("delphi software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="lohja")
	
@delphi.route('/delphi-software-developer-jobs-karleby')
def delphi_software_developer23(page=1):

    job_list = job_obj.get_job("delphi software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="karleby")
	
@delphi.route('/delphi-software-developer-jobs-kajaani')
def delphi_software_developer24(page=1):

    job_list = job_obj.get_job("delphi software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kajaani")
	
@delphi.route('/delphi-software-developer-jobs-rovaniemi')
def delphi_software_developer25(page=1):

    job_list = job_obj.get_job("delphi software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="rovaniemi")
	
@delphi.route('/delphi-software-developer-jobs-tuusula')
def delphi_software_developer26(page=1):

    job_list = job_obj.get_job("delphi software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="tuusula")
	
@delphi.route('/delphi-software-developer-jobs-kirkkonummi')
def delphi_software_developer27(page=1):

    job_list = job_obj.get_job("delphi software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kirkkonummi")
	
@delphi.route('/delphi-software-developer-jobs-seinajoki')
def delphi_software_developer28(page=1):

    job_list = job_obj.get_job("delphi software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="seinajoki")
	
@delphi.route('/delphi-software-developer-jobs-kerava')
def delphi_software_developer29(page=1):

    job_list = job_obj.get_job("delphi software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kerava")
	
@delphi.route('/delphi-software-developer-jobs-kouvola')
def delphi_software_developer30(page=1):

    job_list = job_obj.get_job("delphi software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kouvola")
	
@delphi.route('/delphi-software-developer-jobs-imatra')
def delphi_software_developer31(page=1):

    job_list = job_obj.get_job("delphi software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="imatra")
	
@delphi.route('/delphi-software-developer-jobs-nokia')
def delphi_software_developer32_1(page=1):

    job_list = job_obj.get_job("delphi software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="nokia")
	
@delphi.route('/delphi-software-developer-jobs-savonlinna')
def delphi_software_developer32(page=1):

    job_list = job_obj.get_job("delphi software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="savonlinna")
	
@delphi.route('/delphi-software-developer-jobs-riihimaki')
def delphi_software_developer33(page=1):

    job_list = job_obj.get_job("delphi software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="riihimaki")
	
@delphi.route('/delphi-software-developer-jobs-vihti')
def delphi_software_developer34(page=1):

    job_list = job_obj.get_job("delphi software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="vihti")
	
@delphi.route('/delphi-software-developer-jobs-salo')
def delphi_software_developer35(page=1):

    job_list = job_obj.get_job("delphi software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="salo")
	
@delphi.route('/delphi-software-developer-jobs-kangasala')
def delphi_software_developer36(page=1):

    job_list = job_obj.get_job("delphi software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kangasala")
	
@delphi.route('/delphi-software-developer-jobs-raisio')
def delphi_software_developer37_1(page=1):

    job_list = job_obj.get_job("delphi software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="raisio")
	
@delphi.route('/delphi-software-developer-jobs-karhula')
def delphi_software_developer37(page=1):

    job_list = job_obj.get_job("delphi software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="karhula")
	
@delphi.route('/delphi-software-developer-jobs-kemi')
def delphi_software_developer38(page=1):

    job_list = job_obj.get_job("delphi software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kemi")
	
@delphi.route('/delphi-software-developer-jobs-iisalmi')
def delphi_software_developer39(page=1):

    job_list = job_obj.get_job("delphi software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="iisalmi")
	
@delphi.route('/delphi-software-developer-jobs-varkaus')
def delphi_software_developer40(page=1):

    job_list = job_obj.get_job("delphi software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="varkaus")
	
@delphi.route('/delphi-software-developer-jobs-raahe')
def delphi_software_developer41(page=1):

    job_list = job_obj.get_job("delphi software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="raahe")
	
@delphi.route('/delphi-software-developer-jobs-ylojarvi')
def delphi_software_developer42_1(page=1):

    job_list = job_obj.get_job("delphi software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="ylojarvi")
	
@delphi.route('/delphi-software-developer-jobs-hamina')
def delphi_software_developer42(page=1):

    job_list = job_obj.get_job("delphi software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="hamina")
	
@delphi.route('/delphi-software-developer-jobs-kaarina')
def delphi_software_developer43(page=1):

    job_list = job_obj.get_job("delphi software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kaarina")
	
@delphi.route('/delphi-software-developer-jobs-tornio')
def delphi_software_developer44(page=1):

    job_list = job_obj.get_job("delphi software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="tornio")
	
@delphi.route('/delphi-software-developer-jobs-heinola')
def delphi_software_developer45(page=1):

    job_list = job_obj.get_job("delphi software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="heinola")
	
@delphi.route('/delphi-software-developer-jobs-hollola')
def delphi_software_developer46(page=1):

    job_list = job_obj.get_job("delphi software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="hollola")
	
@delphi.route('/delphi-software-developer-jobs-valkeakoski')
def delphi_software_developer47(page=1):

    job_list = job_obj.get_job("delphi software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="valkeakoski")
	
@delphi.route('/delphi-software-developer-jobs-siilinjarvi')
def delphi_software_developer48(page=1):

    job_list = job_obj.get_job("delphi software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="siilinjarvi")
	
@delphi.route('/delphi-software-developer-jobs-kuusankoski')
def delphi_software_developer49(page=1):

    job_list = job_obj.get_job("delphi software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kuusankoski")
	
@delphi.route('/delphi-software-developer-jobs-sibbo')
def delphi_software_developer50(page=1):

    job_list = job_obj.get_job("delphi software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="sibbo")
	
@delphi.route('/delphi-software-developer-jobs-jakostad')
def delphi_software_developer51(page=1):

    job_list = job_obj.get_job("delphi software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="jakostad")
	
@delphi.route('/delphi-software-developer-jobs-lempaala')
def delphi_software_developer52(page=1):

    job_list = job_obj.get_job("delphi software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="lempaala")
	
@delphi.route('/delphi-software-developer-jobs-mantsala')
def delphi_software_developer52_1(page=1):

    job_list = job_obj.get_job("delphi software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="mantsala")
	
@delphi.route('/delphi-software-developer-jobs-forssa')
def delphi_software_developer53(page=1):

    job_list = job_obj.get_job("delphi software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="forssa")
	
@delphi.route('/delphi-software-developer-jobs-kuusamo')
def delphi_software_developer54(page=1):

    job_list = job_obj.get_job("delphi software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kuusamo")
	
@delphi.route('/delphi-software-developer-jobs-haukipudas')
def delphi_software_developer55(page=1):

    job_list = job_obj.get_job("delphi software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="haukipudas")
	
@delphi.route('/delphi-software-developer-jobs-korsholm')
def delphi_software_developer56(page=1):

    job_list = job_obj.get_job("delphi software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="korsholm")
	
@delphi.route('/delphi-software-developer-jobs-laukaa')
def delphi_software_developer57(page=1):

    job_list = job_obj.get_job("delphi software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="laukaa")
	
@delphi.route('/delphi-software-developer-jobs-anjala')
def delphi_software_developer58(page=1):

    job_list = job_obj.get_job("delphi software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="anjala")
	
@delphi.route('/delphi-software-developer-jobs-uusikaupunki')
def delphi_software_developer59(page=1):

    job_list = job_obj.get_job("delphi software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="uusikaupunki")
	
@delphi.route('/delphi-software-developer-jobs-janakkala')
def delphi_software_developer60(page=1):

    job_list = job_obj.get_job("delphi software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="janakkala")
	
@delphi.route('/delphi-software-developer-jobs-pirkkala')
def delphi_software_developer61(page=1):

    job_list = job_obj.get_job("delphi software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="pirkkala")
	
@delphi.route('/delphi-software-developer-jobs-lansi-turunmaa')
def delphi_software_developer62(page=1):

    job_list = job_obj.get_job("delphi software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="lansi-turunmaa")
	
@delphi.route('/delphi-software-developer-jobs-jamsa')
def delphi_software_developer63(page=1):

    job_list = job_obj.get_job("delphi software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="jamsa")
	
@delphi.route('/delphi-software-developer-jobs-jamsa')
def delphi_software_developer64(page=1):

    job_list = job_obj.get_job("delphi software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="jamsa")
	
@delphi.route('/delphi-software-developer-jobs-vammala')
def delphi_software_developer65(page=1):

    job_list = job_obj.get_job("delphi software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="vammala")
	
@delphi.route('/delphi-software-developer-jobs-nastola')
def delphi_software_developer66(page=1):

    job_list = job_obj.get_job("delphi software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="nastola")
	
@delphi.route('/delphi-software-developer-jobs-orimattila')
def delphi_software_developer67(page=1):

    job_list = job_obj.get_job("delphi software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="orimattila")
	
@delphi.route('/delphi-software-developer-jobs-kauhajoki')
def delphi_software_developer68(page=1):

    job_list = job_obj.get_job("delphi software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kauhajoki")
	
@delphi.route('/delphi-software-developer-jobs-ekenas')
def delphi_software_developer69(page=1):

    job_list = job_obj.get_job("delphi software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="ekenas")
	
@delphi.route('/delphi-software-developer-jobs-kempele')
def delphi_software_developer70(page=1):

    job_list = job_obj.get_job("delphi software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kempele")
	
@delphi.route('/delphi-software-developer-jobs-lapua')
def delphi_software_developer71(page=1):

    job_list = job_obj.get_job("delphi software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="lapua")
	
@delphi.route('/delphi-software-developer-jobs-lieksa')
def delphi_software_developer72(page=1):

    job_list = job_obj.get_job("delphi software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="lieksa")
	
@delphi.route('/delphi-software-developer-jobs-naantali')
def delphi_software_developer73(page=1):

    job_list = job_obj.get_job("delphi software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="naantali")
	
@delphi.route('/delphi-software-developer-jobs-aanekoski')
def delphi_software_developer74(page=1):

    job_list = job_obj.get_job("delphi software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="aanekoski")
	
@delphi.route('/delphi-software-developer-jobs-ylivieska')
def delphi_software_developer75(page=1):

    job_list = job_obj.get_job("delphi software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="ylivieska")
	
@delphi.route('/delphi-software-developer-jobs-kontiolahti')
def delphi_software_developer76(page=1):

    job_list = job_obj.get_job("delphi software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kontiolahti")
	
@delphi.route('/delphi-software-developer-jobs-kankaanpaa')
def delphi_software_developer77(page=1):

    job_list = job_obj.get_job("delphi software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kankaanpaa")
	
@delphi.route('/delphi-software-developer-jobs-ulvila')
def delphi_software_developer78(page=1):

    job_list = job_obj.get_job("delphi software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="ulvila")
	
@delphi.route('/delphi-software-developer-jobs-pieksamaki')
def delphi_software_developer79(page=1):

    job_list = job_obj.get_job("delphi software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="pieksamaki")
	
@delphi.route('/delphi-software-developer-jobs-kiiminki')
def delphi_software_developer80(page=1):

    job_list = job_obj.get_job("delphi software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kiiminki")
	
@delphi.route('/delphi-software-developer-jobs-pargas')
def delphi_software_developer81(page=1):

    job_list = job_obj.get_job("delphi software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="pargas")
	
@delphi.route('/delphi-software-developer-jobs-nurmo')
def delphi_software_developer82(page=1):

    job_list = job_obj.get_job("delphi software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="nurmo")
	
@delphi.route('/delphi-software-developer-jobs-ilmajoki')
def delphi_software_developer83(page=1):

    job_list = job_obj.get_job("delphi software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="ilmajoki")
	
@delphi.route('/delphi-software-developer-jobs-liperi')
def delphi_software_developer84(page=1):

    job_list = job_obj.get_job("delphi software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="liperi")
	
@delphi.route('/delphi-software-developer-jobs-keuruu')
def delphi_software_developer85(page=1):

    job_list = job_obj.get_job("delphi software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="keuruu")
	
@delphi.route('/delphi-software-developer-jobs-leppavirta')
def delphi_software_developer86(page=1):

    job_list = job_obj.get_job("delphi software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="leppavirta")
	
@delphi.route('/delphi-software-developer-jobs-kurikka')
def delphi_software_developer87(page=1):

    job_list = job_obj.get_job("delphi software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kurikka")
	
@delphi.route('/delphi-software-developer-jobs-nivala')
def delphi_software_developer88(page=1):

    job_list = job_obj.get_job("delphi software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="nivala")
	
@delphi.route('/delphi-software-developer-jobs-joutseno')
def delphi_software_developer89(page=1):

    job_list = job_obj.get_job("delphi software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="joutseno")
	
@delphi.route('/delphi-software-developer-jobs-pedersore')
def delphi_software_developer90(page=1):

    job_list = job_obj.get_job("delphi software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="pedersore")
	
@delphi.route('/delphi-software-developer-jobs-sotkamo')
def delphi_software_developer91(page=1):

    job_list = job_obj.get_job("delphi software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="sotkamo")
	
@delphi.route('/delphi-software-developer-jobs-kuhmo')
def delphi_software_developer92(page=1):

    job_list = job_obj.get_job("delphi software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="kuhmo")
	
@delphi.route('/delphi-software-developer-jobs-paimio')
def delphi_software_developer93(page=1):

    job_list = job_obj.get_job("delphi software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="paimio")
	
@delphi.route('/delphi-software-developer-jobs-saarijarvi')
def delphi_software_developer94(page=1):

    job_list = job_obj.get_job("delphi software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="saarijarvi")
	
@delphi.route('/delphi-software-developer-jobs-helsinki')
def delphi_software_developer95(page=1):

    job_list = job_obj.get_job("delphi software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="delphi software developer", location="helsinki")


####################################################################

