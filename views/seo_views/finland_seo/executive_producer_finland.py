from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

executive_producer = Blueprint('executive_producer', __name__)
job_obj = Job()



####################################################################


@executive_producer.route('/executive-producer_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "executive-producer" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@executive_producer.route('/executive-producer-avoimet-tyopaikat-espoo')
def executive_producer_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("executive producer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="espoo")

@executive_producer.route('/executive-producer-avoimet-tyopaikat-tampere')
def executive_producer_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("executive producer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="tampere")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-vantaa')
def executive_producer_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("executive producer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="vantaa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-turku')
def executive_producer_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("executive producer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="turku")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-oulu')
def executive_producer_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("executive producer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="oulu")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-lahti')
def executive_producer_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("executive producer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lahti")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kuopio')
def executive_producer_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("executive producer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kuopio")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-jyvvaskyla')
def executive_producer_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("executive producer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="jyvvaskyla")

@executive_producer.route('/executive-producer-avoimet-tyopaikat-pori')
def executive_producer_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("executive producer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="pori")

@executive_producer.route('/executive-producer-avoimet-tyopaikat-lappeenranta')
def executive_producer_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("executive producer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lappeenranta")	
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-vaasa')
def executive_producer_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("executive producer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="vaasa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kotka')
def executive_producer_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("executive producer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kotka")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-joensuu')
def executive_producer_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("executive producer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="joensuu")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-hameenlinna')
def executive_producer_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("executive producer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="hameenlinna")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-porvoo')
def executive_producer_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("executive producer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="porvoo")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-mikkeli')
def executive_producer_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("executive producer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="mikkeli")

@executive_producer.route('/executive-producer-avoimet-tyopaikat-hyvinkaa')
def executive_producer_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("executive producer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="hyvinkaa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-nurmijarvi')
def executive_producer_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("executive producer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="nurmijarvi")

@executive_producer.route('/executive-producer-avoimet-tyopaikat-jarvenpaa')
def executive_producer_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("executive producer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="jarvenpaa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-rauma')
def executive_producer_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("executive producer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="rauma")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-lohja')
def executive_producer_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("executive producer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lohja")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-karleby')
def executive_producer_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("executive producer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="karleby")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kajaani')
def executive_producer_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("executive producer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kajaani")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-rovaniemi')
def executive_producer_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("executive producer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="rovaniemi")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-tuusula')
def executive_producer_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("executive producer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="tuusula")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kirkkonummi')
def executive_producer_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("executive producer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kirkkonummi")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-seinajoki')
def executive_producer_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("executive producer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="seinajoki")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kerava')
def executive_producer_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("executive producer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kerava")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kouvola')
def executive_producer_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("executive producer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kouvola")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-imatra')
def executive_producer_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("executive producer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="imatra")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-nokia')
def executive_producer_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("executive producer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="nokia")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-savonlinna')
def executive_producer_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("executive producer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="savonlinna")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-riihimaki')
def executive_producer_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("executive producer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="riihimaki")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-vihti')
def executive_producer_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("executive producer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="vihti")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-salo')
def executive_producer_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("executive producer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="salo")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kangasala')
def executive_producer_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("executive producer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kangasala")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-raisio')
def executive_producer_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("executive producer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="raisio")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-karhula')
def executive_producer_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("executive producer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="karhula")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kemi')
def executive_producer_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("executive producer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kemi")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-iisalmi')
def executive_producer_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("executive producer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="iisalmi")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-varkaus')
def executive_producer_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("executive producer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="varkaus")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-raahe')
def executive_producer_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("executive producer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="raahe")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-ylojarvi')
def executive_producer_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("executive producer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="ylojarvi")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-hamina')
def executive_producer_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("executive producer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="hamina")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kaarina')
def executive_producer_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("executive producer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kaarina")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-tornio')
def executive_producer_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("executive producer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="tornio")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-heinola')
def executive_producer_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("executive producer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="heinola")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-hollola')
def executive_producer_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("executive producer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="hollola")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-valkeakoski')
def executive_producer_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("executive producer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="valkeakoski")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-siilinjarvi')
def executive_producer_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("executive producer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="siilinjarvi")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kuusankoski')
def executive_producer_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("executive producer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kuusankoski")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-sibbo')
def executive_producer_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("executive producer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="sibbo")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-jakostad')
def executive_producer_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("executive producer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="jakostad")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-lempaala')
def executive_producer_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("executive producer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lempaala")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-mantsala')
def executive_producer_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("executive producer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="mantsala")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-forssa')
def executive_producer_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("executive producer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="forssa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kuusamo')
def executive_producer_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("executive producer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kuusamo")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-haukipudas')
def executive_producer_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("executive producer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="haukipudas")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-korsholm')
def executive_producer_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("executive producer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="korsholm")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-laukaa')
def executive_producer_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("executive producer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="laukaa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-anjala')
def executive_producer_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("executive producer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="anjala")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-uusikaupunki')
def executive_producer_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("executive producer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="uusikaupunki")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-janakkala')
def executive_producer_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("executive producer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="janakkala")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-pirkkala')
def executive_producer_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("executive producer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="pirkkala")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-lansi-turunmaa')
def executive_producer_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("executive producer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lansi-turunmaa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-jamsa')
def executive_producer_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("executive producer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="jamsa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-jamsa')
def executive_producer_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("executive producer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="jamsa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-vammala')
def executive_producer_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("executive producer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="vammala")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-nastola')
def executive_producer_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("executive producer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="nastola")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-orimattila')
def executive_producer_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("executive producer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="orimattila")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kauhajoki')
def executive_producer_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("executive producer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kauhajoki")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-ekenas')
def executive_producer_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("executive producer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="ekenas")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kempele')
def executive_producer_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("executive producer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kempele")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-lapua')
def executive_producer_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("executive producer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lapua")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-lieksa')
def executive_producer_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("executive producer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lieksa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-naantali')
def executive_producer_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("executive producer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="naantali")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-aanekoski')
def executive_producer_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("executive producer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="aanekoski")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-ylivieska')
def executive_producer_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("executive producer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="ylivieska")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kontiolahti')
def executive_producer_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("executive producer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kontiolahti")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kankaanpaa')
def executive_producer_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("executive producer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kankaanpaa")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-ulvila')
def executive_producer_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("executive producer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="ulvila")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-pieksamaki')
def executive_producer_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("executive producer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="pieksamaki")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kiiminki')
def executive_producer_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("executive producer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kiiminki")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-pargas')
def executive_producer_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("executive producer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="pargas")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-nurmo')
def executive_producer_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("executive producer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="nurmo")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-ilmajoki')
def executive_producer_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("executive producer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="ilmajoki")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-liperi')
def executive_producer_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("executive producer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="liperi")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-keuruu')
def executive_producer_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("executive producer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="keuruu")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-leppavirta')
def executive_producer_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("executive producer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="leppavirta")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kurikka')
def executive_producer_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("executive producer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kurikka")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-nivala')
def executive_producer_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("executive producer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="nivala")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-joutseno')
def executive_producer_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("executive producer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="joutseno")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-pedersore')
def executive_producer_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("executive producer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="pedersore")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-sotkamo')
def executive_producer_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("executive producer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="sotkamo")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-kuhmo')
def executive_producer_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("executive producer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kuhmo")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-paimio')
def executive_producer_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("executive producer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="paimio")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-saarijarvi')
def executive_producer_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("executive producer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="saarijarvi")
	
@executive_producer.route('/executive-producer-avoimet-tyopaikat-helsinki')
def executive_producer_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("executive producer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="helsinki")


####################################################################


##############################################
@executive_producer.route('/executive-producer-jobs-espoo')
def executive_producer_jobs2(page=1):

    job_list = job_obj.get_job("executive producer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="espoo")

@executive_producer.route('/executive-producer-jobs-tampere')
def executive_producer_jobs3(page=1):

    job_list = job_obj.get_job("executive producer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="tampere")
	
@executive_producer.route('/executive-producer-jobs-vantaa')
def executive_producer_jobs4(page=1):

    job_list = job_obj.get_job("executive producer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="vantaa")
	
@executive_producer.route('/executive-producer-jobs-turku')
def executive_producer_jobs5(page=1):

    job_list = job_obj.get_job("executive producer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="turku")
	
@executive_producer.route('/executive-producer-jobs-oulu')
def executive_producer_jobs6(page=1):

    job_list = job_obj.get_job("executive producer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="oulu")
	
@executive_producer.route('/executive-producer-jobs-lahti')
def executive_producer_jobs7(page=1):

    job_list = job_obj.get_job("executive producer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lahti")
	
@executive_producer.route('/executive-producer-jobs-kuopio')
def executive_producer_jobs8(page=1):

    job_list = job_obj.get_job("executive producer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kuopio")
	
@executive_producer.route('/executive-producer-jobs-jyvvaskyla')
def executive_producer_jobs9(page=1):

    job_list = job_obj.get_job("executive producer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="jyvvaskyla")

@executive_producer.route('/executive-producer-jobs-pori')
def executive_producer_jobs10(page=1):

    job_list = job_obj.get_job("executive producer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="pori")

@executive_producer.route('/executive-producer-jobs-lappeenranta')
def executive_producer_jobs11(page=1):

    job_list = job_obj.get_job("executive producer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lappeenranta")	
	
@executive_producer.route('/executive-producer-jobs-vaasa')
def executive_producer_jobs12(page=1):

    job_list = job_obj.get_job("executive producer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="vaasa")
	
@executive_producer.route('/executive-producer-jobs-kotka')
def executive_producer_jobs13(page=1):

    job_list = job_obj.get_job("executive producer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kotka")
	
@executive_producer.route('/executive-producer-jobs-joensuu')
def executive_producer_jobs14(page=1):

    job_list = job_obj.get_job("executive producer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="joensuu")
	
@executive_producer.route('/executive-producer-jobs-hameenlinna')
def executive_producer_jobs15(page=1):

    job_list = job_obj.get_job("executive producer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="hameenlinna")
	
@executive_producer.route('/executive-producer-jobs-porvoo')
def executive_producer_jobs16(page=1):

    job_list = job_obj.get_job("executive producer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="porvoo")
	
@executive_producer.route('/executive-producer-jobs-mikkeli')
def executive_producer_jobs17(page=1):

    job_list = job_obj.get_job("executive producer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="mikkeli")

@executive_producer.route('/executive-producer-jobs-hyvinkaa')
def executive_producer_jobs18(page=1):

    job_list = job_obj.get_job("executive producer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="hyvinkaa")
	
@executive_producer.route('/executive-producer-jobs-nurmijarvi')
def executive_producer_jobs19(page=1):

    job_list = job_obj.get_job("executive producer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="nurmijarvi")

@executive_producer.route('/executive-producer-jobs-jarvenpaa')
def executive_producer_jobs20(page=1):

    job_list = job_obj.get_job("executive producer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="jarvenpaa")
	
@executive_producer.route('/executive-producer-jobs-rauma')
def executive_producer_jobs21(page=1):

    job_list = job_obj.get_job("executive producer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="rauma")
	
@executive_producer.route('/executive-producer-jobs-lohja')
def executive_producer_jobs22(page=1):

    job_list = job_obj.get_job("executive producer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lohja")
	
@executive_producer.route('/executive-producer-jobs-karleby')
def executive_producer_jobs23(page=1):

    job_list = job_obj.get_job("executive producer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="karleby")
	
@executive_producer.route('/executive-producer-jobs-kajaani')
def executive_producer_jobs24(page=1):

    job_list = job_obj.get_job("executive producer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kajaani")
	
@executive_producer.route('/executive-producer-jobs-rovaniemi')
def executive_producer_jobs25(page=1):

    job_list = job_obj.get_job("executive producer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="rovaniemi")
	
@executive_producer.route('/executive-producer-jobs-tuusula')
def executive_producer_jobs26(page=1):

    job_list = job_obj.get_job("executive producer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="tuusula")
	
@executive_producer.route('/executive-producer-jobs-kirkkonummi')
def executive_producer_jobs27(page=1):

    job_list = job_obj.get_job("executive producer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kirkkonummi")
	
@executive_producer.route('/executive-producer-jobs-seinajoki')
def executive_producer_jobs28(page=1):

    job_list = job_obj.get_job("executive producer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="seinajoki")
	
@executive_producer.route('/executive-producer-jobs-kerava')
def executive_producer_jobs29(page=1):

    job_list = job_obj.get_job("executive producer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kerava")
	
@executive_producer.route('/executive-producer-jobs-kouvola')
def executive_producer_jobs30(page=1):

    job_list = job_obj.get_job("executive producer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kouvola")
	
@executive_producer.route('/executive-producer-jobs-imatra')
def executive_producer_jobs31(page=1):

    job_list = job_obj.get_job("executive producer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="imatra")
	
@executive_producer.route('/executive-producer-jobs-nokia')
def executive_producer_jobs32_1(page=1):

    job_list = job_obj.get_job("executive producer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="nokia")
	
@executive_producer.route('/executive-producer-jobs-savonlinna')
def executive_producer_jobs32(page=1):

    job_list = job_obj.get_job("executive producer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="savonlinna")
	
@executive_producer.route('/executive-producer-jobs-riihimaki')
def executive_producer_jobs33(page=1):

    job_list = job_obj.get_job("executive producer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="riihimaki")
	
@executive_producer.route('/executive-producer-jobs-vihti')
def executive_producer_jobs34(page=1):

    job_list = job_obj.get_job("executive producer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="vihti")
	
@executive_producer.route('/executive-producer-jobs-salo')
def executive_producer_jobs35(page=1):

    job_list = job_obj.get_job("executive producer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="salo")
	
@executive_producer.route('/executive-producer-jobs-kangasala')
def executive_producer_jobs36(page=1):

    job_list = job_obj.get_job("executive producer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kangasala")
	
@executive_producer.route('/executive-producer-jobs-raisio')
def executive_producer_jobs37_1(page=1):

    job_list = job_obj.get_job("executive producer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="raisio")
	
@executive_producer.route('/executive-producer-jobs-karhula')
def executive_producer_jobs37(page=1):

    job_list = job_obj.get_job("executive producer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="karhula")
	
@executive_producer.route('/executive-producer-jobs-kemi')
def executive_producer_jobs38(page=1):

    job_list = job_obj.get_job("executive producer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kemi")
	
@executive_producer.route('/executive-producer-jobs-iisalmi')
def executive_producer_jobs39(page=1):

    job_list = job_obj.get_job("executive producer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="iisalmi")
	
@executive_producer.route('/executive-producer-jobs-varkaus')
def executive_producer_jobs40(page=1):

    job_list = job_obj.get_job("executive producer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="varkaus")
	
@executive_producer.route('/executive-producer-jobs-raahe')
def executive_producer_jobs41(page=1):

    job_list = job_obj.get_job("executive producer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="raahe")
	
@executive_producer.route('/executive-producer-jobs-ylojarvi')
def executive_producer_jobs42_1(page=1):

    job_list = job_obj.get_job("executive producer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="ylojarvi")
	
@executive_producer.route('/executive-producer-jobs-hamina')
def executive_producer_jobs42(page=1):

    job_list = job_obj.get_job("executive producer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="hamina")
	
@executive_producer.route('/executive-producer-jobs-kaarina')
def executive_producer_jobs43(page=1):

    job_list = job_obj.get_job("executive producer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kaarina")
	
@executive_producer.route('/executive-producer-jobs-tornio')
def executive_producer_jobs44(page=1):

    job_list = job_obj.get_job("executive producer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="tornio")
	
@executive_producer.route('/executive-producer-jobs-heinola')
def executive_producer_jobs45(page=1):

    job_list = job_obj.get_job("executive producer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="heinola")
	
@executive_producer.route('/executive-producer-jobs-hollola')
def executive_producer_jobs46(page=1):

    job_list = job_obj.get_job("executive producer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="hollola")
	
@executive_producer.route('/executive-producer-jobs-valkeakoski')
def executive_producer_jobs47(page=1):

    job_list = job_obj.get_job("executive producer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="valkeakoski")
	
@executive_producer.route('/executive-producer-jobs-siilinjarvi')
def executive_producer_jobs48(page=1):

    job_list = job_obj.get_job("executive producer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="siilinjarvi")
	
@executive_producer.route('/executive-producer-jobs-kuusankoski')
def executive_producer_jobs49(page=1):

    job_list = job_obj.get_job("executive producer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kuusankoski")
	
@executive_producer.route('/executive-producer-jobs-sibbo')
def executive_producer_jobs50(page=1):

    job_list = job_obj.get_job("executive producer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="sibbo")
	
@executive_producer.route('/executive-producer-jobs-jakostad')
def executive_producer_jobs51(page=1):

    job_list = job_obj.get_job("executive producer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="jakostad")
	
@executive_producer.route('/executive-producer-jobs-lempaala')
def executive_producer_jobs52(page=1):

    job_list = job_obj.get_job("executive producer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lempaala")
	
@executive_producer.route('/executive-producer-jobs-mantsala')
def executive_producer_jobs52_1(page=1):

    job_list = job_obj.get_job("executive producer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="mantsala")
	
@executive_producer.route('/executive-producer-jobs-forssa')
def executive_producer_jobs53(page=1):

    job_list = job_obj.get_job("executive producer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="forssa")
	
@executive_producer.route('/executive-producer-jobs-kuusamo')
def executive_producer_jobs54(page=1):

    job_list = job_obj.get_job("executive producer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kuusamo")
	
@executive_producer.route('/executive-producer-jobs-haukipudas')
def executive_producer_jobs55(page=1):

    job_list = job_obj.get_job("executive producer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="haukipudas")
	
@executive_producer.route('/executive-producer-jobs-korsholm')
def executive_producer_jobs56(page=1):

    job_list = job_obj.get_job("executive producer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="korsholm")
	
@executive_producer.route('/executive-producer-jobs-laukaa')
def executive_producer_jobs57(page=1):

    job_list = job_obj.get_job("executive producer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="laukaa")
	
@executive_producer.route('/executive-producer-jobs-anjala')
def executive_producer_jobs58(page=1):

    job_list = job_obj.get_job("executive producer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="anjala")
	
@executive_producer.route('/executive-producer-jobs-uusikaupunki')
def executive_producer_jobs59(page=1):

    job_list = job_obj.get_job("executive producer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="uusikaupunki")
	
@executive_producer.route('/executive-producer-jobs-janakkala')
def executive_producer_jobs60(page=1):

    job_list = job_obj.get_job("executive producer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="janakkala")
	
@executive_producer.route('/executive-producer-jobs-pirkkala')
def executive_producer_jobs61(page=1):

    job_list = job_obj.get_job("executive producer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="pirkkala")
	
@executive_producer.route('/executive-producer-jobs-lansi-turunmaa')
def executive_producer_jobs62(page=1):

    job_list = job_obj.get_job("executive producer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lansi-turunmaa")
	
@executive_producer.route('/executive-producer-jobs-jamsa')
def executive_producer_jobs63(page=1):

    job_list = job_obj.get_job("executive producer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="jamsa")
	
@executive_producer.route('/executive-producer-jobs-jamsa')
def executive_producer_jobs64(page=1):

    job_list = job_obj.get_job("executive producer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="jamsa")
	
@executive_producer.route('/executive-producer-jobs-vammala')
def executive_producer_jobs65(page=1):

    job_list = job_obj.get_job("executive producer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="vammala")
	
@executive_producer.route('/executive-producer-jobs-nastola')
def executive_producer_jobs66(page=1):

    job_list = job_obj.get_job("executive producer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="nastola")
	
@executive_producer.route('/executive-producer-jobs-orimattila')
def executive_producer_jobs67(page=1):

    job_list = job_obj.get_job("executive producer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="orimattila")
	
@executive_producer.route('/executive-producer-jobs-kauhajoki')
def executive_producer_jobs68(page=1):

    job_list = job_obj.get_job("executive producer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kauhajoki")
	
@executive_producer.route('/executive-producer-jobs-ekenas')
def executive_producer_jobs69(page=1):

    job_list = job_obj.get_job("executive producer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="ekenas")
	
@executive_producer.route('/executive-producer-jobs-kempele')
def executive_producer_jobs70(page=1):

    job_list = job_obj.get_job("executive producer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kempele")
	
@executive_producer.route('/executive-producer-jobs-lapua')
def executive_producer_jobs71(page=1):

    job_list = job_obj.get_job("executive producer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lapua")
	
@executive_producer.route('/executive-producer-jobs-lieksa')
def executive_producer_jobs72(page=1):

    job_list = job_obj.get_job("executive producer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="lieksa")
	
@executive_producer.route('/executive-producer-jobs-naantali')
def executive_producer_jobs73(page=1):

    job_list = job_obj.get_job("executive producer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="naantali")
	
@executive_producer.route('/executive-producer-jobs-aanekoski')
def executive_producer_jobs74(page=1):

    job_list = job_obj.get_job("executive producer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="aanekoski")
	
@executive_producer.route('/executive-producer-jobs-ylivieska')
def executive_producer_jobs75(page=1):

    job_list = job_obj.get_job("executive producer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="ylivieska")
	
@executive_producer.route('/executive-producer-jobs-kontiolahti')
def executive_producer_jobs76(page=1):

    job_list = job_obj.get_job("executive producer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kontiolahti")
	
@executive_producer.route('/executive-producer-jobs-kankaanpaa')
def executive_producer_jobs77(page=1):

    job_list = job_obj.get_job("executive producer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kankaanpaa")
	
@executive_producer.route('/executive-producer-jobs-ulvila')
def executive_producer_jobs78(page=1):

    job_list = job_obj.get_job("executive producer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="ulvila")
	
@executive_producer.route('/executive-producer-jobs-pieksamaki')
def executive_producer_jobs79(page=1):

    job_list = job_obj.get_job("executive producer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="pieksamaki")
	
@executive_producer.route('/executive-producer-jobs-kiiminki')
def executive_producer_jobs80(page=1):

    job_list = job_obj.get_job("executive producer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kiiminki")
	
@executive_producer.route('/executive-producer-jobs-pargas')
def executive_producer_jobs81(page=1):

    job_list = job_obj.get_job("executive producer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="pargas")
	
@executive_producer.route('/executive-producer-jobs-nurmo')
def executive_producer_jobs82(page=1):

    job_list = job_obj.get_job("executive producer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="nurmo")
	
@executive_producer.route('/executive-producer-jobs-ilmajoki')
def executive_producer_jobs83(page=1):

    job_list = job_obj.get_job("executive producer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="ilmajoki")
	
@executive_producer.route('/executive-producer-jobs-liperi')
def executive_producer_jobs84(page=1):

    job_list = job_obj.get_job("executive producer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="liperi")
	
@executive_producer.route('/executive-producer-jobs-keuruu')
def executive_producer_jobs85(page=1):

    job_list = job_obj.get_job("executive producer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="keuruu")
	
@executive_producer.route('/executive-producer-jobs-leppavirta')
def executive_producer_jobs86(page=1):

    job_list = job_obj.get_job("executive producer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="leppavirta")
	
@executive_producer.route('/executive-producer-jobs-kurikka')
def executive_producer_jobs87(page=1):

    job_list = job_obj.get_job("executive producer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kurikka")
	
@executive_producer.route('/executive-producer-jobs-nivala')
def executive_producer_jobs88(page=1):

    job_list = job_obj.get_job("executive producer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="nivala")
	
@executive_producer.route('/executive-producer-jobs-joutseno')
def executive_producer_jobs89(page=1):

    job_list = job_obj.get_job("executive producer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="joutseno")
	
@executive_producer.route('/executive-producer-jobs-pedersore')
def executive_producer_jobs90(page=1):

    job_list = job_obj.get_job("executive producer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="pedersore")
	
@executive_producer.route('/executive-producer-jobs-sotkamo')
def executive_producer_jobs91(page=1):

    job_list = job_obj.get_job("executive producer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="sotkamo")
	
@executive_producer.route('/executive-producer-jobs-kuhmo')
def executive_producer_jobs92(page=1):

    job_list = job_obj.get_job("executive producer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="kuhmo")
	
@executive_producer.route('/executive-producer-jobs-paimio')
def executive_producer_jobs93(page=1):

    job_list = job_obj.get_job("executive producer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="paimio")
	
@executive_producer.route('/executive-producer-jobs-saarijarvi')
def executive_producer_jobs94(page=1):

    job_list = job_obj.get_job("executive producer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="saarijarvi")
	
@executive_producer.route('/executive-producer-jobs-helsinki')
def executive_producer_jobs95(page=1):

    job_list = job_obj.get_job("executive producer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer ", location="helsinki")


####################################################################


##############################################
@executive_producer.route('/executive-producer-tyopaikat-espoo')
def executive_producer_tyopaikat2(page=1):

    job_list = job_obj.get_job("executive producer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="espoo")

@executive_producer.route('/executive-producer-tyopaikat-tampere')
def executive_producer_tyopaikat3(page=1):

    job_list = job_obj.get_job("executive producer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="tampere")
	
@executive_producer.route('/executive-producer-tyopaikat-vantaa')
def executive_producer_tyopaikat4(page=1):

    job_list = job_obj.get_job("executive producer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="vantaa")
	
@executive_producer.route('/executive-producer-tyopaikat-turku')
def executive_producer_tyopaikat5(page=1):

    job_list = job_obj.get_job("executive producer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="turku")
	
@executive_producer.route('/executive-producer-tyopaikat-oulu')
def executive_producer_tyopaikat6(page=1):

    job_list = job_obj.get_job("executive producer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="oulu")
	
@executive_producer.route('/executive-producer-tyopaikat-lahti')
def executive_producer_tyopaikat7(page=1):

    job_list = job_obj.get_job("executive producer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="lahti")
	
@executive_producer.route('/executive-producer-tyopaikat-kuopio')
def executive_producer_tyopaikat8(page=1):

    job_list = job_obj.get_job("executive producer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kuopio")
	
@executive_producer.route('/executive-producer-tyopaikat-jyvvaskyla')
def executive_producer_tyopaikat9(page=1):

    job_list = job_obj.get_job("executive producer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="jyvvaskyla")

@executive_producer.route('/executive-producer-tyopaikat-pori')
def executive_producer_tyopaikat10(page=1):

    job_list = job_obj.get_job("executive producer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="pori")

@executive_producer.route('/executive-producer-tyopaikat-lappeenranta')
def executive_producer_tyopaikat11(page=1):

    job_list = job_obj.get_job("executive producer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="lappeenranta")	
	
@executive_producer.route('/executive-producer-tyopaikat-vaasa')
def executive_producer_tyopaikat12(page=1):

    job_list = job_obj.get_job("executive producer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="vaasa")
	
@executive_producer.route('/executive-producer-tyopaikat-kotka')
def executive_producer_tyopaikat13(page=1):

    job_list = job_obj.get_job("executive producer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kotka")
	
@executive_producer.route('/executive-producer-tyopaikat-joensuu')
def executive_producer_tyopaikat14(page=1):

    job_list = job_obj.get_job("executive producer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="joensuu")
	
@executive_producer.route('/executive-producer-tyopaikat-hameenlinna')
def executive_producer_tyopaikat15(page=1):

    job_list = job_obj.get_job("executive producer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="hameenlinna")
	
@executive_producer.route('/executive-producer-tyopaikat-porvoo')
def executive_producer_tyopaikat16(page=1):

    job_list = job_obj.get_job("executive producer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="porvoo")
	
@executive_producer.route('/executive-producer-tyopaikat-mikkeli')
def executive_producer_tyopaikat17(page=1):

    job_list = job_obj.get_job("executive producer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="mikkeli")

@executive_producer.route('/executive-producer-tyopaikat-hyvinkaa')
def executive_producer_tyopaikat18(page=1):

    job_list = job_obj.get_job("executive producer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="hyvinkaa")
	
@executive_producer.route('/executive-producer-tyopaikat-nurmijarvi')
def executive_producer_tyopaikat19(page=1):

    job_list = job_obj.get_job("executive producer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="nurmijarvi")

@executive_producer.route('/executive-producer-tyopaikat-jarvenpaa')
def executive_producer_tyopaikat20(page=1):

    job_list = job_obj.get_job("executive producer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="jarvenpaa")
	
@executive_producer.route('/executive-producer-tyopaikat-rauma')
def executive_producer_tyopaikat21(page=1):

    job_list = job_obj.get_job("executive producer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="rauma")
	
@executive_producer.route('/executive-producer-tyopaikat-lohja')
def executive_producer_tyopaikat22(page=1):

    job_list = job_obj.get_job("executive producer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="lohja")
	
@executive_producer.route('/executive-producer-tyopaikat-karleby')
def executive_producer_tyopaikat23(page=1):

    job_list = job_obj.get_job("executive producer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="karleby")
	
@executive_producer.route('/executive-producer-tyopaikat-kajaani')
def executive_producer_tyopaikat24(page=1):

    job_list = job_obj.get_job("executive producer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kajaani")
	
@executive_producer.route('/executive-producer-tyopaikat-rovaniemi')
def executive_producer_tyopaikat25(page=1):

    job_list = job_obj.get_job("executive producer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="rovaniemi")
	
@executive_producer.route('/executive-producer-tyopaikat-tuusula')
def executive_producer_tyopaikat26(page=1):

    job_list = job_obj.get_job("executive producer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="tuusula")
	
@executive_producer.route('/executive-producer-tyopaikat-kirkkonummi')
def executive_producer_tyopaikat27(page=1):

    job_list = job_obj.get_job("executive producer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kirkkonummi")
	
@executive_producer.route('/executive-producer-tyopaikat-seinajoki')
def executive_producer_tyopaikat28(page=1):

    job_list = job_obj.get_job("executive producer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="seinajoki")
	
@executive_producer.route('/executive-producer-tyopaikat-kerava')
def executive_producer_tyopaikat29(page=1):

    job_list = job_obj.get_job("executive producer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kerava")
	
@executive_producer.route('/executive-producer-tyopaikat-kouvola')
def executive_producer_tyopaikat30(page=1):

    job_list = job_obj.get_job("executive producer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kouvola")
	
@executive_producer.route('/executive-producer-tyopaikat-imatra')
def executive_producer_tyopaikat31(page=1):

    job_list = job_obj.get_job("executive producer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="imatra")
	
@executive_producer.route('/executive-producer-tyopaikat-nokia')
def executive_producer_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("executive producer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="nokia")
	
@executive_producer.route('/executive-producer-tyopaikat-savonlinna')
def executive_producer_tyopaikat32(page=1):

    job_list = job_obj.get_job("executive producer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="savonlinna")
	
@executive_producer.route('/executive-producer-tyopaikat-riihimaki')
def executive_producer_tyopaikat33(page=1):

    job_list = job_obj.get_job("executive producer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="riihimaki")
	
@executive_producer.route('/executive-producer-tyopaikat-vihti')
def executive_producer_tyopaikat34(page=1):

    job_list = job_obj.get_job("executive producer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="vihti")
	
@executive_producer.route('/executive-producer-tyopaikat-salo')
def executive_producer_tyopaikat35(page=1):

    job_list = job_obj.get_job("executive producer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="salo")
	
@executive_producer.route('/executive-producer-tyopaikat-kangasala')
def executive_producer_tyopaikat36(page=1):

    job_list = job_obj.get_job("executive producer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kangasala")
	
@executive_producer.route('/executive-producer-tyopaikat-raisio')
def executive_producer_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("executive producer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="raisio")
	
@executive_producer.route('/executive-producer-tyopaikat-karhula')
def executive_producer_tyopaikat37(page=1):

    job_list = job_obj.get_job("executive producer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="karhula")
	
@executive_producer.route('/executive-producer-tyopaikat-kemi')
def executive_producer_tyopaikat38(page=1):

    job_list = job_obj.get_job("executive producer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kemi")
	
@executive_producer.route('/executive-producer-tyopaikat-iisalmi')
def executive_producer_tyopaikat39(page=1):

    job_list = job_obj.get_job("executive producer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="iisalmi")
	
@executive_producer.route('/executive-producer-tyopaikat-varkaus')
def executive_producer_tyopaikat40(page=1):

    job_list = job_obj.get_job("executive producer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="varkaus")
	
@executive_producer.route('/executive-producer-tyopaikat-raahe')
def executive_producer_tyopaikat41(page=1):

    job_list = job_obj.get_job("executive producer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="raahe")
	
@executive_producer.route('/executive-producer-tyopaikat-ylojarvi')
def executive_producer_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("executive producer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="ylojarvi")
	
@executive_producer.route('/executive-producer-tyopaikat-hamina')
def executive_producer_tyopaikat42(page=1):

    job_list = job_obj.get_job("executive producer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="hamina")
	
@executive_producer.route('/executive-producer-tyopaikat-kaarina')
def executive_producer_tyopaikat43(page=1):

    job_list = job_obj.get_job("executive producer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kaarina")
	
@executive_producer.route('/executive-producer-tyopaikat-tornio')
def executive_producer_tyopaikat44(page=1):

    job_list = job_obj.get_job("executive producer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="tornio")
	
@executive_producer.route('/executive-producer-tyopaikat-heinola')
def executive_producer_tyopaikat45(page=1):

    job_list = job_obj.get_job("executive producer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="heinola")
	
@executive_producer.route('/executive-producer-tyopaikat-hollola')
def executive_producer_tyopaikat46(page=1):

    job_list = job_obj.get_job("executive producer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="hollola")
	
@executive_producer.route('/executive-producer-tyopaikat-valkeakoski')
def executive_producer_tyopaikat47(page=1):

    job_list = job_obj.get_job("executive producer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="valkeakoski")
	
@executive_producer.route('/executive-producer-tyopaikat-siilinjarvi')
def executive_producer_tyopaikat48(page=1):

    job_list = job_obj.get_job("executive producer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="siilinjarvi")
	
@executive_producer.route('/executive-producer-tyopaikat-kuusankoski')
def executive_producer_tyopaikat49(page=1):

    job_list = job_obj.get_job("executive producer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kuusankoski")
	
@executive_producer.route('/executive-producer-tyopaikat-sibbo')
def executive_producer_tyopaikat50(page=1):

    job_list = job_obj.get_job("executive producer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="sibbo")
	
@executive_producer.route('/executive-producer-tyopaikat-jakostad')
def executive_producer_tyopaikat51(page=1):

    job_list = job_obj.get_job("executive producer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="jakostad")
	
@executive_producer.route('/executive-producer-tyopaikat-lempaala')
def executive_producer_tyopaikat52(page=1):

    job_list = job_obj.get_job("executive producer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="lempaala")
	
@executive_producer.route('/executive-producer-tyopaikat-mantsala')
def executive_producer_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("executive producer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="mantsala")
	
@executive_producer.route('/executive-producer-tyopaikat-forssa')
def executive_producer_tyopaikat53(page=1):

    job_list = job_obj.get_job("executive producer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="forssa")
	
@executive_producer.route('/executive-producer-tyopaikat-kuusamo')
def executive_producer_tyopaikat54(page=1):

    job_list = job_obj.get_job("executive producer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kuusamo")
	
@executive_producer.route('/executive-producer-tyopaikat-haukipudas')
def executive_producer_tyopaikat55(page=1):

    job_list = job_obj.get_job("executive producer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="haukipudas")
	
@executive_producer.route('/executive-producer-tyopaikat-korsholm')
def executive_producer_tyopaikat56(page=1):

    job_list = job_obj.get_job("executive producer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="korsholm")
	
@executive_producer.route('/executive-producer-tyopaikat-laukaa')
def executive_producer_tyopaikat57(page=1):

    job_list = job_obj.get_job("executive producer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="laukaa")
	
@executive_producer.route('/executive-producer-tyopaikat-anjala')
def executive_producer_tyopaikat58(page=1):

    job_list = job_obj.get_job("executive producer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="anjala")
	
@executive_producer.route('/executive-producer-tyopaikat-uusikaupunki')
def executive_producer_tyopaikat59(page=1):

    job_list = job_obj.get_job("executive producer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="uusikaupunki")
	
@executive_producer.route('/executive-producer-tyopaikat-janakkala')
def executive_producer_tyopaikat60(page=1):

    job_list = job_obj.get_job("executive producer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="janakkala")
	
@executive_producer.route('/executive-producer-tyopaikat-pirkkala')
def executive_producer_tyopaikat61(page=1):

    job_list = job_obj.get_job("executive producer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="pirkkala")
	
@executive_producer.route('/executive-producer-tyopaikat-lansi-turunmaa')
def executive_producer_tyopaikat62(page=1):

    job_list = job_obj.get_job("executive producer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="lansi-turunmaa")
	
@executive_producer.route('/executive-producer-tyopaikat-jamsa')
def executive_producer_tyopaikat63(page=1):

    job_list = job_obj.get_job("executive producer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="jamsa")
	
@executive_producer.route('/executive-producer-tyopaikat-jamsa')
def executive_producer_tyopaikat64(page=1):

    job_list = job_obj.get_job("executive producer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="jamsa")
	
@executive_producer.route('/executive-producer-tyopaikat-vammala')
def executive_producer_tyopaikat65(page=1):

    job_list = job_obj.get_job("executive producer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="vammala")
	
@executive_producer.route('/executive-producer-tyopaikat-nastola')
def executive_producer_tyopaikat66(page=1):

    job_list = job_obj.get_job("executive producer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="nastola")
	
@executive_producer.route('/executive-producer-tyopaikat-orimattila')
def executive_producer_tyopaikat67(page=1):

    job_list = job_obj.get_job("executive producer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="orimattila")
	
@executive_producer.route('/executive-producer-tyopaikat-kauhajoki')
def executive_producer_tyopaikat68(page=1):

    job_list = job_obj.get_job("executive producer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kauhajoki")
	
@executive_producer.route('/executive-producer-tyopaikat-ekenas')
def executive_producer_tyopaikat69(page=1):

    job_list = job_obj.get_job("executive producer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="ekenas")
	
@executive_producer.route('/executive-producer-tyopaikat-kempele')
def executive_producer_tyopaikat70(page=1):

    job_list = job_obj.get_job("executive producer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kempele")
	
@executive_producer.route('/executive-producer-tyopaikat-lapua')
def executive_producer_tyopaikat71(page=1):

    job_list = job_obj.get_job("executive producer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="lapua")
	
@executive_producer.route('/executive-producer-tyopaikat-lieksa')
def executive_producer_tyopaikat72(page=1):

    job_list = job_obj.get_job("executive producer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="lieksa")
	
@executive_producer.route('/executive-producer-tyopaikat-naantali')
def executive_producer_tyopaikat73(page=1):

    job_list = job_obj.get_job("executive producer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="naantali")
	
@executive_producer.route('/executive-producer-tyopaikat-aanekoski')
def executive_producer_tyopaikat74(page=1):

    job_list = job_obj.get_job("executive producer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="aanekoski")
	
@executive_producer.route('/executive-producer-tyopaikat-ylivieska')
def executive_producer_tyopaikat75(page=1):

    job_list = job_obj.get_job("executive producer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="ylivieska")
	
@executive_producer.route('/executive-producer-tyopaikat-kontiolahti')
def executive_producer_tyopaikat76(page=1):

    job_list = job_obj.get_job("executive producer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kontiolahti")
	
@executive_producer.route('/executive-producer-tyopaikat-kankaanpaa')
def executive_producer_tyopaikat77(page=1):

    job_list = job_obj.get_job("executive producer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kankaanpaa")
	
@executive_producer.route('/executive-producer-tyopaikat-ulvila')
def executive_producer_tyopaikat78(page=1):

    job_list = job_obj.get_job("executive producer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="ulvila")
	
@executive_producer.route('/executive-producer-tyopaikat-pieksamaki')
def executive_producer_tyopaikat79(page=1):

    job_list = job_obj.get_job("executive producer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="pieksamaki")
	
@executive_producer.route('/executive-producer-tyopaikat-kiiminki')
def executive_producer_tyopaikat80(page=1):

    job_list = job_obj.get_job("executive producer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kiiminki")
	
@executive_producer.route('/executive-producer-tyopaikat-pargas')
def executive_producer_tyopaikat81(page=1):

    job_list = job_obj.get_job("executive producer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="pargas")
	
@executive_producer.route('/executive-producer-tyopaikat-nurmo')
def executive_producer_tyopaikat82(page=1):

    job_list = job_obj.get_job("executive producer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="nurmo")
	
@executive_producer.route('/executive-producer-tyopaikat-ilmajoki')
def executive_producer_tyopaikat83(page=1):

    job_list = job_obj.get_job("executive producer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="ilmajoki")
	
@executive_producer.route('/executive-producer-tyopaikat-liperi')
def executive_producer_tyopaikat84(page=1):

    job_list = job_obj.get_job("executive producer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="liperi")
	
@executive_producer.route('/executive-producer-tyopaikat-keuruu')
def executive_producer_tyopaikat85(page=1):

    job_list = job_obj.get_job("executive producer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="keuruu")
	
@executive_producer.route('/executive-producer-tyopaikat-leppavirta')
def executive_producer_tyopaikat86(page=1):

    job_list = job_obj.get_job("executive producer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="leppavirta")
	
@executive_producer.route('/executive-producer-tyopaikat-kurikka')
def executive_producer_tyopaikat87(page=1):

    job_list = job_obj.get_job("executive producer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kurikka")
	
@executive_producer.route('/executive-producer-tyopaikat-nivala')
def executive_producer_tyopaikat88(page=1):

    job_list = job_obj.get_job("executive producer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="nivala")
	
@executive_producer.route('/executive-producer-tyopaikat-joutseno')
def executive_producer_tyopaikat89(page=1):

    job_list = job_obj.get_job("executive producer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="joutseno")
	
@executive_producer.route('/executive-producer-tyopaikat-pedersore')
def executive_producer_tyopaikat90(page=1):

    job_list = job_obj.get_job("executive producer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="pedersore")
	
@executive_producer.route('/executive-producer-tyopaikat-sotkamo')
def executive_producer_tyopaikat91(page=1):

    job_list = job_obj.get_job("executive producer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="sotkamo")
	
@executive_producer.route('/executive-producer-tyopaikat-kuhmo')
def executive_producer_tyopaikat92(page=1):

    job_list = job_obj.get_job("executive producer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="kuhmo")
	
@executive_producer.route('/executive-producer-tyopaikat-paimio')
def executive_producer_tyopaikat93(page=1):

    job_list = job_obj.get_job("executive producer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="paimio")
	
@executive_producer.route('/executive-producer-tyopaikat-saarijarvi')
def executive_producer_tyopaikat94(page=1):

    job_list = job_obj.get_job("executive producer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer", location="saarijarvi")
	
@executive_producer.route('/executive-producer-tyopaikat-helsinki')
def executive_producer_tyopaikat95(page=1):

    job_list = job_obj.get_job("executive producer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="executive producer  ", location="helsinki")
	  

