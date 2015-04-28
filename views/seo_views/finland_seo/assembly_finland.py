from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

assembly = Blueprint('assembly', __name__)
job_obj = Job()



####################################################################


@assembly.route('/assembly_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "assembly" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def assembly_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="espoo")

@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def assembly_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="tampere")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def assembly_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="vantaa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def assembly_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="turku")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def assembly_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="oulu")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def assembly_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="lahti")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def assembly_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kuopio")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def assembly_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="jyvvaskyla")

@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def assembly_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="pori")

@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def assembly_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="lappeenranta")	
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def assembly_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="vaasa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def assembly_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kotka")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def assembly_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="joensuu")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def assembly_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="hameenlinna")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def assembly_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="porvoo")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def assembly_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="mikkeli")

@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def assembly_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="hyvinkaa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def assembly_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="nurmijarvi")

@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def assembly_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="jarvenpaa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def assembly_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="rauma")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def assembly_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="lohja")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def assembly_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="karleby")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def assembly_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kajaani")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def assembly_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="rovaniemi")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def assembly_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="tuusula")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def assembly_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kirkkonummi")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def assembly_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="seinajoki")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def assembly_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kerava")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def assembly_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kouvola")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def assembly_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="imatra")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def assembly_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="nokia")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def assembly_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="savonlinna")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def assembly_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="riihimaki")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def assembly_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="vihti")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def assembly_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="salo")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def assembly_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kangasala")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def assembly_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="raisio")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def assembly_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="karhula")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def assembly_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kemi")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def assembly_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="iisalmi")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def assembly_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="varkaus")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def assembly_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="raahe")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def assembly_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="ylojarvi")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def assembly_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="hamina")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def assembly_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kaarina")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def assembly_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="tornio")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def assembly_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="heinola")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def assembly_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="hollola")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def assembly_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="valkeakoski")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def assembly_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="siilinjarvi")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def assembly_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kuusankoski")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def assembly_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="sibbo")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def assembly_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="jakostad")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def assembly_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="lempaala")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def assembly_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="mantsala")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def assembly_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="forssa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def assembly_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kuusamo")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def assembly_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="haukipudas")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def assembly_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="korsholm")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def assembly_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="laukaa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def assembly_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="anjala")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def assembly_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="uusikaupunki")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def assembly_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="janakkala")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def assembly_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="pirkkala")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def assembly_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def assembly_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="jamsa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def assembly_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="jamsa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def assembly_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="vammala")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def assembly_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="nastola")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def assembly_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="orimattila")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def assembly_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kauhajoki")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def assembly_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="ekenas")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def assembly_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kempele")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def assembly_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="lapua")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def assembly_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="lieksa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def assembly_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="naantali")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def assembly_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="aanekoski")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def assembly_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="ylivieska")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def assembly_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kontiolahti")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def assembly_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kankaanpaa")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def assembly_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="ulvila")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def assembly_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="pieksamaki")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def assembly_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kiiminki")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def assembly_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="pargas")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def assembly_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="nurmo")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def assembly_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="ilmajoki")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def assembly_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="liperi")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def assembly_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="keuruu")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def assembly_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="leppavirta")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def assembly_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kurikka")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def assembly_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="nivala")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def assembly_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="joutseno")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def assembly_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="pedersore")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def assembly_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="sotkamo")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def assembly_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="kuhmo")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def assembly_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="paimio")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def assembly_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="saarijarvi")
	
@assembly.route('/assembly-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def assembly_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("assembly ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@assembly.route('/assembly-software-developer-jobs-espoo')
def assembly_software_developer2(page=1):

    job_list = job_obj.get_job("assembly software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="espoo")

@assembly.route('/assembly-software-developer-jobs-tampere')
def assembly_software_developer3(page=1):

    job_list = job_obj.get_job("assembly software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="tampere")
	
@assembly.route('/assembly-software-developer-jobs-vantaa')
def assembly_software_developer4(page=1):

    job_list = job_obj.get_job("assembly software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="vantaa")
	
@assembly.route('/assembly-software-developer-jobs-turku')
def assembly_software_developer5(page=1):

    job_list = job_obj.get_job("assembly software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="turku")
	
@assembly.route('/assembly-software-developer-jobs-oulu')
def assembly_software_developer6(page=1):

    job_list = job_obj.get_job("assembly software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="oulu")
	
@assembly.route('/assembly-software-developer-jobs-lahti')
def assembly_software_developer7(page=1):

    job_list = job_obj.get_job("assembly software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="lahti")
	
@assembly.route('/assembly-software-developer-jobs-kuopio')
def assembly_software_developer8(page=1):

    job_list = job_obj.get_job("assembly software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kuopio")
	
@assembly.route('/assembly-software-developer-jobs-jyvvaskyla')
def assembly_software_developer9(page=1):

    job_list = job_obj.get_job("assembly software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="jyvvaskyla")

@assembly.route('/assembly-software-developer-jobs-pori')
def assembly_software_developer10(page=1):

    job_list = job_obj.get_job("assembly software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="pori")

@assembly.route('/assembly-software-developer-jobs-lappeenranta')
def assembly_software_developer11(page=1):

    job_list = job_obj.get_job("assembly software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="lappeenranta")	
	
@assembly.route('/assembly-software-developer-jobs-vaasa')
def assembly_software_developer12(page=1):

    job_list = job_obj.get_job("assembly software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="vaasa")
	
@assembly.route('/assembly-software-developer-jobs-kotka')
def assembly_software_developer13(page=1):

    job_list = job_obj.get_job("assembly software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kotka")
	
@assembly.route('/assembly-software-developer-jobs-joensuu')
def assembly_software_developer14(page=1):

    job_list = job_obj.get_job("assembly software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="joensuu")
	
@assembly.route('/assembly-software-developer-jobs-hameenlinna')
def assembly_software_developer15(page=1):

    job_list = job_obj.get_job("assembly software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="hameenlinna")
	
@assembly.route('/assembly-software-developer-jobs-porvoo')
def assembly_software_developer16(page=1):

    job_list = job_obj.get_job("assembly software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="porvoo")
	
@assembly.route('/assembly-software-developer-jobs-mikkeli')
def assembly_software_developer17(page=1):

    job_list = job_obj.get_job("assembly software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="mikkeli")

@assembly.route('/assembly-software-developer-jobs-hyvinkaa')
def assembly_software_developer18(page=1):

    job_list = job_obj.get_job("assembly software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="hyvinkaa")
	
@assembly.route('/assembly-software-developer-jobs-nurmijarvi')
def assembly_software_developer19(page=1):

    job_list = job_obj.get_job("assembly software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="nurmijarvi")

@assembly.route('/assembly-software-developer-jobs-jarvenpaa')
def assembly_software_developer20(page=1):

    job_list = job_obj.get_job("assembly software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="jarvenpaa")
	
@assembly.route('/assembly-software-developer-jobs-rauma')
def assembly_software_developer21(page=1):

    job_list = job_obj.get_job("assembly software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="rauma")
	
@assembly.route('/assembly-software-developer-jobs-lohja')
def assembly_software_developer22(page=1):

    job_list = job_obj.get_job("assembly software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="lohja")
	
@assembly.route('/assembly-software-developer-jobs-karleby')
def assembly_software_developer23(page=1):

    job_list = job_obj.get_job("assembly software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="karleby")
	
@assembly.route('/assembly-software-developer-jobs-kajaani')
def assembly_software_developer24(page=1):

    job_list = job_obj.get_job("assembly software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kajaani")
	
@assembly.route('/assembly-software-developer-jobs-rovaniemi')
def assembly_software_developer25(page=1):

    job_list = job_obj.get_job("assembly software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="rovaniemi")
	
@assembly.route('/assembly-software-developer-jobs-tuusula')
def assembly_software_developer26(page=1):

    job_list = job_obj.get_job("assembly software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="tuusula")
	
@assembly.route('/assembly-software-developer-jobs-kirkkonummi')
def assembly_software_developer27(page=1):

    job_list = job_obj.get_job("assembly software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kirkkonummi")
	
@assembly.route('/assembly-software-developer-jobs-seinajoki')
def assembly_software_developer28(page=1):

    job_list = job_obj.get_job("assembly software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="seinajoki")
	
@assembly.route('/assembly-software-developer-jobs-kerava')
def assembly_software_developer29(page=1):

    job_list = job_obj.get_job("assembly software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kerava")
	
@assembly.route('/assembly-software-developer-jobs-kouvola')
def assembly_software_developer30(page=1):

    job_list = job_obj.get_job("assembly software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kouvola")
	
@assembly.route('/assembly-software-developer-jobs-imatra')
def assembly_software_developer31(page=1):

    job_list = job_obj.get_job("assembly software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="imatra")
	
@assembly.route('/assembly-software-developer-jobs-nokia')
def assembly_software_developer32_1(page=1):

    job_list = job_obj.get_job("assembly software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="nokia")
	
@assembly.route('/assembly-software-developer-jobs-savonlinna')
def assembly_software_developer32(page=1):

    job_list = job_obj.get_job("assembly software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="savonlinna")
	
@assembly.route('/assembly-software-developer-jobs-riihimaki')
def assembly_software_developer33(page=1):

    job_list = job_obj.get_job("assembly software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="riihimaki")
	
@assembly.route('/assembly-software-developer-jobs-vihti')
def assembly_software_developer34(page=1):

    job_list = job_obj.get_job("assembly software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="vihti")
	
@assembly.route('/assembly-software-developer-jobs-salo')
def assembly_software_developer35(page=1):

    job_list = job_obj.get_job("assembly software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="salo")
	
@assembly.route('/assembly-software-developer-jobs-kangasala')
def assembly_software_developer36(page=1):

    job_list = job_obj.get_job("assembly software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kangasala")
	
@assembly.route('/assembly-software-developer-jobs-raisio')
def assembly_software_developer37_1(page=1):

    job_list = job_obj.get_job("assembly software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="raisio")
	
@assembly.route('/assembly-software-developer-jobs-karhula')
def assembly_software_developer37(page=1):

    job_list = job_obj.get_job("assembly software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="karhula")
	
@assembly.route('/assembly-software-developer-jobs-kemi')
def assembly_software_developer38(page=1):

    job_list = job_obj.get_job("assembly software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kemi")
	
@assembly.route('/assembly-software-developer-jobs-iisalmi')
def assembly_software_developer39(page=1):

    job_list = job_obj.get_job("assembly software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="iisalmi")
	
@assembly.route('/assembly-software-developer-jobs-varkaus')
def assembly_software_developer40(page=1):

    job_list = job_obj.get_job("assembly software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="varkaus")
	
@assembly.route('/assembly-software-developer-jobs-raahe')
def assembly_software_developer41(page=1):

    job_list = job_obj.get_job("assembly software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="raahe")
	
@assembly.route('/assembly-software-developer-jobs-ylojarvi')
def assembly_software_developer42_1(page=1):

    job_list = job_obj.get_job("assembly software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="ylojarvi")
	
@assembly.route('/assembly-software-developer-jobs-hamina')
def assembly_software_developer42(page=1):

    job_list = job_obj.get_job("assembly software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="hamina")
	
@assembly.route('/assembly-software-developer-jobs-kaarina')
def assembly_software_developer43(page=1):

    job_list = job_obj.get_job("assembly software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kaarina")
	
@assembly.route('/assembly-software-developer-jobs-tornio')
def assembly_software_developer44(page=1):

    job_list = job_obj.get_job("assembly software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="tornio")
	
@assembly.route('/assembly-software-developer-jobs-heinola')
def assembly_software_developer45(page=1):

    job_list = job_obj.get_job("assembly software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="heinola")
	
@assembly.route('/assembly-software-developer-jobs-hollola')
def assembly_software_developer46(page=1):

    job_list = job_obj.get_job("assembly software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="hollola")
	
@assembly.route('/assembly-software-developer-jobs-valkeakoski')
def assembly_software_developer47(page=1):

    job_list = job_obj.get_job("assembly software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="valkeakoski")
	
@assembly.route('/assembly-software-developer-jobs-siilinjarvi')
def assembly_software_developer48(page=1):

    job_list = job_obj.get_job("assembly software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="siilinjarvi")
	
@assembly.route('/assembly-software-developer-jobs-kuusankoski')
def assembly_software_developer49(page=1):

    job_list = job_obj.get_job("assembly software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kuusankoski")
	
@assembly.route('/assembly-software-developer-jobs-sibbo')
def assembly_software_developer50(page=1):

    job_list = job_obj.get_job("assembly software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="sibbo")
	
@assembly.route('/assembly-software-developer-jobs-jakostad')
def assembly_software_developer51(page=1):

    job_list = job_obj.get_job("assembly software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="jakostad")
	
@assembly.route('/assembly-software-developer-jobs-lempaala')
def assembly_software_developer52(page=1):

    job_list = job_obj.get_job("assembly software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="lempaala")
	
@assembly.route('/assembly-software-developer-jobs-mantsala')
def assembly_software_developer52_1(page=1):

    job_list = job_obj.get_job("assembly software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="mantsala")
	
@assembly.route('/assembly-software-developer-jobs-forssa')
def assembly_software_developer53(page=1):

    job_list = job_obj.get_job("assembly software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="forssa")
	
@assembly.route('/assembly-software-developer-jobs-kuusamo')
def assembly_software_developer54(page=1):

    job_list = job_obj.get_job("assembly software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kuusamo")
	
@assembly.route('/assembly-software-developer-jobs-haukipudas')
def assembly_software_developer55(page=1):

    job_list = job_obj.get_job("assembly software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="haukipudas")
	
@assembly.route('/assembly-software-developer-jobs-korsholm')
def assembly_software_developer56(page=1):

    job_list = job_obj.get_job("assembly software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="korsholm")
	
@assembly.route('/assembly-software-developer-jobs-laukaa')
def assembly_software_developer57(page=1):

    job_list = job_obj.get_job("assembly software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="laukaa")
	
@assembly.route('/assembly-software-developer-jobs-anjala')
def assembly_software_developer58(page=1):

    job_list = job_obj.get_job("assembly software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="anjala")
	
@assembly.route('/assembly-software-developer-jobs-uusikaupunki')
def assembly_software_developer59(page=1):

    job_list = job_obj.get_job("assembly software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="uusikaupunki")
	
@assembly.route('/assembly-software-developer-jobs-janakkala')
def assembly_software_developer60(page=1):

    job_list = job_obj.get_job("assembly software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="janakkala")
	
@assembly.route('/assembly-software-developer-jobs-pirkkala')
def assembly_software_developer61(page=1):

    job_list = job_obj.get_job("assembly software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="pirkkala")
	
@assembly.route('/assembly-software-developer-jobs-lansi-turunmaa')
def assembly_software_developer62(page=1):

    job_list = job_obj.get_job("assembly software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="lansi-turunmaa")
	
@assembly.route('/assembly-software-developer-jobs-jamsa')
def assembly_software_developer63(page=1):

    job_list = job_obj.get_job("assembly software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="jamsa")
	
@assembly.route('/assembly-software-developer-jobs-jamsa')
def assembly_software_developer64(page=1):

    job_list = job_obj.get_job("assembly software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="jamsa")
	
@assembly.route('/assembly-software-developer-jobs-vammala')
def assembly_software_developer65(page=1):

    job_list = job_obj.get_job("assembly software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="vammala")
	
@assembly.route('/assembly-software-developer-jobs-nastola')
def assembly_software_developer66(page=1):

    job_list = job_obj.get_job("assembly software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="nastola")
	
@assembly.route('/assembly-software-developer-jobs-orimattila')
def assembly_software_developer67(page=1):

    job_list = job_obj.get_job("assembly software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="orimattila")
	
@assembly.route('/assembly-software-developer-jobs-kauhajoki')
def assembly_software_developer68(page=1):

    job_list = job_obj.get_job("assembly software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kauhajoki")
	
@assembly.route('/assembly-software-developer-jobs-ekenas')
def assembly_software_developer69(page=1):

    job_list = job_obj.get_job("assembly software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="ekenas")
	
@assembly.route('/assembly-software-developer-jobs-kempele')
def assembly_software_developer70(page=1):

    job_list = job_obj.get_job("assembly software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kempele")
	
@assembly.route('/assembly-software-developer-jobs-lapua')
def assembly_software_developer71(page=1):

    job_list = job_obj.get_job("assembly software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="lapua")
	
@assembly.route('/assembly-software-developer-jobs-lieksa')
def assembly_software_developer72(page=1):

    job_list = job_obj.get_job("assembly software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="lieksa")
	
@assembly.route('/assembly-software-developer-jobs-naantali')
def assembly_software_developer73(page=1):

    job_list = job_obj.get_job("assembly software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="naantali")
	
@assembly.route('/assembly-software-developer-jobs-aanekoski')
def assembly_software_developer74(page=1):

    job_list = job_obj.get_job("assembly software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="aanekoski")
	
@assembly.route('/assembly-software-developer-jobs-ylivieska')
def assembly_software_developer75(page=1):

    job_list = job_obj.get_job("assembly software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="ylivieska")
	
@assembly.route('/assembly-software-developer-jobs-kontiolahti')
def assembly_software_developer76(page=1):

    job_list = job_obj.get_job("assembly software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kontiolahti")
	
@assembly.route('/assembly-software-developer-jobs-kankaanpaa')
def assembly_software_developer77(page=1):

    job_list = job_obj.get_job("assembly software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kankaanpaa")
	
@assembly.route('/assembly-software-developer-jobs-ulvila')
def assembly_software_developer78(page=1):

    job_list = job_obj.get_job("assembly software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="ulvila")
	
@assembly.route('/assembly-software-developer-jobs-pieksamaki')
def assembly_software_developer79(page=1):

    job_list = job_obj.get_job("assembly software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="pieksamaki")
	
@assembly.route('/assembly-software-developer-jobs-kiiminki')
def assembly_software_developer80(page=1):

    job_list = job_obj.get_job("assembly software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kiiminki")
	
@assembly.route('/assembly-software-developer-jobs-pargas')
def assembly_software_developer81(page=1):

    job_list = job_obj.get_job("assembly software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="pargas")
	
@assembly.route('/assembly-software-developer-jobs-nurmo')
def assembly_software_developer82(page=1):

    job_list = job_obj.get_job("assembly software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="nurmo")
	
@assembly.route('/assembly-software-developer-jobs-ilmajoki')
def assembly_software_developer83(page=1):

    job_list = job_obj.get_job("assembly software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="ilmajoki")
	
@assembly.route('/assembly-software-developer-jobs-liperi')
def assembly_software_developer84(page=1):

    job_list = job_obj.get_job("assembly software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="liperi")
	
@assembly.route('/assembly-software-developer-jobs-keuruu')
def assembly_software_developer85(page=1):

    job_list = job_obj.get_job("assembly software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="keuruu")
	
@assembly.route('/assembly-software-developer-jobs-leppavirta')
def assembly_software_developer86(page=1):

    job_list = job_obj.get_job("assembly software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="leppavirta")
	
@assembly.route('/assembly-software-developer-jobs-kurikka')
def assembly_software_developer87(page=1):

    job_list = job_obj.get_job("assembly software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kurikka")
	
@assembly.route('/assembly-software-developer-jobs-nivala')
def assembly_software_developer88(page=1):

    job_list = job_obj.get_job("assembly software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="nivala")
	
@assembly.route('/assembly-software-developer-jobs-joutseno')
def assembly_software_developer89(page=1):

    job_list = job_obj.get_job("assembly software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="joutseno")
	
@assembly.route('/assembly-software-developer-jobs-pedersore')
def assembly_software_developer90(page=1):

    job_list = job_obj.get_job("assembly software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="pedersore")
	
@assembly.route('/assembly-software-developer-jobs-sotkamo')
def assembly_software_developer91(page=1):

    job_list = job_obj.get_job("assembly software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="sotkamo")
	
@assembly.route('/assembly-software-developer-jobs-kuhmo')
def assembly_software_developer92(page=1):

    job_list = job_obj.get_job("assembly software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="kuhmo")
	
@assembly.route('/assembly-software-developer-jobs-paimio')
def assembly_software_developer93(page=1):

    job_list = job_obj.get_job("assembly software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="paimio")
	
@assembly.route('/assembly-software-developer-jobs-saarijarvi')
def assembly_software_developer94(page=1):

    job_list = job_obj.get_job("assembly software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="saarijarvi")
	
@assembly.route('/assembly-software-developer-jobs-helsinki')
def assembly_software_developer95(page=1):

    job_list = job_obj.get_job("assembly software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="assembly software developer", location="helsinki")


####################################################################

