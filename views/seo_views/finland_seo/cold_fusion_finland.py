from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

coldFusion = Blueprint('coldFusion', __name__)
job_obj = Job()



####################################################################


@coldFusion.route('/coldfusion_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "coldfusion" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def coldfusion_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="espoo")

@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def coldfusion_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="tampere")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def coldfusion_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="vantaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def coldfusion_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="turku")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def coldfusion_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="oulu")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def coldfusion_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="lahti")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def coldfusion_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kuopio")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def coldfusion_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="jyvvaskyla")

@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def coldfusion_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="pori")

@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def coldfusion_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="lappeenranta")	
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def coldfusion_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="vaasa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def coldfusion_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kotka")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def coldfusion_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="joensuu")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def coldfusion_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="hameenlinna")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def coldfusion_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="porvoo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def coldfusion_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="mikkeli")

@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def coldfusion_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="hyvinkaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def coldfusion_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="nurmijarvi")

@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def coldfusion_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="jarvenpaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def coldfusion_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="rauma")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def coldfusion_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="lohja")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def coldfusion_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="karleby")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def coldfusion_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kajaani")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def coldfusion_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="rovaniemi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def coldfusion_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="tuusula")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def coldfusion_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kirkkonummi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def coldfusion_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="seinajoki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def coldfusion_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kerava")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def coldfusion_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kouvola")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def coldfusion_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="imatra")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def coldfusion_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="nokia")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def coldfusion_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="savonlinna")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def coldfusion_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="riihimaki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def coldfusion_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="vihti")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def coldfusion_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="salo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def coldfusion_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kangasala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def coldfusion_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="raisio")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def coldfusion_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="karhula")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def coldfusion_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kemi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def coldfusion_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="iisalmi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def coldfusion_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="varkaus")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def coldfusion_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="raahe")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def coldfusion_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="ylojarvi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def coldfusion_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="hamina")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def coldfusion_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kaarina")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def coldfusion_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="tornio")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def coldfusion_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="heinola")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def coldfusion_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="hollola")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def coldfusion_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="valkeakoski")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def coldfusion_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="siilinjarvi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def coldfusion_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kuusankoski")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def coldfusion_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="sibbo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def coldfusion_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="jakostad")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def coldfusion_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="lempaala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def coldfusion_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="mantsala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def coldfusion_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="forssa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def coldfusion_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kuusamo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def coldfusion_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="haukipudas")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def coldfusion_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="korsholm")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def coldfusion_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="laukaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def coldfusion_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="anjala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def coldfusion_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="uusikaupunki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def coldfusion_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="janakkala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def coldfusion_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="pirkkala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def coldfusion_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def coldfusion_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="jamsa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def coldfusion_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="jamsa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def coldfusion_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="vammala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def coldfusion_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="nastola")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def coldfusion_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="orimattila")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def coldfusion_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kauhajoki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def coldfusion_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="ekenas")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def coldfusion_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kempele")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def coldfusion_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="lapua")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def coldfusion_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="lieksa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def coldfusion_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="naantali")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def coldfusion_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="aanekoski")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def coldfusion_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="ylivieska")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def coldfusion_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kontiolahti")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def coldfusion_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kankaanpaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def coldfusion_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="ulvila")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def coldfusion_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="pieksamaki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def coldfusion_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kiiminki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def coldfusion_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="pargas")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def coldfusion_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="nurmo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def coldfusion_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="ilmajoki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def coldfusion_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="liperi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def coldfusion_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="keuruu")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def coldfusion_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="leppavirta")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def coldfusion_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kurikka")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def coldfusion_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="nivala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def coldfusion_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="joutseno")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def coldfusion_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="pedersore")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def coldfusion_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="sotkamo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def coldfusion_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="kuhmo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def coldfusion_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="paimio")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def coldfusion_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="saarijarvi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def coldfusion_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("coldfusion ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@coldFusion.route('/coldfusion-software-developer-jobs-espoo')
def coldfusion_software_developer2(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="espoo")

@coldFusion.route('/coldfusion-software-developer-jobs-tampere')
def coldfusion_software_developer3(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="tampere")
	
@coldFusion.route('/coldfusion-software-developer-jobs-vantaa')
def coldfusion_software_developer4(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="vantaa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-turku')
def coldfusion_software_developer5(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="turku")
	
@coldFusion.route('/coldfusion-software-developer-jobs-oulu')
def coldfusion_software_developer6(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="oulu")
	
@coldFusion.route('/coldfusion-software-developer-jobs-lahti')
def coldfusion_software_developer7(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="lahti")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kuopio')
def coldfusion_software_developer8(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kuopio")
	
@coldFusion.route('/coldfusion-software-developer-jobs-jyvvaskyla')
def coldfusion_software_developer9(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="jyvvaskyla")

@coldFusion.route('/coldfusion-software-developer-jobs-pori')
def coldfusion_software_developer10(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="pori")

@coldFusion.route('/coldfusion-software-developer-jobs-lappeenranta')
def coldfusion_software_developer11(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="lappeenranta")	
	
@coldFusion.route('/coldfusion-software-developer-jobs-vaasa')
def coldfusion_software_developer12(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="vaasa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kotka')
def coldfusion_software_developer13(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kotka")
	
@coldFusion.route('/coldfusion-software-developer-jobs-joensuu')
def coldfusion_software_developer14(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="joensuu")
	
@coldFusion.route('/coldfusion-software-developer-jobs-hameenlinna')
def coldfusion_software_developer15(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="hameenlinna")
	
@coldFusion.route('/coldfusion-software-developer-jobs-porvoo')
def coldfusion_software_developer16(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="porvoo")
	
@coldFusion.route('/coldfusion-software-developer-jobs-mikkeli')
def coldfusion_software_developer17(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="mikkeli")

@coldFusion.route('/coldfusion-software-developer-jobs-hyvinkaa')
def coldfusion_software_developer18(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="hyvinkaa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-nurmijarvi')
def coldfusion_software_developer19(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="nurmijarvi")

@coldFusion.route('/coldfusion-software-developer-jobs-jarvenpaa')
def coldfusion_software_developer20(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="jarvenpaa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-rauma')
def coldfusion_software_developer21(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="rauma")
	
@coldFusion.route('/coldfusion-software-developer-jobs-lohja')
def coldfusion_software_developer22(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="lohja")
	
@coldFusion.route('/coldfusion-software-developer-jobs-karleby')
def coldfusion_software_developer23(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="karleby")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kajaani')
def coldfusion_software_developer24(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kajaani")
	
@coldFusion.route('/coldfusion-software-developer-jobs-rovaniemi')
def coldfusion_software_developer25(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="rovaniemi")
	
@coldFusion.route('/coldfusion-software-developer-jobs-tuusula')
def coldfusion_software_developer26(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="tuusula")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kirkkonummi')
def coldfusion_software_developer27(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kirkkonummi")
	
@coldFusion.route('/coldfusion-software-developer-jobs-seinajoki')
def coldfusion_software_developer28(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="seinajoki")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kerava')
def coldfusion_software_developer29(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kerava")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kouvola')
def coldfusion_software_developer30(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kouvola")
	
@coldFusion.route('/coldfusion-software-developer-jobs-imatra')
def coldfusion_software_developer31(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="imatra")
	
@coldFusion.route('/coldfusion-software-developer-jobs-nokia')
def coldfusion_software_developer32_1(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="nokia")
	
@coldFusion.route('/coldfusion-software-developer-jobs-savonlinna')
def coldfusion_software_developer32(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="savonlinna")
	
@coldFusion.route('/coldfusion-software-developer-jobs-riihimaki')
def coldfusion_software_developer33(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="riihimaki")
	
@coldFusion.route('/coldfusion-software-developer-jobs-vihti')
def coldfusion_software_developer34(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="vihti")
	
@coldFusion.route('/coldfusion-software-developer-jobs-salo')
def coldfusion_software_developer35(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="salo")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kangasala')
def coldfusion_software_developer36(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kangasala")
	
@coldFusion.route('/coldfusion-software-developer-jobs-raisio')
def coldfusion_software_developer37_1(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="raisio")
	
@coldFusion.route('/coldfusion-software-developer-jobs-karhula')
def coldfusion_software_developer37(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="karhula")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kemi')
def coldfusion_software_developer38(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kemi")
	
@coldFusion.route('/coldfusion-software-developer-jobs-iisalmi')
def coldfusion_software_developer39(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="iisalmi")
	
@coldFusion.route('/coldfusion-software-developer-jobs-varkaus')
def coldfusion_software_developer40(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="varkaus")
	
@coldFusion.route('/coldfusion-software-developer-jobs-raahe')
def coldfusion_software_developer41(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="raahe")
	
@coldFusion.route('/coldfusion-software-developer-jobs-ylojarvi')
def coldfusion_software_developer42_1(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="ylojarvi")
	
@coldFusion.route('/coldfusion-software-developer-jobs-hamina')
def coldfusion_software_developer42(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="hamina")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kaarina')
def coldfusion_software_developer43(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kaarina")
	
@coldFusion.route('/coldfusion-software-developer-jobs-tornio')
def coldfusion_software_developer44(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="tornio")
	
@coldFusion.route('/coldfusion-software-developer-jobs-heinola')
def coldfusion_software_developer45(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="heinola")
	
@coldFusion.route('/coldfusion-software-developer-jobs-hollola')
def coldfusion_software_developer46(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="hollola")
	
@coldFusion.route('/coldfusion-software-developer-jobs-valkeakoski')
def coldfusion_software_developer47(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="valkeakoski")
	
@coldFusion.route('/coldfusion-software-developer-jobs-siilinjarvi')
def coldfusion_software_developer48(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="siilinjarvi")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kuusankoski')
def coldfusion_software_developer49(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kuusankoski")
	
@coldFusion.route('/coldfusion-software-developer-jobs-sibbo')
def coldfusion_software_developer50(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="sibbo")
	
@coldFusion.route('/coldfusion-software-developer-jobs-jakostad')
def coldfusion_software_developer51(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="jakostad")
	
@coldFusion.route('/coldfusion-software-developer-jobs-lempaala')
def coldfusion_software_developer52(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="lempaala")
	
@coldFusion.route('/coldfusion-software-developer-jobs-mantsala')
def coldfusion_software_developer52_1(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="mantsala")
	
@coldFusion.route('/coldfusion-software-developer-jobs-forssa')
def coldfusion_software_developer53(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="forssa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kuusamo')
def coldfusion_software_developer54(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kuusamo")
	
@coldFusion.route('/coldfusion-software-developer-jobs-haukipudas')
def coldfusion_software_developer55(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="haukipudas")
	
@coldFusion.route('/coldfusion-software-developer-jobs-korsholm')
def coldfusion_software_developer56(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="korsholm")
	
@coldFusion.route('/coldfusion-software-developer-jobs-laukaa')
def coldfusion_software_developer57(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="laukaa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-anjala')
def coldfusion_software_developer58(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="anjala")
	
@coldFusion.route('/coldfusion-software-developer-jobs-uusikaupunki')
def coldfusion_software_developer59(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="uusikaupunki")
	
@coldFusion.route('/coldfusion-software-developer-jobs-janakkala')
def coldfusion_software_developer60(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="janakkala")
	
@coldFusion.route('/coldfusion-software-developer-jobs-pirkkala')
def coldfusion_software_developer61(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="pirkkala")
	
@coldFusion.route('/coldfusion-software-developer-jobs-lansi-turunmaa')
def coldfusion_software_developer62(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="lansi-turunmaa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-jamsa')
def coldfusion_software_developer63(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="jamsa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-jamsa')
def coldfusion_software_developer64(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="jamsa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-vammala')
def coldfusion_software_developer65(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="vammala")
	
@coldFusion.route('/coldfusion-software-developer-jobs-nastola')
def coldfusion_software_developer66(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="nastola")
	
@coldFusion.route('/coldfusion-software-developer-jobs-orimattila')
def coldfusion_software_developer67(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="orimattila")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kauhajoki')
def coldfusion_software_developer68(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kauhajoki")
	
@coldFusion.route('/coldfusion-software-developer-jobs-ekenas')
def coldfusion_software_developer69(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="ekenas")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kempele')
def coldfusion_software_developer70(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kempele")
	
@coldFusion.route('/coldfusion-software-developer-jobs-lapua')
def coldfusion_software_developer71(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="lapua")
	
@coldFusion.route('/coldfusion-software-developer-jobs-lieksa')
def coldfusion_software_developer72(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="lieksa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-naantali')
def coldfusion_software_developer73(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="naantali")
	
@coldFusion.route('/coldfusion-software-developer-jobs-aanekoski')
def coldfusion_software_developer74(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="aanekoski")
	
@coldFusion.route('/coldfusion-software-developer-jobs-ylivieska')
def coldfusion_software_developer75(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="ylivieska")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kontiolahti')
def coldfusion_software_developer76(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kontiolahti")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kankaanpaa')
def coldfusion_software_developer77(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kankaanpaa")
	
@coldFusion.route('/coldfusion-software-developer-jobs-ulvila')
def coldfusion_software_developer78(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="ulvila")
	
@coldFusion.route('/coldfusion-software-developer-jobs-pieksamaki')
def coldfusion_software_developer79(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="pieksamaki")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kiiminki')
def coldfusion_software_developer80(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kiiminki")
	
@coldFusion.route('/coldfusion-software-developer-jobs-pargas')
def coldfusion_software_developer81(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="pargas")
	
@coldFusion.route('/coldfusion-software-developer-jobs-nurmo')
def coldfusion_software_developer82(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="nurmo")
	
@coldFusion.route('/coldfusion-software-developer-jobs-ilmajoki')
def coldfusion_software_developer83(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="ilmajoki")
	
@coldFusion.route('/coldfusion-software-developer-jobs-liperi')
def coldfusion_software_developer84(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="liperi")
	
@coldFusion.route('/coldfusion-software-developer-jobs-keuruu')
def coldfusion_software_developer85(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="keuruu")
	
@coldFusion.route('/coldfusion-software-developer-jobs-leppavirta')
def coldfusion_software_developer86(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="leppavirta")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kurikka')
def coldfusion_software_developer87(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kurikka")
	
@coldFusion.route('/coldfusion-software-developer-jobs-nivala')
def coldfusion_software_developer88(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="nivala")
	
@coldFusion.route('/coldfusion-software-developer-jobs-joutseno')
def coldfusion_software_developer89(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="joutseno")
	
@coldFusion.route('/coldfusion-software-developer-jobs-pedersore')
def coldfusion_software_developer90(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="pedersore")
	
@coldFusion.route('/coldfusion-software-developer-jobs-sotkamo')
def coldfusion_software_developer91(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="sotkamo")
	
@coldFusion.route('/coldfusion-software-developer-jobs-kuhmo')
def coldfusion_software_developer92(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="kuhmo")
	
@coldFusion.route('/coldfusion-software-developer-jobs-paimio')
def coldfusion_software_developer93(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="paimio")
	
@coldFusion.route('/coldfusion-software-developer-jobs-saarijarvi')
def coldfusion_software_developer94(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="saarijarvi")
	
@coldFusion.route('/coldfusion-software-developer-jobs-helsinki')
def coldfusion_software_developer95(page=1):

    job_list = job_obj.get_job("coldfusion software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion software developer", location="helsinki")


####################################################################


##############################################
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-espoo')
def coldfusionohjelmistosuunnittelija_tyopaikat2(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="espoo")

@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-tampere')
def coldfusionohjelmistosuunnittelija_tyopaikat3(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="tampere")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-vantaa')
def coldfusionohjelmistosuunnittelija_tyopaikat4(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="vantaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-turku')
def coldfusionohjelmistosuunnittelija_tyopaikat5(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="turku")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-oulu')
def coldfusionohjelmistosuunnittelija_tyopaikat6(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="oulu")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-lahti')
def coldfusionohjelmistosuunnittelija_tyopaikat7(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="lahti")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kuopio')
def coldfusionohjelmistosuunnittelija_tyopaikat8(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kuopio")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-jyvvaskyla')
def coldfusionohjelmistosuunnittelija_tyopaikat9(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="jyvvaskyla")

@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-pori')
def coldfusionohjelmistosuunnittelija_tyopaikat10(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="pori")

@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-lappeenranta')
def coldfusionohjelmistosuunnittelija_tyopaikat11(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="lappeenranta")	
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-vaasa')
def coldfusionohjelmistosuunnittelija_tyopaikat12(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="vaasa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kotka')
def coldfusionohjelmistosuunnittelija_tyopaikat13(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kotka")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-joensuu')
def coldfusionohjelmistosuunnittelija_tyopaikat14(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="joensuu")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-hameenlinna')
def coldfusionohjelmistosuunnittelija_tyopaikat15(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="hameenlinna")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-porvoo')
def coldfusionohjelmistosuunnittelija_tyopaikat16(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="porvoo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-mikkeli')
def coldfusionohjelmistosuunnittelija_tyopaikat17(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="mikkeli")

@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-hyvinkaa')
def coldfusionohjelmistosuunnittelija_tyopaikat18(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="hyvinkaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-nurmijarvi')
def coldfusionohjelmistosuunnittelija_tyopaikat19(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="nurmijarvi")

@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-jarvenpaa')
def coldfusionohjelmistosuunnittelija_tyopaikat20(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="jarvenpaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-rauma')
def coldfusionohjelmistosuunnittelija_tyopaikat21(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="rauma")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-lohja')
def coldfusionohjelmistosuunnittelija_tyopaikat22(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="lohja")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-karleby')
def coldfusionohjelmistosuunnittelija_tyopaikat23(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="karleby")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kajaani')
def coldfusionohjelmistosuunnittelija_tyopaikat24(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kajaani")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-rovaniemi')
def coldfusionohjelmistosuunnittelija_tyopaikat25(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="rovaniemi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-tuusula')
def coldfusionohjelmistosuunnittelija_tyopaikat26(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="tuusula")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kirkkonummi')
def coldfusionohjelmistosuunnittelija_tyopaikat27(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kirkkonummi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-seinajoki')
def coldfusionohjelmistosuunnittelija_tyopaikat28(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="seinajoki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kerava')
def coldfusionohjelmistosuunnittelija_tyopaikat29(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kerava")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kouvola')
def coldfusionohjelmistosuunnittelija_tyopaikat30(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kouvola")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-imatra')
def coldfusionohjelmistosuunnittelija_tyopaikat31(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="imatra")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-nokia')
def coldfusionohjelmistosuunnittelija_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="nokia")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-savonlinna')
def coldfusionohjelmistosuunnittelija_tyopaikat32(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="savonlinna")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-riihimaki')
def coldfusionohjelmistosuunnittelija_tyopaikat33(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="riihimaki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-vihti')
def coldfusionohjelmistosuunnittelija_tyopaikat34(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="vihti")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-salo')
def coldfusionohjelmistosuunnittelija_tyopaikat35(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="salo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kangasala')
def coldfusionohjelmistosuunnittelija_tyopaikat36(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kangasala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-raisio')
def coldfusionohjelmistosuunnittelija_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="raisio")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-karhula')
def coldfusionohjelmistosuunnittelija_tyopaikat37(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="karhula")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kemi')
def coldfusionohjelmistosuunnittelija_tyopaikat38(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kemi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-iisalmi')
def coldfusionohjelmistosuunnittelija_tyopaikat39(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="iisalmi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-varkaus')
def coldfusionohjelmistosuunnittelija_tyopaikat40(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="varkaus")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-raahe')
def coldfusionohjelmistosuunnittelija_tyopaikat41(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="raahe")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-ylojarvi')
def coldfusionohjelmistosuunnittelija_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="ylojarvi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-hamina')
def coldfusionohjelmistosuunnittelija_tyopaikat42(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="hamina")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kaarina')
def coldfusionohjelmistosuunnittelija_tyopaikat43(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kaarina")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-tornio')
def coldfusionohjelmistosuunnittelija_tyopaikat44(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="tornio")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-heinola')
def coldfusionohjelmistosuunnittelija_tyopaikat45(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="heinola")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-hollola')
def coldfusionohjelmistosuunnittelija_tyopaikat46(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="hollola")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-valkeakoski')
def coldfusionohjelmistosuunnittelija_tyopaikat47(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="valkeakoski")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-siilinjarvi')
def coldfusionohjelmistosuunnittelija_tyopaikat48(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="siilinjarvi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kuusankoski')
def coldfusionohjelmistosuunnittelija_tyopaikat49(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kuusankoski")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-sibbo')
def coldfusionohjelmistosuunnittelija_tyopaikat50(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="sibbo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-jakostad')
def coldfusionohjelmistosuunnittelija_tyopaikat51(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="jakostad")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-lempaala')
def coldfusionohjelmistosuunnittelija_tyopaikat52(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="lempaala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-mantsala')
def coldfusionohjelmistosuunnittelija_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="mantsala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-forssa')
def coldfusionohjelmistosuunnittelija_tyopaikat53(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="forssa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kuusamo')
def coldfusionohjelmistosuunnittelija_tyopaikat54(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kuusamo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-haukipudas')
def coldfusionohjelmistosuunnittelija_tyopaikat55(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="haukipudas")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-korsholm')
def coldfusionohjelmistosuunnittelija_tyopaikat56(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="korsholm")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-laukaa')
def coldfusionohjelmistosuunnittelija_tyopaikat57(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="laukaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-anjala')
def coldfusionohjelmistosuunnittelija_tyopaikat58(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="anjala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-uusikaupunki')
def coldfusionohjelmistosuunnittelija_tyopaikat59(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="uusikaupunki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-janakkala')
def coldfusionohjelmistosuunnittelija_tyopaikat60(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="janakkala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-pirkkala')
def coldfusionohjelmistosuunnittelija_tyopaikat61(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="pirkkala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-lansi-turunmaa')
def coldfusionohjelmistosuunnittelija_tyopaikat62(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-jamsa')
def coldfusionohjelmistosuunnittelija_tyopaikat63(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="jamsa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-jamsa')
def coldfusionohjelmistosuunnittelija_tyopaikat64(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="jamsa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-vammala')
def coldfusionohjelmistosuunnittelija_tyopaikat65(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="vammala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-nastola')
def coldfusionohjelmistosuunnittelija_tyopaikat66(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="nastola")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-orimattila')
def coldfusionohjelmistosuunnittelija_tyopaikat67(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="orimattila")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kauhajoki')
def coldfusionohjelmistosuunnittelija_tyopaikat68(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kauhajoki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-ekenas')
def coldfusionohjelmistosuunnittelija_tyopaikat69(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="ekenas")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kempele')
def coldfusionohjelmistosuunnittelija_tyopaikat70(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kempele")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-lapua')
def coldfusionohjelmistosuunnittelija_tyopaikat71(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="lapua")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-lieksa')
def coldfusionohjelmistosuunnittelija_tyopaikat72(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="lieksa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-naantali')
def coldfusionohjelmistosuunnittelija_tyopaikat73(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="naantali")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-aanekoski')
def coldfusionohjelmistosuunnittelija_tyopaikat74(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="aanekoski")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-ylivieska')
def coldfusionohjelmistosuunnittelija_tyopaikat75(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="ylivieska")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kontiolahti')
def coldfusionohjelmistosuunnittelija_tyopaikat76(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kontiolahti")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kankaanpaa')
def coldfusionohjelmistosuunnittelija_tyopaikat77(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kankaanpaa")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-ulvila')
def coldfusionohjelmistosuunnittelija_tyopaikat78(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="ulvila")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-pieksamaki')
def coldfusionohjelmistosuunnittelija_tyopaikat79(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="pieksamaki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kiiminki')
def coldfusionohjelmistosuunnittelija_tyopaikat80(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kiiminki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-pargas')
def coldfusionohjelmistosuunnittelija_tyopaikat81(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="pargas")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-nurmo')
def coldfusionohjelmistosuunnittelija_tyopaikat82(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="nurmo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-ilmajoki')
def coldfusionohjelmistosuunnittelija_tyopaikat83(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="ilmajoki")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-liperi')
def coldfusionohjelmistosuunnittelija_tyopaikat84(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="liperi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-keuruu')
def coldfusionohjelmistosuunnittelija_tyopaikat85(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="keuruu")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-leppavirta')
def coldfusionohjelmistosuunnittelija_tyopaikat86(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="leppavirta")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kurikka')
def coldfusionohjelmistosuunnittelija_tyopaikat87(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kurikka")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-nivala')
def coldfusionohjelmistosuunnittelija_tyopaikat88(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="nivala")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-joutseno')
def coldfusionohjelmistosuunnittelija_tyopaikat89(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="joutseno")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-pedersore')
def coldfusionohjelmistosuunnittelija_tyopaikat90(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="pedersore")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-sotkamo')
def coldfusionohjelmistosuunnittelija_tyopaikat91(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="sotkamo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-kuhmo')
def coldfusionohjelmistosuunnittelija_tyopaikat92(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="kuhmo")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-paimio')
def coldfusionohjelmistosuunnittelija_tyopaikat93(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="paimio")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-saarijarvi')
def coldfusionohjelmistosuunnittelija_tyopaikat94(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="saarijarvi")
	
@coldFusion.route('/coldfusion-ohjelmistosuunnittelija-tyopaikat-helsinki')
def coldfusionohjelmistosuunnittelija_tyopaikat95(page=1):

    job_list = job_obj.get_job("coldfusion  ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="coldfusion  ohjelmistosuunnittelija", location="helsinki")
	  

