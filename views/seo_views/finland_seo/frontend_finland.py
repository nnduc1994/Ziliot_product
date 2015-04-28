from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

frontend = Blueprint('frontend', __name__)
job_obj = Job()



####################################################################


@frontend.route('/frontend_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "frontend" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def frontend_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="espoo")

@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def frontend_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="tampere")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def frontend_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="vantaa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def frontend_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="turku")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def frontend_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="oulu")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def frontend_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="lahti")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def frontend_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kuopio")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def frontend_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="jyvvaskyla")

@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def frontend_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="pori")

@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def frontend_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="lappeenranta")	
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def frontend_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="vaasa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def frontend_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kotka")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def frontend_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="joensuu")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def frontend_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="hameenlinna")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def frontend_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="porvoo")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def frontend_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="mikkeli")

@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def frontend_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="hyvinkaa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def frontend_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="nurmijarvi")

@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def frontend_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="jarvenpaa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def frontend_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="rauma")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def frontend_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="lohja")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def frontend_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="karleby")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def frontend_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kajaani")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def frontend_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="rovaniemi")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def frontend_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="tuusula")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def frontend_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kirkkonummi")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def frontend_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="seinajoki")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def frontend_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kerava")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def frontend_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kouvola")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def frontend_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="imatra")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def frontend_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="nokia")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def frontend_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="savonlinna")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def frontend_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="riihimaki")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def frontend_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="vihti")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def frontend_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="salo")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def frontend_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kangasala")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def frontend_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="raisio")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def frontend_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="karhula")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def frontend_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kemi")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def frontend_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="iisalmi")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def frontend_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="varkaus")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def frontend_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="raahe")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def frontend_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="ylojarvi")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def frontend_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="hamina")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def frontend_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kaarina")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def frontend_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="tornio")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def frontend_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="heinola")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def frontend_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="hollola")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def frontend_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="valkeakoski")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def frontend_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="siilinjarvi")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def frontend_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kuusankoski")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def frontend_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="sibbo")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def frontend_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="jakostad")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def frontend_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="lempaala")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def frontend_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="mantsala")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def frontend_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="forssa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def frontend_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kuusamo")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def frontend_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="haukipudas")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def frontend_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="korsholm")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def frontend_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="laukaa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def frontend_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="anjala")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def frontend_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="uusikaupunki")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def frontend_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="janakkala")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def frontend_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="pirkkala")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def frontend_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def frontend_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="jamsa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def frontend_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="jamsa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def frontend_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="vammala")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def frontend_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="nastola")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def frontend_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="orimattila")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def frontend_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kauhajoki")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def frontend_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="ekenas")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def frontend_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kempele")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def frontend_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="lapua")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def frontend_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="lieksa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def frontend_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="naantali")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def frontend_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="aanekoski")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def frontend_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="ylivieska")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def frontend_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kontiolahti")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def frontend_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kankaanpaa")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def frontend_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="ulvila")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def frontend_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="pieksamaki")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def frontend_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kiiminki")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def frontend_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="pargas")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def frontend_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="nurmo")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def frontend_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="ilmajoki")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def frontend_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="liperi")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def frontend_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="keuruu")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def frontend_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="leppavirta")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def frontend_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kurikka")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def frontend_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="nivala")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def frontend_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="joutseno")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def frontend_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="pedersore")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def frontend_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="sotkamo")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def frontend_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="kuhmo")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def frontend_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="paimio")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def frontend_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="saarijarvi")
	
@frontend.route('/frontend-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def frontend_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("frontend ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@frontend.route('/frontend-software-developer-jobs-espoo')
def frontend_software_developer2(page=1):

    job_list = job_obj.get_job("frontend software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="espoo")

@frontend.route('/frontend-software-developer-jobs-tampere')
def frontend_software_developer3(page=1):

    job_list = job_obj.get_job("frontend software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="tampere")
	
@frontend.route('/frontend-software-developer-jobs-vantaa')
def frontend_software_developer4(page=1):

    job_list = job_obj.get_job("frontend software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="vantaa")
	
@frontend.route('/frontend-software-developer-jobs-turku')
def frontend_software_developer5(page=1):

    job_list = job_obj.get_job("frontend software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="turku")
	
@frontend.route('/frontend-software-developer-jobs-oulu')
def frontend_software_developer6(page=1):

    job_list = job_obj.get_job("frontend software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="oulu")
	
@frontend.route('/frontend-software-developer-jobs-lahti')
def frontend_software_developer7(page=1):

    job_list = job_obj.get_job("frontend software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="lahti")
	
@frontend.route('/frontend-software-developer-jobs-kuopio')
def frontend_software_developer8(page=1):

    job_list = job_obj.get_job("frontend software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kuopio")
	
@frontend.route('/frontend-software-developer-jobs-jyvvaskyla')
def frontend_software_developer9(page=1):

    job_list = job_obj.get_job("frontend software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="jyvvaskyla")

@frontend.route('/frontend-software-developer-jobs-pori')
def frontend_software_developer10(page=1):

    job_list = job_obj.get_job("frontend software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="pori")

@frontend.route('/frontend-software-developer-jobs-lappeenranta')
def frontend_software_developer11(page=1):

    job_list = job_obj.get_job("frontend software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="lappeenranta")	
	
@frontend.route('/frontend-software-developer-jobs-vaasa')
def frontend_software_developer12(page=1):

    job_list = job_obj.get_job("frontend software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="vaasa")
	
@frontend.route('/frontend-software-developer-jobs-kotka')
def frontend_software_developer13(page=1):

    job_list = job_obj.get_job("frontend software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kotka")
	
@frontend.route('/frontend-software-developer-jobs-joensuu')
def frontend_software_developer14(page=1):

    job_list = job_obj.get_job("frontend software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="joensuu")
	
@frontend.route('/frontend-software-developer-jobs-hameenlinna')
def frontend_software_developer15(page=1):

    job_list = job_obj.get_job("frontend software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="hameenlinna")
	
@frontend.route('/frontend-software-developer-jobs-porvoo')
def frontend_software_developer16(page=1):

    job_list = job_obj.get_job("frontend software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="porvoo")
	
@frontend.route('/frontend-software-developer-jobs-mikkeli')
def frontend_software_developer17(page=1):

    job_list = job_obj.get_job("frontend software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="mikkeli")

@frontend.route('/frontend-software-developer-jobs-hyvinkaa')
def frontend_software_developer18(page=1):

    job_list = job_obj.get_job("frontend software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="hyvinkaa")
	
@frontend.route('/frontend-software-developer-jobs-nurmijarvi')
def frontend_software_developer19(page=1):

    job_list = job_obj.get_job("frontend software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="nurmijarvi")

@frontend.route('/frontend-software-developer-jobs-jarvenpaa')
def frontend_software_developer20(page=1):

    job_list = job_obj.get_job("frontend software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="jarvenpaa")
	
@frontend.route('/frontend-software-developer-jobs-rauma')
def frontend_software_developer21(page=1):

    job_list = job_obj.get_job("frontend software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="rauma")
	
@frontend.route('/frontend-software-developer-jobs-lohja')
def frontend_software_developer22(page=1):

    job_list = job_obj.get_job("frontend software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="lohja")
	
@frontend.route('/frontend-software-developer-jobs-karleby')
def frontend_software_developer23(page=1):

    job_list = job_obj.get_job("frontend software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="karleby")
	
@frontend.route('/frontend-software-developer-jobs-kajaani')
def frontend_software_developer24(page=1):

    job_list = job_obj.get_job("frontend software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kajaani")
	
@frontend.route('/frontend-software-developer-jobs-rovaniemi')
def frontend_software_developer25(page=1):

    job_list = job_obj.get_job("frontend software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="rovaniemi")
	
@frontend.route('/frontend-software-developer-jobs-tuusula')
def frontend_software_developer26(page=1):

    job_list = job_obj.get_job("frontend software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="tuusula")
	
@frontend.route('/frontend-software-developer-jobs-kirkkonummi')
def frontend_software_developer27(page=1):

    job_list = job_obj.get_job("frontend software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kirkkonummi")
	
@frontend.route('/frontend-software-developer-jobs-seinajoki')
def frontend_software_developer28(page=1):

    job_list = job_obj.get_job("frontend software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="seinajoki")
	
@frontend.route('/frontend-software-developer-jobs-kerava')
def frontend_software_developer29(page=1):

    job_list = job_obj.get_job("frontend software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kerava")
	
@frontend.route('/frontend-software-developer-jobs-kouvola')
def frontend_software_developer30(page=1):

    job_list = job_obj.get_job("frontend software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kouvola")
	
@frontend.route('/frontend-software-developer-jobs-imatra')
def frontend_software_developer31(page=1):

    job_list = job_obj.get_job("frontend software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="imatra")
	
@frontend.route('/frontend-software-developer-jobs-nokia')
def frontend_software_developer32_1(page=1):

    job_list = job_obj.get_job("frontend software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="nokia")
	
@frontend.route('/frontend-software-developer-jobs-savonlinna')
def frontend_software_developer32(page=1):

    job_list = job_obj.get_job("frontend software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="savonlinna")
	
@frontend.route('/frontend-software-developer-jobs-riihimaki')
def frontend_software_developer33(page=1):

    job_list = job_obj.get_job("frontend software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="riihimaki")
	
@frontend.route('/frontend-software-developer-jobs-vihti')
def frontend_software_developer34(page=1):

    job_list = job_obj.get_job("frontend software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="vihti")
	
@frontend.route('/frontend-software-developer-jobs-salo')
def frontend_software_developer35(page=1):

    job_list = job_obj.get_job("frontend software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="salo")
	
@frontend.route('/frontend-software-developer-jobs-kangasala')
def frontend_software_developer36(page=1):

    job_list = job_obj.get_job("frontend software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kangasala")
	
@frontend.route('/frontend-software-developer-jobs-raisio')
def frontend_software_developer37_1(page=1):

    job_list = job_obj.get_job("frontend software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="raisio")
	
@frontend.route('/frontend-software-developer-jobs-karhula')
def frontend_software_developer37(page=1):

    job_list = job_obj.get_job("frontend software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="karhula")
	
@frontend.route('/frontend-software-developer-jobs-kemi')
def frontend_software_developer38(page=1):

    job_list = job_obj.get_job("frontend software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kemi")
	
@frontend.route('/frontend-software-developer-jobs-iisalmi')
def frontend_software_developer39(page=1):

    job_list = job_obj.get_job("frontend software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="iisalmi")
	
@frontend.route('/frontend-software-developer-jobs-varkaus')
def frontend_software_developer40(page=1):

    job_list = job_obj.get_job("frontend software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="varkaus")
	
@frontend.route('/frontend-software-developer-jobs-raahe')
def frontend_software_developer41(page=1):

    job_list = job_obj.get_job("frontend software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="raahe")
	
@frontend.route('/frontend-software-developer-jobs-ylojarvi')
def frontend_software_developer42_1(page=1):

    job_list = job_obj.get_job("frontend software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="ylojarvi")
	
@frontend.route('/frontend-software-developer-jobs-hamina')
def frontend_software_developer42(page=1):

    job_list = job_obj.get_job("frontend software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="hamina")
	
@frontend.route('/frontend-software-developer-jobs-kaarina')
def frontend_software_developer43(page=1):

    job_list = job_obj.get_job("frontend software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kaarina")
	
@frontend.route('/frontend-software-developer-jobs-tornio')
def frontend_software_developer44(page=1):

    job_list = job_obj.get_job("frontend software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="tornio")
	
@frontend.route('/frontend-software-developer-jobs-heinola')
def frontend_software_developer45(page=1):

    job_list = job_obj.get_job("frontend software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="heinola")
	
@frontend.route('/frontend-software-developer-jobs-hollola')
def frontend_software_developer46(page=1):

    job_list = job_obj.get_job("frontend software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="hollola")
	
@frontend.route('/frontend-software-developer-jobs-valkeakoski')
def frontend_software_developer47(page=1):

    job_list = job_obj.get_job("frontend software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="valkeakoski")
	
@frontend.route('/frontend-software-developer-jobs-siilinjarvi')
def frontend_software_developer48(page=1):

    job_list = job_obj.get_job("frontend software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="siilinjarvi")
	
@frontend.route('/frontend-software-developer-jobs-kuusankoski')
def frontend_software_developer49(page=1):

    job_list = job_obj.get_job("frontend software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kuusankoski")
	
@frontend.route('/frontend-software-developer-jobs-sibbo')
def frontend_software_developer50(page=1):

    job_list = job_obj.get_job("frontend software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="sibbo")
	
@frontend.route('/frontend-software-developer-jobs-jakostad')
def frontend_software_developer51(page=1):

    job_list = job_obj.get_job("frontend software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="jakostad")
	
@frontend.route('/frontend-software-developer-jobs-lempaala')
def frontend_software_developer52(page=1):

    job_list = job_obj.get_job("frontend software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="lempaala")
	
@frontend.route('/frontend-software-developer-jobs-mantsala')
def frontend_software_developer52_1(page=1):

    job_list = job_obj.get_job("frontend software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="mantsala")
	
@frontend.route('/frontend-software-developer-jobs-forssa')
def frontend_software_developer53(page=1):

    job_list = job_obj.get_job("frontend software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="forssa")
	
@frontend.route('/frontend-software-developer-jobs-kuusamo')
def frontend_software_developer54(page=1):

    job_list = job_obj.get_job("frontend software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kuusamo")
	
@frontend.route('/frontend-software-developer-jobs-haukipudas')
def frontend_software_developer55(page=1):

    job_list = job_obj.get_job("frontend software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="haukipudas")
	
@frontend.route('/frontend-software-developer-jobs-korsholm')
def frontend_software_developer56(page=1):

    job_list = job_obj.get_job("frontend software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="korsholm")
	
@frontend.route('/frontend-software-developer-jobs-laukaa')
def frontend_software_developer57(page=1):

    job_list = job_obj.get_job("frontend software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="laukaa")
	
@frontend.route('/frontend-software-developer-jobs-anjala')
def frontend_software_developer58(page=1):

    job_list = job_obj.get_job("frontend software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="anjala")
	
@frontend.route('/frontend-software-developer-jobs-uusikaupunki')
def frontend_software_developer59(page=1):

    job_list = job_obj.get_job("frontend software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="uusikaupunki")
	
@frontend.route('/frontend-software-developer-jobs-janakkala')
def frontend_software_developer60(page=1):

    job_list = job_obj.get_job("frontend software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="janakkala")
	
@frontend.route('/frontend-software-developer-jobs-pirkkala')
def frontend_software_developer61(page=1):

    job_list = job_obj.get_job("frontend software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="pirkkala")
	
@frontend.route('/frontend-software-developer-jobs-lansi-turunmaa')
def frontend_software_developer62(page=1):

    job_list = job_obj.get_job("frontend software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="lansi-turunmaa")
	
@frontend.route('/frontend-software-developer-jobs-jamsa')
def frontend_software_developer63(page=1):

    job_list = job_obj.get_job("frontend software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="jamsa")
	
@frontend.route('/frontend-software-developer-jobs-jamsa')
def frontend_software_developer64(page=1):

    job_list = job_obj.get_job("frontend software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="jamsa")
	
@frontend.route('/frontend-software-developer-jobs-vammala')
def frontend_software_developer65(page=1):

    job_list = job_obj.get_job("frontend software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="vammala")
	
@frontend.route('/frontend-software-developer-jobs-nastola')
def frontend_software_developer66(page=1):

    job_list = job_obj.get_job("frontend software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="nastola")
	
@frontend.route('/frontend-software-developer-jobs-orimattila')
def frontend_software_developer67(page=1):

    job_list = job_obj.get_job("frontend software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="orimattila")
	
@frontend.route('/frontend-software-developer-jobs-kauhajoki')
def frontend_software_developer68(page=1):

    job_list = job_obj.get_job("frontend software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kauhajoki")
	
@frontend.route('/frontend-software-developer-jobs-ekenas')
def frontend_software_developer69(page=1):

    job_list = job_obj.get_job("frontend software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="ekenas")
	
@frontend.route('/frontend-software-developer-jobs-kempele')
def frontend_software_developer70(page=1):

    job_list = job_obj.get_job("frontend software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kempele")
	
@frontend.route('/frontend-software-developer-jobs-lapua')
def frontend_software_developer71(page=1):

    job_list = job_obj.get_job("frontend software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="lapua")
	
@frontend.route('/frontend-software-developer-jobs-lieksa')
def frontend_software_developer72(page=1):

    job_list = job_obj.get_job("frontend software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="lieksa")
	
@frontend.route('/frontend-software-developer-jobs-naantali')
def frontend_software_developer73(page=1):

    job_list = job_obj.get_job("frontend software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="naantali")
	
@frontend.route('/frontend-software-developer-jobs-aanekoski')
def frontend_software_developer74(page=1):

    job_list = job_obj.get_job("frontend software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="aanekoski")
	
@frontend.route('/frontend-software-developer-jobs-ylivieska')
def frontend_software_developer75(page=1):

    job_list = job_obj.get_job("frontend software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="ylivieska")
	
@frontend.route('/frontend-software-developer-jobs-kontiolahti')
def frontend_software_developer76(page=1):

    job_list = job_obj.get_job("frontend software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kontiolahti")
	
@frontend.route('/frontend-software-developer-jobs-kankaanpaa')
def frontend_software_developer77(page=1):

    job_list = job_obj.get_job("frontend software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kankaanpaa")
	
@frontend.route('/frontend-software-developer-jobs-ulvila')
def frontend_software_developer78(page=1):

    job_list = job_obj.get_job("frontend software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="ulvila")
	
@frontend.route('/frontend-software-developer-jobs-pieksamaki')
def frontend_software_developer79(page=1):

    job_list = job_obj.get_job("frontend software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="pieksamaki")
	
@frontend.route('/frontend-software-developer-jobs-kiiminki')
def frontend_software_developer80(page=1):

    job_list = job_obj.get_job("frontend software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kiiminki")
	
@frontend.route('/frontend-software-developer-jobs-pargas')
def frontend_software_developer81(page=1):

    job_list = job_obj.get_job("frontend software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="pargas")
	
@frontend.route('/frontend-software-developer-jobs-nurmo')
def frontend_software_developer82(page=1):

    job_list = job_obj.get_job("frontend software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="nurmo")
	
@frontend.route('/frontend-software-developer-jobs-ilmajoki')
def frontend_software_developer83(page=1):

    job_list = job_obj.get_job("frontend software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="ilmajoki")
	
@frontend.route('/frontend-software-developer-jobs-liperi')
def frontend_software_developer84(page=1):

    job_list = job_obj.get_job("frontend software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="liperi")
	
@frontend.route('/frontend-software-developer-jobs-keuruu')
def frontend_software_developer85(page=1):

    job_list = job_obj.get_job("frontend software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="keuruu")
	
@frontend.route('/frontend-software-developer-jobs-leppavirta')
def frontend_software_developer86(page=1):

    job_list = job_obj.get_job("frontend software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="leppavirta")
	
@frontend.route('/frontend-software-developer-jobs-kurikka')
def frontend_software_developer87(page=1):

    job_list = job_obj.get_job("frontend software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kurikka")
	
@frontend.route('/frontend-software-developer-jobs-nivala')
def frontend_software_developer88(page=1):

    job_list = job_obj.get_job("frontend software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="nivala")
	
@frontend.route('/frontend-software-developer-jobs-joutseno')
def frontend_software_developer89(page=1):

    job_list = job_obj.get_job("frontend software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="joutseno")
	
@frontend.route('/frontend-software-developer-jobs-pedersore')
def frontend_software_developer90(page=1):

    job_list = job_obj.get_job("frontend software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="pedersore")
	
@frontend.route('/frontend-software-developer-jobs-sotkamo')
def frontend_software_developer91(page=1):

    job_list = job_obj.get_job("frontend software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="sotkamo")
	
@frontend.route('/frontend-software-developer-jobs-kuhmo')
def frontend_software_developer92(page=1):

    job_list = job_obj.get_job("frontend software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="kuhmo")
	
@frontend.route('/frontend-software-developer-jobs-paimio')
def frontend_software_developer93(page=1):

    job_list = job_obj.get_job("frontend software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="paimio")
	
@frontend.route('/frontend-software-developer-jobs-saarijarvi')
def frontend_software_developer94(page=1):

    job_list = job_obj.get_job("frontend software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="saarijarvi")
	
@frontend.route('/frontend-software-developer-jobs-helsinki')
def frontend_software_developer95(page=1):

    job_list = job_obj.get_job("frontend software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="frontend software developer", location="helsinki")


####################################################################

