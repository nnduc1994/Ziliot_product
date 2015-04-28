from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

pascal = Blueprint('pascal', __name__)
job_obj = Job()



####################################################################


@pascal.route('/pascal_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "pascal" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def pascal_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="espoo")

@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def pascal_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="tampere")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def pascal_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="vantaa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def pascal_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="turku")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def pascal_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="oulu")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def pascal_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="lahti")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def pascal_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kuopio")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def pascal_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="jyvvaskyla")

@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def pascal_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="pori")

@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def pascal_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="lappeenranta")	
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def pascal_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="vaasa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def pascal_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kotka")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def pascal_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="joensuu")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def pascal_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="hameenlinna")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def pascal_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="porvoo")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def pascal_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="mikkeli")

@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def pascal_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="hyvinkaa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def pascal_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="nurmijarvi")

@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def pascal_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="jarvenpaa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def pascal_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="rauma")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def pascal_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="lohja")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def pascal_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="karleby")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def pascal_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kajaani")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def pascal_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="rovaniemi")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def pascal_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="tuusula")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def pascal_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kirkkonummi")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def pascal_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="seinajoki")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def pascal_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kerava")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def pascal_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kouvola")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def pascal_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="imatra")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def pascal_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="nokia")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def pascal_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="savonlinna")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def pascal_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="riihimaki")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def pascal_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="vihti")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def pascal_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="salo")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def pascal_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kangasala")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def pascal_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="raisio")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def pascal_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="karhula")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def pascal_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kemi")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def pascal_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="iisalmi")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def pascal_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="varkaus")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def pascal_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="raahe")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def pascal_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="ylojarvi")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def pascal_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="hamina")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def pascal_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kaarina")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def pascal_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="tornio")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def pascal_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="heinola")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def pascal_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="hollola")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def pascal_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="valkeakoski")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def pascal_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="siilinjarvi")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def pascal_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kuusankoski")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def pascal_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="sibbo")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def pascal_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="jakostad")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def pascal_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="lempaala")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def pascal_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="mantsala")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def pascal_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="forssa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def pascal_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kuusamo")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def pascal_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="haukipudas")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def pascal_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="korsholm")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def pascal_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="laukaa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def pascal_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="anjala")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def pascal_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="uusikaupunki")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def pascal_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="janakkala")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def pascal_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="pirkkala")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def pascal_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def pascal_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="jamsa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def pascal_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="jamsa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def pascal_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="vammala")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def pascal_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="nastola")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def pascal_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="orimattila")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def pascal_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kauhajoki")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def pascal_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="ekenas")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def pascal_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kempele")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def pascal_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="lapua")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def pascal_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="lieksa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def pascal_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="naantali")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def pascal_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="aanekoski")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def pascal_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="ylivieska")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def pascal_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kontiolahti")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def pascal_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kankaanpaa")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def pascal_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="ulvila")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def pascal_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="pieksamaki")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def pascal_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kiiminki")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def pascal_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="pargas")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def pascal_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="nurmo")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def pascal_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="ilmajoki")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def pascal_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="liperi")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def pascal_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="keuruu")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def pascal_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="leppavirta")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def pascal_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kurikka")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def pascal_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="nivala")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def pascal_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="joutseno")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def pascal_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="pedersore")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def pascal_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="sotkamo")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def pascal_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="kuhmo")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def pascal_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="paimio")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def pascal_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="saarijarvi")
	
@pascal.route('/pascal-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def pascal_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("pascal ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@pascal.route('/pascal-software-developer-jobs-espoo')
def pascal_software_developer2(page=1):

    job_list = job_obj.get_job("pascal software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="espoo")

@pascal.route('/pascal-software-developer-jobs-tampere')
def pascal_software_developer3(page=1):

    job_list = job_obj.get_job("pascal software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="tampere")
	
@pascal.route('/pascal-software-developer-jobs-vantaa')
def pascal_software_developer4(page=1):

    job_list = job_obj.get_job("pascal software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="vantaa")
	
@pascal.route('/pascal-software-developer-jobs-turku')
def pascal_software_developer5(page=1):

    job_list = job_obj.get_job("pascal software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="turku")
	
@pascal.route('/pascal-software-developer-jobs-oulu')
def pascal_software_developer6(page=1):

    job_list = job_obj.get_job("pascal software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="oulu")
	
@pascal.route('/pascal-software-developer-jobs-lahti')
def pascal_software_developer7(page=1):

    job_list = job_obj.get_job("pascal software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="lahti")
	
@pascal.route('/pascal-software-developer-jobs-kuopio')
def pascal_software_developer8(page=1):

    job_list = job_obj.get_job("pascal software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kuopio")
	
@pascal.route('/pascal-software-developer-jobs-jyvvaskyla')
def pascal_software_developer9(page=1):

    job_list = job_obj.get_job("pascal software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="jyvvaskyla")

@pascal.route('/pascal-software-developer-jobs-pori')
def pascal_software_developer10(page=1):

    job_list = job_obj.get_job("pascal software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="pori")

@pascal.route('/pascal-software-developer-jobs-lappeenranta')
def pascal_software_developer11(page=1):

    job_list = job_obj.get_job("pascal software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="lappeenranta")	
	
@pascal.route('/pascal-software-developer-jobs-vaasa')
def pascal_software_developer12(page=1):

    job_list = job_obj.get_job("pascal software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="vaasa")
	
@pascal.route('/pascal-software-developer-jobs-kotka')
def pascal_software_developer13(page=1):

    job_list = job_obj.get_job("pascal software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kotka")
	
@pascal.route('/pascal-software-developer-jobs-joensuu')
def pascal_software_developer14(page=1):

    job_list = job_obj.get_job("pascal software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="joensuu")
	
@pascal.route('/pascal-software-developer-jobs-hameenlinna')
def pascal_software_developer15(page=1):

    job_list = job_obj.get_job("pascal software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="hameenlinna")
	
@pascal.route('/pascal-software-developer-jobs-porvoo')
def pascal_software_developer16(page=1):

    job_list = job_obj.get_job("pascal software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="porvoo")
	
@pascal.route('/pascal-software-developer-jobs-mikkeli')
def pascal_software_developer17(page=1):

    job_list = job_obj.get_job("pascal software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="mikkeli")

@pascal.route('/pascal-software-developer-jobs-hyvinkaa')
def pascal_software_developer18(page=1):

    job_list = job_obj.get_job("pascal software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="hyvinkaa")
	
@pascal.route('/pascal-software-developer-jobs-nurmijarvi')
def pascal_software_developer19(page=1):

    job_list = job_obj.get_job("pascal software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="nurmijarvi")

@pascal.route('/pascal-software-developer-jobs-jarvenpaa')
def pascal_software_developer20(page=1):

    job_list = job_obj.get_job("pascal software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="jarvenpaa")
	
@pascal.route('/pascal-software-developer-jobs-rauma')
def pascal_software_developer21(page=1):

    job_list = job_obj.get_job("pascal software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="rauma")
	
@pascal.route('/pascal-software-developer-jobs-lohja')
def pascal_software_developer22(page=1):

    job_list = job_obj.get_job("pascal software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="lohja")
	
@pascal.route('/pascal-software-developer-jobs-karleby')
def pascal_software_developer23(page=1):

    job_list = job_obj.get_job("pascal software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="karleby")
	
@pascal.route('/pascal-software-developer-jobs-kajaani')
def pascal_software_developer24(page=1):

    job_list = job_obj.get_job("pascal software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kajaani")
	
@pascal.route('/pascal-software-developer-jobs-rovaniemi')
def pascal_software_developer25(page=1):

    job_list = job_obj.get_job("pascal software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="rovaniemi")
	
@pascal.route('/pascal-software-developer-jobs-tuusula')
def pascal_software_developer26(page=1):

    job_list = job_obj.get_job("pascal software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="tuusula")
	
@pascal.route('/pascal-software-developer-jobs-kirkkonummi')
def pascal_software_developer27(page=1):

    job_list = job_obj.get_job("pascal software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kirkkonummi")
	
@pascal.route('/pascal-software-developer-jobs-seinajoki')
def pascal_software_developer28(page=1):

    job_list = job_obj.get_job("pascal software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="seinajoki")
	
@pascal.route('/pascal-software-developer-jobs-kerava')
def pascal_software_developer29(page=1):

    job_list = job_obj.get_job("pascal software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kerava")
	
@pascal.route('/pascal-software-developer-jobs-kouvola')
def pascal_software_developer30(page=1):

    job_list = job_obj.get_job("pascal software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kouvola")
	
@pascal.route('/pascal-software-developer-jobs-imatra')
def pascal_software_developer31(page=1):

    job_list = job_obj.get_job("pascal software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="imatra")
	
@pascal.route('/pascal-software-developer-jobs-nokia')
def pascal_software_developer32_1(page=1):

    job_list = job_obj.get_job("pascal software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="nokia")
	
@pascal.route('/pascal-software-developer-jobs-savonlinna')
def pascal_software_developer32(page=1):

    job_list = job_obj.get_job("pascal software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="savonlinna")
	
@pascal.route('/pascal-software-developer-jobs-riihimaki')
def pascal_software_developer33(page=1):

    job_list = job_obj.get_job("pascal software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="riihimaki")
	
@pascal.route('/pascal-software-developer-jobs-vihti')
def pascal_software_developer34(page=1):

    job_list = job_obj.get_job("pascal software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="vihti")
	
@pascal.route('/pascal-software-developer-jobs-salo')
def pascal_software_developer35(page=1):

    job_list = job_obj.get_job("pascal software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="salo")
	
@pascal.route('/pascal-software-developer-jobs-kangasala')
def pascal_software_developer36(page=1):

    job_list = job_obj.get_job("pascal software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kangasala")
	
@pascal.route('/pascal-software-developer-jobs-raisio')
def pascal_software_developer37_1(page=1):

    job_list = job_obj.get_job("pascal software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="raisio")
	
@pascal.route('/pascal-software-developer-jobs-karhula')
def pascal_software_developer37(page=1):

    job_list = job_obj.get_job("pascal software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="karhula")
	
@pascal.route('/pascal-software-developer-jobs-kemi')
def pascal_software_developer38(page=1):

    job_list = job_obj.get_job("pascal software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kemi")
	
@pascal.route('/pascal-software-developer-jobs-iisalmi')
def pascal_software_developer39(page=1):

    job_list = job_obj.get_job("pascal software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="iisalmi")
	
@pascal.route('/pascal-software-developer-jobs-varkaus')
def pascal_software_developer40(page=1):

    job_list = job_obj.get_job("pascal software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="varkaus")
	
@pascal.route('/pascal-software-developer-jobs-raahe')
def pascal_software_developer41(page=1):

    job_list = job_obj.get_job("pascal software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="raahe")
	
@pascal.route('/pascal-software-developer-jobs-ylojarvi')
def pascal_software_developer42_1(page=1):

    job_list = job_obj.get_job("pascal software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="ylojarvi")
	
@pascal.route('/pascal-software-developer-jobs-hamina')
def pascal_software_developer42(page=1):

    job_list = job_obj.get_job("pascal software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="hamina")
	
@pascal.route('/pascal-software-developer-jobs-kaarina')
def pascal_software_developer43(page=1):

    job_list = job_obj.get_job("pascal software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kaarina")
	
@pascal.route('/pascal-software-developer-jobs-tornio')
def pascal_software_developer44(page=1):

    job_list = job_obj.get_job("pascal software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="tornio")
	
@pascal.route('/pascal-software-developer-jobs-heinola')
def pascal_software_developer45(page=1):

    job_list = job_obj.get_job("pascal software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="heinola")
	
@pascal.route('/pascal-software-developer-jobs-hollola')
def pascal_software_developer46(page=1):

    job_list = job_obj.get_job("pascal software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="hollola")
	
@pascal.route('/pascal-software-developer-jobs-valkeakoski')
def pascal_software_developer47(page=1):

    job_list = job_obj.get_job("pascal software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="valkeakoski")
	
@pascal.route('/pascal-software-developer-jobs-siilinjarvi')
def pascal_software_developer48(page=1):

    job_list = job_obj.get_job("pascal software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="siilinjarvi")
	
@pascal.route('/pascal-software-developer-jobs-kuusankoski')
def pascal_software_developer49(page=1):

    job_list = job_obj.get_job("pascal software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kuusankoski")
	
@pascal.route('/pascal-software-developer-jobs-sibbo')
def pascal_software_developer50(page=1):

    job_list = job_obj.get_job("pascal software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="sibbo")
	
@pascal.route('/pascal-software-developer-jobs-jakostad')
def pascal_software_developer51(page=1):

    job_list = job_obj.get_job("pascal software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="jakostad")
	
@pascal.route('/pascal-software-developer-jobs-lempaala')
def pascal_software_developer52(page=1):

    job_list = job_obj.get_job("pascal software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="lempaala")
	
@pascal.route('/pascal-software-developer-jobs-mantsala')
def pascal_software_developer52_1(page=1):

    job_list = job_obj.get_job("pascal software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="mantsala")
	
@pascal.route('/pascal-software-developer-jobs-forssa')
def pascal_software_developer53(page=1):

    job_list = job_obj.get_job("pascal software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="forssa")
	
@pascal.route('/pascal-software-developer-jobs-kuusamo')
def pascal_software_developer54(page=1):

    job_list = job_obj.get_job("pascal software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kuusamo")
	
@pascal.route('/pascal-software-developer-jobs-haukipudas')
def pascal_software_developer55(page=1):

    job_list = job_obj.get_job("pascal software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="haukipudas")
	
@pascal.route('/pascal-software-developer-jobs-korsholm')
def pascal_software_developer56(page=1):

    job_list = job_obj.get_job("pascal software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="korsholm")
	
@pascal.route('/pascal-software-developer-jobs-laukaa')
def pascal_software_developer57(page=1):

    job_list = job_obj.get_job("pascal software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="laukaa")
	
@pascal.route('/pascal-software-developer-jobs-anjala')
def pascal_software_developer58(page=1):

    job_list = job_obj.get_job("pascal software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="anjala")
	
@pascal.route('/pascal-software-developer-jobs-uusikaupunki')
def pascal_software_developer59(page=1):

    job_list = job_obj.get_job("pascal software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="uusikaupunki")
	
@pascal.route('/pascal-software-developer-jobs-janakkala')
def pascal_software_developer60(page=1):

    job_list = job_obj.get_job("pascal software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="janakkala")
	
@pascal.route('/pascal-software-developer-jobs-pirkkala')
def pascal_software_developer61(page=1):

    job_list = job_obj.get_job("pascal software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="pirkkala")
	
@pascal.route('/pascal-software-developer-jobs-lansi-turunmaa')
def pascal_software_developer62(page=1):

    job_list = job_obj.get_job("pascal software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="lansi-turunmaa")
	
@pascal.route('/pascal-software-developer-jobs-jamsa')
def pascal_software_developer63(page=1):

    job_list = job_obj.get_job("pascal software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="jamsa")
	
@pascal.route('/pascal-software-developer-jobs-jamsa')
def pascal_software_developer64(page=1):

    job_list = job_obj.get_job("pascal software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="jamsa")
	
@pascal.route('/pascal-software-developer-jobs-vammala')
def pascal_software_developer65(page=1):

    job_list = job_obj.get_job("pascal software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="vammala")
	
@pascal.route('/pascal-software-developer-jobs-nastola')
def pascal_software_developer66(page=1):

    job_list = job_obj.get_job("pascal software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="nastola")
	
@pascal.route('/pascal-software-developer-jobs-orimattila')
def pascal_software_developer67(page=1):

    job_list = job_obj.get_job("pascal software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="orimattila")
	
@pascal.route('/pascal-software-developer-jobs-kauhajoki')
def pascal_software_developer68(page=1):

    job_list = job_obj.get_job("pascal software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kauhajoki")
	
@pascal.route('/pascal-software-developer-jobs-ekenas')
def pascal_software_developer69(page=1):

    job_list = job_obj.get_job("pascal software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="ekenas")
	
@pascal.route('/pascal-software-developer-jobs-kempele')
def pascal_software_developer70(page=1):

    job_list = job_obj.get_job("pascal software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kempele")
	
@pascal.route('/pascal-software-developer-jobs-lapua')
def pascal_software_developer71(page=1):

    job_list = job_obj.get_job("pascal software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="lapua")
	
@pascal.route('/pascal-software-developer-jobs-lieksa')
def pascal_software_developer72(page=1):

    job_list = job_obj.get_job("pascal software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="lieksa")
	
@pascal.route('/pascal-software-developer-jobs-naantali')
def pascal_software_developer73(page=1):

    job_list = job_obj.get_job("pascal software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="naantali")
	
@pascal.route('/pascal-software-developer-jobs-aanekoski')
def pascal_software_developer74(page=1):

    job_list = job_obj.get_job("pascal software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="aanekoski")
	
@pascal.route('/pascal-software-developer-jobs-ylivieska')
def pascal_software_developer75(page=1):

    job_list = job_obj.get_job("pascal software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="ylivieska")
	
@pascal.route('/pascal-software-developer-jobs-kontiolahti')
def pascal_software_developer76(page=1):

    job_list = job_obj.get_job("pascal software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kontiolahti")
	
@pascal.route('/pascal-software-developer-jobs-kankaanpaa')
def pascal_software_developer77(page=1):

    job_list = job_obj.get_job("pascal software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kankaanpaa")
	
@pascal.route('/pascal-software-developer-jobs-ulvila')
def pascal_software_developer78(page=1):

    job_list = job_obj.get_job("pascal software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="ulvila")
	
@pascal.route('/pascal-software-developer-jobs-pieksamaki')
def pascal_software_developer79(page=1):

    job_list = job_obj.get_job("pascal software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="pieksamaki")
	
@pascal.route('/pascal-software-developer-jobs-kiiminki')
def pascal_software_developer80(page=1):

    job_list = job_obj.get_job("pascal software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kiiminki")
	
@pascal.route('/pascal-software-developer-jobs-pargas')
def pascal_software_developer81(page=1):

    job_list = job_obj.get_job("pascal software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="pargas")
	
@pascal.route('/pascal-software-developer-jobs-nurmo')
def pascal_software_developer82(page=1):

    job_list = job_obj.get_job("pascal software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="nurmo")
	
@pascal.route('/pascal-software-developer-jobs-ilmajoki')
def pascal_software_developer83(page=1):

    job_list = job_obj.get_job("pascal software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="ilmajoki")
	
@pascal.route('/pascal-software-developer-jobs-liperi')
def pascal_software_developer84(page=1):

    job_list = job_obj.get_job("pascal software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="liperi")
	
@pascal.route('/pascal-software-developer-jobs-keuruu')
def pascal_software_developer85(page=1):

    job_list = job_obj.get_job("pascal software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="keuruu")
	
@pascal.route('/pascal-software-developer-jobs-leppavirta')
def pascal_software_developer86(page=1):

    job_list = job_obj.get_job("pascal software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="leppavirta")
	
@pascal.route('/pascal-software-developer-jobs-kurikka')
def pascal_software_developer87(page=1):

    job_list = job_obj.get_job("pascal software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kurikka")
	
@pascal.route('/pascal-software-developer-jobs-nivala')
def pascal_software_developer88(page=1):

    job_list = job_obj.get_job("pascal software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="nivala")
	
@pascal.route('/pascal-software-developer-jobs-joutseno')
def pascal_software_developer89(page=1):

    job_list = job_obj.get_job("pascal software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="joutseno")
	
@pascal.route('/pascal-software-developer-jobs-pedersore')
def pascal_software_developer90(page=1):

    job_list = job_obj.get_job("pascal software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="pedersore")
	
@pascal.route('/pascal-software-developer-jobs-sotkamo')
def pascal_software_developer91(page=1):

    job_list = job_obj.get_job("pascal software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="sotkamo")
	
@pascal.route('/pascal-software-developer-jobs-kuhmo')
def pascal_software_developer92(page=1):

    job_list = job_obj.get_job("pascal software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="kuhmo")
	
@pascal.route('/pascal-software-developer-jobs-paimio')
def pascal_software_developer93(page=1):

    job_list = job_obj.get_job("pascal software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="paimio")
	
@pascal.route('/pascal-software-developer-jobs-saarijarvi')
def pascal_software_developer94(page=1):

    job_list = job_obj.get_job("pascal software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="saarijarvi")
	
@pascal.route('/pascal-software-developer-jobs-helsinki')
def pascal_software_developer95(page=1):

    job_list = job_obj.get_job("pascal software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="pascal software developer", location="helsinki")


####################################################################

