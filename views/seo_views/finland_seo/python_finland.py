from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PAGE = 7

python = Blueprint('python', __name__)
job_obj = Job()



####################################################################


@python.route('/python_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "python" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def python_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="espoo")

@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def python_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="tampere")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def python_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="vantaa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def python_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="turku")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def python_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="oulu")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def python_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lahti")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def python_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kuopio")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def python_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="jyvvaskyla")

@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def python_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="pori")

@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def python_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lappeenranta")	
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def python_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="vaasa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def python_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kotka")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def python_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="joensuu")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def python_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="hameenlinna")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def python_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="porvoo")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def python_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="mikkeli")

@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def python_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="hyvinkaa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def python_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="nurmijarvi")

@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def python_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="jarvenpaa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def python_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="rauma")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def python_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lohja")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def python_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="karleby")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def python_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kajaani")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def python_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="rovaniemi")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def python_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="tuusula")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def python_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kirkkonummi")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def python_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="seinajoki")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def python_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kerava")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def python_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kouvola")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def python_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="imatra")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def python_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="nokia")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def python_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="savonlinna")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def python_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="riihimaki")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def python_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="vihti")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def python_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="salo")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def python_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kangasala")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def python_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="raisio")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def python_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="karhula")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def python_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kemi")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def python_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="iisalmi")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def python_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="varkaus")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def python_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="raahe")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def python_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="ylojarvi")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def python_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="hamina")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def python_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kaarina")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def python_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="tornio")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def python_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="heinola")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def python_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="hollola")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def python_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="valkeakoski")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def python_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="siilinjarvi")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def python_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kuusankoski")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def python_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="sibbo")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def python_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="jakostad")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def python_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lempaala")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def python_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="mantsala")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def python_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="forssa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def python_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kuusamo")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def python_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="haukipudas")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def python_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="korsholm")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def python_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="laukaa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def python_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="anjala")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def python_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="uusikaupunki")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def python_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="janakkala")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def python_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="pirkkala")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def python_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def python_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="jamsa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def python_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="jamsa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def python_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="vammala")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def python_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="nastola")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def python_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="orimattila")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def python_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kauhajoki")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def python_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="ekenas")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def python_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kempele")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def python_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lapua")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def python_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lieksa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def python_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="naantali")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def python_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="aanekoski")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def python_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="ylivieska")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def python_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kontiolahti")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def python_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kankaanpaa")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def python_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="ulvila")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def python_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="pieksamaki")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def python_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kiiminki")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def python_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="pargas")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def python_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="nurmo")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def python_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="ilmajoki")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def python_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="liperi")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def python_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="keuruu")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def python_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="leppavirta")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def python_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kurikka")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def python_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="nivala")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def python_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="joutseno")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def python_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="pedersore")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def python_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="sotkamo")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def python_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kuhmo")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def python_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="paimio")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def python_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="saarijarvi")
	
@python.route('/python-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def python_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="helsinki")



	 
##############################################
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-espoo')
def python_ohjelmistosuunnittelija_tyopaikat2(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="espoo")

@python.route('/python-ohjelmistosuunnittelija-tyopaikat-tampere')
def python_ohjelmistosuunnittelija_tyopaikat3(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="tampere")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-vantaa')
def python_ohjelmistosuunnittelija_tyopaikat4(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="vantaa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-turku')
def python_ohjelmistosuunnittelija_tyopaikat5(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="turku")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-oulu')
def python_ohjelmistosuunnittelija_tyopaikat6(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="oulu")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-lahti')
def python_ohjelmistosuunnittelija_tyopaikat7(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lahti")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kuopio')
def python_ohjelmistosuunnittelija_tyopaikat8(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kuopio")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-jyvvaskyla')
def python_ohjelmistosuunnittelija_tyopaikat9(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="jyvvaskyla")

@python.route('/python-ohjelmistosuunnittelija-tyopaikat-pori')
def python_ohjelmistosuunnittelija_tyopaikat10(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="pori")

@python.route('/python-ohjelmistosuunnittelija-tyopaikat-lappeenranta')
def python_ohjelmistosuunnittelija_tyopaikat11(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lappeenranta")	
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-vaasa')
def python_ohjelmistosuunnittelija_tyopaikat12(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="vaasa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kotka')
def python_ohjelmistosuunnittelija_tyopaikat13(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kotka")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-joensuu')
def python_ohjelmistosuunnittelija_tyopaikat14(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="joensuu")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-hameenlinna')
def python_ohjelmistosuunnittelija_tyopaikat15(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="hameenlinna")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-porvoo')
def python_ohjelmistosuunnittelija_tyopaikat16(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="porvoo")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-mikkeli')
def python_ohjelmistosuunnittelija_tyopaikat17(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="mikkeli")

@python.route('/python-ohjelmistosuunnittelija-tyopaikat-hyvinkaa')
def python_ohjelmistosuunnittelija_tyopaikat18(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="hyvinkaa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-nurmijarvi')
def python_ohjelmistosuunnittelija_tyopaikat19(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="nurmijarvi")

@python.route('/python-ohjelmistosuunnittelija-tyopaikat-jarvenpaa')
def python_ohjelmistosuunnittelija_tyopaikat20(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="jarvenpaa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-rauma')
def python_ohjelmistosuunnittelija_tyopaikat21(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="rauma")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-lohja')
def python_ohjelmistosuunnittelija_tyopaikat22(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lohja")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-karleby')
def python_ohjelmistosuunnittelija_tyopaikat23(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="karleby")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kajaani')
def python_ohjelmistosuunnittelija_tyopaikat24(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kajaani")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-rovaniemi')
def python_ohjelmistosuunnittelija_tyopaikat25(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="rovaniemi")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-tuusula')
def python_ohjelmistosuunnittelija_tyopaikat26(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="tuusula")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kirkkonummi')
def python_ohjelmistosuunnittelija_tyopaikat27(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kirkkonummi")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-seinajoki')
def python_ohjelmistosuunnittelija_tyopaikat28(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="seinajoki")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kerava')
def python_ohjelmistosuunnittelija_tyopaikat29(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kerava")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kouvola')
def python_ohjelmistosuunnittelija_tyopaikat30(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kouvola")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-imatra')
def python_ohjelmistosuunnittelija_tyopaikat31(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="imatra")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-nokia')
def python_ohjelmistosuunnittelija_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="nokia")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-savonlinna')
def python_ohjelmistosuunnittelija_tyopaikat32(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="savonlinna")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-riihimaki')
def python_ohjelmistosuunnittelija_tyopaikat33(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="riihimaki")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-vihti')
def python_ohjelmistosuunnittelija_tyopaikat34(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="vihti")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-salo')
def python_ohjelmistosuunnittelija_tyopaikat35(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="salo")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kangasala')
def python_ohjelmistosuunnittelija_tyopaikat36(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kangasala")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-raisio')
def python_ohjelmistosuunnittelija_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="raisio")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-karhula')
def python_ohjelmistosuunnittelija_tyopaikat37(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="karhula")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kemi')
def python_ohjelmistosuunnittelija_tyopaikat38(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kemi")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-iisalmi')
def python_ohjelmistosuunnittelija_tyopaikat39(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="iisalmi")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-varkaus')
def python_ohjelmistosuunnittelija_tyopaikat40(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="varkaus")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-raahe')
def python_ohjelmistosuunnittelija_tyopaikat41(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="raahe")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-ylojarvi')
def python_ohjelmistosuunnittelija_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="ylojarvi")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-hamina')
def python_ohjelmistosuunnittelija_tyopaikat42(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="hamina")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kaarina')
def python_ohjelmistosuunnittelija_tyopaikat43(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kaarina")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-tornio')
def python_ohjelmistosuunnittelija_tyopaikat44(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="tornio")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-heinola')
def python_ohjelmistosuunnittelija_tyopaikat45(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="heinola")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-hollola')
def python_ohjelmistosuunnittelija_tyopaikat46(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="hollola")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-valkeakoski')
def python_ohjelmistosuunnittelija_tyopaikat47(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="valkeakoski")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-siilinjarvi')
def python_ohjelmistosuunnittelija_tyopaikat48(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="siilinjarvi")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kuusankoski')
def python_ohjelmistosuunnittelija_tyopaikat49(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kuusankoski")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-sibbo')
def python_ohjelmistosuunnittelija_tyopaikat50(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="sibbo")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-jakostad')
def python_ohjelmistosuunnittelija_tyopaikat51(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="jakostad")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-lempaala')
def python_ohjelmistosuunnittelija_tyopaikat52(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lempaala")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-mantsala')
def python_ohjelmistosuunnittelija_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="mantsala")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-forssa')
def python_ohjelmistosuunnittelija_tyopaikat53(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="forssa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kuusamo')
def python_ohjelmistosuunnittelija_tyopaikat54(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kuusamo")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-haukipudas')
def python_ohjelmistosuunnittelija_tyopaikat55(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="haukipudas")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-korsholm')
def python_ohjelmistosuunnittelija_tyopaikat56(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="korsholm")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-laukaa')
def python_ohjelmistosuunnittelija_tyopaikat57(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="laukaa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-anjala')
def python_ohjelmistosuunnittelija_tyopaikat58(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="anjala")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-uusikaupunki')
def python_ohjelmistosuunnittelija_tyopaikat59(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="uusikaupunki")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-janakkala')
def python_ohjelmistosuunnittelija_tyopaikat60(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="janakkala")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-pirkkala')
def python_ohjelmistosuunnittelija_tyopaikat61(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="pirkkala")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-lansi-turunmaa')
def python_ohjelmistosuunnittelija_tyopaikat62(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-jamsa')
def python_ohjelmistosuunnittelija_tyopaikat63(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="jamsa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-jamsa')
def python_ohjelmistosuunnittelija_tyopaikat64(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="jamsa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-vammala')
def python_ohjelmistosuunnittelija_tyopaikat65(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="vammala")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-nastola')
def python_ohjelmistosuunnittelija_tyopaikat66(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="nastola")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-orimattila')
def python_ohjelmistosuunnittelija_tyopaikat67(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="orimattila")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kauhajoki')
def python_ohjelmistosuunnittelija_tyopaikat68(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kauhajoki")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-ekenas')
def python_ohjelmistosuunnittelija_tyopaikat69(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="ekenas")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kempele')
def python_ohjelmistosuunnittelija_tyopaikat70(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kempele")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-lapua')
def python_ohjelmistosuunnittelija_tyopaikat71(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lapua")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-lieksa')
def python_ohjelmistosuunnittelija_tyopaikat72(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="lieksa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-naantali')
def python_ohjelmistosuunnittelija_tyopaikat73(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="naantali")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-aanekoski')
def python_ohjelmistosuunnittelija_tyopaikat74(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="aanekoski")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-ylivieska')
def python_ohjelmistosuunnittelija_tyopaikat75(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="ylivieska")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kontiolahti')
def python_ohjelmistosuunnittelija_tyopaikat76(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kontiolahti")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kankaanpaa')
def python_ohjelmistosuunnittelija_tyopaikat77(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kankaanpaa")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-ulvila')
def python_ohjelmistosuunnittelija_tyopaikat78(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="ulvila")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-pieksamaki')
def python_ohjelmistosuunnittelija_tyopaikat79(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="pieksamaki")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kiiminki')
def python_ohjelmistosuunnittelija_tyopaikat80(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kiiminki")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-pargas')
def python_ohjelmistosuunnittelija_tyopaikat81(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="pargas")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-nurmo')
def python_ohjelmistosuunnittelija_tyopaikat82(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="nurmo")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-ilmajoki')
def python_ohjelmistosuunnittelija_tyopaikat83(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="ilmajoki")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-liperi')
def python_ohjelmistosuunnittelija_tyopaikat84(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="liperi")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-keuruu')
def python_ohjelmistosuunnittelija_tyopaikat85(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="keuruu")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-leppavirta')
def python_ohjelmistosuunnittelija_tyopaikat86(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="leppavirta")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kurikka')
def python_ohjelmistosuunnittelija_tyopaikat87(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kurikka")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-nivala')
def python_ohjelmistosuunnittelija_tyopaikat88(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="nivala")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-joutseno')
def python_ohjelmistosuunnittelija_tyopaikat89(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="joutseno")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-pedersore')
def python_ohjelmistosuunnittelija_tyopaikat90(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="pedersore")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-sotkamo')
def python_ohjelmistosuunnittelija_tyopaikat91(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="sotkamo")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-kuhmo')
def python_ohjelmistosuunnittelija_tyopaikat92(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="kuhmo")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-paimio')
def python_ohjelmistosuunnittelija_tyopaikat93(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="paimio")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-saarijarvi')
def python_ohjelmistosuunnittelija_tyopaikat94(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="saarijarvi")
	
@python.route('/python-ohjelmistosuunnittelija-tyopaikat-helsinki')
def python_ohjelmistosuunnittelija_tyopaikat95(page=1):

    job_list = job_obj.get_job("python ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python ohjelmistosuunnittelija", location="helsinki")


####################################################################



##############################################
@python.route('/python-software-developer-jobs-espoo')
def python_software_developer2(page=1):

    job_list = job_obj.get_job("python software developer", "espoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="espoo")

@python.route('/python-software-developer-jobs-tampere')
def python_software_developer3(page=1):

    job_list = job_obj.get_job("python software developer", "tampere").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="tampere")
	
@python.route('/python-software-developer-jobs-vantaa')
def python_software_developer4(page=1):

    job_list = job_obj.get_job("python software developer", "vantaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="vantaa")
	
@python.route('/python-software-developer-jobs-turku')
def python_software_developer5(page=1):

    job_list = job_obj.get_job("python software developer", "turku").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="turku")
	
@python.route('/python-software-developer-jobs-oulu')
def python_software_developer6(page=1):

    job_list = job_obj.get_job("python software developer", "oulu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="oulu")
	
@python.route('/python-software-developer-jobs-lahti')
def python_software_developer7(page=1):

    job_list = job_obj.get_job("python software developer", "lahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="lahti")
	
@python.route('/python-software-developer-jobs-kuopio')
def python_software_developer8(page=1):

    job_list = job_obj.get_job("python software developer", "kuopio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kuopio")
	
@python.route('/python-software-developer-jobs-jyvvaskyla')
def python_software_developer9(page=1):

    job_list = job_obj.get_job("python software developer", "jyvvaskyla").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="jyvvaskyla")

@python.route('/python-software-developer-jobs-pori')
def python_software_developer10(page=1):

    job_list = job_obj.get_job("python software developer", "pori").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="pori")

@python.route('/python-software-developer-jobs-lappeenranta')
def python_software_developer11(page=1):

    job_list = job_obj.get_job("python software developer", "lappeenranta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="lappeenranta")	
	
@python.route('/python-software-developer-jobs-vaasa')
def python_software_developer12(page=1):

    job_list = job_obj.get_job("python software developer", "vaasa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="vaasa")
	
@python.route('/python-software-developer-jobs-kotka')
def python_software_developer13(page=1):

    job_list = job_obj.get_job("python software developer", "kotka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kotka")
	
@python.route('/python-software-developer-jobs-joensuu')
def python_software_developer14(page=1):

    job_list = job_obj.get_job("python software developer", "joensuu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="joensuu")
	
@python.route('/python-software-developer-jobs-hameenlinna')
def python_software_developer15(page=1):

    job_list = job_obj.get_job("python software developer", "hameenlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="hameenlinna")
	
@python.route('/python-software-developer-jobs-porvoo')
def python_software_developer16(page=1):

    job_list = job_obj.get_job("python software developer", "porvoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="porvoo")
	
@python.route('/python-software-developer-jobs-mikkeli')
def python_software_developer17(page=1):

    job_list = job_obj.get_job("python software developer", "mikkeli").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="mikkeli")

@python.route('/python-software-developer-jobs-hyvinkaa')
def python_software_developer18(page=1):

    job_list = job_obj.get_job("python software developer", "hyvinkaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="hyvinkaa")
	
@python.route('/python-software-developer-jobs-nurmijarvi')
def python_software_developer19(page=1):

    job_list = job_obj.get_job("python software developer", "nurmijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="nurmijarvi")

@python.route('/python-software-developer-jobs-jarvenpaa')
def python_software_developer20(page=1):

    job_list = job_obj.get_job("python software developer", "jarvenpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="jarvenpaa")
	
@python.route('/python-software-developer-jobs-rauma')
def python_software_developer21(page=1):

    job_list = job_obj.get_job("python software developer", "rauma").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="rauma")
	
@python.route('/python-software-developer-jobs-lohja')
def python_software_developer22(page=1):

    job_list = job_obj.get_job("python software developer", "lohja").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="lohja")
	
@python.route('/python-software-developer-jobs-karleby')
def python_software_developer23(page=1):

    job_list = job_obj.get_job("python software developer", "karleby").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="karleby")
	
@python.route('/python-software-developer-jobs-kajaani')
def python_software_developer24(page=1):

    job_list = job_obj.get_job("python software developer", "kajaani").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kajaani")
	
@python.route('/python-software-developer-jobs-rovaniemi')
def python_software_developer25(page=1):

    job_list = job_obj.get_job("python software developer", "rovaniemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="rovaniemi")
	
@python.route('/python-software-developer-jobs-tuusula')
def python_software_developer26(page=1):

    job_list = job_obj.get_job("python software developer", "tuusula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="tuusula")
	
@python.route('/python-software-developer-jobs-kirkkonummi')
def python_software_developer27(page=1):

    job_list = job_obj.get_job("python software developer", "kirkkonummi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kirkkonummi")
	
@python.route('/python-software-developer-jobs-seinajoki')
def python_software_developer28(page=1):

    job_list = job_obj.get_job("python software developer", "seinajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="seinajoki")
	
@python.route('/python-software-developer-jobs-kerava')
def python_software_developer29(page=1):

    job_list = job_obj.get_job("python software developer", "kerava").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kerava")
	
@python.route('/python-software-developer-jobs-kouvola')
def python_software_developer30(page=1):

    job_list = job_obj.get_job("python software developer", "kouvola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kouvola")
	
@python.route('/python-software-developer-jobs-imatra')
def python_software_developer31(page=1):

    job_list = job_obj.get_job("python software developer", "imatra").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="imatra")
	
@python.route('/python-software-developer-jobs-nokia')
def python_software_developer32_1(page=1):

    job_list = job_obj.get_job("python software developer", "nokia").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="nokia")
	
@python.route('/python-software-developer-jobs-savonlinna')
def python_software_developer32(page=1):

    job_list = job_obj.get_job("python software developer", "savonlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="savonlinna")
	
@python.route('/python-software-developer-jobs-riihimaki')
def python_software_developer33(page=1):

    job_list = job_obj.get_job("python software developer", "riihimaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="riihimaki")
	
@python.route('/python-software-developer-jobs-vihti')
def python_software_developer34(page=1):

    job_list = job_obj.get_job("python software developer", "vihti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="vihti")
	
@python.route('/python-software-developer-jobs-salo')
def python_software_developer35(page=1):

    job_list = job_obj.get_job("python software developer", "salo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="salo")
	
@python.route('/python-software-developer-jobs-kangasala')
def python_software_developer36(page=1):

    job_list = job_obj.get_job("python software developer", "kangasala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kangasala")
	
@python.route('/python-software-developer-jobs-raisio')
def python_software_developer37_1(page=1):

    job_list = job_obj.get_job("python software developer", "raisio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="raisio")
	
@python.route('/python-software-developer-jobs-karhula')
def python_software_developer37(page=1):

    job_list = job_obj.get_job("python software developer", "karhula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="karhula")
	
@python.route('/python-software-developer-jobs-kemi')
def python_software_developer38(page=1):

    job_list = job_obj.get_job("python software developer", "kemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kemi")
	
@python.route('/python-software-developer-jobs-iisalmi')
def python_software_developer39(page=1):

    job_list = job_obj.get_job("python software developer", "iisalmi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="iisalmi")
	
@python.route('/python-software-developer-jobs-varkaus')
def python_software_developer40(page=1):

    job_list = job_obj.get_job("python software developer", "varkaus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="varkaus")
	
@python.route('/python-software-developer-jobs-raahe')
def python_software_developer41(page=1):

    job_list = job_obj.get_job("python software developer", "raahe").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="raahe")
	
@python.route('/python-software-developer-jobs-ylojarvi')
def python_software_developer42_1(page=1):

    job_list = job_obj.get_job("python software developer", "ylojarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="ylojarvi")
	
@python.route('/python-software-developer-jobs-hamina')
def python_software_developer42(page=1):

    job_list = job_obj.get_job("python software developer", "hamina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="hamina")
	
@python.route('/python-software-developer-jobs-kaarina')
def python_software_developer43(page=1):

    job_list = job_obj.get_job("python software developer", "kaarina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kaarina")
	
@python.route('/python-software-developer-jobs-tornio')
def python_software_developer44(page=1):

    job_list = job_obj.get_job("python software developer", "tornio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="tornio")
	
@python.route('/python-software-developer-jobs-heinola')
def python_software_developer45(page=1):

    job_list = job_obj.get_job("python software developer", "heinola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="heinola")
	
@python.route('/python-software-developer-jobs-hollola')
def python_software_developer46(page=1):

    job_list = job_obj.get_job("python software developer", "hollola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="hollola")
	
@python.route('/python-software-developer-jobs-valkeakoski')
def python_software_developer47(page=1):

    job_list = job_obj.get_job("python software developer", "valkeakoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="valkeakoski")
	
@python.route('/python-software-developer-jobs-siilinjarvi')
def python_software_developer48(page=1):

    job_list = job_obj.get_job("python software developer", "siilinjarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="siilinjarvi")
	
@python.route('/python-software-developer-jobs-kuusankoski')
def python_software_developer49(page=1):

    job_list = job_obj.get_job("python software developer", "kuusankoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kuusankoski")
	
@python.route('/python-software-developer-jobs-sibbo')
def python_software_developer50(page=1):

    job_list = job_obj.get_job("python software developer", "sibbo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="sibbo")
	
@python.route('/python-software-developer-jobs-jakostad')
def python_software_developer51(page=1):

    job_list = job_obj.get_job("python software developer", "jakostad").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="jakostad")
	
@python.route('/python-software-developer-jobs-lempaala')
def python_software_developer52(page=1):

    job_list = job_obj.get_job("python software developer", "lempaala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="lempaala")
	
@python.route('/python-software-developer-jobs-mantsala')
def python_software_developer52_1(page=1):

    job_list = job_obj.get_job("python software developer", "mantsala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="mantsala")
	
@python.route('/python-software-developer-jobs-forssa')
def python_software_developer53(page=1):

    job_list = job_obj.get_job("python software developer", "forssa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="forssa")
	
@python.route('/python-software-developer-jobs-kuusamo')
def python_software_developer54(page=1):

    job_list = job_obj.get_job("python software developer", "kuusamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kuusamo")
	
@python.route('/python-software-developer-jobs-haukipudas')
def python_software_developer55(page=1):

    job_list = job_obj.get_job("python software developer", "haukipudas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="haukipudas")
	
@python.route('/python-software-developer-jobs-korsholm')
def python_software_developer56(page=1):

    job_list = job_obj.get_job("python software developer", "korsholm").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="korsholm")
	
@python.route('/python-software-developer-jobs-laukaa')
def python_software_developer57(page=1):

    job_list = job_obj.get_job("python software developer", "laukaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="laukaa")
	
@python.route('/python-software-developer-jobs-anjala')
def python_software_developer58(page=1):

    job_list = job_obj.get_job("python software developer", "anjala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="anjala")
	
@python.route('/python-software-developer-jobs-uusikaupunki')
def python_software_developer59(page=1):

    job_list = job_obj.get_job("python software developer", "uusikaupunki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="uusikaupunki")
	
@python.route('/python-software-developer-jobs-janakkala')
def python_software_developer60(page=1):

    job_list = job_obj.get_job("python software developer", "janakkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="janakkala")
	
@python.route('/python-software-developer-jobs-pirkkala')
def python_software_developer61(page=1):

    job_list = job_obj.get_job("python software developer", "pirkkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="pirkkala")
	
@python.route('/python-software-developer-jobs-lansi-turunmaa')
def python_software_developer62(page=1):

    job_list = job_obj.get_job("python software developer", "lansi-turunmaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="lansi-turunmaa")
	
@python.route('/python-software-developer-jobs-jamsa')
def python_software_developer63(page=1):

    job_list = job_obj.get_job("python software developer", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="jamsa")
	
@python.route('/python-software-developer-jobs-jamsa')
def python_software_developer64(page=1):

    job_list = job_obj.get_job("python software developer", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="jamsa")
	
@python.route('/python-software-developer-jobs-vammala')
def python_software_developer65(page=1):

    job_list = job_obj.get_job("python software developer", "vammala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="vammala")
	
@python.route('/python-software-developer-jobs-nastola')
def python_software_developer66(page=1):

    job_list = job_obj.get_job("python software developer", "nastola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="nastola")
	
@python.route('/python-software-developer-jobs-orimattila')
def python_software_developer67(page=1):

    job_list = job_obj.get_job("python software developer", "orimattila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="orimattila")
	
@python.route('/python-software-developer-jobs-kauhajoki')
def python_software_developer68(page=1):

    job_list = job_obj.get_job("python software developer", "kauhajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kauhajoki")
	
@python.route('/python-software-developer-jobs-ekenas')
def python_software_developer69(page=1):

    job_list = job_obj.get_job("python software developer", "ekenas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="ekenas")
	
@python.route('/python-software-developer-jobs-kempele')
def python_software_developer70(page=1):

    job_list = job_obj.get_job("python software developer", "kempele").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kempele")
	
@python.route('/python-software-developer-jobs-lapua')
def python_software_developer71(page=1):

    job_list = job_obj.get_job("python software developer", "lapua").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="lapua")
	
@python.route('/python-software-developer-jobs-lieksa')
def python_software_developer72(page=1):

    job_list = job_obj.get_job("python software developer", "lieksa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="lieksa")
	
@python.route('/python-software-developer-jobs-naantali')
def python_software_developer73(page=1):

    job_list = job_obj.get_job("python software developer", "naantali").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="naantali")
	
@python.route('/python-software-developer-jobs-aanekoski')
def python_software_developer74(page=1):

    job_list = job_obj.get_job("python software developer", "aanekoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="aanekoski")
	
@python.route('/python-software-developer-jobs-ylivieska')
def python_software_developer75(page=1):

    job_list = job_obj.get_job("python software developer", "ylivieska").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="ylivieska")
	
@python.route('/python-software-developer-jobs-kontiolahti')
def python_software_developer76(page=1):

    job_list = job_obj.get_job("python software developer", "kontiolahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kontiolahti")
	
@python.route('/python-software-developer-jobs-kankaanpaa')
def python_software_developer77(page=1):

    job_list = job_obj.get_job("python software developer", "kankaanpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kankaanpaa")
	
@python.route('/python-software-developer-jobs-ulvila')
def python_software_developer78(page=1):

    job_list = job_obj.get_job("python software developer", "ulvila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="ulvila")
	
@python.route('/python-software-developer-jobs-pieksamaki')
def python_software_developer79(page=1):

    job_list = job_obj.get_job("python software developer", "pieksamaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="pieksamaki")
	
@python.route('/python-software-developer-jobs-kiiminki')
def python_software_developer80(page=1):

    job_list = job_obj.get_job("python software developer", "kiiminki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kiiminki")
	
@python.route('/python-software-developer-jobs-pargas')
def python_software_developer81(page=1):

    job_list = job_obj.get_job("python software developer", "pargas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="pargas")
	
@python.route('/python-software-developer-jobs-nurmo')
def python_software_developer82(page=1):

    job_list = job_obj.get_job("python software developer", "nurmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="nurmo")
	
@python.route('/python-software-developer-jobs-ilmajoki')
def python_software_developer83(page=1):

    job_list = job_obj.get_job("python software developer", "ilmajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="ilmajoki")
	
@python.route('/python-software-developer-jobs-liperi')
def python_software_developer84(page=1):

    job_list = job_obj.get_job("python software developer", "liperi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="liperi")
	
@python.route('/python-software-developer-jobs-keuruu')
def python_software_developer85(page=1):

    job_list = job_obj.get_job("python software developer", "keuruu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="keuruu")
	
@python.route('/python-software-developer-jobs-leppavirta')
def python_software_developer86(page=1):

    job_list = job_obj.get_job("python software developer", "leppavirta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="leppavirta")
	
@python.route('/python-software-developer-jobs-kurikka')
def python_software_developer87(page=1):

    job_list = job_obj.get_job("python software developer", "kurikka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kurikka")
	
@python.route('/python-software-developer-jobs-nivala')
def python_software_developer88(page=1):

    job_list = job_obj.get_job("python software developer", "nivala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="nivala")
	
@python.route('/python-software-developer-jobs-joutseno')
def python_software_developer89(page=1):

    job_list = job_obj.get_job("python software developer", "joutseno").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="joutseno")
	
@python.route('/python-software-developer-jobs-pedersore')
def python_software_developer90(page=1):

    job_list = job_obj.get_job("python software developer", "pedersore").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="pedersore")
	
@python.route('/python-software-developer-jobs-sotkamo')
def python_software_developer91(page=1):

    job_list = job_obj.get_job("python software developer", "sotkamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="sotkamo")
	
@python.route('/python-software-developer-jobs-kuhmo')
def python_software_developer92(page=1):

    job_list = job_obj.get_job("python software developer", "kuhmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="kuhmo")
	
@python.route('/python-software-developer-jobs-paimio')
def python_software_developer93(page=1):

    job_list = job_obj.get_job("python software developer", "paimio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="paimio")
	
@python.route('/python-software-developer-jobs-saarijarvi')
def python_software_developer94(page=1):

    job_list = job_obj.get_job("python software developer", "saarijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="saarijarvi")
	
@python.route('/python-software-developer-jobs-helsinki')
def python_software_developer95(page=1):

    job_list = job_obj.get_job("python software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="python software developer", location="helsinki")


####################################################################
