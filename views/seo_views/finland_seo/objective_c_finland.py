from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

objective_c = Blueprint('objective_c', __name__)
job_obj = Job()



####################################################################


@objective_c.route('/objective-c_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "objective-c" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def objective_c_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="espoo")

@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def objective_c_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="tampere")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def objective_c_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="vantaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def objective_c_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="turku")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def objective_c_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="oulu")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def objective_c_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="lahti")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def objective_c_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kuopio")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def objective_c_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="jyvvaskyla")

@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def objective_c_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="pori")

@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def objective_c_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="lappeenranta")	
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def objective_c_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="vaasa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def objective_c_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kotka")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def objective_c_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="joensuu")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def objective_c_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="hameenlinna")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def objective_c_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="porvoo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def objective_c_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="mikkeli")

@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def objective_c_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="hyvinkaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def objective_c_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="nurmijarvi")

@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def objective_c_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="jarvenpaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def objective_c_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="rauma")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def objective_c_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="lohja")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def objective_c_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="karleby")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def objective_c_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kajaani")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def objective_c_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="rovaniemi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def objective_c_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="tuusula")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def objective_c_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kirkkonummi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def objective_c_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="seinajoki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def objective_c_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kerava")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def objective_c_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kouvola")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def objective_c_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="imatra")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def objective_c_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="nokia")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def objective_c_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="savonlinna")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def objective_c_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="riihimaki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def objective_c_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="vihti")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def objective_c_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="salo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def objective_c_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kangasala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def objective_c_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="raisio")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def objective_c_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="karhula")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def objective_c_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kemi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def objective_c_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="iisalmi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def objective_c_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="varkaus")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def objective_c_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="raahe")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def objective_c_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="ylojarvi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def objective_c_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="hamina")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def objective_c_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kaarina")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def objective_c_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="tornio")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def objective_c_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="heinola")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def objective_c_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="hollola")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def objective_c_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="valkeakoski")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def objective_c_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="siilinjarvi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def objective_c_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kuusankoski")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def objective_c_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="sibbo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def objective_c_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="jakostad")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def objective_c_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="lempaala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def objective_c_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="mantsala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def objective_c_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="forssa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def objective_c_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kuusamo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def objective_c_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="haukipudas")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def objective_c_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="korsholm")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def objective_c_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="laukaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def objective_c_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="anjala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def objective_c_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="uusikaupunki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def objective_c_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="janakkala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def objective_c_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="pirkkala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def objective_c_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def objective_c_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="jamsa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def objective_c_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="jamsa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def objective_c_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="vammala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def objective_c_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="nastola")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def objective_c_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="orimattila")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def objective_c_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kauhajoki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def objective_c_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="ekenas")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def objective_c_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kempele")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def objective_c_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="lapua")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def objective_c_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="lieksa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def objective_c_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="naantali")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def objective_c_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="aanekoski")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def objective_c_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="ylivieska")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def objective_c_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kontiolahti")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def objective_c_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kankaanpaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def objective_c_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="ulvila")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def objective_c_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="pieksamaki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def objective_c_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kiiminki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def objective_c_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="pargas")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def objective_c_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="nurmo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def objective_c_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="ilmajoki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def objective_c_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="liperi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def objective_c_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="keuruu")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def objective_c_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="leppavirta")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def objective_c_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kurikka")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def objective_c_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="nivala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def objective_c_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="joutseno")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def objective_c_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="pedersore")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def objective_c_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="sotkamo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def objective_c_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="kuhmo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def objective_c_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="paimio")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def objective_c_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="saarijarvi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def objective_c_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("objective c ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@objective_c.route('/objective-c-software-developer-jobs-espoo')
def objective_c_software_developer2(page=1):

    job_list = job_obj.get_job("objective c software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="espoo")

@objective_c.route('/objective-c-software-developer-jobs-tampere')
def objective_c_software_developer3(page=1):

    job_list = job_obj.get_job("objective c software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="tampere")
	
@objective_c.route('/objective-c-software-developer-jobs-vantaa')
def objective_c_software_developer4(page=1):

    job_list = job_obj.get_job("objective c software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="vantaa")
	
@objective_c.route('/objective-c-software-developer-jobs-turku')
def objective_c_software_developer5(page=1):

    job_list = job_obj.get_job("objective c software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="turku")
	
@objective_c.route('/objective-c-software-developer-jobs-oulu')
def objective_c_software_developer6(page=1):

    job_list = job_obj.get_job("objective c software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="oulu")
	
@objective_c.route('/objective-c-software-developer-jobs-lahti')
def objective_c_software_developer7(page=1):

    job_list = job_obj.get_job("objective c software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="lahti")
	
@objective_c.route('/objective-c-software-developer-jobs-kuopio')
def objective_c_software_developer8(page=1):

    job_list = job_obj.get_job("objective c software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kuopio")
	
@objective_c.route('/objective-c-software-developer-jobs-jyvvaskyla')
def objective_c_software_developer9(page=1):

    job_list = job_obj.get_job("objective c software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="jyvvaskyla")

@objective_c.route('/objective-c-software-developer-jobs-pori')
def objective_c_software_developer10(page=1):

    job_list = job_obj.get_job("objective c software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="pori")

@objective_c.route('/objective-c-software-developer-jobs-lappeenranta')
def objective_c_software_developer11(page=1):

    job_list = job_obj.get_job("objective c software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="lappeenranta")	
	
@objective_c.route('/objective-c-software-developer-jobs-vaasa')
def objective_c_software_developer12(page=1):

    job_list = job_obj.get_job("objective c software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="vaasa")
	
@objective_c.route('/objective-c-software-developer-jobs-kotka')
def objective_c_software_developer13(page=1):

    job_list = job_obj.get_job("objective c software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kotka")
	
@objective_c.route('/objective-c-software-developer-jobs-joensuu')
def objective_c_software_developer14(page=1):

    job_list = job_obj.get_job("objective c software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="joensuu")
	
@objective_c.route('/objective-c-software-developer-jobs-hameenlinna')
def objective_c_software_developer15(page=1):

    job_list = job_obj.get_job("objective c software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="hameenlinna")
	
@objective_c.route('/objective-c-software-developer-jobs-porvoo')
def objective_c_software_developer16(page=1):

    job_list = job_obj.get_job("objective c software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="porvoo")
	
@objective_c.route('/objective-c-software-developer-jobs-mikkeli')
def objective_c_software_developer17(page=1):

    job_list = job_obj.get_job("objective c software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="mikkeli")

@objective_c.route('/objective-c-software-developer-jobs-hyvinkaa')
def objective_c_software_developer18(page=1):

    job_list = job_obj.get_job("objective c software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="hyvinkaa")
	
@objective_c.route('/objective-c-software-developer-jobs-nurmijarvi')
def objective_c_software_developer19(page=1):

    job_list = job_obj.get_job("objective c software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="nurmijarvi")

@objective_c.route('/objective-c-software-developer-jobs-jarvenpaa')
def objective_c_software_developer20(page=1):

    job_list = job_obj.get_job("objective c software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="jarvenpaa")
	
@objective_c.route('/objective-c-software-developer-jobs-rauma')
def objective_c_software_developer21(page=1):

    job_list = job_obj.get_job("objective c software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="rauma")
	
@objective_c.route('/objective-c-software-developer-jobs-lohja')
def objective_c_software_developer22(page=1):

    job_list = job_obj.get_job("objective c software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="lohja")
	
@objective_c.route('/objective-c-software-developer-jobs-karleby')
def objective_c_software_developer23(page=1):

    job_list = job_obj.get_job("objective c software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="karleby")
	
@objective_c.route('/objective-c-software-developer-jobs-kajaani')
def objective_c_software_developer24(page=1):

    job_list = job_obj.get_job("objective c software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kajaani")
	
@objective_c.route('/objective-c-software-developer-jobs-rovaniemi')
def objective_c_software_developer25(page=1):

    job_list = job_obj.get_job("objective c software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="rovaniemi")
	
@objective_c.route('/objective-c-software-developer-jobs-tuusula')
def objective_c_software_developer26(page=1):

    job_list = job_obj.get_job("objective c software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="tuusula")
	
@objective_c.route('/objective-c-software-developer-jobs-kirkkonummi')
def objective_c_software_developer27(page=1):

    job_list = job_obj.get_job("objective c software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kirkkonummi")
	
@objective_c.route('/objective-c-software-developer-jobs-seinajoki')
def objective_c_software_developer28(page=1):

    job_list = job_obj.get_job("objective c software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="seinajoki")
	
@objective_c.route('/objective-c-software-developer-jobs-kerava')
def objective_c_software_developer29(page=1):

    job_list = job_obj.get_job("objective c software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kerava")
	
@objective_c.route('/objective-c-software-developer-jobs-kouvola')
def objective_c_software_developer30(page=1):

    job_list = job_obj.get_job("objective c software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kouvola")
	
@objective_c.route('/objective-c-software-developer-jobs-imatra')
def objective_c_software_developer31(page=1):

    job_list = job_obj.get_job("objective c software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="imatra")
	
@objective_c.route('/objective-c-software-developer-jobs-nokia')
def objective_c_software_developer32_1(page=1):

    job_list = job_obj.get_job("objective c software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="nokia")
	
@objective_c.route('/objective-c-software-developer-jobs-savonlinna')
def objective_c_software_developer32(page=1):

    job_list = job_obj.get_job("objective c software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="savonlinna")
	
@objective_c.route('/objective-c-software-developer-jobs-riihimaki')
def objective_c_software_developer33(page=1):

    job_list = job_obj.get_job("objective c software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="riihimaki")
	
@objective_c.route('/objective-c-software-developer-jobs-vihti')
def objective_c_software_developer34(page=1):

    job_list = job_obj.get_job("objective c software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="vihti")
	
@objective_c.route('/objective-c-software-developer-jobs-salo')
def objective_c_software_developer35(page=1):

    job_list = job_obj.get_job("objective c software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="salo")
	
@objective_c.route('/objective-c-software-developer-jobs-kangasala')
def objective_c_software_developer36(page=1):

    job_list = job_obj.get_job("objective c software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kangasala")
	
@objective_c.route('/objective-c-software-developer-jobs-raisio')
def objective_c_software_developer37_1(page=1):

    job_list = job_obj.get_job("objective c software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="raisio")
	
@objective_c.route('/objective-c-software-developer-jobs-karhula')
def objective_c_software_developer37(page=1):

    job_list = job_obj.get_job("objective c software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="karhula")
	
@objective_c.route('/objective-c-software-developer-jobs-kemi')
def objective_c_software_developer38(page=1):

    job_list = job_obj.get_job("objective c software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kemi")
	
@objective_c.route('/objective-c-software-developer-jobs-iisalmi')
def objective_c_software_developer39(page=1):

    job_list = job_obj.get_job("objective c software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="iisalmi")
	
@objective_c.route('/objective-c-software-developer-jobs-varkaus')
def objective_c_software_developer40(page=1):

    job_list = job_obj.get_job("objective c software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="varkaus")
	
@objective_c.route('/objective-c-software-developer-jobs-raahe')
def objective_c_software_developer41(page=1):

    job_list = job_obj.get_job("objective c software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="raahe")
	
@objective_c.route('/objective-c-software-developer-jobs-ylojarvi')
def objective_c_software_developer42_1(page=1):

    job_list = job_obj.get_job("objective c software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="ylojarvi")
	
@objective_c.route('/objective-c-software-developer-jobs-hamina')
def objective_c_software_developer42(page=1):

    job_list = job_obj.get_job("objective c software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="hamina")
	
@objective_c.route('/objective-c-software-developer-jobs-kaarina')
def objective_c_software_developer43(page=1):

    job_list = job_obj.get_job("objective c software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kaarina")
	
@objective_c.route('/objective-c-software-developer-jobs-tornio')
def objective_c_software_developer44(page=1):

    job_list = job_obj.get_job("objective c software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="tornio")
	
@objective_c.route('/objective-c-software-developer-jobs-heinola')
def objective_c_software_developer45(page=1):

    job_list = job_obj.get_job("objective c software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="heinola")
	
@objective_c.route('/objective-c-software-developer-jobs-hollola')
def objective_c_software_developer46(page=1):

    job_list = job_obj.get_job("objective c software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="hollola")
	
@objective_c.route('/objective-c-software-developer-jobs-valkeakoski')
def objective_c_software_developer47(page=1):

    job_list = job_obj.get_job("objective c software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="valkeakoski")
	
@objective_c.route('/objective-c-software-developer-jobs-siilinjarvi')
def objective_c_software_developer48(page=1):

    job_list = job_obj.get_job("objective c software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="siilinjarvi")
	
@objective_c.route('/objective-c-software-developer-jobs-kuusankoski')
def objective_c_software_developer49(page=1):

    job_list = job_obj.get_job("objective c software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kuusankoski")
	
@objective_c.route('/objective-c-software-developer-jobs-sibbo')
def objective_c_software_developer50(page=1):

    job_list = job_obj.get_job("objective c software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="sibbo")
	
@objective_c.route('/objective-c-software-developer-jobs-jakostad')
def objective_c_software_developer51(page=1):

    job_list = job_obj.get_job("objective c software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="jakostad")
	
@objective_c.route('/objective-c-software-developer-jobs-lempaala')
def objective_c_software_developer52(page=1):

    job_list = job_obj.get_job("objective c software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="lempaala")
	
@objective_c.route('/objective-c-software-developer-jobs-mantsala')
def objective_c_software_developer52_1(page=1):

    job_list = job_obj.get_job("objective c software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="mantsala")
	
@objective_c.route('/objective-c-software-developer-jobs-forssa')
def objective_c_software_developer53(page=1):

    job_list = job_obj.get_job("objective c software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="forssa")
	
@objective_c.route('/objective-c-software-developer-jobs-kuusamo')
def objective_c_software_developer54(page=1):

    job_list = job_obj.get_job("objective c software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kuusamo")
	
@objective_c.route('/objective-c-software-developer-jobs-haukipudas')
def objective_c_software_developer55(page=1):

    job_list = job_obj.get_job("objective c software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="haukipudas")
	
@objective_c.route('/objective-c-software-developer-jobs-korsholm')
def objective_c_software_developer56(page=1):

    job_list = job_obj.get_job("objective c software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="korsholm")
	
@objective_c.route('/objective-c-software-developer-jobs-laukaa')
def objective_c_software_developer57(page=1):

    job_list = job_obj.get_job("objective c software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="laukaa")
	
@objective_c.route('/objective-c-software-developer-jobs-anjala')
def objective_c_software_developer58(page=1):

    job_list = job_obj.get_job("objective c software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="anjala")
	
@objective_c.route('/objective-c-software-developer-jobs-uusikaupunki')
def objective_c_software_developer59(page=1):

    job_list = job_obj.get_job("objective c software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="uusikaupunki")
	
@objective_c.route('/objective-c-software-developer-jobs-janakkala')
def objective_c_software_developer60(page=1):

    job_list = job_obj.get_job("objective c software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="janakkala")
	
@objective_c.route('/objective-c-software-developer-jobs-pirkkala')
def objective_c_software_developer61(page=1):

    job_list = job_obj.get_job("objective c software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="pirkkala")
	
@objective_c.route('/objective-c-software-developer-jobs-lansi-turunmaa')
def objective_c_software_developer62(page=1):

    job_list = job_obj.get_job("objective c software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="lansi-turunmaa")
	
@objective_c.route('/objective-c-software-developer-jobs-jamsa')
def objective_c_software_developer63(page=1):

    job_list = job_obj.get_job("objective c software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="jamsa")
	
@objective_c.route('/objective-c-software-developer-jobs-jamsa')
def objective_c_software_developer64(page=1):

    job_list = job_obj.get_job("objective c software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="jamsa")
	
@objective_c.route('/objective-c-software-developer-jobs-vammala')
def objective_c_software_developer65(page=1):

    job_list = job_obj.get_job("objective c software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="vammala")
	
@objective_c.route('/objective-c-software-developer-jobs-nastola')
def objective_c_software_developer66(page=1):

    job_list = job_obj.get_job("objective c software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="nastola")
	
@objective_c.route('/objective-c-software-developer-jobs-orimattila')
def objective_c_software_developer67(page=1):

    job_list = job_obj.get_job("objective c software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="orimattila")
	
@objective_c.route('/objective-c-software-developer-jobs-kauhajoki')
def objective_c_software_developer68(page=1):

    job_list = job_obj.get_job("objective c software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kauhajoki")
	
@objective_c.route('/objective-c-software-developer-jobs-ekenas')
def objective_c_software_developer69(page=1):

    job_list = job_obj.get_job("objective c software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="ekenas")
	
@objective_c.route('/objective-c-software-developer-jobs-kempele')
def objective_c_software_developer70(page=1):

    job_list = job_obj.get_job("objective c software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kempele")
	
@objective_c.route('/objective-c-software-developer-jobs-lapua')
def objective_c_software_developer71(page=1):

    job_list = job_obj.get_job("objective c software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="lapua")
	
@objective_c.route('/objective-c-software-developer-jobs-lieksa')
def objective_c_software_developer72(page=1):

    job_list = job_obj.get_job("objective c software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="lieksa")
	
@objective_c.route('/objective-c-software-developer-jobs-naantali')
def objective_c_software_developer73(page=1):

    job_list = job_obj.get_job("objective c software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="naantali")
	
@objective_c.route('/objective-c-software-developer-jobs-aanekoski')
def objective_c_software_developer74(page=1):

    job_list = job_obj.get_job("objective c software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="aanekoski")
	
@objective_c.route('/objective-c-software-developer-jobs-ylivieska')
def objective_c_software_developer75(page=1):

    job_list = job_obj.get_job("objective c software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="ylivieska")
	
@objective_c.route('/objective-c-software-developer-jobs-kontiolahti')
def objective_c_software_developer76(page=1):

    job_list = job_obj.get_job("objective c software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kontiolahti")
	
@objective_c.route('/objective-c-software-developer-jobs-kankaanpaa')
def objective_c_software_developer77(page=1):

    job_list = job_obj.get_job("objective c software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kankaanpaa")
	
@objective_c.route('/objective-c-software-developer-jobs-ulvila')
def objective_c_software_developer78(page=1):

    job_list = job_obj.get_job("objective c software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="ulvila")
	
@objective_c.route('/objective-c-software-developer-jobs-pieksamaki')
def objective_c_software_developer79(page=1):

    job_list = job_obj.get_job("objective c software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="pieksamaki")
	
@objective_c.route('/objective-c-software-developer-jobs-kiiminki')
def objective_c_software_developer80(page=1):

    job_list = job_obj.get_job("objective c software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kiiminki")
	
@objective_c.route('/objective-c-software-developer-jobs-pargas')
def objective_c_software_developer81(page=1):

    job_list = job_obj.get_job("objective c software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="pargas")
	
@objective_c.route('/objective-c-software-developer-jobs-nurmo')
def objective_c_software_developer82(page=1):

    job_list = job_obj.get_job("objective c software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="nurmo")
	
@objective_c.route('/objective-c-software-developer-jobs-ilmajoki')
def objective_c_software_developer83(page=1):

    job_list = job_obj.get_job("objective c software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="ilmajoki")
	
@objective_c.route('/objective-c-software-developer-jobs-liperi')
def objective_c_software_developer84(page=1):

    job_list = job_obj.get_job("objective c software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="liperi")
	
@objective_c.route('/objective-c-software-developer-jobs-keuruu')
def objective_c_software_developer85(page=1):

    job_list = job_obj.get_job("objective c software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="keuruu")
	
@objective_c.route('/objective-c-software-developer-jobs-leppavirta')
def objective_c_software_developer86(page=1):

    job_list = job_obj.get_job("objective c software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="leppavirta")
	
@objective_c.route('/objective-c-software-developer-jobs-kurikka')
def objective_c_software_developer87(page=1):

    job_list = job_obj.get_job("objective c software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kurikka")
	
@objective_c.route('/objective-c-software-developer-jobs-nivala')
def objective_c_software_developer88(page=1):

    job_list = job_obj.get_job("objective c software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="nivala")
	
@objective_c.route('/objective-c-software-developer-jobs-joutseno')
def objective_c_software_developer89(page=1):

    job_list = job_obj.get_job("objective c software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="joutseno")
	
@objective_c.route('/objective-c-software-developer-jobs-pedersore')
def objective_c_software_developer90(page=1):

    job_list = job_obj.get_job("objective c software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="pedersore")
	
@objective_c.route('/objective-c-software-developer-jobs-sotkamo')
def objective_c_software_developer91(page=1):

    job_list = job_obj.get_job("objective c software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="sotkamo")
	
@objective_c.route('/objective-c-software-developer-jobs-kuhmo')
def objective_c_software_developer92(page=1):

    job_list = job_obj.get_job("objective c software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="kuhmo")
	
@objective_c.route('/objective-c-software-developer-jobs-paimio')
def objective_c_software_developer93(page=1):

    job_list = job_obj.get_job("objective c software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="paimio")
	
@objective_c.route('/objective-c-software-developer-jobs-saarijarvi')
def objective_c_software_developer94(page=1):

    job_list = job_obj.get_job("objective c software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="saarijarvi")
	
@objective_c.route('/objective-c-software-developer-jobs-helsinki')
def objective_c_software_developer95(page=1):

    job_list = job_obj.get_job("objective c software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c software developer", location="helsinki")


####################################################################


##############################################
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-espoo')
def objective_c_ohjelmistosuunnittelija_tyopaikat2(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="espoo")

@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-tampere')
def objective_c_ohjelmistosuunnittelija_tyopaikat3(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="tampere")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-vantaa')
def objective_c_ohjelmistosuunnittelija_tyopaikat4(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="vantaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-turku')
def objective_c_ohjelmistosuunnittelija_tyopaikat5(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="turku")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-oulu')
def objective_c_ohjelmistosuunnittelija_tyopaikat6(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="oulu")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-lahti')
def objective_c_ohjelmistosuunnittelija_tyopaikat7(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="lahti")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kuopio')
def objective_c_ohjelmistosuunnittelija_tyopaikat8(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kuopio")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-jyvvaskyla')
def objective_c_ohjelmistosuunnittelija_tyopaikat9(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="jyvvaskyla")

@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-pori')
def objective_c_ohjelmistosuunnittelija_tyopaikat10(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="pori")

@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-lappeenranta')
def objective_c_ohjelmistosuunnittelija_tyopaikat11(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="lappeenranta")	
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-vaasa')
def objective_c_ohjelmistosuunnittelija_tyopaikat12(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="vaasa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kotka')
def objective_c_ohjelmistosuunnittelija_tyopaikat13(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kotka")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-joensuu')
def objective_c_ohjelmistosuunnittelija_tyopaikat14(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="joensuu")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-hameenlinna')
def objective_c_ohjelmistosuunnittelija_tyopaikat15(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="hameenlinna")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-porvoo')
def objective_c_ohjelmistosuunnittelija_tyopaikat16(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="porvoo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-mikkeli')
def objective_c_ohjelmistosuunnittelija_tyopaikat17(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="mikkeli")

@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-hyvinkaa')
def objective_c_ohjelmistosuunnittelija_tyopaikat18(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="hyvinkaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-nurmijarvi')
def objective_c_ohjelmistosuunnittelija_tyopaikat19(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="nurmijarvi")

@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-jarvenpaa')
def objective_c_ohjelmistosuunnittelija_tyopaikat20(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="jarvenpaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-rauma')
def objective_c_ohjelmistosuunnittelija_tyopaikat21(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="rauma")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-lohja')
def objective_c_ohjelmistosuunnittelija_tyopaikat22(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="lohja")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-karleby')
def objective_c_ohjelmistosuunnittelija_tyopaikat23(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="karleby")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kajaani')
def objective_c_ohjelmistosuunnittelija_tyopaikat24(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kajaani")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-rovaniemi')
def objective_c_ohjelmistosuunnittelija_tyopaikat25(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="rovaniemi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-tuusula')
def objective_c_ohjelmistosuunnittelija_tyopaikat26(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="tuusula")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kirkkonummi')
def objective_c_ohjelmistosuunnittelija_tyopaikat27(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kirkkonummi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-seinajoki')
def objective_c_ohjelmistosuunnittelija_tyopaikat28(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="seinajoki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kerava')
def objective_c_ohjelmistosuunnittelija_tyopaikat29(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kerava")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kouvola')
def objective_c_ohjelmistosuunnittelija_tyopaikat30(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kouvola")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-imatra')
def objective_c_ohjelmistosuunnittelija_tyopaikat31(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="imatra")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-nokia')
def objective_c_ohjelmistosuunnittelija_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="nokia")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-savonlinna')
def objective_c_ohjelmistosuunnittelija_tyopaikat32(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="savonlinna")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-riihimaki')
def objective_c_ohjelmistosuunnittelija_tyopaikat33(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="riihimaki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-vihti')
def objective_c_ohjelmistosuunnittelija_tyopaikat34(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="vihti")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-salo')
def objective_c_ohjelmistosuunnittelija_tyopaikat35(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="salo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kangasala')
def objective_c_ohjelmistosuunnittelija_tyopaikat36(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kangasala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-raisio')
def objective_c_ohjelmistosuunnittelija_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="raisio")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-karhula')
def objective_c_ohjelmistosuunnittelija_tyopaikat37(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="karhula")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kemi')
def objective_c_ohjelmistosuunnittelija_tyopaikat38(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kemi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-iisalmi')
def objective_c_ohjelmistosuunnittelija_tyopaikat39(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="iisalmi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-varkaus')
def objective_c_ohjelmistosuunnittelija_tyopaikat40(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="varkaus")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-raahe')
def objective_c_ohjelmistosuunnittelija_tyopaikat41(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="raahe")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-ylojarvi')
def objective_c_ohjelmistosuunnittelija_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="ylojarvi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-hamina')
def objective_c_ohjelmistosuunnittelija_tyopaikat42(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="hamina")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kaarina')
def objective_c_ohjelmistosuunnittelija_tyopaikat43(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kaarina")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-tornio')
def objective_c_ohjelmistosuunnittelija_tyopaikat44(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="tornio")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-heinola')
def objective_c_ohjelmistosuunnittelija_tyopaikat45(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="heinola")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-hollola')
def objective_c_ohjelmistosuunnittelija_tyopaikat46(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="hollola")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-valkeakoski')
def objective_c_ohjelmistosuunnittelija_tyopaikat47(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="valkeakoski")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-siilinjarvi')
def objective_c_ohjelmistosuunnittelija_tyopaikat48(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="siilinjarvi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kuusankoski')
def objective_c_ohjelmistosuunnittelija_tyopaikat49(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kuusankoski")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-sibbo')
def objective_c_ohjelmistosuunnittelija_tyopaikat50(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="sibbo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-jakostad')
def objective_c_ohjelmistosuunnittelija_tyopaikat51(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="jakostad")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-lempaala')
def objective_c_ohjelmistosuunnittelija_tyopaikat52(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="lempaala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-mantsala')
def objective_c_ohjelmistosuunnittelija_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="mantsala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-forssa')
def objective_c_ohjelmistosuunnittelija_tyopaikat53(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="forssa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kuusamo')
def objective_c_ohjelmistosuunnittelija_tyopaikat54(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kuusamo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-haukipudas')
def objective_c_ohjelmistosuunnittelija_tyopaikat55(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="haukipudas")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-korsholm')
def objective_c_ohjelmistosuunnittelija_tyopaikat56(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="korsholm")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-laukaa')
def objective_c_ohjelmistosuunnittelija_tyopaikat57(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="laukaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-anjala')
def objective_c_ohjelmistosuunnittelija_tyopaikat58(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="anjala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-uusikaupunki')
def objective_c_ohjelmistosuunnittelija_tyopaikat59(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="uusikaupunki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-janakkala')
def objective_c_ohjelmistosuunnittelija_tyopaikat60(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="janakkala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-pirkkala')
def objective_c_ohjelmistosuunnittelija_tyopaikat61(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="pirkkala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-lansi-turunmaa')
def objective_c_ohjelmistosuunnittelija_tyopaikat62(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-jamsa')
def objective_c_ohjelmistosuunnittelija_tyopaikat63(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="jamsa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-jamsa')
def objective_c_ohjelmistosuunnittelija_tyopaikat64(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="jamsa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-vammala')
def objective_c_ohjelmistosuunnittelija_tyopaikat65(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="vammala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-nastola')
def objective_c_ohjelmistosuunnittelija_tyopaikat66(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="nastola")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-orimattila')
def objective_c_ohjelmistosuunnittelija_tyopaikat67(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="orimattila")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kauhajoki')
def objective_c_ohjelmistosuunnittelija_tyopaikat68(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kauhajoki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-ekenas')
def objective_c_ohjelmistosuunnittelija_tyopaikat69(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="ekenas")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kempele')
def objective_c_ohjelmistosuunnittelija_tyopaikat70(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kempele")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-lapua')
def objective_c_ohjelmistosuunnittelija_tyopaikat71(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="lapua")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-lieksa')
def objective_c_ohjelmistosuunnittelija_tyopaikat72(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="lieksa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-naantali')
def objective_c_ohjelmistosuunnittelija_tyopaikat73(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="naantali")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-aanekoski')
def objective_c_ohjelmistosuunnittelija_tyopaikat74(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="aanekoski")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-ylivieska')
def objective_c_ohjelmistosuunnittelija_tyopaikat75(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="ylivieska")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kontiolahti')
def objective_c_ohjelmistosuunnittelija_tyopaikat76(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kontiolahti")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kankaanpaa')
def objective_c_ohjelmistosuunnittelija_tyopaikat77(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kankaanpaa")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-ulvila')
def objective_c_ohjelmistosuunnittelija_tyopaikat78(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="ulvila")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-pieksamaki')
def objective_c_ohjelmistosuunnittelija_tyopaikat79(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="pieksamaki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kiiminki')
def objective_c_ohjelmistosuunnittelija_tyopaikat80(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kiiminki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-pargas')
def objective_c_ohjelmistosuunnittelija_tyopaikat81(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="pargas")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-nurmo')
def objective_c_ohjelmistosuunnittelija_tyopaikat82(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="nurmo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-ilmajoki')
def objective_c_ohjelmistosuunnittelija_tyopaikat83(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="ilmajoki")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-liperi')
def objective_c_ohjelmistosuunnittelija_tyopaikat84(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="liperi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-keuruu')
def objective_c_ohjelmistosuunnittelija_tyopaikat85(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="keuruu")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-leppavirta')
def objective_c_ohjelmistosuunnittelija_tyopaikat86(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="leppavirta")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kurikka')
def objective_c_ohjelmistosuunnittelija_tyopaikat87(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kurikka")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-nivala')
def objective_c_ohjelmistosuunnittelija_tyopaikat88(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="nivala")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-joutseno')
def objective_c_ohjelmistosuunnittelija_tyopaikat89(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="joutseno")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-pedersore')
def objective_c_ohjelmistosuunnittelija_tyopaikat90(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="pedersore")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-sotkamo')
def objective_c_ohjelmistosuunnittelija_tyopaikat91(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="sotkamo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-kuhmo')
def objective_c_ohjelmistosuunnittelija_tyopaikat92(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="kuhmo")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-paimio')
def objective_c_ohjelmistosuunnittelija_tyopaikat93(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="paimio")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-saarijarvi')
def objective_c_ohjelmistosuunnittelija_tyopaikat94(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="saarijarvi")
	
@objective_c.route('/objective-c-ohjelmistosuunnittelija-tyopaikat-helsinki')
def objective_c_ohjelmistosuunnittelija_tyopaikat95(page=1):

    job_list = job_obj.get_job("objective c  ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="objective c  ohjelmistosuunnittelija", location="helsinki")
	  

