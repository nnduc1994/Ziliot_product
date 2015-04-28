from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PAGE = 7

php = Blueprint('php', __name__)
job_obj = Job()



####################################################################


@php.route('/php_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "php" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def php_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="espoo")

@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def php_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="tampere")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def php_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="vantaa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def php_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="turku")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def php_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="oulu")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def php_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lahti")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def php_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kuopio")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def php_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="jyvvaskyla")

@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def php_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="pori")

@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def php_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lappeenranta")	
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def php_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="vaasa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def php_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kotka")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def php_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="joensuu")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def php_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="hameenlinna")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def php_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="porvoo")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def php_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="mikkeli")

@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def php_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="hyvinkaa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def php_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="nurmijarvi")

@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def php_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="jarvenpaa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def php_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="rauma")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def php_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lohja")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def php_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="karleby")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def php_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kajaani")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def php_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="rovaniemi")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def php_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="tuusula")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def php_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kirkkonummi")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def php_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="seinajoki")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def php_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kerava")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def php_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kouvola")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def php_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="imatra")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def php_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="nokia")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def php_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="savonlinna")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def php_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="riihimaki")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def php_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="vihti")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def php_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="salo")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def php_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kangasala")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def php_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="raisio")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def php_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="karhula")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def php_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kemi")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def php_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="iisalmi")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def php_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="varkaus")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def php_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="raahe")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def php_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="ylojarvi")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def php_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="hamina")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def php_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kaarina")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def php_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="tornio")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def php_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="heinola")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def php_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="hollola")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def php_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="valkeakoski")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def php_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="siilinjarvi")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def php_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kuusankoski")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def php_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="sibbo")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def php_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="jakostad")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def php_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lempaala")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def php_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="mantsala")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def php_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="forssa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def php_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kuusamo")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def php_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="haukipudas")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def php_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="korsholm")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def php_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="laukaa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def php_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="anjala")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def php_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="uusikaupunki")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def php_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="janakkala")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def php_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="pirkkala")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def php_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def php_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="jamsa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def php_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="jamsa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def php_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="vammala")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def php_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="nastola")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def php_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="orimattila")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def php_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kauhajoki")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def php_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="ekenas")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def php_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kempele")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def php_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lapua")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def php_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lieksa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def php_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="naantali")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def php_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="aanekoski")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def php_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="ylivieska")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def php_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kontiolahti")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def php_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kankaanpaa")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def php_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="ulvila")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def php_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="pieksamaki")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def php_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kiiminki")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def php_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="pargas")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def php_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="nurmo")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def php_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="ilmajoki")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def php_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="liperi")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def php_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="keuruu")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def php_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="leppavirta")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def php_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kurikka")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def php_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="nivala")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def php_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="joutseno")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def php_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="pedersore")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def php_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="sotkamo")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def php_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kuhmo")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def php_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="paimio")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def php_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="saarijarvi")
	
@php.route('/php-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def php_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@php.route('/php-software-developer-jobs-espoo')
def php_software_developer2(page=1):

    job_list = job_obj.get_job("php software developer", "espoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="espoo")

@php.route('/php-software-developer-jobs-tampere')
def php_software_developer3(page=1):

    job_list = job_obj.get_job("php software developer", "tampere").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="tampere")
	
@php.route('/php-software-developer-jobs-vantaa')
def php_software_developer4(page=1):

    job_list = job_obj.get_job("php software developer", "vantaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="vantaa")
	
@php.route('/php-software-developer-jobs-turku')
def php_software_developer5(page=1):

    job_list = job_obj.get_job("php software developer", "turku").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="turku")
	
@php.route('/php-software-developer-jobs-oulu')
def php_software_developer6(page=1):

    job_list = job_obj.get_job("php software developer", "oulu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="oulu")
	
@php.route('/php-software-developer-jobs-lahti')
def php_software_developer7(page=1):

    job_list = job_obj.get_job("php software developer", "lahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="lahti")
	
@php.route('/php-software-developer-jobs-kuopio')
def php_software_developer8(page=1):

    job_list = job_obj.get_job("php software developer", "kuopio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kuopio")
	
@php.route('/php-software-developer-jobs-jyvvaskyla')
def php_software_developer9(page=1):

    job_list = job_obj.get_job("php software developer", "jyvvaskyla").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="jyvvaskyla")

@php.route('/php-software-developer-jobs-pori')
def php_software_developer10(page=1):

    job_list = job_obj.get_job("php software developer", "pori").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="pori")

@php.route('/php-software-developer-jobs-lappeenranta')
def php_software_developer11(page=1):

    job_list = job_obj.get_job("php software developer", "lappeenranta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="lappeenranta")	
	
@php.route('/php-software-developer-jobs-vaasa')
def php_software_developer12(page=1):

    job_list = job_obj.get_job("php software developer", "vaasa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="vaasa")
	
@php.route('/php-software-developer-jobs-kotka')
def php_software_developer13(page=1):

    job_list = job_obj.get_job("php software developer", "kotka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kotka")
	
@php.route('/php-software-developer-jobs-joensuu')
def php_software_developer14(page=1):

    job_list = job_obj.get_job("php software developer", "joensuu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="joensuu")
	
@php.route('/php-software-developer-jobs-hameenlinna')
def php_software_developer15(page=1):

    job_list = job_obj.get_job("php software developer", "hameenlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="hameenlinna")
	
@php.route('/php-software-developer-jobs-porvoo')
def php_software_developer16(page=1):

    job_list = job_obj.get_job("php software developer", "porvoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="porvoo")
	
@php.route('/php-software-developer-jobs-mikkeli')
def php_software_developer17(page=1):

    job_list = job_obj.get_job("php software developer", "mikkeli").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="mikkeli")

@php.route('/php-software-developer-jobs-hyvinkaa')
def php_software_developer18(page=1):

    job_list = job_obj.get_job("php software developer", "hyvinkaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="hyvinkaa")
	
@php.route('/php-software-developer-jobs-nurmijarvi')
def php_software_developer19(page=1):

    job_list = job_obj.get_job("php software developer", "nurmijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="nurmijarvi")

@php.route('/php-software-developer-jobs-jarvenpaa')
def php_software_developer20(page=1):

    job_list = job_obj.get_job("php software developer", "jarvenpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="jarvenpaa")
	
@php.route('/php-software-developer-jobs-rauma')
def php_software_developer21(page=1):

    job_list = job_obj.get_job("php software developer", "rauma").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="rauma")
	
@php.route('/php-software-developer-jobs-lohja')
def php_software_developer22(page=1):

    job_list = job_obj.get_job("php software developer", "lohja").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="lohja")
	
@php.route('/php-software-developer-jobs-karleby')
def php_software_developer23(page=1):

    job_list = job_obj.get_job("php software developer", "karleby").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="karleby")
	
@php.route('/php-software-developer-jobs-kajaani')
def php_software_developer24(page=1):

    job_list = job_obj.get_job("php software developer", "kajaani").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kajaani")
	
@php.route('/php-software-developer-jobs-rovaniemi')
def php_software_developer25(page=1):

    job_list = job_obj.get_job("php software developer", "rovaniemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="rovaniemi")
	
@php.route('/php-software-developer-jobs-tuusula')
def php_software_developer26(page=1):

    job_list = job_obj.get_job("php software developer", "tuusula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="tuusula")
	
@php.route('/php-software-developer-jobs-kirkkonummi')
def php_software_developer27(page=1):

    job_list = job_obj.get_job("php software developer", "kirkkonummi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kirkkonummi")
	
@php.route('/php-software-developer-jobs-seinajoki')
def php_software_developer28(page=1):

    job_list = job_obj.get_job("php software developer", "seinajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="seinajoki")
	
@php.route('/php-software-developer-jobs-kerava')
def php_software_developer29(page=1):

    job_list = job_obj.get_job("php software developer", "kerava").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kerava")
	
@php.route('/php-software-developer-jobs-kouvola')
def php_software_developer30(page=1):

    job_list = job_obj.get_job("php software developer", "kouvola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kouvola")
	
@php.route('/php-software-developer-jobs-imatra')
def php_software_developer31(page=1):

    job_list = job_obj.get_job("php software developer", "imatra").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="imatra")
	
@php.route('/php-software-developer-jobs-nokia')
def php_software_developer32_1(page=1):

    job_list = job_obj.get_job("php software developer", "nokia").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="nokia")
	
@php.route('/php-software-developer-jobs-savonlinna')
def php_software_developer32(page=1):

    job_list = job_obj.get_job("php software developer", "savonlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="savonlinna")
	
@php.route('/php-software-developer-jobs-riihimaki')
def php_software_developer33(page=1):

    job_list = job_obj.get_job("php software developer", "riihimaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="riihimaki")
	
@php.route('/php-software-developer-jobs-vihti')
def php_software_developer34(page=1):

    job_list = job_obj.get_job("php software developer", "vihti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="vihti")
	
@php.route('/php-software-developer-jobs-salo')
def php_software_developer35(page=1):

    job_list = job_obj.get_job("php software developer", "salo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="salo")
	
@php.route('/php-software-developer-jobs-kangasala')
def php_software_developer36(page=1):

    job_list = job_obj.get_job("php software developer", "kangasala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kangasala")
	
@php.route('/php-software-developer-jobs-raisio')
def php_software_developer37_1(page=1):

    job_list = job_obj.get_job("php software developer", "raisio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="raisio")
	
@php.route('/php-software-developer-jobs-karhula')
def php_software_developer37(page=1):

    job_list = job_obj.get_job("php software developer", "karhula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="karhula")
	
@php.route('/php-software-developer-jobs-kemi')
def php_software_developer38(page=1):

    job_list = job_obj.get_job("php software developer", "kemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kemi")
	
@php.route('/php-software-developer-jobs-iisalmi')
def php_software_developer39(page=1):

    job_list = job_obj.get_job("php software developer", "iisalmi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="iisalmi")
	
@php.route('/php-software-developer-jobs-varkaus')
def php_software_developer40(page=1):

    job_list = job_obj.get_job("php software developer", "varkaus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="varkaus")
	
@php.route('/php-software-developer-jobs-raahe')
def php_software_developer41(page=1):

    job_list = job_obj.get_job("php software developer", "raahe").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="raahe")
	
@php.route('/php-software-developer-jobs-ylojarvi')
def php_software_developer42_1(page=1):

    job_list = job_obj.get_job("php software developer", "ylojarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="ylojarvi")
	
@php.route('/php-software-developer-jobs-hamina')
def php_software_developer42(page=1):

    job_list = job_obj.get_job("php software developer", "hamina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="hamina")
	
@php.route('/php-software-developer-jobs-kaarina')
def php_software_developer43(page=1):

    job_list = job_obj.get_job("php software developer", "kaarina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kaarina")
	
@php.route('/php-software-developer-jobs-tornio')
def php_software_developer44(page=1):

    job_list = job_obj.get_job("php software developer", "tornio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="tornio")
	
@php.route('/php-software-developer-jobs-heinola')
def php_software_developer45(page=1):

    job_list = job_obj.get_job("php software developer", "heinola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="heinola")
	
@php.route('/php-software-developer-jobs-hollola')
def php_software_developer46(page=1):

    job_list = job_obj.get_job("php software developer", "hollola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="hollola")
	
@php.route('/php-software-developer-jobs-valkeakoski')
def php_software_developer47(page=1):

    job_list = job_obj.get_job("php software developer", "valkeakoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="valkeakoski")
	
@php.route('/php-software-developer-jobs-siilinjarvi')
def php_software_developer48(page=1):

    job_list = job_obj.get_job("php software developer", "siilinjarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="siilinjarvi")
	
@php.route('/php-software-developer-jobs-kuusankoski')
def php_software_developer49(page=1):

    job_list = job_obj.get_job("php software developer", "kuusankoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kuusankoski")
	
@php.route('/php-software-developer-jobs-sibbo')
def php_software_developer50(page=1):

    job_list = job_obj.get_job("php software developer", "sibbo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="sibbo")
	
@php.route('/php-software-developer-jobs-jakostad')
def php_software_developer51(page=1):

    job_list = job_obj.get_job("php software developer", "jakostad").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="jakostad")
	
@php.route('/php-software-developer-jobs-lempaala')
def php_software_developer52(page=1):

    job_list = job_obj.get_job("php software developer", "lempaala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="lempaala")
	
@php.route('/php-software-developer-jobs-mantsala')
def php_software_developer52_1(page=1):

    job_list = job_obj.get_job("php software developer", "mantsala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="mantsala")
	
@php.route('/php-software-developer-jobs-forssa')
def php_software_developer53(page=1):

    job_list = job_obj.get_job("php software developer", "forssa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="forssa")
	
@php.route('/php-software-developer-jobs-kuusamo')
def php_software_developer54(page=1):

    job_list = job_obj.get_job("php software developer", "kuusamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kuusamo")
	
@php.route('/php-software-developer-jobs-haukipudas')
def php_software_developer55(page=1):

    job_list = job_obj.get_job("php software developer", "haukipudas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="haukipudas")
	
@php.route('/php-software-developer-jobs-korsholm')
def php_software_developer56(page=1):

    job_list = job_obj.get_job("php software developer", "korsholm").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="korsholm")
	
@php.route('/php-software-developer-jobs-laukaa')
def php_software_developer57(page=1):

    job_list = job_obj.get_job("php software developer", "laukaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="laukaa")
	
@php.route('/php-software-developer-jobs-anjala')
def php_software_developer58(page=1):

    job_list = job_obj.get_job("php software developer", "anjala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="anjala")
	
@php.route('/php-software-developer-jobs-uusikaupunki')
def php_software_developer59(page=1):

    job_list = job_obj.get_job("php software developer", "uusikaupunki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="uusikaupunki")
	
@php.route('/php-software-developer-jobs-janakkala')
def php_software_developer60(page=1):

    job_list = job_obj.get_job("php software developer", "janakkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="janakkala")
	
@php.route('/php-software-developer-jobs-pirkkala')
def php_software_developer61(page=1):

    job_list = job_obj.get_job("php software developer", "pirkkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="pirkkala")
	
@php.route('/php-software-developer-jobs-lansi-turunmaa')
def php_software_developer62(page=1):

    job_list = job_obj.get_job("php software developer", "lansi-turunmaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="lansi-turunmaa")
	
@php.route('/php-software-developer-jobs-jamsa')
def php_software_developer63(page=1):

    job_list = job_obj.get_job("php software developer", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="jamsa")
	
@php.route('/php-software-developer-jobs-jamsa')
def php_software_developer64(page=1):

    job_list = job_obj.get_job("php software developer", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="jamsa")
	
@php.route('/php-software-developer-jobs-vammala')
def php_software_developer65(page=1):

    job_list = job_obj.get_job("php software developer", "vammala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="vammala")
	
@php.route('/php-software-developer-jobs-nastola')
def php_software_developer66(page=1):

    job_list = job_obj.get_job("php software developer", "nastola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="nastola")
	
@php.route('/php-software-developer-jobs-orimattila')
def php_software_developer67(page=1):

    job_list = job_obj.get_job("php software developer", "orimattila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="orimattila")
	
@php.route('/php-software-developer-jobs-kauhajoki')
def php_software_developer68(page=1):

    job_list = job_obj.get_job("php software developer", "kauhajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kauhajoki")
	
@php.route('/php-software-developer-jobs-ekenas')
def php_software_developer69(page=1):

    job_list = job_obj.get_job("php software developer", "ekenas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="ekenas")
	
@php.route('/php-software-developer-jobs-kempele')
def php_software_developer70(page=1):

    job_list = job_obj.get_job("php software developer", "kempele").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kempele")
	
@php.route('/php-software-developer-jobs-lapua')
def php_software_developer71(page=1):

    job_list = job_obj.get_job("php software developer", "lapua").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="lapua")
	
@php.route('/php-software-developer-jobs-lieksa')
def php_software_developer72(page=1):

    job_list = job_obj.get_job("php software developer", "lieksa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="lieksa")
	
@php.route('/php-software-developer-jobs-naantali')
def php_software_developer73(page=1):

    job_list = job_obj.get_job("php software developer", "naantali").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="naantali")
	
@php.route('/php-software-developer-jobs-aanekoski')
def php_software_developer74(page=1):

    job_list = job_obj.get_job("php software developer", "aanekoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="aanekoski")
	
@php.route('/php-software-developer-jobs-ylivieska')
def php_software_developer75(page=1):

    job_list = job_obj.get_job("php software developer", "ylivieska").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="ylivieska")
	
@php.route('/php-software-developer-jobs-kontiolahti')
def php_software_developer76(page=1):

    job_list = job_obj.get_job("php software developer", "kontiolahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kontiolahti")
	
@php.route('/php-software-developer-jobs-kankaanpaa')
def php_software_developer77(page=1):

    job_list = job_obj.get_job("php software developer", "kankaanpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kankaanpaa")
	
@php.route('/php-software-developer-jobs-ulvila')
def php_software_developer78(page=1):

    job_list = job_obj.get_job("php software developer", "ulvila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="ulvila")
	
@php.route('/php-software-developer-jobs-pieksamaki')
def php_software_developer79(page=1):

    job_list = job_obj.get_job("php software developer", "pieksamaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="pieksamaki")
	
@php.route('/php-software-developer-jobs-kiiminki')
def php_software_developer80(page=1):

    job_list = job_obj.get_job("php software developer", "kiiminki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kiiminki")
	
@php.route('/php-software-developer-jobs-pargas')
def php_software_developer81(page=1):

    job_list = job_obj.get_job("php software developer", "pargas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="pargas")
	
@php.route('/php-software-developer-jobs-nurmo')
def php_software_developer82(page=1):

    job_list = job_obj.get_job("php software developer", "nurmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="nurmo")
	
@php.route('/php-software-developer-jobs-ilmajoki')
def php_software_developer83(page=1):

    job_list = job_obj.get_job("php software developer", "ilmajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="ilmajoki")
	
@php.route('/php-software-developer-jobs-liperi')
def php_software_developer84(page=1):

    job_list = job_obj.get_job("php software developer", "liperi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="liperi")
	
@php.route('/php-software-developer-jobs-keuruu')
def php_software_developer85(page=1):

    job_list = job_obj.get_job("php software developer", "keuruu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="keuruu")
	
@php.route('/php-software-developer-jobs-leppavirta')
def php_software_developer86(page=1):

    job_list = job_obj.get_job("php software developer", "leppavirta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="leppavirta")
	
@php.route('/php-software-developer-jobs-kurikka')
def php_software_developer87(page=1):

    job_list = job_obj.get_job("php software developer", "kurikka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kurikka")
	
@php.route('/php-software-developer-jobs-nivala')
def php_software_developer88(page=1):

    job_list = job_obj.get_job("php software developer", "nivala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="nivala")
	
@php.route('/php-software-developer-jobs-joutseno')
def php_software_developer89(page=1):

    job_list = job_obj.get_job("php software developer", "joutseno").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="joutseno")
	
@php.route('/php-software-developer-jobs-pedersore')
def php_software_developer90(page=1):

    job_list = job_obj.get_job("php software developer", "pedersore").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="pedersore")
	
@php.route('/php-software-developer-jobs-sotkamo')
def php_software_developer91(page=1):

    job_list = job_obj.get_job("php software developer", "sotkamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="sotkamo")
	
@php.route('/php-software-developer-jobs-kuhmo')
def php_software_developer92(page=1):

    job_list = job_obj.get_job("php software developer", "kuhmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="kuhmo")
	
@php.route('/php-software-developer-jobs-paimio')
def php_software_developer93(page=1):

    job_list = job_obj.get_job("php software developer", "paimio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="paimio")
	
@php.route('/php-software-developer-jobs-saarijarvi')
def php_software_developer94(page=1):

    job_list = job_obj.get_job("php software developer", "saarijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="saarijarvi")
	
@php.route('/php-software-developer-jobs-helsinki')
def php_software_developer95(page=1):

    job_list = job_obj.get_job("php software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php software developer", location="helsinki")



	 
##############################################
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-espoo')
def php_ohjelmistosuunnittelija_tyopaikat2(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="espoo")

@php.route('/php-ohjelmistosuunnittelija-tyopaikat-tampere')
def php_ohjelmistosuunnittelija_tyopaikat3(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="tampere")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-vantaa')
def php_ohjelmistosuunnittelija_tyopaikat4(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="vantaa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-turku')
def php_ohjelmistosuunnittelija_tyopaikat5(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="turku")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-oulu')
def php_ohjelmistosuunnittelija_tyopaikat6(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="oulu")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-lahti')
def php_ohjelmistosuunnittelija_tyopaikat7(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lahti")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kuopio')
def php_ohjelmistosuunnittelija_tyopaikat8(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kuopio")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-jyvvaskyla')
def php_ohjelmistosuunnittelija_tyopaikat9(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="jyvvaskyla")

@php.route('/php-ohjelmistosuunnittelija-tyopaikat-pori')
def php_ohjelmistosuunnittelija_tyopaikat10(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="pori")

@php.route('/php-ohjelmistosuunnittelija-tyopaikat-lappeenranta')
def php_ohjelmistosuunnittelija_tyopaikat11(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lappeenranta")	
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-vaasa')
def php_ohjelmistosuunnittelija_tyopaikat12(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="vaasa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kotka')
def php_ohjelmistosuunnittelija_tyopaikat13(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kotka")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-joensuu')
def php_ohjelmistosuunnittelija_tyopaikat14(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="joensuu")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-hameenlinna')
def php_ohjelmistosuunnittelija_tyopaikat15(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="hameenlinna")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-porvoo')
def php_ohjelmistosuunnittelija_tyopaikat16(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="porvoo")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-mikkeli')
def php_ohjelmistosuunnittelija_tyopaikat17(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="mikkeli")

@php.route('/php-ohjelmistosuunnittelija-tyopaikat-hyvinkaa')
def php_ohjelmistosuunnittelija_tyopaikat18(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="hyvinkaa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-nurmijarvi')
def php_ohjelmistosuunnittelija_tyopaikat19(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="nurmijarvi")

@php.route('/php-ohjelmistosuunnittelija-tyopaikat-jarvenpaa')
def php_ohjelmistosuunnittelija_tyopaikat20(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="jarvenpaa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-rauma')
def php_ohjelmistosuunnittelija_tyopaikat21(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="rauma")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-lohja')
def php_ohjelmistosuunnittelija_tyopaikat22(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lohja")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-karleby')
def php_ohjelmistosuunnittelija_tyopaikat23(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="karleby")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kajaani')
def php_ohjelmistosuunnittelija_tyopaikat24(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kajaani")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-rovaniemi')
def php_ohjelmistosuunnittelija_tyopaikat25(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="rovaniemi")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-tuusula')
def php_ohjelmistosuunnittelija_tyopaikat26(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="tuusula")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kirkkonummi')
def php_ohjelmistosuunnittelija_tyopaikat27(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kirkkonummi")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-seinajoki')
def php_ohjelmistosuunnittelija_tyopaikat28(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="seinajoki")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kerava')
def php_ohjelmistosuunnittelija_tyopaikat29(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kerava")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kouvola')
def php_ohjelmistosuunnittelija_tyopaikat30(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kouvola")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-imatra')
def php_ohjelmistosuunnittelija_tyopaikat31(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="imatra")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-nokia')
def php_ohjelmistosuunnittelija_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="nokia")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-savonlinna')
def php_ohjelmistosuunnittelija_tyopaikat32(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="savonlinna")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-riihimaki')
def php_ohjelmistosuunnittelija_tyopaikat33(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="riihimaki")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-vihti')
def php_ohjelmistosuunnittelija_tyopaikat34(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="vihti")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-salo')
def php_ohjelmistosuunnittelija_tyopaikat35(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="salo")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kangasala')
def php_ohjelmistosuunnittelija_tyopaikat36(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kangasala")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-raisio')
def php_ohjelmistosuunnittelija_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="raisio")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-karhula')
def php_ohjelmistosuunnittelija_tyopaikat37(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="karhula")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kemi')
def php_ohjelmistosuunnittelija_tyopaikat38(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kemi")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-iisalmi')
def php_ohjelmistosuunnittelija_tyopaikat39(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="iisalmi")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-varkaus')
def php_ohjelmistosuunnittelija_tyopaikat40(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="varkaus")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-raahe')
def php_ohjelmistosuunnittelija_tyopaikat41(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="raahe")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-ylojarvi')
def php_ohjelmistosuunnittelija_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="ylojarvi")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-hamina')
def php_ohjelmistosuunnittelija_tyopaikat42(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="hamina")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kaarina')
def php_ohjelmistosuunnittelija_tyopaikat43(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kaarina")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-tornio')
def php_ohjelmistosuunnittelija_tyopaikat44(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="tornio")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-heinola')
def php_ohjelmistosuunnittelija_tyopaikat45(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="heinola")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-hollola')
def php_ohjelmistosuunnittelija_tyopaikat46(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="hollola")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-valkeakoski')
def php_ohjelmistosuunnittelija_tyopaikat47(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="valkeakoski")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-siilinjarvi')
def php_ohjelmistosuunnittelija_tyopaikat48(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="siilinjarvi")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kuusankoski')
def php_ohjelmistosuunnittelija_tyopaikat49(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kuusankoski")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-sibbo')
def php_ohjelmistosuunnittelija_tyopaikat50(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="sibbo")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-jakostad')
def php_ohjelmistosuunnittelija_tyopaikat51(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="jakostad")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-lempaala')
def php_ohjelmistosuunnittelija_tyopaikat52(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lempaala")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-mantsala')
def php_ohjelmistosuunnittelija_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="mantsala")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-forssa')
def php_ohjelmistosuunnittelija_tyopaikat53(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="forssa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kuusamo')
def php_ohjelmistosuunnittelija_tyopaikat54(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kuusamo")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-haukipudas')
def php_ohjelmistosuunnittelija_tyopaikat55(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="haukipudas")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-korsholm')
def php_ohjelmistosuunnittelija_tyopaikat56(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="korsholm")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-laukaa')
def php_ohjelmistosuunnittelija_tyopaikat57(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="laukaa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-anjala')
def php_ohjelmistosuunnittelija_tyopaikat58(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="anjala")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-uusikaupunki')
def php_ohjelmistosuunnittelija_tyopaikat59(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="uusikaupunki")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-janakkala')
def php_ohjelmistosuunnittelija_tyopaikat60(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="janakkala")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-pirkkala')
def php_ohjelmistosuunnittelija_tyopaikat61(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="pirkkala")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-lansi-turunmaa')
def php_ohjelmistosuunnittelija_tyopaikat62(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-jamsa')
def php_ohjelmistosuunnittelija_tyopaikat63(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="jamsa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-jamsa')
def php_ohjelmistosuunnittelija_tyopaikat64(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="jamsa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-vammala')
def php_ohjelmistosuunnittelija_tyopaikat65(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="vammala")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-nastola')
def php_ohjelmistosuunnittelija_tyopaikat66(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="nastola")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-orimattila')
def php_ohjelmistosuunnittelija_tyopaikat67(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="orimattila")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kauhajoki')
def php_ohjelmistosuunnittelija_tyopaikat68(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kauhajoki")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-ekenas')
def php_ohjelmistosuunnittelija_tyopaikat69(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="ekenas")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kempele')
def php_ohjelmistosuunnittelija_tyopaikat70(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kempele")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-lapua')
def php_ohjelmistosuunnittelija_tyopaikat71(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lapua")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-lieksa')
def php_ohjelmistosuunnittelija_tyopaikat72(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="lieksa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-naantali')
def php_ohjelmistosuunnittelija_tyopaikat73(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="naantali")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-aanekoski')
def php_ohjelmistosuunnittelija_tyopaikat74(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="aanekoski")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-ylivieska')
def php_ohjelmistosuunnittelija_tyopaikat75(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="ylivieska")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kontiolahti')
def php_ohjelmistosuunnittelija_tyopaikat76(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kontiolahti")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kankaanpaa')
def php_ohjelmistosuunnittelija_tyopaikat77(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kankaanpaa")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-ulvila')
def php_ohjelmistosuunnittelija_tyopaikat78(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="ulvila")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-pieksamaki')
def php_ohjelmistosuunnittelija_tyopaikat79(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="pieksamaki")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kiiminki')
def php_ohjelmistosuunnittelija_tyopaikat80(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kiiminki")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-pargas')
def php_ohjelmistosuunnittelija_tyopaikat81(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="pargas")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-nurmo')
def php_ohjelmistosuunnittelija_tyopaikat82(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="nurmo")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-ilmajoki')
def php_ohjelmistosuunnittelija_tyopaikat83(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="ilmajoki")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-liperi')
def php_ohjelmistosuunnittelija_tyopaikat84(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="liperi")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-keuruu')
def php_ohjelmistosuunnittelija_tyopaikat85(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="keuruu")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-leppavirta')
def php_ohjelmistosuunnittelija_tyopaikat86(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="leppavirta")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kurikka')
def php_ohjelmistosuunnittelija_tyopaikat87(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kurikka")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-nivala')
def php_ohjelmistosuunnittelija_tyopaikat88(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="nivala")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-joutseno')
def php_ohjelmistosuunnittelija_tyopaikat89(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="joutseno")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-pedersore')
def php_ohjelmistosuunnittelija_tyopaikat90(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="pedersore")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-sotkamo')
def php_ohjelmistosuunnittelija_tyopaikat91(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="sotkamo")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-kuhmo')
def php_ohjelmistosuunnittelija_tyopaikat92(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="kuhmo")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-paimio')
def php_ohjelmistosuunnittelija_tyopaikat93(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="paimio")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-saarijarvi')
def php_ohjelmistosuunnittelija_tyopaikat94(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="saarijarvi")
	
@php.route('/php-ohjelmistosuunnittelija-tyopaikat-helsinki')
def php_ohjelmistosuunnittelija_tyopaikat95(page=1):

    job_list = job_obj.get_job("php ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="php ohjelmistosuunnittelija", location="helsinki")


####################################################################

