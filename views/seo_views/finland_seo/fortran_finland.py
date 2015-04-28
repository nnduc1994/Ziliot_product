from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

fortran = Blueprint('fortran', __name__)
job_obj = Job()



####################################################################


@fortran.route('/fortran_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "fortran" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def fortran_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="espoo")

@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def fortran_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="tampere")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def fortran_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="vantaa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def fortran_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="turku")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def fortran_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="oulu")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def fortran_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="lahti")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def fortran_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kuopio")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def fortran_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="jyvvaskyla")

@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def fortran_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="pori")

@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def fortran_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="lappeenranta")	
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def fortran_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="vaasa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def fortran_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kotka")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def fortran_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="joensuu")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def fortran_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="hameenlinna")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def fortran_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="porvoo")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def fortran_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="mikkeli")

@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def fortran_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="hyvinkaa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def fortran_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="nurmijarvi")

@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def fortran_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="jarvenpaa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def fortran_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="rauma")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def fortran_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="lohja")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def fortran_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="karleby")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def fortran_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kajaani")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def fortran_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="rovaniemi")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def fortran_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="tuusula")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def fortran_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kirkkonummi")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def fortran_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="seinajoki")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def fortran_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kerava")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def fortran_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kouvola")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def fortran_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="imatra")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def fortran_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="nokia")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def fortran_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="savonlinna")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def fortran_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="riihimaki")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def fortran_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="vihti")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def fortran_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="salo")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def fortran_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kangasala")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def fortran_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="raisio")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def fortran_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="karhula")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def fortran_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kemi")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def fortran_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="iisalmi")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def fortran_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="varkaus")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def fortran_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="raahe")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def fortran_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="ylojarvi")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def fortran_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="hamina")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def fortran_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kaarina")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def fortran_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="tornio")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def fortran_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="heinola")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def fortran_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="hollola")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def fortran_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="valkeakoski")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def fortran_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="siilinjarvi")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def fortran_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kuusankoski")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def fortran_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="sibbo")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def fortran_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="jakostad")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def fortran_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="lempaala")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def fortran_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="mantsala")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def fortran_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="forssa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def fortran_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kuusamo")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def fortran_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="haukipudas")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def fortran_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="korsholm")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def fortran_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="laukaa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def fortran_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="anjala")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def fortran_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="uusikaupunki")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def fortran_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="janakkala")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def fortran_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="pirkkala")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def fortran_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def fortran_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="jamsa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def fortran_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="jamsa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def fortran_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="vammala")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def fortran_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="nastola")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def fortran_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="orimattila")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def fortran_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kauhajoki")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def fortran_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="ekenas")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def fortran_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kempele")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def fortran_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="lapua")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def fortran_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="lieksa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def fortran_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="naantali")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def fortran_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="aanekoski")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def fortran_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="ylivieska")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def fortran_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kontiolahti")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def fortran_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kankaanpaa")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def fortran_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="ulvila")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def fortran_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="pieksamaki")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def fortran_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kiiminki")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def fortran_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="pargas")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def fortran_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="nurmo")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def fortran_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="ilmajoki")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def fortran_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="liperi")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def fortran_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="keuruu")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def fortran_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="leppavirta")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def fortran_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kurikka")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def fortran_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="nivala")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def fortran_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="joutseno")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def fortran_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="pedersore")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def fortran_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="sotkamo")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def fortran_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="kuhmo")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def fortran_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="paimio")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def fortran_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="saarijarvi")
	
@fortran.route('/fortran-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def fortran_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("fortran ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@fortran.route('/fortran-software-developer-jobs-espoo')
def fortran_software_developer2(page=1):

    job_list = job_obj.get_job("fortran software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="espoo")

@fortran.route('/fortran-software-developer-jobs-tampere')
def fortran_software_developer3(page=1):

    job_list = job_obj.get_job("fortran software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="tampere")
	
@fortran.route('/fortran-software-developer-jobs-vantaa')
def fortran_software_developer4(page=1):

    job_list = job_obj.get_job("fortran software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="vantaa")
	
@fortran.route('/fortran-software-developer-jobs-turku')
def fortran_software_developer5(page=1):

    job_list = job_obj.get_job("fortran software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="turku")
	
@fortran.route('/fortran-software-developer-jobs-oulu')
def fortran_software_developer6(page=1):

    job_list = job_obj.get_job("fortran software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="oulu")
	
@fortran.route('/fortran-software-developer-jobs-lahti')
def fortran_software_developer7(page=1):

    job_list = job_obj.get_job("fortran software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="lahti")
	
@fortran.route('/fortran-software-developer-jobs-kuopio')
def fortran_software_developer8(page=1):

    job_list = job_obj.get_job("fortran software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kuopio")
	
@fortran.route('/fortran-software-developer-jobs-jyvvaskyla')
def fortran_software_developer9(page=1):

    job_list = job_obj.get_job("fortran software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="jyvvaskyla")

@fortran.route('/fortran-software-developer-jobs-pori')
def fortran_software_developer10(page=1):

    job_list = job_obj.get_job("fortran software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="pori")

@fortran.route('/fortran-software-developer-jobs-lappeenranta')
def fortran_software_developer11(page=1):

    job_list = job_obj.get_job("fortran software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="lappeenranta")	
	
@fortran.route('/fortran-software-developer-jobs-vaasa')
def fortran_software_developer12(page=1):

    job_list = job_obj.get_job("fortran software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="vaasa")
	
@fortran.route('/fortran-software-developer-jobs-kotka')
def fortran_software_developer13(page=1):

    job_list = job_obj.get_job("fortran software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kotka")
	
@fortran.route('/fortran-software-developer-jobs-joensuu')
def fortran_software_developer14(page=1):

    job_list = job_obj.get_job("fortran software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="joensuu")
	
@fortran.route('/fortran-software-developer-jobs-hameenlinna')
def fortran_software_developer15(page=1):

    job_list = job_obj.get_job("fortran software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="hameenlinna")
	
@fortran.route('/fortran-software-developer-jobs-porvoo')
def fortran_software_developer16(page=1):

    job_list = job_obj.get_job("fortran software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="porvoo")
	
@fortran.route('/fortran-software-developer-jobs-mikkeli')
def fortran_software_developer17(page=1):

    job_list = job_obj.get_job("fortran software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="mikkeli")

@fortran.route('/fortran-software-developer-jobs-hyvinkaa')
def fortran_software_developer18(page=1):

    job_list = job_obj.get_job("fortran software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="hyvinkaa")
	
@fortran.route('/fortran-software-developer-jobs-nurmijarvi')
def fortran_software_developer19(page=1):

    job_list = job_obj.get_job("fortran software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="nurmijarvi")

@fortran.route('/fortran-software-developer-jobs-jarvenpaa')
def fortran_software_developer20(page=1):

    job_list = job_obj.get_job("fortran software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="jarvenpaa")
	
@fortran.route('/fortran-software-developer-jobs-rauma')
def fortran_software_developer21(page=1):

    job_list = job_obj.get_job("fortran software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="rauma")
	
@fortran.route('/fortran-software-developer-jobs-lohja')
def fortran_software_developer22(page=1):

    job_list = job_obj.get_job("fortran software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="lohja")
	
@fortran.route('/fortran-software-developer-jobs-karleby')
def fortran_software_developer23(page=1):

    job_list = job_obj.get_job("fortran software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="karleby")
	
@fortran.route('/fortran-software-developer-jobs-kajaani')
def fortran_software_developer24(page=1):

    job_list = job_obj.get_job("fortran software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kajaani")
	
@fortran.route('/fortran-software-developer-jobs-rovaniemi')
def fortran_software_developer25(page=1):

    job_list = job_obj.get_job("fortran software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="rovaniemi")
	
@fortran.route('/fortran-software-developer-jobs-tuusula')
def fortran_software_developer26(page=1):

    job_list = job_obj.get_job("fortran software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="tuusula")
	
@fortran.route('/fortran-software-developer-jobs-kirkkonummi')
def fortran_software_developer27(page=1):

    job_list = job_obj.get_job("fortran software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kirkkonummi")
	
@fortran.route('/fortran-software-developer-jobs-seinajoki')
def fortran_software_developer28(page=1):

    job_list = job_obj.get_job("fortran software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="seinajoki")
	
@fortran.route('/fortran-software-developer-jobs-kerava')
def fortran_software_developer29(page=1):

    job_list = job_obj.get_job("fortran software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kerava")
	
@fortran.route('/fortran-software-developer-jobs-kouvola')
def fortran_software_developer30(page=1):

    job_list = job_obj.get_job("fortran software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kouvola")
	
@fortran.route('/fortran-software-developer-jobs-imatra')
def fortran_software_developer31(page=1):

    job_list = job_obj.get_job("fortran software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="imatra")
	
@fortran.route('/fortran-software-developer-jobs-nokia')
def fortran_software_developer32_1(page=1):

    job_list = job_obj.get_job("fortran software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="nokia")
	
@fortran.route('/fortran-software-developer-jobs-savonlinna')
def fortran_software_developer32(page=1):

    job_list = job_obj.get_job("fortran software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="savonlinna")
	
@fortran.route('/fortran-software-developer-jobs-riihimaki')
def fortran_software_developer33(page=1):

    job_list = job_obj.get_job("fortran software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="riihimaki")
	
@fortran.route('/fortran-software-developer-jobs-vihti')
def fortran_software_developer34(page=1):

    job_list = job_obj.get_job("fortran software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="vihti")
	
@fortran.route('/fortran-software-developer-jobs-salo')
def fortran_software_developer35(page=1):

    job_list = job_obj.get_job("fortran software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="salo")
	
@fortran.route('/fortran-software-developer-jobs-kangasala')
def fortran_software_developer36(page=1):

    job_list = job_obj.get_job("fortran software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kangasala")
	
@fortran.route('/fortran-software-developer-jobs-raisio')
def fortran_software_developer37_1(page=1):

    job_list = job_obj.get_job("fortran software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="raisio")
	
@fortran.route('/fortran-software-developer-jobs-karhula')
def fortran_software_developer37(page=1):

    job_list = job_obj.get_job("fortran software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="karhula")
	
@fortran.route('/fortran-software-developer-jobs-kemi')
def fortran_software_developer38(page=1):

    job_list = job_obj.get_job("fortran software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kemi")
	
@fortran.route('/fortran-software-developer-jobs-iisalmi')
def fortran_software_developer39(page=1):

    job_list = job_obj.get_job("fortran software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="iisalmi")
	
@fortran.route('/fortran-software-developer-jobs-varkaus')
def fortran_software_developer40(page=1):

    job_list = job_obj.get_job("fortran software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="varkaus")
	
@fortran.route('/fortran-software-developer-jobs-raahe')
def fortran_software_developer41(page=1):

    job_list = job_obj.get_job("fortran software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="raahe")
	
@fortran.route('/fortran-software-developer-jobs-ylojarvi')
def fortran_software_developer42_1(page=1):

    job_list = job_obj.get_job("fortran software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="ylojarvi")
	
@fortran.route('/fortran-software-developer-jobs-hamina')
def fortran_software_developer42(page=1):

    job_list = job_obj.get_job("fortran software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="hamina")
	
@fortran.route('/fortran-software-developer-jobs-kaarina')
def fortran_software_developer43(page=1):

    job_list = job_obj.get_job("fortran software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kaarina")
	
@fortran.route('/fortran-software-developer-jobs-tornio')
def fortran_software_developer44(page=1):

    job_list = job_obj.get_job("fortran software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="tornio")
	
@fortran.route('/fortran-software-developer-jobs-heinola')
def fortran_software_developer45(page=1):

    job_list = job_obj.get_job("fortran software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="heinola")
	
@fortran.route('/fortran-software-developer-jobs-hollola')
def fortran_software_developer46(page=1):

    job_list = job_obj.get_job("fortran software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="hollola")
	
@fortran.route('/fortran-software-developer-jobs-valkeakoski')
def fortran_software_developer47(page=1):

    job_list = job_obj.get_job("fortran software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="valkeakoski")
	
@fortran.route('/fortran-software-developer-jobs-siilinjarvi')
def fortran_software_developer48(page=1):

    job_list = job_obj.get_job("fortran software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="siilinjarvi")
	
@fortran.route('/fortran-software-developer-jobs-kuusankoski')
def fortran_software_developer49(page=1):

    job_list = job_obj.get_job("fortran software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kuusankoski")
	
@fortran.route('/fortran-software-developer-jobs-sibbo')
def fortran_software_developer50(page=1):

    job_list = job_obj.get_job("fortran software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="sibbo")
	
@fortran.route('/fortran-software-developer-jobs-jakostad')
def fortran_software_developer51(page=1):

    job_list = job_obj.get_job("fortran software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="jakostad")
	
@fortran.route('/fortran-software-developer-jobs-lempaala')
def fortran_software_developer52(page=1):

    job_list = job_obj.get_job("fortran software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="lempaala")
	
@fortran.route('/fortran-software-developer-jobs-mantsala')
def fortran_software_developer52_1(page=1):

    job_list = job_obj.get_job("fortran software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="mantsala")
	
@fortran.route('/fortran-software-developer-jobs-forssa')
def fortran_software_developer53(page=1):

    job_list = job_obj.get_job("fortran software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="forssa")
	
@fortran.route('/fortran-software-developer-jobs-kuusamo')
def fortran_software_developer54(page=1):

    job_list = job_obj.get_job("fortran software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kuusamo")
	
@fortran.route('/fortran-software-developer-jobs-haukipudas')
def fortran_software_developer55(page=1):

    job_list = job_obj.get_job("fortran software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="haukipudas")
	
@fortran.route('/fortran-software-developer-jobs-korsholm')
def fortran_software_developer56(page=1):

    job_list = job_obj.get_job("fortran software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="korsholm")
	
@fortran.route('/fortran-software-developer-jobs-laukaa')
def fortran_software_developer57(page=1):

    job_list = job_obj.get_job("fortran software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="laukaa")
	
@fortran.route('/fortran-software-developer-jobs-anjala')
def fortran_software_developer58(page=1):

    job_list = job_obj.get_job("fortran software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="anjala")
	
@fortran.route('/fortran-software-developer-jobs-uusikaupunki')
def fortran_software_developer59(page=1):

    job_list = job_obj.get_job("fortran software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="uusikaupunki")
	
@fortran.route('/fortran-software-developer-jobs-janakkala')
def fortran_software_developer60(page=1):

    job_list = job_obj.get_job("fortran software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="janakkala")
	
@fortran.route('/fortran-software-developer-jobs-pirkkala')
def fortran_software_developer61(page=1):

    job_list = job_obj.get_job("fortran software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="pirkkala")
	
@fortran.route('/fortran-software-developer-jobs-lansi-turunmaa')
def fortran_software_developer62(page=1):

    job_list = job_obj.get_job("fortran software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="lansi-turunmaa")
	
@fortran.route('/fortran-software-developer-jobs-jamsa')
def fortran_software_developer63(page=1):

    job_list = job_obj.get_job("fortran software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="jamsa")
	
@fortran.route('/fortran-software-developer-jobs-jamsa')
def fortran_software_developer64(page=1):

    job_list = job_obj.get_job("fortran software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="jamsa")
	
@fortran.route('/fortran-software-developer-jobs-vammala')
def fortran_software_developer65(page=1):

    job_list = job_obj.get_job("fortran software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="vammala")
	
@fortran.route('/fortran-software-developer-jobs-nastola')
def fortran_software_developer66(page=1):

    job_list = job_obj.get_job("fortran software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="nastola")
	
@fortran.route('/fortran-software-developer-jobs-orimattila')
def fortran_software_developer67(page=1):

    job_list = job_obj.get_job("fortran software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="orimattila")
	
@fortran.route('/fortran-software-developer-jobs-kauhajoki')
def fortran_software_developer68(page=1):

    job_list = job_obj.get_job("fortran software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kauhajoki")
	
@fortran.route('/fortran-software-developer-jobs-ekenas')
def fortran_software_developer69(page=1):

    job_list = job_obj.get_job("fortran software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="ekenas")
	
@fortran.route('/fortran-software-developer-jobs-kempele')
def fortran_software_developer70(page=1):

    job_list = job_obj.get_job("fortran software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kempele")
	
@fortran.route('/fortran-software-developer-jobs-lapua')
def fortran_software_developer71(page=1):

    job_list = job_obj.get_job("fortran software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="lapua")
	
@fortran.route('/fortran-software-developer-jobs-lieksa')
def fortran_software_developer72(page=1):

    job_list = job_obj.get_job("fortran software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="lieksa")
	
@fortran.route('/fortran-software-developer-jobs-naantali')
def fortran_software_developer73(page=1):

    job_list = job_obj.get_job("fortran software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="naantali")
	
@fortran.route('/fortran-software-developer-jobs-aanekoski')
def fortran_software_developer74(page=1):

    job_list = job_obj.get_job("fortran software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="aanekoski")
	
@fortran.route('/fortran-software-developer-jobs-ylivieska')
def fortran_software_developer75(page=1):

    job_list = job_obj.get_job("fortran software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="ylivieska")
	
@fortran.route('/fortran-software-developer-jobs-kontiolahti')
def fortran_software_developer76(page=1):

    job_list = job_obj.get_job("fortran software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kontiolahti")
	
@fortran.route('/fortran-software-developer-jobs-kankaanpaa')
def fortran_software_developer77(page=1):

    job_list = job_obj.get_job("fortran software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kankaanpaa")
	
@fortran.route('/fortran-software-developer-jobs-ulvila')
def fortran_software_developer78(page=1):

    job_list = job_obj.get_job("fortran software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="ulvila")
	
@fortran.route('/fortran-software-developer-jobs-pieksamaki')
def fortran_software_developer79(page=1):

    job_list = job_obj.get_job("fortran software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="pieksamaki")
	
@fortran.route('/fortran-software-developer-jobs-kiiminki')
def fortran_software_developer80(page=1):

    job_list = job_obj.get_job("fortran software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kiiminki")
	
@fortran.route('/fortran-software-developer-jobs-pargas')
def fortran_software_developer81(page=1):

    job_list = job_obj.get_job("fortran software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="pargas")
	
@fortran.route('/fortran-software-developer-jobs-nurmo')
def fortran_software_developer82(page=1):

    job_list = job_obj.get_job("fortran software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="nurmo")
	
@fortran.route('/fortran-software-developer-jobs-ilmajoki')
def fortran_software_developer83(page=1):

    job_list = job_obj.get_job("fortran software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="ilmajoki")
	
@fortran.route('/fortran-software-developer-jobs-liperi')
def fortran_software_developer84(page=1):

    job_list = job_obj.get_job("fortran software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="liperi")
	
@fortran.route('/fortran-software-developer-jobs-keuruu')
def fortran_software_developer85(page=1):

    job_list = job_obj.get_job("fortran software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="keuruu")
	
@fortran.route('/fortran-software-developer-jobs-leppavirta')
def fortran_software_developer86(page=1):

    job_list = job_obj.get_job("fortran software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="leppavirta")
	
@fortran.route('/fortran-software-developer-jobs-kurikka')
def fortran_software_developer87(page=1):

    job_list = job_obj.get_job("fortran software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kurikka")
	
@fortran.route('/fortran-software-developer-jobs-nivala')
def fortran_software_developer88(page=1):

    job_list = job_obj.get_job("fortran software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="nivala")
	
@fortran.route('/fortran-software-developer-jobs-joutseno')
def fortran_software_developer89(page=1):

    job_list = job_obj.get_job("fortran software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="joutseno")
	
@fortran.route('/fortran-software-developer-jobs-pedersore')
def fortran_software_developer90(page=1):

    job_list = job_obj.get_job("fortran software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="pedersore")
	
@fortran.route('/fortran-software-developer-jobs-sotkamo')
def fortran_software_developer91(page=1):

    job_list = job_obj.get_job("fortran software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="sotkamo")
	
@fortran.route('/fortran-software-developer-jobs-kuhmo')
def fortran_software_developer92(page=1):

    job_list = job_obj.get_job("fortran software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="kuhmo")
	
@fortran.route('/fortran-software-developer-jobs-paimio')
def fortran_software_developer93(page=1):

    job_list = job_obj.get_job("fortran software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="paimio")
	
@fortran.route('/fortran-software-developer-jobs-saarijarvi')
def fortran_software_developer94(page=1):

    job_list = job_obj.get_job("fortran software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="saarijarvi")
	
@fortran.route('/fortran-software-developer-jobs-helsinki')
def fortran_software_developer95(page=1):

    job_list = job_obj.get_job("fortran software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="fortran software developer", location="helsinki")


####################################################################

