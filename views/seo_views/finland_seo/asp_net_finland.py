from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

asp_net = Blueprint('asp_net', __name__)
job_obj = Job()



####################################################################


@asp_net.route('/asp.net_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "asp.net" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def asp_net_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="espoo")

@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def asp_net_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="tampere")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def asp_net_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="vantaa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def asp_net_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="turku")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def asp_net_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="oulu")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def asp_net_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="lahti")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def asp_net_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kuopio")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def asp_net_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="jyvvaskyla")

@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def asp_net_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="pori")

@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def asp_net_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="lappeenranta")	
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def asp_net_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="vaasa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def asp_net_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kotka")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def asp_net_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="joensuu")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def asp_net_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="hameenlinna")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def asp_net_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="porvoo")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def asp_net_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="mikkeli")

@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def asp_net_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="hyvinkaa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def asp_net_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="nurmijarvi")

@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def asp_net_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="jarvenpaa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def asp_net_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="rauma")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def asp_net_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="lohja")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def asp_net_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="karleby")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def asp_net_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kajaani")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def asp_net_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="rovaniemi")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def asp_net_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="tuusula")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def asp_net_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kirkkonummi")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def asp_net_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="seinajoki")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def asp_net_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kerava")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def asp_net_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kouvola")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def asp_net_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="imatra")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def asp_net_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="nokia")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def asp_net_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="savonlinna")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def asp_net_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="riihimaki")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def asp_net_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="vihti")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def asp_net_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="salo")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def asp_net_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kangasala")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def asp_net_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="raisio")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def asp_net_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="karhula")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def asp_net_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kemi")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def asp_net_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="iisalmi")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def asp_net_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="varkaus")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def asp_net_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="raahe")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def asp_net_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="ylojarvi")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def asp_net_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="hamina")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def asp_net_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kaarina")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def asp_net_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="tornio")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def asp_net_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="heinola")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def asp_net_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="hollola")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def asp_net_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="valkeakoski")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def asp_net_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="siilinjarvi")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def asp_net_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kuusankoski")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def asp_net_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="sibbo")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def asp_net_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="jakostad")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def asp_net_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="lempaala")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def asp_net_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="mantsala")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def asp_net_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="forssa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def asp_net_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kuusamo")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def asp_net_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="haukipudas")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def asp_net_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="korsholm")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def asp_net_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="laukaa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def asp_net_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="anjala")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def asp_net_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="uusikaupunki")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def asp_net_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="janakkala")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def asp_net_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="pirkkala")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def asp_net_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def asp_net_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="jamsa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def asp_net_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="jamsa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def asp_net_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="vammala")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def asp_net_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="nastola")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def asp_net_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="orimattila")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def asp_net_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kauhajoki")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def asp_net_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="ekenas")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def asp_net_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kempele")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def asp_net_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="lapua")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def asp_net_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="lieksa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def asp_net_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="naantali")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def asp_net_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="aanekoski")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def asp_net_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="ylivieska")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def asp_net_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kontiolahti")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def asp_net_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kankaanpaa")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def asp_net_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="ulvila")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def asp_net_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="pieksamaki")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def asp_net_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kiiminki")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def asp_net_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="pargas")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def asp_net_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="nurmo")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def asp_net_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="ilmajoki")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def asp_net_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="liperi")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def asp_net_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="keuruu")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def asp_net_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="leppavirta")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def asp_net_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kurikka")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def asp_net_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="nivala")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def asp_net_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="joutseno")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def asp_net_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="pedersore")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def asp_net_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="sotkamo")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def asp_net_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="kuhmo")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def asp_net_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="paimio")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def asp_net_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="saarijarvi")
	
@asp_net.route('/asp.net-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def asp_net_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("asp.net ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@asp_net.route('/asp.net-software-developer-jobs-espoo')
def asp_net_software_developer2(page=1):

    job_list = job_obj.get_job("asp.net software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="espoo")

@asp_net.route('/asp.net-software-developer-jobs-tampere')
def asp_net_software_developer3(page=1):

    job_list = job_obj.get_job("asp.net software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="tampere")
	
@asp_net.route('/asp.net-software-developer-jobs-vantaa')
def asp_net_software_developer4(page=1):

    job_list = job_obj.get_job("asp.net software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="vantaa")
	
@asp_net.route('/asp.net-software-developer-jobs-turku')
def asp_net_software_developer5(page=1):

    job_list = job_obj.get_job("asp.net software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="turku")
	
@asp_net.route('/asp.net-software-developer-jobs-oulu')
def asp_net_software_developer6(page=1):

    job_list = job_obj.get_job("asp.net software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="oulu")
	
@asp_net.route('/asp.net-software-developer-jobs-lahti')
def asp_net_software_developer7(page=1):

    job_list = job_obj.get_job("asp.net software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="lahti")
	
@asp_net.route('/asp.net-software-developer-jobs-kuopio')
def asp_net_software_developer8(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kuopio")
	
@asp_net.route('/asp.net-software-developer-jobs-jyvvaskyla')
def asp_net_software_developer9(page=1):

    job_list = job_obj.get_job("asp.net software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="jyvvaskyla")

@asp_net.route('/asp.net-software-developer-jobs-pori')
def asp_net_software_developer10(page=1):

    job_list = job_obj.get_job("asp.net software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="pori")

@asp_net.route('/asp.net-software-developer-jobs-lappeenranta')
def asp_net_software_developer11(page=1):

    job_list = job_obj.get_job("asp.net software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="lappeenranta")	
	
@asp_net.route('/asp.net-software-developer-jobs-vaasa')
def asp_net_software_developer12(page=1):

    job_list = job_obj.get_job("asp.net software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="vaasa")
	
@asp_net.route('/asp.net-software-developer-jobs-kotka')
def asp_net_software_developer13(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kotka")
	
@asp_net.route('/asp.net-software-developer-jobs-joensuu')
def asp_net_software_developer14(page=1):

    job_list = job_obj.get_job("asp.net software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="joensuu")
	
@asp_net.route('/asp.net-software-developer-jobs-hameenlinna')
def asp_net_software_developer15(page=1):

    job_list = job_obj.get_job("asp.net software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="hameenlinna")
	
@asp_net.route('/asp.net-software-developer-jobs-porvoo')
def asp_net_software_developer16(page=1):

    job_list = job_obj.get_job("asp.net software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="porvoo")
	
@asp_net.route('/asp.net-software-developer-jobs-mikkeli')
def asp_net_software_developer17(page=1):

    job_list = job_obj.get_job("asp.net software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="mikkeli")

@asp_net.route('/asp.net-software-developer-jobs-hyvinkaa')
def asp_net_software_developer18(page=1):

    job_list = job_obj.get_job("asp.net software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="hyvinkaa")
	
@asp_net.route('/asp.net-software-developer-jobs-nurmijarvi')
def asp_net_software_developer19(page=1):

    job_list = job_obj.get_job("asp.net software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="nurmijarvi")

@asp_net.route('/asp.net-software-developer-jobs-jarvenpaa')
def asp_net_software_developer20(page=1):

    job_list = job_obj.get_job("asp.net software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="jarvenpaa")
	
@asp_net.route('/asp.net-software-developer-jobs-rauma')
def asp_net_software_developer21(page=1):

    job_list = job_obj.get_job("asp.net software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="rauma")
	
@asp_net.route('/asp.net-software-developer-jobs-lohja')
def asp_net_software_developer22(page=1):

    job_list = job_obj.get_job("asp.net software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="lohja")
	
@asp_net.route('/asp.net-software-developer-jobs-karleby')
def asp_net_software_developer23(page=1):

    job_list = job_obj.get_job("asp.net software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="karleby")
	
@asp_net.route('/asp.net-software-developer-jobs-kajaani')
def asp_net_software_developer24(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kajaani")
	
@asp_net.route('/asp.net-software-developer-jobs-rovaniemi')
def asp_net_software_developer25(page=1):

    job_list = job_obj.get_job("asp.net software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="rovaniemi")
	
@asp_net.route('/asp.net-software-developer-jobs-tuusula')
def asp_net_software_developer26(page=1):

    job_list = job_obj.get_job("asp.net software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="tuusula")
	
@asp_net.route('/asp.net-software-developer-jobs-kirkkonummi')
def asp_net_software_developer27(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kirkkonummi")
	
@asp_net.route('/asp.net-software-developer-jobs-seinajoki')
def asp_net_software_developer28(page=1):

    job_list = job_obj.get_job("asp.net software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="seinajoki")
	
@asp_net.route('/asp.net-software-developer-jobs-kerava')
def asp_net_software_developer29(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kerava")
	
@asp_net.route('/asp.net-software-developer-jobs-kouvola')
def asp_net_software_developer30(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kouvola")
	
@asp_net.route('/asp.net-software-developer-jobs-imatra')
def asp_net_software_developer31(page=1):

    job_list = job_obj.get_job("asp.net software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="imatra")
	
@asp_net.route('/asp.net-software-developer-jobs-nokia')
def asp_net_software_developer32_1(page=1):

    job_list = job_obj.get_job("asp.net software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="nokia")
	
@asp_net.route('/asp.net-software-developer-jobs-savonlinna')
def asp_net_software_developer32(page=1):

    job_list = job_obj.get_job("asp.net software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="savonlinna")
	
@asp_net.route('/asp.net-software-developer-jobs-riihimaki')
def asp_net_software_developer33(page=1):

    job_list = job_obj.get_job("asp.net software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="riihimaki")
	
@asp_net.route('/asp.net-software-developer-jobs-vihti')
def asp_net_software_developer34(page=1):

    job_list = job_obj.get_job("asp.net software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="vihti")
	
@asp_net.route('/asp.net-software-developer-jobs-salo')
def asp_net_software_developer35(page=1):

    job_list = job_obj.get_job("asp.net software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="salo")
	
@asp_net.route('/asp.net-software-developer-jobs-kangasala')
def asp_net_software_developer36(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kangasala")
	
@asp_net.route('/asp.net-software-developer-jobs-raisio')
def asp_net_software_developer37_1(page=1):

    job_list = job_obj.get_job("asp.net software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="raisio")
	
@asp_net.route('/asp.net-software-developer-jobs-karhula')
def asp_net_software_developer37(page=1):

    job_list = job_obj.get_job("asp.net software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="karhula")
	
@asp_net.route('/asp.net-software-developer-jobs-kemi')
def asp_net_software_developer38(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kemi")
	
@asp_net.route('/asp.net-software-developer-jobs-iisalmi')
def asp_net_software_developer39(page=1):

    job_list = job_obj.get_job("asp.net software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="iisalmi")
	
@asp_net.route('/asp.net-software-developer-jobs-varkaus')
def asp_net_software_developer40(page=1):

    job_list = job_obj.get_job("asp.net software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="varkaus")
	
@asp_net.route('/asp.net-software-developer-jobs-raahe')
def asp_net_software_developer41(page=1):

    job_list = job_obj.get_job("asp.net software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="raahe")
	
@asp_net.route('/asp.net-software-developer-jobs-ylojarvi')
def asp_net_software_developer42_1(page=1):

    job_list = job_obj.get_job("asp.net software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="ylojarvi")
	
@asp_net.route('/asp.net-software-developer-jobs-hamina')
def asp_net_software_developer42(page=1):

    job_list = job_obj.get_job("asp.net software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="hamina")
	
@asp_net.route('/asp.net-software-developer-jobs-kaarina')
def asp_net_software_developer43(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kaarina")
	
@asp_net.route('/asp.net-software-developer-jobs-tornio')
def asp_net_software_developer44(page=1):

    job_list = job_obj.get_job("asp.net software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="tornio")
	
@asp_net.route('/asp.net-software-developer-jobs-heinola')
def asp_net_software_developer45(page=1):

    job_list = job_obj.get_job("asp.net software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="heinola")
	
@asp_net.route('/asp.net-software-developer-jobs-hollola')
def asp_net_software_developer46(page=1):

    job_list = job_obj.get_job("asp.net software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="hollola")
	
@asp_net.route('/asp.net-software-developer-jobs-valkeakoski')
def asp_net_software_developer47(page=1):

    job_list = job_obj.get_job("asp.net software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="valkeakoski")
	
@asp_net.route('/asp.net-software-developer-jobs-siilinjarvi')
def asp_net_software_developer48(page=1):

    job_list = job_obj.get_job("asp.net software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="siilinjarvi")
	
@asp_net.route('/asp.net-software-developer-jobs-kuusankoski')
def asp_net_software_developer49(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kuusankoski")
	
@asp_net.route('/asp.net-software-developer-jobs-sibbo')
def asp_net_software_developer50(page=1):

    job_list = job_obj.get_job("asp.net software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="sibbo")
	
@asp_net.route('/asp.net-software-developer-jobs-jakostad')
def asp_net_software_developer51(page=1):

    job_list = job_obj.get_job("asp.net software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="jakostad")
	
@asp_net.route('/asp.net-software-developer-jobs-lempaala')
def asp_net_software_developer52(page=1):

    job_list = job_obj.get_job("asp.net software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="lempaala")
	
@asp_net.route('/asp.net-software-developer-jobs-mantsala')
def asp_net_software_developer52_1(page=1):

    job_list = job_obj.get_job("asp.net software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="mantsala")
	
@asp_net.route('/asp.net-software-developer-jobs-forssa')
def asp_net_software_developer53(page=1):

    job_list = job_obj.get_job("asp.net software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="forssa")
	
@asp_net.route('/asp.net-software-developer-jobs-kuusamo')
def asp_net_software_developer54(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kuusamo")
	
@asp_net.route('/asp.net-software-developer-jobs-haukipudas')
def asp_net_software_developer55(page=1):

    job_list = job_obj.get_job("asp.net software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="haukipudas")
	
@asp_net.route('/asp.net-software-developer-jobs-korsholm')
def asp_net_software_developer56(page=1):

    job_list = job_obj.get_job("asp.net software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="korsholm")
	
@asp_net.route('/asp.net-software-developer-jobs-laukaa')
def asp_net_software_developer57(page=1):

    job_list = job_obj.get_job("asp.net software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="laukaa")
	
@asp_net.route('/asp.net-software-developer-jobs-anjala')
def asp_net_software_developer58(page=1):

    job_list = job_obj.get_job("asp.net software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="anjala")
	
@asp_net.route('/asp.net-software-developer-jobs-uusikaupunki')
def asp_net_software_developer59(page=1):

    job_list = job_obj.get_job("asp.net software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="uusikaupunki")
	
@asp_net.route('/asp.net-software-developer-jobs-janakkala')
def asp_net_software_developer60(page=1):

    job_list = job_obj.get_job("asp.net software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="janakkala")
	
@asp_net.route('/asp.net-software-developer-jobs-pirkkala')
def asp_net_software_developer61(page=1):

    job_list = job_obj.get_job("asp.net software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="pirkkala")
	
@asp_net.route('/asp.net-software-developer-jobs-lansi-turunmaa')
def asp_net_software_developer62(page=1):

    job_list = job_obj.get_job("asp.net software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="lansi-turunmaa")
	
@asp_net.route('/asp.net-software-developer-jobs-jamsa')
def asp_net_software_developer63(page=1):

    job_list = job_obj.get_job("asp.net software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="jamsa")
	
@asp_net.route('/asp.net-software-developer-jobs-jamsa')
def asp_net_software_developer64(page=1):

    job_list = job_obj.get_job("asp.net software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="jamsa")
	
@asp_net.route('/asp.net-software-developer-jobs-vammala')
def asp_net_software_developer65(page=1):

    job_list = job_obj.get_job("asp.net software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="vammala")
	
@asp_net.route('/asp.net-software-developer-jobs-nastola')
def asp_net_software_developer66(page=1):

    job_list = job_obj.get_job("asp.net software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="nastola")
	
@asp_net.route('/asp.net-software-developer-jobs-orimattila')
def asp_net_software_developer67(page=1):

    job_list = job_obj.get_job("asp.net software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="orimattila")
	
@asp_net.route('/asp.net-software-developer-jobs-kauhajoki')
def asp_net_software_developer68(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kauhajoki")
	
@asp_net.route('/asp.net-software-developer-jobs-ekenas')
def asp_net_software_developer69(page=1):

    job_list = job_obj.get_job("asp.net software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="ekenas")
	
@asp_net.route('/asp.net-software-developer-jobs-kempele')
def asp_net_software_developer70(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kempele")
	
@asp_net.route('/asp.net-software-developer-jobs-lapua')
def asp_net_software_developer71(page=1):

    job_list = job_obj.get_job("asp.net software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="lapua")
	
@asp_net.route('/asp.net-software-developer-jobs-lieksa')
def asp_net_software_developer72(page=1):

    job_list = job_obj.get_job("asp.net software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="lieksa")
	
@asp_net.route('/asp.net-software-developer-jobs-naantali')
def asp_net_software_developer73(page=1):

    job_list = job_obj.get_job("asp.net software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="naantali")
	
@asp_net.route('/asp.net-software-developer-jobs-aanekoski')
def asp_net_software_developer74(page=1):

    job_list = job_obj.get_job("asp.net software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="aanekoski")
	
@asp_net.route('/asp.net-software-developer-jobs-ylivieska')
def asp_net_software_developer75(page=1):

    job_list = job_obj.get_job("asp.net software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="ylivieska")
	
@asp_net.route('/asp.net-software-developer-jobs-kontiolahti')
def asp_net_software_developer76(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kontiolahti")
	
@asp_net.route('/asp.net-software-developer-jobs-kankaanpaa')
def asp_net_software_developer77(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kankaanpaa")
	
@asp_net.route('/asp.net-software-developer-jobs-ulvila')
def asp_net_software_developer78(page=1):

    job_list = job_obj.get_job("asp.net software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="ulvila")
	
@asp_net.route('/asp.net-software-developer-jobs-pieksamaki')
def asp_net_software_developer79(page=1):

    job_list = job_obj.get_job("asp.net software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="pieksamaki")
	
@asp_net.route('/asp.net-software-developer-jobs-kiiminki')
def asp_net_software_developer80(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kiiminki")
	
@asp_net.route('/asp.net-software-developer-jobs-pargas')
def asp_net_software_developer81(page=1):

    job_list = job_obj.get_job("asp.net software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="pargas")
	
@asp_net.route('/asp.net-software-developer-jobs-nurmo')
def asp_net_software_developer82(page=1):

    job_list = job_obj.get_job("asp.net software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="nurmo")
	
@asp_net.route('/asp.net-software-developer-jobs-ilmajoki')
def asp_net_software_developer83(page=1):

    job_list = job_obj.get_job("asp.net software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="ilmajoki")
	
@asp_net.route('/asp.net-software-developer-jobs-liperi')
def asp_net_software_developer84(page=1):

    job_list = job_obj.get_job("asp.net software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="liperi")
	
@asp_net.route('/asp.net-software-developer-jobs-keuruu')
def asp_net_software_developer85(page=1):

    job_list = job_obj.get_job("asp.net software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="keuruu")
	
@asp_net.route('/asp.net-software-developer-jobs-leppavirta')
def asp_net_software_developer86(page=1):

    job_list = job_obj.get_job("asp.net software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="leppavirta")
	
@asp_net.route('/asp.net-software-developer-jobs-kurikka')
def asp_net_software_developer87(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kurikka")
	
@asp_net.route('/asp.net-software-developer-jobs-nivala')
def asp_net_software_developer88(page=1):

    job_list = job_obj.get_job("asp.net software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="nivala")
	
@asp_net.route('/asp.net-software-developer-jobs-joutseno')
def asp_net_software_developer89(page=1):

    job_list = job_obj.get_job("asp.net software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="joutseno")
	
@asp_net.route('/asp.net-software-developer-jobs-pedersore')
def asp_net_software_developer90(page=1):

    job_list = job_obj.get_job("asp.net software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="pedersore")
	
@asp_net.route('/asp.net-software-developer-jobs-sotkamo')
def asp_net_software_developer91(page=1):

    job_list = job_obj.get_job("asp.net software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="sotkamo")
	
@asp_net.route('/asp.net-software-developer-jobs-kuhmo')
def asp_net_software_developer92(page=1):

    job_list = job_obj.get_job("asp.net software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="kuhmo")
	
@asp_net.route('/asp.net-software-developer-jobs-paimio')
def asp_net_software_developer93(page=1):

    job_list = job_obj.get_job("asp.net software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="paimio")
	
@asp_net.route('/asp.net-software-developer-jobs-saarijarvi')
def asp_net_software_developer94(page=1):

    job_list = job_obj.get_job("asp.net software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="saarijarvi")
	
@asp_net.route('/asp.net-software-developer-jobs-helsinki')
def asp_net_software_developer95(page=1):

    job_list = job_obj.get_job("asp.net software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="asp.net software developer", location="helsinki")


####################################################################

