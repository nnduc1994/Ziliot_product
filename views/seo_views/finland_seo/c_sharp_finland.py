from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

c_sharp = Blueprint('c_sharp', __name__)
job_obj = Job()



####################################################################


@c_sharp.route('/c_sharp_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "c#" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  

##############################################
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def c_sharp_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="espoo")

@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def c_sharp_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="tampere")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def c_sharp_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="vantaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def c_sharp_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="turku")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def c_sharp_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="oulu")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def c_sharp_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lahti")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def c_sharp_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kuopio")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def c_sharp_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="jyvvaskyla")

@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def c_sharp_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="pori")

@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def c_sharp_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lappeenranta")	
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def c_sharp_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="vaasa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def c_sharp_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kotka")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def c_sharp_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="joensuu")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def c_sharp_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="hameenlinna")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def c_sharp_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="porvoo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def c_sharp_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="mikkeli")

@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def c_sharp_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="hyvinkaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def c_sharp_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="nurmijarvi")

@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def c_sharp_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="jarvenpaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def c_sharp_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="rauma")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def c_sharp_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lohja")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def c_sharp_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="karleby")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def c_sharp_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kajaani")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def c_sharp_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="rovaniemi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def c_sharp_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="tuusula")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def c_sharp_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kirkkonummi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def c_sharp_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="seinajoki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def c_sharp_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kerava")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def c_sharp_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kouvola")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def c_sharp_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="imatra")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def c_sharp_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="nokia")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def c_sharp_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="savonlinna")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def c_sharp_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="riihimaki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def c_sharp_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="vihti")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def c_sharp_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="salo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def c_sharp_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kangasala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def c_sharp_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="raisio")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def c_sharp_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="karhula")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def c_sharp_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kemi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def c_sharp_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="iisalmi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def c_sharp_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="varkaus")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def c_sharp_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="raahe")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def c_sharp_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="ylojarvi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def c_sharp_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="hamina")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def c_sharp_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kaarina")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def c_sharp_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="tornio")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def c_sharp_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="heinola")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def c_sharp_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="hollola")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def c_sharp_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="valkeakoski")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def c_sharp_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="siilinjarvi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def c_sharp_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kuusankoski")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def c_sharp_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="sibbo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def c_sharp_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="jakostad")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def c_sharp_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lempaala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def c_sharp_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="mantsala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def c_sharp_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="forssa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def c_sharp_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kuusamo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def c_sharp_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="haukipudas")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def c_sharp_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="korsholm")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def c_sharp_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="laukaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def c_sharp_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="anjala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def c_sharp_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="uusikaupunki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def c_sharp_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="janakkala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def c_sharp_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="pirkkala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def c_sharp_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def c_sharp_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="jamsa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def c_sharp_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="jamsa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def c_sharp_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="vammala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def c_sharp_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="nastola")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def c_sharp_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="orimattila")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def c_sharp_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kauhajoki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def c_sharp_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="ekenas")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def c_sharp_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kempele")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def c_sharp_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lapua")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def c_sharp_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lieksa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def c_sharp_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="naantali")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def c_sharp_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="aanekoski")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def c_sharp_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="ylivieska")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def c_sharp_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kontiolahti")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def c_sharp_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kankaanpaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def c_sharp_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="ulvila")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def c_sharp_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="pieksamaki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def c_sharp_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kiiminki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def c_sharp_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="pargas")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def c_sharp_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="nurmo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def c_sharp_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="ilmajoki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def c_sharp_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="liperi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def c_sharp_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="keuruu")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def c_sharp_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="leppavirta")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def c_sharp_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kurikka")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def c_sharp_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="nivala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def c_sharp_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="joutseno")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def c_sharp_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="pedersore")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def c_sharp_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="sotkamo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def c_sharp_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kuhmo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def c_sharp_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="paimio")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def c_sharp_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="saarijarvi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def c_sharp_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-espoo')
def c_sharp_ohjelmistosuunnittelija_tyopaikat2(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="espoo")

@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-tampere')
def c_sharp_ohjelmistosuunnittelija_tyopaikat3(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="tampere")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-vantaa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat4(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="vantaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-turku')
def c_sharp_ohjelmistosuunnittelija_tyopaikat5(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="turku")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-oulu')
def c_sharp_ohjelmistosuunnittelija_tyopaikat6(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="oulu")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-lahti')
def c_sharp_ohjelmistosuunnittelija_tyopaikat7(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lahti")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kuopio')
def c_sharp_ohjelmistosuunnittelija_tyopaikat8(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kuopio")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-jyvvaskyla')
def c_sharp_ohjelmistosuunnittelija_tyopaikat9(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="jyvvaskyla")

@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-pori')
def c_sharp_ohjelmistosuunnittelija_tyopaikat10(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="pori")

@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-lappeenranta')
def c_sharp_ohjelmistosuunnittelija_tyopaikat11(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lappeenranta")	
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-vaasa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat12(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="vaasa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kotka')
def c_sharp_ohjelmistosuunnittelija_tyopaikat13(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kotka")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-joensuu')
def c_sharp_ohjelmistosuunnittelija_tyopaikat14(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="joensuu")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-hameenlinna')
def c_sharp_ohjelmistosuunnittelija_tyopaikat15(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="hameenlinna")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-porvoo')
def c_sharp_ohjelmistosuunnittelija_tyopaikat16(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="porvoo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-mikkeli')
def c_sharp_ohjelmistosuunnittelija_tyopaikat17(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="mikkeli")

@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-hyvinkaa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat18(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="hyvinkaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-nurmijarvi')
def c_sharp_ohjelmistosuunnittelija_tyopaikat19(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="nurmijarvi")

@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-jarvenpaa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat20(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="jarvenpaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-rauma')
def c_sharp_ohjelmistosuunnittelija_tyopaikat21(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="rauma")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-lohja')
def c_sharp_ohjelmistosuunnittelija_tyopaikat22(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lohja")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-karleby')
def c_sharp_ohjelmistosuunnittelija_tyopaikat23(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="karleby")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kajaani')
def c_sharp_ohjelmistosuunnittelija_tyopaikat24(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kajaani")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-rovaniemi')
def c_sharp_ohjelmistosuunnittelija_tyopaikat25(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="rovaniemi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-tuusula')
def c_sharp_ohjelmistosuunnittelija_tyopaikat26(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="tuusula")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kirkkonummi')
def c_sharp_ohjelmistosuunnittelija_tyopaikat27(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kirkkonummi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-seinajoki')
def c_sharp_ohjelmistosuunnittelija_tyopaikat28(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="seinajoki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kerava')
def c_sharp_ohjelmistosuunnittelija_tyopaikat29(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kerava")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kouvola')
def c_sharp_ohjelmistosuunnittelija_tyopaikat30(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kouvola")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-imatra')
def c_sharp_ohjelmistosuunnittelija_tyopaikat31(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="imatra")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-nokia')
def c_sharp_ohjelmistosuunnittelija_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="nokia")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-savonlinna')
def c_sharp_ohjelmistosuunnittelija_tyopaikat32(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="savonlinna")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-riihimaki')
def c_sharp_ohjelmistosuunnittelija_tyopaikat33(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="riihimaki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-vihti')
def c_sharp_ohjelmistosuunnittelija_tyopaikat34(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="vihti")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-salo')
def c_sharp_ohjelmistosuunnittelija_tyopaikat35(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="salo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kangasala')
def c_sharp_ohjelmistosuunnittelija_tyopaikat36(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kangasala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-raisio')
def c_sharp_ohjelmistosuunnittelija_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="raisio")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-karhula')
def c_sharp_ohjelmistosuunnittelija_tyopaikat37(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="karhula")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kemi')
def c_sharp_ohjelmistosuunnittelija_tyopaikat38(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kemi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-iisalmi')
def c_sharp_ohjelmistosuunnittelija_tyopaikat39(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="iisalmi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-varkaus')
def c_sharp_ohjelmistosuunnittelija_tyopaikat40(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="varkaus")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-raahe')
def c_sharp_ohjelmistosuunnittelija_tyopaikat41(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="raahe")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-ylojarvi')
def c_sharp_ohjelmistosuunnittelija_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="ylojarvi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-hamina')
def c_sharp_ohjelmistosuunnittelija_tyopaikat42(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="hamina")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kaarina')
def c_sharp_ohjelmistosuunnittelija_tyopaikat43(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kaarina")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-tornio')
def c_sharp_ohjelmistosuunnittelija_tyopaikat44(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="tornio")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-heinola')
def c_sharp_ohjelmistosuunnittelija_tyopaikat45(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="heinola")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-hollola')
def c_sharp_ohjelmistosuunnittelija_tyopaikat46(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="hollola")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-valkeakoski')
def c_sharp_ohjelmistosuunnittelija_tyopaikat47(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="valkeakoski")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-siilinjarvi')
def c_sharp_ohjelmistosuunnittelija_tyopaikat48(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="siilinjarvi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kuusankoski')
def c_sharp_ohjelmistosuunnittelija_tyopaikat49(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kuusankoski")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-sibbo')
def c_sharp_ohjelmistosuunnittelija_tyopaikat50(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="sibbo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-jakostad')
def c_sharp_ohjelmistosuunnittelija_tyopaikat51(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="jakostad")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-lempaala')
def c_sharp_ohjelmistosuunnittelija_tyopaikat52(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lempaala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-mantsala')
def c_sharp_ohjelmistosuunnittelija_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="mantsala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-forssa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat53(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="forssa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kuusamo')
def c_sharp_ohjelmistosuunnittelija_tyopaikat54(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kuusamo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-haukipudas')
def c_sharp_ohjelmistosuunnittelija_tyopaikat55(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="haukipudas")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-korsholm')
def c_sharp_ohjelmistosuunnittelija_tyopaikat56(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="korsholm")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-laukaa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat57(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="laukaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-anjala')
def c_sharp_ohjelmistosuunnittelija_tyopaikat58(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="anjala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-uusikaupunki')
def c_sharp_ohjelmistosuunnittelija_tyopaikat59(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="uusikaupunki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-janakkala')
def c_sharp_ohjelmistosuunnittelija_tyopaikat60(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="janakkala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-pirkkala')
def c_sharp_ohjelmistosuunnittelija_tyopaikat61(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="pirkkala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-lansi-turunmaa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat62(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-jamsa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat63(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="jamsa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-jamsa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat64(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="jamsa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-vammala')
def c_sharp_ohjelmistosuunnittelija_tyopaikat65(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="vammala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-nastola')
def c_sharp_ohjelmistosuunnittelija_tyopaikat66(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="nastola")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-orimattila')
def c_sharp_ohjelmistosuunnittelija_tyopaikat67(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="orimattila")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kauhajoki')
def c_sharp_ohjelmistosuunnittelija_tyopaikat68(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kauhajoki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-ekenas')
def c_sharp_ohjelmistosuunnittelija_tyopaikat69(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="ekenas")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kempele')
def c_sharp_ohjelmistosuunnittelija_tyopaikat70(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kempele")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-lapua')
def c_sharp_ohjelmistosuunnittelija_tyopaikat71(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lapua")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-lieksa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat72(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="lieksa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-naantali')
def c_sharp_ohjelmistosuunnittelija_tyopaikat73(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="naantali")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-aanekoski')
def c_sharp_ohjelmistosuunnittelija_tyopaikat74(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="aanekoski")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-ylivieska')
def c_sharp_ohjelmistosuunnittelija_tyopaikat75(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="ylivieska")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kontiolahti')
def c_sharp_ohjelmistosuunnittelija_tyopaikat76(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kontiolahti")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kankaanpaa')
def c_sharp_ohjelmistosuunnittelija_tyopaikat77(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kankaanpaa")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-ulvila')
def c_sharp_ohjelmistosuunnittelija_tyopaikat78(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="ulvila")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-pieksamaki')
def c_sharp_ohjelmistosuunnittelija_tyopaikat79(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="pieksamaki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kiiminki')
def c_sharp_ohjelmistosuunnittelija_tyopaikat80(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kiiminki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-pargas')
def c_sharp_ohjelmistosuunnittelija_tyopaikat81(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="pargas")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-nurmo')
def c_sharp_ohjelmistosuunnittelija_tyopaikat82(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="nurmo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-ilmajoki')
def c_sharp_ohjelmistosuunnittelija_tyopaikat83(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="ilmajoki")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-liperi')
def c_sharp_ohjelmistosuunnittelija_tyopaikat84(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="liperi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-keuruu')
def c_sharp_ohjelmistosuunnittelija_tyopaikat85(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="keuruu")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-leppavirta')
def c_sharp_ohjelmistosuunnittelija_tyopaikat86(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="leppavirta")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kurikka')
def c_sharp_ohjelmistosuunnittelija_tyopaikat87(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kurikka")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-nivala')
def c_sharp_ohjelmistosuunnittelija_tyopaikat88(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="nivala")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-joutseno')
def c_sharp_ohjelmistosuunnittelija_tyopaikat89(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="joutseno")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-pedersore')
def c_sharp_ohjelmistosuunnittelija_tyopaikat90(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="pedersore")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-sotkamo')
def c_sharp_ohjelmistosuunnittelija_tyopaikat91(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="sotkamo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-kuhmo')
def c_sharp_ohjelmistosuunnittelija_tyopaikat92(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="kuhmo")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-paimio')
def c_sharp_ohjelmistosuunnittelija_tyopaikat93(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="paimio")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-saarijarvi')
def c_sharp_ohjelmistosuunnittelija_tyopaikat94(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="saarijarvi")
	
@c_sharp.route('/c#-ohjelmistosuunnittelija-tyopaikat-helsinki')
def c_sharp_ohjelmistosuunnittelija_tyopaikat95(page=1):

    job_list = job_obj.get_job("c# ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@c_sharp.route('/c#-software-developer-jobs-espoo')
def c_sharp_software_developer2(page=1):

    job_list = job_obj.get_job("c# software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="espoo")

@c_sharp.route('/c#-software-developer-jobs-tampere')
def c_sharp_software_developer3(page=1):

    job_list = job_obj.get_job("c# software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="tampere")
	
@c_sharp.route('/c#-software-developer-jobs-vantaa')
def c_sharp_software_developer4(page=1):

    job_list = job_obj.get_job("c# software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="vantaa")
	
@c_sharp.route('/c#-software-developer-jobs-turku')
def c_sharp_software_developer5(page=1):

    job_list = job_obj.get_job("c# software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="turku")
	
@c_sharp.route('/c#-software-developer-jobs-oulu')
def c_sharp_software_developer6(page=1):

    job_list = job_obj.get_job("c# software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="oulu")
	
@c_sharp.route('/c#-software-developer-jobs-lahti')
def c_sharp_software_developer7(page=1):

    job_list = job_obj.get_job("c# software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="lahti")
	
@c_sharp.route('/c#-software-developer-jobs-kuopio')
def c_sharp_software_developer8(page=1):

    job_list = job_obj.get_job("c# software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kuopio")
	
@c_sharp.route('/c#-software-developer-jobs-jyvvaskyla')
def c_sharp_software_developer9(page=1):

    job_list = job_obj.get_job("c# software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="jyvvaskyla")

@c_sharp.route('/c#-software-developer-jobs-pori')
def c_sharp_software_developer10(page=1):

    job_list = job_obj.get_job("c# software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="pori")

@c_sharp.route('/c#-software-developer-jobs-lappeenranta')
def c_sharp_software_developer11(page=1):

    job_list = job_obj.get_job("c# software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="lappeenranta")	
	
@c_sharp.route('/c#-software-developer-jobs-vaasa')
def c_sharp_software_developer12(page=1):

    job_list = job_obj.get_job("c# software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="vaasa")
	
@c_sharp.route('/c#-software-developer-jobs-kotka')
def c_sharp_software_developer13(page=1):

    job_list = job_obj.get_job("c# software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kotka")
	
@c_sharp.route('/c#-software-developer-jobs-joensuu')
def c_sharp_software_developer14(page=1):

    job_list = job_obj.get_job("c# software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="joensuu")
	
@c_sharp.route('/c#-software-developer-jobs-hameenlinna')
def c_sharp_software_developer15(page=1):

    job_list = job_obj.get_job("c# software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="hameenlinna")
	
@c_sharp.route('/c#-software-developer-jobs-porvoo')
def c_sharp_software_developer16(page=1):

    job_list = job_obj.get_job("c# software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="porvoo")
	
@c_sharp.route('/c#-software-developer-jobs-mikkeli')
def c_sharp_software_developer17(page=1):

    job_list = job_obj.get_job("c# software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="mikkeli")

@c_sharp.route('/c#-software-developer-jobs-hyvinkaa')
def c_sharp_software_developer18(page=1):

    job_list = job_obj.get_job("c# software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="hyvinkaa")
	
@c_sharp.route('/c#-software-developer-jobs-nurmijarvi')
def c_sharp_software_developer19(page=1):

    job_list = job_obj.get_job("c# software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="nurmijarvi")

@c_sharp.route('/c#-software-developer-jobs-jarvenpaa')
def c_sharp_software_developer20(page=1):

    job_list = job_obj.get_job("c# software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="jarvenpaa")
	
@c_sharp.route('/c#-software-developer-jobs-rauma')
def c_sharp_software_developer21(page=1):

    job_list = job_obj.get_job("c# software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="rauma")
	
@c_sharp.route('/c#-software-developer-jobs-lohja')
def c_sharp_software_developer22(page=1):

    job_list = job_obj.get_job("c# software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="lohja")
	
@c_sharp.route('/c#-software-developer-jobs-karleby')
def c_sharp_software_developer23(page=1):

    job_list = job_obj.get_job("c# software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="karleby")
	
@c_sharp.route('/c#-software-developer-jobs-kajaani')
def c_sharp_software_developer24(page=1):

    job_list = job_obj.get_job("c# software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kajaani")
	
@c_sharp.route('/c#-software-developer-jobs-rovaniemi')
def c_sharp_software_developer25(page=1):

    job_list = job_obj.get_job("c# software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="rovaniemi")
	
@c_sharp.route('/c#-software-developer-jobs-tuusula')
def c_sharp_software_developer26(page=1):

    job_list = job_obj.get_job("c# software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="tuusula")
	
@c_sharp.route('/c#-software-developer-jobs-kirkkonummi')
def c_sharp_software_developer27(page=1):

    job_list = job_obj.get_job("c# software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kirkkonummi")
	
@c_sharp.route('/c#-software-developer-jobs-seinajoki')
def c_sharp_software_developer28(page=1):

    job_list = job_obj.get_job("c# software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="seinajoki")
	
@c_sharp.route('/c#-software-developer-jobs-kerava')
def c_sharp_software_developer29(page=1):

    job_list = job_obj.get_job("c# software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kerava")
	
@c_sharp.route('/c#-software-developer-jobs-kouvola')
def c_sharp_software_developer30(page=1):

    job_list = job_obj.get_job("c# software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kouvola")
	
@c_sharp.route('/c#-software-developer-jobs-imatra')
def c_sharp_software_developer31(page=1):

    job_list = job_obj.get_job("c# software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="imatra")
	
@c_sharp.route('/c#-software-developer-jobs-nokia')
def c_sharp_software_developer32_1(page=1):

    job_list = job_obj.get_job("c# software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="nokia")
	
@c_sharp.route('/c#-software-developer-jobs-savonlinna')
def c_sharp_software_developer32(page=1):

    job_list = job_obj.get_job("c# software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="savonlinna")
	
@c_sharp.route('/c#-software-developer-jobs-riihimaki')
def c_sharp_software_developer33(page=1):

    job_list = job_obj.get_job("c# software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="riihimaki")
	
@c_sharp.route('/c#-software-developer-jobs-vihti')
def c_sharp_software_developer34(page=1):

    job_list = job_obj.get_job("c# software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="vihti")
	
@c_sharp.route('/c#-software-developer-jobs-salo')
def c_sharp_software_developer35(page=1):

    job_list = job_obj.get_job("c# software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="salo")
	
@c_sharp.route('/c#-software-developer-jobs-kangasala')
def c_sharp_software_developer36(page=1):

    job_list = job_obj.get_job("c# software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kangasala")
	
@c_sharp.route('/c#-software-developer-jobs-raisio')
def c_sharp_software_developer37_1(page=1):

    job_list = job_obj.get_job("c# software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="raisio")
	
@c_sharp.route('/c#-software-developer-jobs-karhula')
def c_sharp_software_developer37(page=1):

    job_list = job_obj.get_job("c# software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="karhula")
	
@c_sharp.route('/c#-software-developer-jobs-kemi')
def c_sharp_software_developer38(page=1):

    job_list = job_obj.get_job("c# software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kemi")
	
@c_sharp.route('/c#-software-developer-jobs-iisalmi')
def c_sharp_software_developer39(page=1):

    job_list = job_obj.get_job("c# software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="iisalmi")
	
@c_sharp.route('/c#-software-developer-jobs-varkaus')
def c_sharp_software_developer40(page=1):

    job_list = job_obj.get_job("c# software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="varkaus")
	
@c_sharp.route('/c#-software-developer-jobs-raahe')
def c_sharp_software_developer41(page=1):

    job_list = job_obj.get_job("c# software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="raahe")
	
@c_sharp.route('/c#-software-developer-jobs-ylojarvi')
def c_sharp_software_developer42_1(page=1):

    job_list = job_obj.get_job("c# software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="ylojarvi")
	
@c_sharp.route('/c#-software-developer-jobs-hamina')
def c_sharp_software_developer42(page=1):

    job_list = job_obj.get_job("c# software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="hamina")
	
@c_sharp.route('/c#-software-developer-jobs-kaarina')
def c_sharp_software_developer43(page=1):

    job_list = job_obj.get_job("c# software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kaarina")
	
@c_sharp.route('/c#-software-developer-jobs-tornio')
def c_sharp_software_developer44(page=1):

    job_list = job_obj.get_job("c# software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="tornio")
	
@c_sharp.route('/c#-software-developer-jobs-heinola')
def c_sharp_software_developer45(page=1):

    job_list = job_obj.get_job("c# software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="heinola")
	
@c_sharp.route('/c#-software-developer-jobs-hollola')
def c_sharp_software_developer46(page=1):

    job_list = job_obj.get_job("c# software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="hollola")
	
@c_sharp.route('/c#-software-developer-jobs-valkeakoski')
def c_sharp_software_developer47(page=1):

    job_list = job_obj.get_job("c# software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="valkeakoski")
	
@c_sharp.route('/c#-software-developer-jobs-siilinjarvi')
def c_sharp_software_developer48(page=1):

    job_list = job_obj.get_job("c# software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="siilinjarvi")
	
@c_sharp.route('/c#-software-developer-jobs-kuusankoski')
def c_sharp_software_developer49(page=1):

    job_list = job_obj.get_job("c# software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kuusankoski")
	
@c_sharp.route('/c#-software-developer-jobs-sibbo')
def c_sharp_software_developer50(page=1):

    job_list = job_obj.get_job("c# software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="sibbo")
	
@c_sharp.route('/c#-software-developer-jobs-jakostad')
def c_sharp_software_developer51(page=1):

    job_list = job_obj.get_job("c# software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="jakostad")
	
@c_sharp.route('/c#-software-developer-jobs-lempaala')
def c_sharp_software_developer52(page=1):

    job_list = job_obj.get_job("c# software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="lempaala")
	
@c_sharp.route('/c#-software-developer-jobs-mantsala')
def c_sharp_software_developer52_1(page=1):

    job_list = job_obj.get_job("c# software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="mantsala")
	
@c_sharp.route('/c#-software-developer-jobs-forssa')
def c_sharp_software_developer53(page=1):

    job_list = job_obj.get_job("c# software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="forssa")
	
@c_sharp.route('/c#-software-developer-jobs-kuusamo')
def c_sharp_software_developer54(page=1):

    job_list = job_obj.get_job("c# software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kuusamo")
	
@c_sharp.route('/c#-software-developer-jobs-haukipudas')
def c_sharp_software_developer55(page=1):

    job_list = job_obj.get_job("c# software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="haukipudas")
	
@c_sharp.route('/c#-software-developer-jobs-korsholm')
def c_sharp_software_developer56(page=1):

    job_list = job_obj.get_job("c# software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="korsholm")
	
@c_sharp.route('/c#-software-developer-jobs-laukaa')
def c_sharp_software_developer57(page=1):

    job_list = job_obj.get_job("c# software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="laukaa")
	
@c_sharp.route('/c#-software-developer-jobs-anjala')
def c_sharp_software_developer58(page=1):

    job_list = job_obj.get_job("c# software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="anjala")
	
@c_sharp.route('/c#-software-developer-jobs-uusikaupunki')
def c_sharp_software_developer59(page=1):

    job_list = job_obj.get_job("c# software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="uusikaupunki")
	
@c_sharp.route('/c#-software-developer-jobs-janakkala')
def c_sharp_software_developer60(page=1):

    job_list = job_obj.get_job("c# software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="janakkala")
	
@c_sharp.route('/c#-software-developer-jobs-pirkkala')
def c_sharp_software_developer61(page=1):

    job_list = job_obj.get_job("c# software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="pirkkala")
	
@c_sharp.route('/c#-software-developer-jobs-lansi-turunmaa')
def c_sharp_software_developer62(page=1):

    job_list = job_obj.get_job("c# software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="lansi-turunmaa")
	
@c_sharp.route('/c#-software-developer-jobs-jamsa')
def c_sharp_software_developer63(page=1):

    job_list = job_obj.get_job("c# software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="jamsa")
	
@c_sharp.route('/c#-software-developer-jobs-jamsa')
def c_sharp_software_developer64(page=1):

    job_list = job_obj.get_job("c# software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="jamsa")
	
@c_sharp.route('/c#-software-developer-jobs-vammala')
def c_sharp_software_developer65(page=1):

    job_list = job_obj.get_job("c# software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="vammala")
	
@c_sharp.route('/c#-software-developer-jobs-nastola')
def c_sharp_software_developer66(page=1):

    job_list = job_obj.get_job("c# software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="nastola")
	
@c_sharp.route('/c#-software-developer-jobs-orimattila')
def c_sharp_software_developer67(page=1):

    job_list = job_obj.get_job("c# software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="orimattila")
	
@c_sharp.route('/c#-software-developer-jobs-kauhajoki')
def c_sharp_software_developer68(page=1):

    job_list = job_obj.get_job("c# software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kauhajoki")
	
@c_sharp.route('/c#-software-developer-jobs-ekenas')
def c_sharp_software_developer69(page=1):

    job_list = job_obj.get_job("c# software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="ekenas")
	
@c_sharp.route('/c#-software-developer-jobs-kempele')
def c_sharp_software_developer70(page=1):

    job_list = job_obj.get_job("c# software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kempele")
	
@c_sharp.route('/c#-software-developer-jobs-lapua')
def c_sharp_software_developer71(page=1):

    job_list = job_obj.get_job("c# software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="lapua")
	
@c_sharp.route('/c#-software-developer-jobs-lieksa')
def c_sharp_software_developer72(page=1):

    job_list = job_obj.get_job("c# software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="lieksa")
	
@c_sharp.route('/c#-software-developer-jobs-naantali')
def c_sharp_software_developer73(page=1):

    job_list = job_obj.get_job("c# software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="naantali")
	
@c_sharp.route('/c#-software-developer-jobs-aanekoski')
def c_sharp_software_developer74(page=1):

    job_list = job_obj.get_job("c# software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="aanekoski")
	
@c_sharp.route('/c#-software-developer-jobs-ylivieska')
def c_sharp_software_developer75(page=1):

    job_list = job_obj.get_job("c# software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="ylivieska")
	
@c_sharp.route('/c#-software-developer-jobs-kontiolahti')
def c_sharp_software_developer76(page=1):

    job_list = job_obj.get_job("c# software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kontiolahti")
	
@c_sharp.route('/c#-software-developer-jobs-kankaanpaa')
def c_sharp_software_developer77(page=1):

    job_list = job_obj.get_job("c# software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kankaanpaa")
	
@c_sharp.route('/c#-software-developer-jobs-ulvila')
def c_sharp_software_developer78(page=1):

    job_list = job_obj.get_job("c# software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="ulvila")
	
@c_sharp.route('/c#-software-developer-jobs-pieksamaki')
def c_sharp_software_developer79(page=1):

    job_list = job_obj.get_job("c# software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="pieksamaki")
	
@c_sharp.route('/c#-software-developer-jobs-kiiminki')
def c_sharp_software_developer80(page=1):

    job_list = job_obj.get_job("c# software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kiiminki")
	
@c_sharp.route('/c#-software-developer-jobs-pargas')
def c_sharp_software_developer81(page=1):

    job_list = job_obj.get_job("c# software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="pargas")
	
@c_sharp.route('/c#-software-developer-jobs-nurmo')
def c_sharp_software_developer82(page=1):

    job_list = job_obj.get_job("c# software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="nurmo")
	
@c_sharp.route('/c#-software-developer-jobs-ilmajoki')
def c_sharp_software_developer83(page=1):

    job_list = job_obj.get_job("c# software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="ilmajoki")
	
@c_sharp.route('/c#-software-developer-jobs-liperi')
def c_sharp_software_developer84(page=1):

    job_list = job_obj.get_job("c# software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="liperi")
	
@c_sharp.route('/c#-software-developer-jobs-keuruu')
def c_sharp_software_developer85(page=1):

    job_list = job_obj.get_job("c# software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="keuruu")
	
@c_sharp.route('/c#-software-developer-jobs-leppavirta')
def c_sharp_software_developer86(page=1):

    job_list = job_obj.get_job("c# software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="leppavirta")
	
@c_sharp.route('/c#-software-developer-jobs-kurikka')
def c_sharp_software_developer87(page=1):

    job_list = job_obj.get_job("c# software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kurikka")
	
@c_sharp.route('/c#-software-developer-jobs-nivala')
def c_sharp_software_developer88(page=1):

    job_list = job_obj.get_job("c# software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="nivala")
	
@c_sharp.route('/c#-software-developer-jobs-joutseno')
def c_sharp_software_developer89(page=1):

    job_list = job_obj.get_job("c# software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="joutseno")
	
@c_sharp.route('/c#-software-developer-jobs-pedersore')
def c_sharp_software_developer90(page=1):

    job_list = job_obj.get_job("c# software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="pedersore")
	
@c_sharp.route('/c#-software-developer-jobs-sotkamo')
def c_sharp_software_developer91(page=1):

    job_list = job_obj.get_job("c# software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="sotkamo")
	
@c_sharp.route('/c#-software-developer-jobs-kuhmo')
def c_sharp_software_developer92(page=1):

    job_list = job_obj.get_job("c# software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="kuhmo")
	
@c_sharp.route('/c#-software-developer-jobs-paimio')
def c_sharp_software_developer93(page=1):

    job_list = job_obj.get_job("c# software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="paimio")
	
@c_sharp.route('/c#-software-developer-jobs-saarijarvi')
def c_sharp_software_developer94(page=1):

    job_list = job_obj.get_job("c# software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="saarijarvi")
	
@c_sharp.route('/c#-software-developer-jobs-helsinki')
def c_sharp_software_developer95(page=1):

    job_list = job_obj.get_job("c# software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="c# software developer", location="helsinki")


####################################################################