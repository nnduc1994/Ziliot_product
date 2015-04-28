from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

visual_basic = Blueprint('visual_basic', __name__)
job_obj = Job()



####################################################################


@visual_basic.route('/visual-basic_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "visual-basic" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def visual_basic_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="espoo")

@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def visual_basic_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="tampere")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def visual_basic_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="vantaa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def visual_basic_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="turku")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def visual_basic_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="oulu")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def visual_basic_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="lahti")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def visual_basic_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kuopio")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def visual_basic_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="jyvvaskyla")

@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def visual_basic_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="pori")

@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def visual_basic_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="lappeenranta")	
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def visual_basic_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="vaasa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def visual_basic_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kotka")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def visual_basic_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="joensuu")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def visual_basic_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="hameenlinna")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def visual_basic_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="porvoo")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def visual_basic_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="mikkeli")

@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def visual_basic_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="hyvinkaa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def visual_basic_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="nurmijarvi")

@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def visual_basic_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="jarvenpaa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def visual_basic_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="rauma")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def visual_basic_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="lohja")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def visual_basic_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="karleby")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def visual_basic_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kajaani")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def visual_basic_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="rovaniemi")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def visual_basic_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="tuusula")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def visual_basic_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kirkkonummi")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def visual_basic_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="seinajoki")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def visual_basic_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kerava")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def visual_basic_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kouvola")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def visual_basic_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="imatra")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def visual_basic_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="nokia")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def visual_basic_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="savonlinna")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def visual_basic_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="riihimaki")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def visual_basic_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="vihti")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def visual_basic_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="salo")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def visual_basic_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kangasala")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def visual_basic_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="raisio")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def visual_basic_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="karhula")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def visual_basic_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kemi")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def visual_basic_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="iisalmi")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def visual_basic_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="varkaus")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def visual_basic_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="raahe")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def visual_basic_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="ylojarvi")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def visual_basic_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="hamina")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def visual_basic_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kaarina")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def visual_basic_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="tornio")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def visual_basic_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="heinola")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def visual_basic_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="hollola")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def visual_basic_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="valkeakoski")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def visual_basic_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="siilinjarvi")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def visual_basic_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kuusankoski")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def visual_basic_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="sibbo")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def visual_basic_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="jakostad")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def visual_basic_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="lempaala")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def visual_basic_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="mantsala")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def visual_basic_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="forssa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def visual_basic_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kuusamo")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def visual_basic_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="haukipudas")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def visual_basic_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="korsholm")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def visual_basic_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="laukaa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def visual_basic_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="anjala")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def visual_basic_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="uusikaupunki")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def visual_basic_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="janakkala")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def visual_basic_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="pirkkala")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def visual_basic_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def visual_basic_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="jamsa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def visual_basic_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="jamsa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def visual_basic_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="vammala")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def visual_basic_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="nastola")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def visual_basic_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="orimattila")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def visual_basic_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kauhajoki")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def visual_basic_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="ekenas")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def visual_basic_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kempele")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def visual_basic_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="lapua")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def visual_basic_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="lieksa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def visual_basic_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="naantali")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def visual_basic_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="aanekoski")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def visual_basic_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="ylivieska")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def visual_basic_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kontiolahti")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def visual_basic_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kankaanpaa")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def visual_basic_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="ulvila")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def visual_basic_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="pieksamaki")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def visual_basic_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kiiminki")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def visual_basic_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="pargas")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def visual_basic_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="nurmo")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def visual_basic_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="ilmajoki")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def visual_basic_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="liperi")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def visual_basic_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="keuruu")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def visual_basic_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="leppavirta")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def visual_basic_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kurikka")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def visual_basic_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="nivala")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def visual_basic_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="joutseno")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def visual_basic_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="pedersore")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def visual_basic_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="sotkamo")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def visual_basic_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="kuhmo")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def visual_basic_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="paimio")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def visual_basic_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="saarijarvi")
	
@visual_basic.route('/visual-basic-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def visual_basic_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("visual basic ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@visual_basic.route('/visual-basic-software-developer-jobs-espoo')
def visual_basic_software_developer2(page=1):

    job_list = job_obj.get_job("visual basic software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="espoo")

@visual_basic.route('/visual-basic-software-developer-jobs-tampere')
def visual_basic_software_developer3(page=1):

    job_list = job_obj.get_job("visual basic software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="tampere")
	
@visual_basic.route('/visual-basic-software-developer-jobs-vantaa')
def visual_basic_software_developer4(page=1):

    job_list = job_obj.get_job("visual basic software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="vantaa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-turku')
def visual_basic_software_developer5(page=1):

    job_list = job_obj.get_job("visual basic software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="turku")
	
@visual_basic.route('/visual-basic-software-developer-jobs-oulu')
def visual_basic_software_developer6(page=1):

    job_list = job_obj.get_job("visual basic software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="oulu")
	
@visual_basic.route('/visual-basic-software-developer-jobs-lahti')
def visual_basic_software_developer7(page=1):

    job_list = job_obj.get_job("visual basic software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="lahti")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kuopio')
def visual_basic_software_developer8(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kuopio")
	
@visual_basic.route('/visual-basic-software-developer-jobs-jyvvaskyla')
def visual_basic_software_developer9(page=1):

    job_list = job_obj.get_job("visual basic software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="jyvvaskyla")

@visual_basic.route('/visual-basic-software-developer-jobs-pori')
def visual_basic_software_developer10(page=1):

    job_list = job_obj.get_job("visual basic software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="pori")

@visual_basic.route('/visual-basic-software-developer-jobs-lappeenranta')
def visual_basic_software_developer11(page=1):

    job_list = job_obj.get_job("visual basic software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="lappeenranta")	
	
@visual_basic.route('/visual-basic-software-developer-jobs-vaasa')
def visual_basic_software_developer12(page=1):

    job_list = job_obj.get_job("visual basic software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="vaasa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kotka')
def visual_basic_software_developer13(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kotka")
	
@visual_basic.route('/visual-basic-software-developer-jobs-joensuu')
def visual_basic_software_developer14(page=1):

    job_list = job_obj.get_job("visual basic software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="joensuu")
	
@visual_basic.route('/visual-basic-software-developer-jobs-hameenlinna')
def visual_basic_software_developer15(page=1):

    job_list = job_obj.get_job("visual basic software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="hameenlinna")
	
@visual_basic.route('/visual-basic-software-developer-jobs-porvoo')
def visual_basic_software_developer16(page=1):

    job_list = job_obj.get_job("visual basic software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="porvoo")
	
@visual_basic.route('/visual-basic-software-developer-jobs-mikkeli')
def visual_basic_software_developer17(page=1):

    job_list = job_obj.get_job("visual basic software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="mikkeli")

@visual_basic.route('/visual-basic-software-developer-jobs-hyvinkaa')
def visual_basic_software_developer18(page=1):

    job_list = job_obj.get_job("visual basic software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="hyvinkaa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-nurmijarvi')
def visual_basic_software_developer19(page=1):

    job_list = job_obj.get_job("visual basic software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="nurmijarvi")

@visual_basic.route('/visual-basic-software-developer-jobs-jarvenpaa')
def visual_basic_software_developer20(page=1):

    job_list = job_obj.get_job("visual basic software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="jarvenpaa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-rauma')
def visual_basic_software_developer21(page=1):

    job_list = job_obj.get_job("visual basic software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="rauma")
	
@visual_basic.route('/visual-basic-software-developer-jobs-lohja')
def visual_basic_software_developer22(page=1):

    job_list = job_obj.get_job("visual basic software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="lohja")
	
@visual_basic.route('/visual-basic-software-developer-jobs-karleby')
def visual_basic_software_developer23(page=1):

    job_list = job_obj.get_job("visual basic software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="karleby")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kajaani')
def visual_basic_software_developer24(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kajaani")
	
@visual_basic.route('/visual-basic-software-developer-jobs-rovaniemi')
def visual_basic_software_developer25(page=1):

    job_list = job_obj.get_job("visual basic software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="rovaniemi")
	
@visual_basic.route('/visual-basic-software-developer-jobs-tuusula')
def visual_basic_software_developer26(page=1):

    job_list = job_obj.get_job("visual basic software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="tuusula")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kirkkonummi')
def visual_basic_software_developer27(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kirkkonummi")
	
@visual_basic.route('/visual-basic-software-developer-jobs-seinajoki')
def visual_basic_software_developer28(page=1):

    job_list = job_obj.get_job("visual basic software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="seinajoki")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kerava')
def visual_basic_software_developer29(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kerava")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kouvola')
def visual_basic_software_developer30(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kouvola")
	
@visual_basic.route('/visual-basic-software-developer-jobs-imatra')
def visual_basic_software_developer31(page=1):

    job_list = job_obj.get_job("visual basic software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="imatra")
	
@visual_basic.route('/visual-basic-software-developer-jobs-nokia')
def visual_basic_software_developer32_1(page=1):

    job_list = job_obj.get_job("visual basic software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="nokia")
	
@visual_basic.route('/visual-basic-software-developer-jobs-savonlinna')
def visual_basic_software_developer32(page=1):

    job_list = job_obj.get_job("visual basic software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="savonlinna")
	
@visual_basic.route('/visual-basic-software-developer-jobs-riihimaki')
def visual_basic_software_developer33(page=1):

    job_list = job_obj.get_job("visual basic software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="riihimaki")
	
@visual_basic.route('/visual-basic-software-developer-jobs-vihti')
def visual_basic_software_developer34(page=1):

    job_list = job_obj.get_job("visual basic software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="vihti")
	
@visual_basic.route('/visual-basic-software-developer-jobs-salo')
def visual_basic_software_developer35(page=1):

    job_list = job_obj.get_job("visual basic software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="salo")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kangasala')
def visual_basic_software_developer36(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kangasala")
	
@visual_basic.route('/visual-basic-software-developer-jobs-raisio')
def visual_basic_software_developer37_1(page=1):

    job_list = job_obj.get_job("visual basic software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="raisio")
	
@visual_basic.route('/visual-basic-software-developer-jobs-karhula')
def visual_basic_software_developer37(page=1):

    job_list = job_obj.get_job("visual basic software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="karhula")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kemi')
def visual_basic_software_developer38(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kemi")
	
@visual_basic.route('/visual-basic-software-developer-jobs-iisalmi')
def visual_basic_software_developer39(page=1):

    job_list = job_obj.get_job("visual basic software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="iisalmi")
	
@visual_basic.route('/visual-basic-software-developer-jobs-varkaus')
def visual_basic_software_developer40(page=1):

    job_list = job_obj.get_job("visual basic software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="varkaus")
	
@visual_basic.route('/visual-basic-software-developer-jobs-raahe')
def visual_basic_software_developer41(page=1):

    job_list = job_obj.get_job("visual basic software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="raahe")
	
@visual_basic.route('/visual-basic-software-developer-jobs-ylojarvi')
def visual_basic_software_developer42_1(page=1):

    job_list = job_obj.get_job("visual basic software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="ylojarvi")
	
@visual_basic.route('/visual-basic-software-developer-jobs-hamina')
def visual_basic_software_developer42(page=1):

    job_list = job_obj.get_job("visual basic software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="hamina")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kaarina')
def visual_basic_software_developer43(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kaarina")
	
@visual_basic.route('/visual-basic-software-developer-jobs-tornio')
def visual_basic_software_developer44(page=1):

    job_list = job_obj.get_job("visual basic software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="tornio")
	
@visual_basic.route('/visual-basic-software-developer-jobs-heinola')
def visual_basic_software_developer45(page=1):

    job_list = job_obj.get_job("visual basic software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="heinola")
	
@visual_basic.route('/visual-basic-software-developer-jobs-hollola')
def visual_basic_software_developer46(page=1):

    job_list = job_obj.get_job("visual basic software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="hollola")
	
@visual_basic.route('/visual-basic-software-developer-jobs-valkeakoski')
def visual_basic_software_developer47(page=1):

    job_list = job_obj.get_job("visual basic software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="valkeakoski")
	
@visual_basic.route('/visual-basic-software-developer-jobs-siilinjarvi')
def visual_basic_software_developer48(page=1):

    job_list = job_obj.get_job("visual basic software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="siilinjarvi")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kuusankoski')
def visual_basic_software_developer49(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kuusankoski")
	
@visual_basic.route('/visual-basic-software-developer-jobs-sibbo')
def visual_basic_software_developer50(page=1):

    job_list = job_obj.get_job("visual basic software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="sibbo")
	
@visual_basic.route('/visual-basic-software-developer-jobs-jakostad')
def visual_basic_software_developer51(page=1):

    job_list = job_obj.get_job("visual basic software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="jakostad")
	
@visual_basic.route('/visual-basic-software-developer-jobs-lempaala')
def visual_basic_software_developer52(page=1):

    job_list = job_obj.get_job("visual basic software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="lempaala")
	
@visual_basic.route('/visual-basic-software-developer-jobs-mantsala')
def visual_basic_software_developer52_1(page=1):

    job_list = job_obj.get_job("visual basic software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="mantsala")
	
@visual_basic.route('/visual-basic-software-developer-jobs-forssa')
def visual_basic_software_developer53(page=1):

    job_list = job_obj.get_job("visual basic software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="forssa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kuusamo')
def visual_basic_software_developer54(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kuusamo")
	
@visual_basic.route('/visual-basic-software-developer-jobs-haukipudas')
def visual_basic_software_developer55(page=1):

    job_list = job_obj.get_job("visual basic software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="haukipudas")
	
@visual_basic.route('/visual-basic-software-developer-jobs-korsholm')
def visual_basic_software_developer56(page=1):

    job_list = job_obj.get_job("visual basic software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="korsholm")
	
@visual_basic.route('/visual-basic-software-developer-jobs-laukaa')
def visual_basic_software_developer57(page=1):

    job_list = job_obj.get_job("visual basic software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="laukaa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-anjala')
def visual_basic_software_developer58(page=1):

    job_list = job_obj.get_job("visual basic software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="anjala")
	
@visual_basic.route('/visual-basic-software-developer-jobs-uusikaupunki')
def visual_basic_software_developer59(page=1):

    job_list = job_obj.get_job("visual basic software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="uusikaupunki")
	
@visual_basic.route('/visual-basic-software-developer-jobs-janakkala')
def visual_basic_software_developer60(page=1):

    job_list = job_obj.get_job("visual basic software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="janakkala")
	
@visual_basic.route('/visual-basic-software-developer-jobs-pirkkala')
def visual_basic_software_developer61(page=1):

    job_list = job_obj.get_job("visual basic software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="pirkkala")
	
@visual_basic.route('/visual-basic-software-developer-jobs-lansi-turunmaa')
def visual_basic_software_developer62(page=1):

    job_list = job_obj.get_job("visual basic software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="lansi-turunmaa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-jamsa')
def visual_basic_software_developer63(page=1):

    job_list = job_obj.get_job("visual basic software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="jamsa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-jamsa')
def visual_basic_software_developer64(page=1):

    job_list = job_obj.get_job("visual basic software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="jamsa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-vammala')
def visual_basic_software_developer65(page=1):

    job_list = job_obj.get_job("visual basic software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="vammala")
	
@visual_basic.route('/visual-basic-software-developer-jobs-nastola')
def visual_basic_software_developer66(page=1):

    job_list = job_obj.get_job("visual basic software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="nastola")
	
@visual_basic.route('/visual-basic-software-developer-jobs-orimattila')
def visual_basic_software_developer67(page=1):

    job_list = job_obj.get_job("visual basic software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="orimattila")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kauhajoki')
def visual_basic_software_developer68(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kauhajoki")
	
@visual_basic.route('/visual-basic-software-developer-jobs-ekenas')
def visual_basic_software_developer69(page=1):

    job_list = job_obj.get_job("visual basic software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="ekenas")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kempele')
def visual_basic_software_developer70(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kempele")
	
@visual_basic.route('/visual-basic-software-developer-jobs-lapua')
def visual_basic_software_developer71(page=1):

    job_list = job_obj.get_job("visual basic software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="lapua")
	
@visual_basic.route('/visual-basic-software-developer-jobs-lieksa')
def visual_basic_software_developer72(page=1):

    job_list = job_obj.get_job("visual basic software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="lieksa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-naantali')
def visual_basic_software_developer73(page=1):

    job_list = job_obj.get_job("visual basic software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="naantali")
	
@visual_basic.route('/visual-basic-software-developer-jobs-aanekoski')
def visual_basic_software_developer74(page=1):

    job_list = job_obj.get_job("visual basic software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="aanekoski")
	
@visual_basic.route('/visual-basic-software-developer-jobs-ylivieska')
def visual_basic_software_developer75(page=1):

    job_list = job_obj.get_job("visual basic software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="ylivieska")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kontiolahti')
def visual_basic_software_developer76(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kontiolahti")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kankaanpaa')
def visual_basic_software_developer77(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kankaanpaa")
	
@visual_basic.route('/visual-basic-software-developer-jobs-ulvila')
def visual_basic_software_developer78(page=1):

    job_list = job_obj.get_job("visual basic software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="ulvila")
	
@visual_basic.route('/visual-basic-software-developer-jobs-pieksamaki')
def visual_basic_software_developer79(page=1):

    job_list = job_obj.get_job("visual basic software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="pieksamaki")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kiiminki')
def visual_basic_software_developer80(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kiiminki")
	
@visual_basic.route('/visual-basic-software-developer-jobs-pargas')
def visual_basic_software_developer81(page=1):

    job_list = job_obj.get_job("visual basic software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="pargas")
	
@visual_basic.route('/visual-basic-software-developer-jobs-nurmo')
def visual_basic_software_developer82(page=1):

    job_list = job_obj.get_job("visual basic software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="nurmo")
	
@visual_basic.route('/visual-basic-software-developer-jobs-ilmajoki')
def visual_basic_software_developer83(page=1):

    job_list = job_obj.get_job("visual basic software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="ilmajoki")
	
@visual_basic.route('/visual-basic-software-developer-jobs-liperi')
def visual_basic_software_developer84(page=1):

    job_list = job_obj.get_job("visual basic software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="liperi")
	
@visual_basic.route('/visual-basic-software-developer-jobs-keuruu')
def visual_basic_software_developer85(page=1):

    job_list = job_obj.get_job("visual basic software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="keuruu")
	
@visual_basic.route('/visual-basic-software-developer-jobs-leppavirta')
def visual_basic_software_developer86(page=1):

    job_list = job_obj.get_job("visual basic software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="leppavirta")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kurikka')
def visual_basic_software_developer87(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kurikka")
	
@visual_basic.route('/visual-basic-software-developer-jobs-nivala')
def visual_basic_software_developer88(page=1):

    job_list = job_obj.get_job("visual basic software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="nivala")
	
@visual_basic.route('/visual-basic-software-developer-jobs-joutseno')
def visual_basic_software_developer89(page=1):

    job_list = job_obj.get_job("visual basic software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="joutseno")
	
@visual_basic.route('/visual-basic-software-developer-jobs-pedersore')
def visual_basic_software_developer90(page=1):

    job_list = job_obj.get_job("visual basic software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="pedersore")
	
@visual_basic.route('/visual-basic-software-developer-jobs-sotkamo')
def visual_basic_software_developer91(page=1):

    job_list = job_obj.get_job("visual basic software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="sotkamo")
	
@visual_basic.route('/visual-basic-software-developer-jobs-kuhmo')
def visual_basic_software_developer92(page=1):

    job_list = job_obj.get_job("visual basic software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="kuhmo")
	
@visual_basic.route('/visual-basic-software-developer-jobs-paimio')
def visual_basic_software_developer93(page=1):

    job_list = job_obj.get_job("visual basic software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="paimio")
	
@visual_basic.route('/visual-basic-software-developer-jobs-saarijarvi')
def visual_basic_software_developer94(page=1):

    job_list = job_obj.get_job("visual basic software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="saarijarvi")
	
@visual_basic.route('/visual-basic-software-developer-jobs-helsinki')
def visual_basic_software_developer95(page=1):

    job_list = job_obj.get_job("visual basic software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="visual basic software developer", location="helsinki")


####################################################################
