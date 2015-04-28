from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

perl = Blueprint('perl', __name__)
job_obj = Job()



####################################################################


@perl.route('/perl_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "perl" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def perl_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="espoo")

@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def perl_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="tampere")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def perl_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="vantaa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def perl_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="turku")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def perl_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="oulu")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def perl_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="lahti")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def perl_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kuopio")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def perl_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="jyvvaskyla")

@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def perl_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="pori")

@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def perl_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="lappeenranta")	
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def perl_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="vaasa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def perl_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kotka")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def perl_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="joensuu")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def perl_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="hameenlinna")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def perl_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="porvoo")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def perl_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="mikkeli")

@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def perl_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="hyvinkaa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def perl_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="nurmijarvi")

@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def perl_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="jarvenpaa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def perl_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="rauma")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def perl_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="lohja")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def perl_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="karleby")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def perl_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kajaani")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def perl_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="rovaniemi")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def perl_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="tuusula")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def perl_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kirkkonummi")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def perl_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="seinajoki")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def perl_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kerava")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def perl_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kouvola")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def perl_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="imatra")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def perl_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="nokia")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def perl_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="savonlinna")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def perl_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="riihimaki")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def perl_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="vihti")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def perl_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="salo")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def perl_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kangasala")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def perl_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="raisio")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def perl_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="karhula")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def perl_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kemi")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def perl_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="iisalmi")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def perl_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="varkaus")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def perl_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="raahe")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def perl_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="ylojarvi")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def perl_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="hamina")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def perl_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kaarina")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def perl_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="tornio")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def perl_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="heinola")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def perl_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="hollola")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def perl_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="valkeakoski")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def perl_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="siilinjarvi")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def perl_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kuusankoski")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def perl_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="sibbo")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def perl_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="jakostad")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def perl_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="lempaala")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def perl_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="mantsala")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def perl_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="forssa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def perl_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kuusamo")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def perl_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="haukipudas")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def perl_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="korsholm")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def perl_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="laukaa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def perl_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="anjala")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def perl_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="uusikaupunki")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def perl_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="janakkala")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def perl_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="pirkkala")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def perl_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def perl_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="jamsa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def perl_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="jamsa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def perl_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="vammala")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def perl_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="nastola")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def perl_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="orimattila")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def perl_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kauhajoki")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def perl_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="ekenas")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def perl_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kempele")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def perl_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="lapua")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def perl_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="lieksa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def perl_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="naantali")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def perl_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="aanekoski")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def perl_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="ylivieska")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def perl_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kontiolahti")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def perl_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kankaanpaa")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def perl_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="ulvila")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def perl_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="pieksamaki")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def perl_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kiiminki")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def perl_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="pargas")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def perl_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="nurmo")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def perl_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="ilmajoki")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def perl_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="liperi")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def perl_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="keuruu")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def perl_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="leppavirta")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def perl_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kurikka")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def perl_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="nivala")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def perl_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="joutseno")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def perl_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="pedersore")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def perl_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="sotkamo")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def perl_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="kuhmo")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def perl_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="paimio")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def perl_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="saarijarvi")
	
@perl.route('/perl-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def perl_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("perl ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@perl.route('/perl-software-developer-jobs-espoo')
def perl_software_developer2(page=1):

    job_list = job_obj.get_job("perl software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="espoo")

@perl.route('/perl-software-developer-jobs-tampere')
def perl_software_developer3(page=1):

    job_list = job_obj.get_job("perl software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="tampere")
	
@perl.route('/perl-software-developer-jobs-vantaa')
def perl_software_developer4(page=1):

    job_list = job_obj.get_job("perl software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="vantaa")
	
@perl.route('/perl-software-developer-jobs-turku')
def perl_software_developer5(page=1):

    job_list = job_obj.get_job("perl software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="turku")
	
@perl.route('/perl-software-developer-jobs-oulu')
def perl_software_developer6(page=1):

    job_list = job_obj.get_job("perl software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="oulu")
	
@perl.route('/perl-software-developer-jobs-lahti')
def perl_software_developer7(page=1):

    job_list = job_obj.get_job("perl software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="lahti")
	
@perl.route('/perl-software-developer-jobs-kuopio')
def perl_software_developer8(page=1):

    job_list = job_obj.get_job("perl software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kuopio")
	
@perl.route('/perl-software-developer-jobs-jyvvaskyla')
def perl_software_developer9(page=1):

    job_list = job_obj.get_job("perl software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="jyvvaskyla")

@perl.route('/perl-software-developer-jobs-pori')
def perl_software_developer10(page=1):

    job_list = job_obj.get_job("perl software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="pori")

@perl.route('/perl-software-developer-jobs-lappeenranta')
def perl_software_developer11(page=1):

    job_list = job_obj.get_job("perl software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="lappeenranta")	
	
@perl.route('/perl-software-developer-jobs-vaasa')
def perl_software_developer12(page=1):

    job_list = job_obj.get_job("perl software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="vaasa")
	
@perl.route('/perl-software-developer-jobs-kotka')
def perl_software_developer13(page=1):

    job_list = job_obj.get_job("perl software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kotka")
	
@perl.route('/perl-software-developer-jobs-joensuu')
def perl_software_developer14(page=1):

    job_list = job_obj.get_job("perl software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="joensuu")
	
@perl.route('/perl-software-developer-jobs-hameenlinna')
def perl_software_developer15(page=1):

    job_list = job_obj.get_job("perl software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="hameenlinna")
	
@perl.route('/perl-software-developer-jobs-porvoo')
def perl_software_developer16(page=1):

    job_list = job_obj.get_job("perl software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="porvoo")
	
@perl.route('/perl-software-developer-jobs-mikkeli')
def perl_software_developer17(page=1):

    job_list = job_obj.get_job("perl software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="mikkeli")

@perl.route('/perl-software-developer-jobs-hyvinkaa')
def perl_software_developer18(page=1):

    job_list = job_obj.get_job("perl software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="hyvinkaa")
	
@perl.route('/perl-software-developer-jobs-nurmijarvi')
def perl_software_developer19(page=1):

    job_list = job_obj.get_job("perl software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="nurmijarvi")

@perl.route('/perl-software-developer-jobs-jarvenpaa')
def perl_software_developer20(page=1):

    job_list = job_obj.get_job("perl software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="jarvenpaa")
	
@perl.route('/perl-software-developer-jobs-rauma')
def perl_software_developer21(page=1):

    job_list = job_obj.get_job("perl software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="rauma")
	
@perl.route('/perl-software-developer-jobs-lohja')
def perl_software_developer22(page=1):

    job_list = job_obj.get_job("perl software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="lohja")
	
@perl.route('/perl-software-developer-jobs-karleby')
def perl_software_developer23(page=1):

    job_list = job_obj.get_job("perl software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="karleby")
	
@perl.route('/perl-software-developer-jobs-kajaani')
def perl_software_developer24(page=1):

    job_list = job_obj.get_job("perl software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kajaani")
	
@perl.route('/perl-software-developer-jobs-rovaniemi')
def perl_software_developer25(page=1):

    job_list = job_obj.get_job("perl software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="rovaniemi")
	
@perl.route('/perl-software-developer-jobs-tuusula')
def perl_software_developer26(page=1):

    job_list = job_obj.get_job("perl software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="tuusula")
	
@perl.route('/perl-software-developer-jobs-kirkkonummi')
def perl_software_developer27(page=1):

    job_list = job_obj.get_job("perl software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kirkkonummi")
	
@perl.route('/perl-software-developer-jobs-seinajoki')
def perl_software_developer28(page=1):

    job_list = job_obj.get_job("perl software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="seinajoki")
	
@perl.route('/perl-software-developer-jobs-kerava')
def perl_software_developer29(page=1):

    job_list = job_obj.get_job("perl software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kerava")
	
@perl.route('/perl-software-developer-jobs-kouvola')
def perl_software_developer30(page=1):

    job_list = job_obj.get_job("perl software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kouvola")
	
@perl.route('/perl-software-developer-jobs-imatra')
def perl_software_developer31(page=1):

    job_list = job_obj.get_job("perl software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="imatra")
	
@perl.route('/perl-software-developer-jobs-nokia')
def perl_software_developer32_1(page=1):

    job_list = job_obj.get_job("perl software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="nokia")
	
@perl.route('/perl-software-developer-jobs-savonlinna')
def perl_software_developer32(page=1):

    job_list = job_obj.get_job("perl software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="savonlinna")
	
@perl.route('/perl-software-developer-jobs-riihimaki')
def perl_software_developer33(page=1):

    job_list = job_obj.get_job("perl software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="riihimaki")
	
@perl.route('/perl-software-developer-jobs-vihti')
def perl_software_developer34(page=1):

    job_list = job_obj.get_job("perl software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="vihti")
	
@perl.route('/perl-software-developer-jobs-salo')
def perl_software_developer35(page=1):

    job_list = job_obj.get_job("perl software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="salo")
	
@perl.route('/perl-software-developer-jobs-kangasala')
def perl_software_developer36(page=1):

    job_list = job_obj.get_job("perl software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kangasala")
	
@perl.route('/perl-software-developer-jobs-raisio')
def perl_software_developer37_1(page=1):

    job_list = job_obj.get_job("perl software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="raisio")
	
@perl.route('/perl-software-developer-jobs-karhula')
def perl_software_developer37(page=1):

    job_list = job_obj.get_job("perl software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="karhula")
	
@perl.route('/perl-software-developer-jobs-kemi')
def perl_software_developer38(page=1):

    job_list = job_obj.get_job("perl software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kemi")
	
@perl.route('/perl-software-developer-jobs-iisalmi')
def perl_software_developer39(page=1):

    job_list = job_obj.get_job("perl software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="iisalmi")
	
@perl.route('/perl-software-developer-jobs-varkaus')
def perl_software_developer40(page=1):

    job_list = job_obj.get_job("perl software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="varkaus")
	
@perl.route('/perl-software-developer-jobs-raahe')
def perl_software_developer41(page=1):

    job_list = job_obj.get_job("perl software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="raahe")
	
@perl.route('/perl-software-developer-jobs-ylojarvi')
def perl_software_developer42_1(page=1):

    job_list = job_obj.get_job("perl software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="ylojarvi")
	
@perl.route('/perl-software-developer-jobs-hamina')
def perl_software_developer42(page=1):

    job_list = job_obj.get_job("perl software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="hamina")
	
@perl.route('/perl-software-developer-jobs-kaarina')
def perl_software_developer43(page=1):

    job_list = job_obj.get_job("perl software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kaarina")
	
@perl.route('/perl-software-developer-jobs-tornio')
def perl_software_developer44(page=1):

    job_list = job_obj.get_job("perl software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="tornio")
	
@perl.route('/perl-software-developer-jobs-heinola')
def perl_software_developer45(page=1):

    job_list = job_obj.get_job("perl software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="heinola")
	
@perl.route('/perl-software-developer-jobs-hollola')
def perl_software_developer46(page=1):

    job_list = job_obj.get_job("perl software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="hollola")
	
@perl.route('/perl-software-developer-jobs-valkeakoski')
def perl_software_developer47(page=1):

    job_list = job_obj.get_job("perl software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="valkeakoski")
	
@perl.route('/perl-software-developer-jobs-siilinjarvi')
def perl_software_developer48(page=1):

    job_list = job_obj.get_job("perl software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="siilinjarvi")
	
@perl.route('/perl-software-developer-jobs-kuusankoski')
def perl_software_developer49(page=1):

    job_list = job_obj.get_job("perl software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kuusankoski")
	
@perl.route('/perl-software-developer-jobs-sibbo')
def perl_software_developer50(page=1):

    job_list = job_obj.get_job("perl software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="sibbo")
	
@perl.route('/perl-software-developer-jobs-jakostad')
def perl_software_developer51(page=1):

    job_list = job_obj.get_job("perl software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="jakostad")
	
@perl.route('/perl-software-developer-jobs-lempaala')
def perl_software_developer52(page=1):

    job_list = job_obj.get_job("perl software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="lempaala")
	
@perl.route('/perl-software-developer-jobs-mantsala')
def perl_software_developer52_1(page=1):

    job_list = job_obj.get_job("perl software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="mantsala")
	
@perl.route('/perl-software-developer-jobs-forssa')
def perl_software_developer53(page=1):

    job_list = job_obj.get_job("perl software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="forssa")
	
@perl.route('/perl-software-developer-jobs-kuusamo')
def perl_software_developer54(page=1):

    job_list = job_obj.get_job("perl software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kuusamo")
	
@perl.route('/perl-software-developer-jobs-haukipudas')
def perl_software_developer55(page=1):

    job_list = job_obj.get_job("perl software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="haukipudas")
	
@perl.route('/perl-software-developer-jobs-korsholm')
def perl_software_developer56(page=1):

    job_list = job_obj.get_job("perl software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="korsholm")
	
@perl.route('/perl-software-developer-jobs-laukaa')
def perl_software_developer57(page=1):

    job_list = job_obj.get_job("perl software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="laukaa")
	
@perl.route('/perl-software-developer-jobs-anjala')
def perl_software_developer58(page=1):

    job_list = job_obj.get_job("perl software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="anjala")
	
@perl.route('/perl-software-developer-jobs-uusikaupunki')
def perl_software_developer59(page=1):

    job_list = job_obj.get_job("perl software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="uusikaupunki")
	
@perl.route('/perl-software-developer-jobs-janakkala')
def perl_software_developer60(page=1):

    job_list = job_obj.get_job("perl software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="janakkala")
	
@perl.route('/perl-software-developer-jobs-pirkkala')
def perl_software_developer61(page=1):

    job_list = job_obj.get_job("perl software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="pirkkala")
	
@perl.route('/perl-software-developer-jobs-lansi-turunmaa')
def perl_software_developer62(page=1):

    job_list = job_obj.get_job("perl software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="lansi-turunmaa")
	
@perl.route('/perl-software-developer-jobs-jamsa')
def perl_software_developer63(page=1):

    job_list = job_obj.get_job("perl software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="jamsa")
	
@perl.route('/perl-software-developer-jobs-jamsa')
def perl_software_developer64(page=1):

    job_list = job_obj.get_job("perl software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="jamsa")
	
@perl.route('/perl-software-developer-jobs-vammala')
def perl_software_developer65(page=1):

    job_list = job_obj.get_job("perl software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="vammala")
	
@perl.route('/perl-software-developer-jobs-nastola')
def perl_software_developer66(page=1):

    job_list = job_obj.get_job("perl software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="nastola")
	
@perl.route('/perl-software-developer-jobs-orimattila')
def perl_software_developer67(page=1):

    job_list = job_obj.get_job("perl software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="orimattila")
	
@perl.route('/perl-software-developer-jobs-kauhajoki')
def perl_software_developer68(page=1):

    job_list = job_obj.get_job("perl software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kauhajoki")
	
@perl.route('/perl-software-developer-jobs-ekenas')
def perl_software_developer69(page=1):

    job_list = job_obj.get_job("perl software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="ekenas")
	
@perl.route('/perl-software-developer-jobs-kempele')
def perl_software_developer70(page=1):

    job_list = job_obj.get_job("perl software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kempele")
	
@perl.route('/perl-software-developer-jobs-lapua')
def perl_software_developer71(page=1):

    job_list = job_obj.get_job("perl software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="lapua")
	
@perl.route('/perl-software-developer-jobs-lieksa')
def perl_software_developer72(page=1):

    job_list = job_obj.get_job("perl software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="lieksa")
	
@perl.route('/perl-software-developer-jobs-naantali')
def perl_software_developer73(page=1):

    job_list = job_obj.get_job("perl software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="naantali")
	
@perl.route('/perl-software-developer-jobs-aanekoski')
def perl_software_developer74(page=1):

    job_list = job_obj.get_job("perl software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="aanekoski")
	
@perl.route('/perl-software-developer-jobs-ylivieska')
def perl_software_developer75(page=1):

    job_list = job_obj.get_job("perl software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="ylivieska")
	
@perl.route('/perl-software-developer-jobs-kontiolahti')
def perl_software_developer76(page=1):

    job_list = job_obj.get_job("perl software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kontiolahti")
	
@perl.route('/perl-software-developer-jobs-kankaanpaa')
def perl_software_developer77(page=1):

    job_list = job_obj.get_job("perl software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kankaanpaa")
	
@perl.route('/perl-software-developer-jobs-ulvila')
def perl_software_developer78(page=1):

    job_list = job_obj.get_job("perl software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="ulvila")
	
@perl.route('/perl-software-developer-jobs-pieksamaki')
def perl_software_developer79(page=1):

    job_list = job_obj.get_job("perl software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="pieksamaki")
	
@perl.route('/perl-software-developer-jobs-kiiminki')
def perl_software_developer80(page=1):

    job_list = job_obj.get_job("perl software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kiiminki")
	
@perl.route('/perl-software-developer-jobs-pargas')
def perl_software_developer81(page=1):

    job_list = job_obj.get_job("perl software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="pargas")
	
@perl.route('/perl-software-developer-jobs-nurmo')
def perl_software_developer82(page=1):

    job_list = job_obj.get_job("perl software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="nurmo")
	
@perl.route('/perl-software-developer-jobs-ilmajoki')
def perl_software_developer83(page=1):

    job_list = job_obj.get_job("perl software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="ilmajoki")
	
@perl.route('/perl-software-developer-jobs-liperi')
def perl_software_developer84(page=1):

    job_list = job_obj.get_job("perl software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="liperi")
	
@perl.route('/perl-software-developer-jobs-keuruu')
def perl_software_developer85(page=1):

    job_list = job_obj.get_job("perl software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="keuruu")
	
@perl.route('/perl-software-developer-jobs-leppavirta')
def perl_software_developer86(page=1):

    job_list = job_obj.get_job("perl software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="leppavirta")
	
@perl.route('/perl-software-developer-jobs-kurikka')
def perl_software_developer87(page=1):

    job_list = job_obj.get_job("perl software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kurikka")
	
@perl.route('/perl-software-developer-jobs-nivala')
def perl_software_developer88(page=1):

    job_list = job_obj.get_job("perl software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="nivala")
	
@perl.route('/perl-software-developer-jobs-joutseno')
def perl_software_developer89(page=1):

    job_list = job_obj.get_job("perl software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="joutseno")
	
@perl.route('/perl-software-developer-jobs-pedersore')
def perl_software_developer90(page=1):

    job_list = job_obj.get_job("perl software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="pedersore")
	
@perl.route('/perl-software-developer-jobs-sotkamo')
def perl_software_developer91(page=1):

    job_list = job_obj.get_job("perl software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="sotkamo")
	
@perl.route('/perl-software-developer-jobs-kuhmo')
def perl_software_developer92(page=1):

    job_list = job_obj.get_job("perl software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="kuhmo")
	
@perl.route('/perl-software-developer-jobs-paimio')
def perl_software_developer93(page=1):

    job_list = job_obj.get_job("perl software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="paimio")
	
@perl.route('/perl-software-developer-jobs-saarijarvi')
def perl_software_developer94(page=1):

    job_list = job_obj.get_job("perl software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="saarijarvi")
	
@perl.route('/perl-software-developer-jobs-helsinki')
def perl_software_developer95(page=1):

    job_list = job_obj.get_job("perl software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="perl software developer", location="helsinki")


####################################################################

