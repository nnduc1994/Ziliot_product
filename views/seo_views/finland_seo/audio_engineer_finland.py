from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

audio_engineer = Blueprint('audio_engineer', __name__)
job_obj = Job()



####################################################################


@audio_engineer.route('/audio-engineer_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "audio-engineer" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-espoo')
def audio_engineer_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("audio engineer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="espoo")

@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-tampere')
def audio_engineer_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("audio engineer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="tampere")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-vantaa')
def audio_engineer_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("audio engineer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="vantaa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-turku')
def audio_engineer_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("audio engineer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="turku")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-oulu')
def audio_engineer_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("audio engineer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="oulu")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-lahti')
def audio_engineer_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("audio engineer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lahti")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kuopio')
def audio_engineer_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("audio engineer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kuopio")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-jyvvaskyla')
def audio_engineer_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("audio engineer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="jyvvaskyla")

@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-pori')
def audio_engineer_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("audio engineer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="pori")

@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-lappeenranta')
def audio_engineer_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("audio engineer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lappeenranta")	
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-vaasa')
def audio_engineer_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("audio engineer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="vaasa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kotka')
def audio_engineer_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("audio engineer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kotka")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-joensuu')
def audio_engineer_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("audio engineer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="joensuu")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-hameenlinna')
def audio_engineer_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("audio engineer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="hameenlinna")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-porvoo')
def audio_engineer_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("audio engineer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="porvoo")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-mikkeli')
def audio_engineer_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("audio engineer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="mikkeli")

@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-hyvinkaa')
def audio_engineer_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("audio engineer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="hyvinkaa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-nurmijarvi')
def audio_engineer_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("audio engineer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="nurmijarvi")

@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-jarvenpaa')
def audio_engineer_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("audio engineer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="jarvenpaa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-rauma')
def audio_engineer_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("audio engineer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="rauma")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-lohja')
def audio_engineer_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("audio engineer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lohja")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-karleby')
def audio_engineer_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("audio engineer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="karleby")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kajaani')
def audio_engineer_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("audio engineer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kajaani")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-rovaniemi')
def audio_engineer_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("audio engineer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="rovaniemi")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-tuusula')
def audio_engineer_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("audio engineer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="tuusula")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kirkkonummi')
def audio_engineer_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("audio engineer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kirkkonummi")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-seinajoki')
def audio_engineer_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("audio engineer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="seinajoki")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kerava')
def audio_engineer_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("audio engineer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kerava")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kouvola')
def audio_engineer_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("audio engineer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kouvola")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-imatra')
def audio_engineer_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("audio engineer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="imatra")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-nokia')
def audio_engineer_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("audio engineer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="nokia")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-savonlinna')
def audio_engineer_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("audio engineer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="savonlinna")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-riihimaki')
def audio_engineer_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("audio engineer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="riihimaki")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-vihti')
def audio_engineer_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("audio engineer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="vihti")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-salo')
def audio_engineer_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("audio engineer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="salo")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kangasala')
def audio_engineer_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("audio engineer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kangasala")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-raisio')
def audio_engineer_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("audio engineer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="raisio")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-karhula')
def audio_engineer_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("audio engineer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="karhula")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kemi')
def audio_engineer_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("audio engineer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kemi")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-iisalmi')
def audio_engineer_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("audio engineer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="iisalmi")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-varkaus')
def audio_engineer_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("audio engineer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="varkaus")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-raahe')
def audio_engineer_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("audio engineer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="raahe")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-ylojarvi')
def audio_engineer_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("audio engineer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="ylojarvi")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-hamina')
def audio_engineer_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("audio engineer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="hamina")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kaarina')
def audio_engineer_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("audio engineer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kaarina")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-tornio')
def audio_engineer_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("audio engineer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="tornio")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-heinola')
def audio_engineer_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("audio engineer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="heinola")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-hollola')
def audio_engineer_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("audio engineer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="hollola")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-valkeakoski')
def audio_engineer_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("audio engineer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="valkeakoski")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-siilinjarvi')
def audio_engineer_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("audio engineer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="siilinjarvi")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kuusankoski')
def audio_engineer_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("audio engineer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kuusankoski")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-sibbo')
def audio_engineer_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("audio engineer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="sibbo")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-jakostad')
def audio_engineer_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("audio engineer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="jakostad")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-lempaala')
def audio_engineer_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("audio engineer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lempaala")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-mantsala')
def audio_engineer_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("audio engineer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="mantsala")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-forssa')
def audio_engineer_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("audio engineer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="forssa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kuusamo')
def audio_engineer_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("audio engineer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kuusamo")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-haukipudas')
def audio_engineer_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("audio engineer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="haukipudas")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-korsholm')
def audio_engineer_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("audio engineer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="korsholm")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-laukaa')
def audio_engineer_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("audio engineer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="laukaa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-anjala')
def audio_engineer_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("audio engineer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="anjala")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-uusikaupunki')
def audio_engineer_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("audio engineer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="uusikaupunki")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-janakkala')
def audio_engineer_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("audio engineer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="janakkala")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-pirkkala')
def audio_engineer_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("audio engineer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="pirkkala")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-lansi-turunmaa')
def audio_engineer_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("audio engineer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lansi-turunmaa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-jamsa')
def audio_engineer_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("audio engineer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="jamsa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-jamsa')
def audio_engineer_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("audio engineer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="jamsa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-vammala')
def audio_engineer_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("audio engineer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="vammala")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-nastola')
def audio_engineer_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("audio engineer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="nastola")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-orimattila')
def audio_engineer_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("audio engineer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="orimattila")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kauhajoki')
def audio_engineer_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("audio engineer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kauhajoki")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-ekenas')
def audio_engineer_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("audio engineer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="ekenas")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kempele')
def audio_engineer_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("audio engineer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kempele")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-lapua')
def audio_engineer_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("audio engineer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lapua")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-lieksa')
def audio_engineer_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("audio engineer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lieksa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-naantali')
def audio_engineer_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("audio engineer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="naantali")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-aanekoski')
def audio_engineer_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("audio engineer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="aanekoski")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-ylivieska')
def audio_engineer_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("audio engineer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="ylivieska")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kontiolahti')
def audio_engineer_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("audio engineer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kontiolahti")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kankaanpaa')
def audio_engineer_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("audio engineer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kankaanpaa")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-ulvila')
def audio_engineer_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("audio engineer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="ulvila")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-pieksamaki')
def audio_engineer_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("audio engineer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="pieksamaki")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kiiminki')
def audio_engineer_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("audio engineer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kiiminki")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-pargas')
def audio_engineer_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("audio engineer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="pargas")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-nurmo')
def audio_engineer_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("audio engineer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="nurmo")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-ilmajoki')
def audio_engineer_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("audio engineer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="ilmajoki")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-liperi')
def audio_engineer_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("audio engineer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="liperi")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-keuruu')
def audio_engineer_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("audio engineer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="keuruu")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-leppavirta')
def audio_engineer_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("audio engineer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="leppavirta")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kurikka')
def audio_engineer_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("audio engineer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kurikka")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-nivala')
def audio_engineer_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("audio engineer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="nivala")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-joutseno')
def audio_engineer_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("audio engineer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="joutseno")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-pedersore')
def audio_engineer_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("audio engineer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="pedersore")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-sotkamo')
def audio_engineer_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("audio engineer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="sotkamo")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-kuhmo')
def audio_engineer_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("audio engineer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kuhmo")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-paimio')
def audio_engineer_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("audio engineer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="paimio")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-saarijarvi')
def audio_engineer_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("audio engineer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="saarijarvi")
	
@audio_engineer.route('/audio-engineer-avoimet-tyopaikat-helsinki')
def audio_engineer_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("audio engineer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="helsinki")


####################################################################


##############################################
@audio_engineer.route('/audio-engineer-jobs-espoo')
def audio_engineer_jobs2(page=1):

    job_list = job_obj.get_job("audio engineer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="espoo")

@audio_engineer.route('/audio-engineer-jobs-tampere')
def audio_engineer_jobs3(page=1):

    job_list = job_obj.get_job("audio engineer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="tampere")
	
@audio_engineer.route('/audio-engineer-jobs-vantaa')
def audio_engineer_jobs4(page=1):

    job_list = job_obj.get_job("audio engineer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="vantaa")
	
@audio_engineer.route('/audio-engineer-jobs-turku')
def audio_engineer_jobs5(page=1):

    job_list = job_obj.get_job("audio engineer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="turku")
	
@audio_engineer.route('/audio-engineer-jobs-oulu')
def audio_engineer_jobs6(page=1):

    job_list = job_obj.get_job("audio engineer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="oulu")
	
@audio_engineer.route('/audio-engineer-jobs-lahti')
def audio_engineer_jobs7(page=1):

    job_list = job_obj.get_job("audio engineer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lahti")
	
@audio_engineer.route('/audio-engineer-jobs-kuopio')
def audio_engineer_jobs8(page=1):

    job_list = job_obj.get_job("audio engineer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kuopio")
	
@audio_engineer.route('/audio-engineer-jobs-jyvvaskyla')
def audio_engineer_jobs9(page=1):

    job_list = job_obj.get_job("audio engineer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="jyvvaskyla")

@audio_engineer.route('/audio-engineer-jobs-pori')
def audio_engineer_jobs10(page=1):

    job_list = job_obj.get_job("audio engineer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="pori")

@audio_engineer.route('/audio-engineer-jobs-lappeenranta')
def audio_engineer_jobs11(page=1):

    job_list = job_obj.get_job("audio engineer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lappeenranta")	
	
@audio_engineer.route('/audio-engineer-jobs-vaasa')
def audio_engineer_jobs12(page=1):

    job_list = job_obj.get_job("audio engineer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="vaasa")
	
@audio_engineer.route('/audio-engineer-jobs-kotka')
def audio_engineer_jobs13(page=1):

    job_list = job_obj.get_job("audio engineer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kotka")
	
@audio_engineer.route('/audio-engineer-jobs-joensuu')
def audio_engineer_jobs14(page=1):

    job_list = job_obj.get_job("audio engineer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="joensuu")
	
@audio_engineer.route('/audio-engineer-jobs-hameenlinna')
def audio_engineer_jobs15(page=1):

    job_list = job_obj.get_job("audio engineer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="hameenlinna")
	
@audio_engineer.route('/audio-engineer-jobs-porvoo')
def audio_engineer_jobs16(page=1):

    job_list = job_obj.get_job("audio engineer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="porvoo")
	
@audio_engineer.route('/audio-engineer-jobs-mikkeli')
def audio_engineer_jobs17(page=1):

    job_list = job_obj.get_job("audio engineer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="mikkeli")

@audio_engineer.route('/audio-engineer-jobs-hyvinkaa')
def audio_engineer_jobs18(page=1):

    job_list = job_obj.get_job("audio engineer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="hyvinkaa")
	
@audio_engineer.route('/audio-engineer-jobs-nurmijarvi')
def audio_engineer_jobs19(page=1):

    job_list = job_obj.get_job("audio engineer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="nurmijarvi")

@audio_engineer.route('/audio-engineer-jobs-jarvenpaa')
def audio_engineer_jobs20(page=1):

    job_list = job_obj.get_job("audio engineer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="jarvenpaa")
	
@audio_engineer.route('/audio-engineer-jobs-rauma')
def audio_engineer_jobs21(page=1):

    job_list = job_obj.get_job("audio engineer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="rauma")
	
@audio_engineer.route('/audio-engineer-jobs-lohja')
def audio_engineer_jobs22(page=1):

    job_list = job_obj.get_job("audio engineer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lohja")
	
@audio_engineer.route('/audio-engineer-jobs-karleby')
def audio_engineer_jobs23(page=1):

    job_list = job_obj.get_job("audio engineer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="karleby")
	
@audio_engineer.route('/audio-engineer-jobs-kajaani')
def audio_engineer_jobs24(page=1):

    job_list = job_obj.get_job("audio engineer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kajaani")
	
@audio_engineer.route('/audio-engineer-jobs-rovaniemi')
def audio_engineer_jobs25(page=1):

    job_list = job_obj.get_job("audio engineer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="rovaniemi")
	
@audio_engineer.route('/audio-engineer-jobs-tuusula')
def audio_engineer_jobs26(page=1):

    job_list = job_obj.get_job("audio engineer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="tuusula")
	
@audio_engineer.route('/audio-engineer-jobs-kirkkonummi')
def audio_engineer_jobs27(page=1):

    job_list = job_obj.get_job("audio engineer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kirkkonummi")
	
@audio_engineer.route('/audio-engineer-jobs-seinajoki')
def audio_engineer_jobs28(page=1):

    job_list = job_obj.get_job("audio engineer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="seinajoki")
	
@audio_engineer.route('/audio-engineer-jobs-kerava')
def audio_engineer_jobs29(page=1):

    job_list = job_obj.get_job("audio engineer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kerava")
	
@audio_engineer.route('/audio-engineer-jobs-kouvola')
def audio_engineer_jobs30(page=1):

    job_list = job_obj.get_job("audio engineer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kouvola")
	
@audio_engineer.route('/audio-engineer-jobs-imatra')
def audio_engineer_jobs31(page=1):

    job_list = job_obj.get_job("audio engineer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="imatra")
	
@audio_engineer.route('/audio-engineer-jobs-nokia')
def audio_engineer_jobs32_1(page=1):

    job_list = job_obj.get_job("audio engineer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="nokia")
	
@audio_engineer.route('/audio-engineer-jobs-savonlinna')
def audio_engineer_jobs32(page=1):

    job_list = job_obj.get_job("audio engineer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="savonlinna")
	
@audio_engineer.route('/audio-engineer-jobs-riihimaki')
def audio_engineer_jobs33(page=1):

    job_list = job_obj.get_job("audio engineer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="riihimaki")
	
@audio_engineer.route('/audio-engineer-jobs-vihti')
def audio_engineer_jobs34(page=1):

    job_list = job_obj.get_job("audio engineer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="vihti")
	
@audio_engineer.route('/audio-engineer-jobs-salo')
def audio_engineer_jobs35(page=1):

    job_list = job_obj.get_job("audio engineer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="salo")
	
@audio_engineer.route('/audio-engineer-jobs-kangasala')
def audio_engineer_jobs36(page=1):

    job_list = job_obj.get_job("audio engineer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kangasala")
	
@audio_engineer.route('/audio-engineer-jobs-raisio')
def audio_engineer_jobs37_1(page=1):

    job_list = job_obj.get_job("audio engineer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="raisio")
	
@audio_engineer.route('/audio-engineer-jobs-karhula')
def audio_engineer_jobs37(page=1):

    job_list = job_obj.get_job("audio engineer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="karhula")
	
@audio_engineer.route('/audio-engineer-jobs-kemi')
def audio_engineer_jobs38(page=1):

    job_list = job_obj.get_job("audio engineer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kemi")
	
@audio_engineer.route('/audio-engineer-jobs-iisalmi')
def audio_engineer_jobs39(page=1):

    job_list = job_obj.get_job("audio engineer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="iisalmi")
	
@audio_engineer.route('/audio-engineer-jobs-varkaus')
def audio_engineer_jobs40(page=1):

    job_list = job_obj.get_job("audio engineer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="varkaus")
	
@audio_engineer.route('/audio-engineer-jobs-raahe')
def audio_engineer_jobs41(page=1):

    job_list = job_obj.get_job("audio engineer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="raahe")
	
@audio_engineer.route('/audio-engineer-jobs-ylojarvi')
def audio_engineer_jobs42_1(page=1):

    job_list = job_obj.get_job("audio engineer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="ylojarvi")
	
@audio_engineer.route('/audio-engineer-jobs-hamina')
def audio_engineer_jobs42(page=1):

    job_list = job_obj.get_job("audio engineer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="hamina")
	
@audio_engineer.route('/audio-engineer-jobs-kaarina')
def audio_engineer_jobs43(page=1):

    job_list = job_obj.get_job("audio engineer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kaarina")
	
@audio_engineer.route('/audio-engineer-jobs-tornio')
def audio_engineer_jobs44(page=1):

    job_list = job_obj.get_job("audio engineer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="tornio")
	
@audio_engineer.route('/audio-engineer-jobs-heinola')
def audio_engineer_jobs45(page=1):

    job_list = job_obj.get_job("audio engineer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="heinola")
	
@audio_engineer.route('/audio-engineer-jobs-hollola')
def audio_engineer_jobs46(page=1):

    job_list = job_obj.get_job("audio engineer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="hollola")
	
@audio_engineer.route('/audio-engineer-jobs-valkeakoski')
def audio_engineer_jobs47(page=1):

    job_list = job_obj.get_job("audio engineer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="valkeakoski")
	
@audio_engineer.route('/audio-engineer-jobs-siilinjarvi')
def audio_engineer_jobs48(page=1):

    job_list = job_obj.get_job("audio engineer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="siilinjarvi")
	
@audio_engineer.route('/audio-engineer-jobs-kuusankoski')
def audio_engineer_jobs49(page=1):

    job_list = job_obj.get_job("audio engineer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kuusankoski")
	
@audio_engineer.route('/audio-engineer-jobs-sibbo')
def audio_engineer_jobs50(page=1):

    job_list = job_obj.get_job("audio engineer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="sibbo")
	
@audio_engineer.route('/audio-engineer-jobs-jakostad')
def audio_engineer_jobs51(page=1):

    job_list = job_obj.get_job("audio engineer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="jakostad")
	
@audio_engineer.route('/audio-engineer-jobs-lempaala')
def audio_engineer_jobs52(page=1):

    job_list = job_obj.get_job("audio engineer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lempaala")
	
@audio_engineer.route('/audio-engineer-jobs-mantsala')
def audio_engineer_jobs52_1(page=1):

    job_list = job_obj.get_job("audio engineer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="mantsala")
	
@audio_engineer.route('/audio-engineer-jobs-forssa')
def audio_engineer_jobs53(page=1):

    job_list = job_obj.get_job("audio engineer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="forssa")
	
@audio_engineer.route('/audio-engineer-jobs-kuusamo')
def audio_engineer_jobs54(page=1):

    job_list = job_obj.get_job("audio engineer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kuusamo")
	
@audio_engineer.route('/audio-engineer-jobs-haukipudas')
def audio_engineer_jobs55(page=1):

    job_list = job_obj.get_job("audio engineer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="haukipudas")
	
@audio_engineer.route('/audio-engineer-jobs-korsholm')
def audio_engineer_jobs56(page=1):

    job_list = job_obj.get_job("audio engineer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="korsholm")
	
@audio_engineer.route('/audio-engineer-jobs-laukaa')
def audio_engineer_jobs57(page=1):

    job_list = job_obj.get_job("audio engineer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="laukaa")
	
@audio_engineer.route('/audio-engineer-jobs-anjala')
def audio_engineer_jobs58(page=1):

    job_list = job_obj.get_job("audio engineer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="anjala")
	
@audio_engineer.route('/audio-engineer-jobs-uusikaupunki')
def audio_engineer_jobs59(page=1):

    job_list = job_obj.get_job("audio engineer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="uusikaupunki")
	
@audio_engineer.route('/audio-engineer-jobs-janakkala')
def audio_engineer_jobs60(page=1):

    job_list = job_obj.get_job("audio engineer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="janakkala")
	
@audio_engineer.route('/audio-engineer-jobs-pirkkala')
def audio_engineer_jobs61(page=1):

    job_list = job_obj.get_job("audio engineer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="pirkkala")
	
@audio_engineer.route('/audio-engineer-jobs-lansi-turunmaa')
def audio_engineer_jobs62(page=1):

    job_list = job_obj.get_job("audio engineer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lansi-turunmaa")
	
@audio_engineer.route('/audio-engineer-jobs-jamsa')
def audio_engineer_jobs63(page=1):

    job_list = job_obj.get_job("audio engineer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="jamsa")
	
@audio_engineer.route('/audio-engineer-jobs-jamsa')
def audio_engineer_jobs64(page=1):

    job_list = job_obj.get_job("audio engineer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="jamsa")
	
@audio_engineer.route('/audio-engineer-jobs-vammala')
def audio_engineer_jobs65(page=1):

    job_list = job_obj.get_job("audio engineer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="vammala")
	
@audio_engineer.route('/audio-engineer-jobs-nastola')
def audio_engineer_jobs66(page=1):

    job_list = job_obj.get_job("audio engineer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="nastola")
	
@audio_engineer.route('/audio-engineer-jobs-orimattila')
def audio_engineer_jobs67(page=1):

    job_list = job_obj.get_job("audio engineer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="orimattila")
	
@audio_engineer.route('/audio-engineer-jobs-kauhajoki')
def audio_engineer_jobs68(page=1):

    job_list = job_obj.get_job("audio engineer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kauhajoki")
	
@audio_engineer.route('/audio-engineer-jobs-ekenas')
def audio_engineer_jobs69(page=1):

    job_list = job_obj.get_job("audio engineer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="ekenas")
	
@audio_engineer.route('/audio-engineer-jobs-kempele')
def audio_engineer_jobs70(page=1):

    job_list = job_obj.get_job("audio engineer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kempele")
	
@audio_engineer.route('/audio-engineer-jobs-lapua')
def audio_engineer_jobs71(page=1):

    job_list = job_obj.get_job("audio engineer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lapua")
	
@audio_engineer.route('/audio-engineer-jobs-lieksa')
def audio_engineer_jobs72(page=1):

    job_list = job_obj.get_job("audio engineer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="lieksa")
	
@audio_engineer.route('/audio-engineer-jobs-naantali')
def audio_engineer_jobs73(page=1):

    job_list = job_obj.get_job("audio engineer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="naantali")
	
@audio_engineer.route('/audio-engineer-jobs-aanekoski')
def audio_engineer_jobs74(page=1):

    job_list = job_obj.get_job("audio engineer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="aanekoski")
	
@audio_engineer.route('/audio-engineer-jobs-ylivieska')
def audio_engineer_jobs75(page=1):

    job_list = job_obj.get_job("audio engineer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="ylivieska")
	
@audio_engineer.route('/audio-engineer-jobs-kontiolahti')
def audio_engineer_jobs76(page=1):

    job_list = job_obj.get_job("audio engineer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kontiolahti")
	
@audio_engineer.route('/audio-engineer-jobs-kankaanpaa')
def audio_engineer_jobs77(page=1):

    job_list = job_obj.get_job("audio engineer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kankaanpaa")
	
@audio_engineer.route('/audio-engineer-jobs-ulvila')
def audio_engineer_jobs78(page=1):

    job_list = job_obj.get_job("audio engineer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="ulvila")
	
@audio_engineer.route('/audio-engineer-jobs-pieksamaki')
def audio_engineer_jobs79(page=1):

    job_list = job_obj.get_job("audio engineer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="pieksamaki")
	
@audio_engineer.route('/audio-engineer-jobs-kiiminki')
def audio_engineer_jobs80(page=1):

    job_list = job_obj.get_job("audio engineer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kiiminki")
	
@audio_engineer.route('/audio-engineer-jobs-pargas')
def audio_engineer_jobs81(page=1):

    job_list = job_obj.get_job("audio engineer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="pargas")
	
@audio_engineer.route('/audio-engineer-jobs-nurmo')
def audio_engineer_jobs82(page=1):

    job_list = job_obj.get_job("audio engineer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="nurmo")
	
@audio_engineer.route('/audio-engineer-jobs-ilmajoki')
def audio_engineer_jobs83(page=1):

    job_list = job_obj.get_job("audio engineer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="ilmajoki")
	
@audio_engineer.route('/audio-engineer-jobs-liperi')
def audio_engineer_jobs84(page=1):

    job_list = job_obj.get_job("audio engineer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="liperi")
	
@audio_engineer.route('/audio-engineer-jobs-keuruu')
def audio_engineer_jobs85(page=1):

    job_list = job_obj.get_job("audio engineer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="keuruu")
	
@audio_engineer.route('/audio-engineer-jobs-leppavirta')
def audio_engineer_jobs86(page=1):

    job_list = job_obj.get_job("audio engineer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="leppavirta")
	
@audio_engineer.route('/audio-engineer-jobs-kurikka')
def audio_engineer_jobs87(page=1):

    job_list = job_obj.get_job("audio engineer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kurikka")
	
@audio_engineer.route('/audio-engineer-jobs-nivala')
def audio_engineer_jobs88(page=1):

    job_list = job_obj.get_job("audio engineer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="nivala")
	
@audio_engineer.route('/audio-engineer-jobs-joutseno')
def audio_engineer_jobs89(page=1):

    job_list = job_obj.get_job("audio engineer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="joutseno")
	
@audio_engineer.route('/audio-engineer-jobs-pedersore')
def audio_engineer_jobs90(page=1):

    job_list = job_obj.get_job("audio engineer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="pedersore")
	
@audio_engineer.route('/audio-engineer-jobs-sotkamo')
def audio_engineer_jobs91(page=1):

    job_list = job_obj.get_job("audio engineer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="sotkamo")
	
@audio_engineer.route('/audio-engineer-jobs-kuhmo')
def audio_engineer_jobs92(page=1):

    job_list = job_obj.get_job("audio engineer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="kuhmo")
	
@audio_engineer.route('/audio-engineer-jobs-paimio')
def audio_engineer_jobs93(page=1):

    job_list = job_obj.get_job("audio engineer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="paimio")
	
@audio_engineer.route('/audio-engineer-jobs-saarijarvi')
def audio_engineer_jobs94(page=1):

    job_list = job_obj.get_job("audio engineer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="saarijarvi")
	
@audio_engineer.route('/audio-engineer-jobs-helsinki')
def audio_engineer_jobs95(page=1):

    job_list = job_obj.get_job("audio engineer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer ", location="helsinki")


####################################################################


##############################################
@audio_engineer.route('/audio-engineer-tyopaikat-espoo')
def audio_engineer_tyopaikat2(page=1):

    job_list = job_obj.get_job("audio engineer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="espoo")

@audio_engineer.route('/audio-engineer-tyopaikat-tampere')
def audio_engineer_tyopaikat3(page=1):

    job_list = job_obj.get_job("audio engineer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="tampere")
	
@audio_engineer.route('/audio-engineer-tyopaikat-vantaa')
def audio_engineer_tyopaikat4(page=1):

    job_list = job_obj.get_job("audio engineer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="vantaa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-turku')
def audio_engineer_tyopaikat5(page=1):

    job_list = job_obj.get_job("audio engineer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="turku")
	
@audio_engineer.route('/audio-engineer-tyopaikat-oulu')
def audio_engineer_tyopaikat6(page=1):

    job_list = job_obj.get_job("audio engineer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="oulu")
	
@audio_engineer.route('/audio-engineer-tyopaikat-lahti')
def audio_engineer_tyopaikat7(page=1):

    job_list = job_obj.get_job("audio engineer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="lahti")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kuopio')
def audio_engineer_tyopaikat8(page=1):

    job_list = job_obj.get_job("audio engineer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kuopio")
	
@audio_engineer.route('/audio-engineer-tyopaikat-jyvvaskyla')
def audio_engineer_tyopaikat9(page=1):

    job_list = job_obj.get_job("audio engineer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="jyvvaskyla")

@audio_engineer.route('/audio-engineer-tyopaikat-pori')
def audio_engineer_tyopaikat10(page=1):

    job_list = job_obj.get_job("audio engineer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="pori")

@audio_engineer.route('/audio-engineer-tyopaikat-lappeenranta')
def audio_engineer_tyopaikat11(page=1):

    job_list = job_obj.get_job("audio engineer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="lappeenranta")	
	
@audio_engineer.route('/audio-engineer-tyopaikat-vaasa')
def audio_engineer_tyopaikat12(page=1):

    job_list = job_obj.get_job("audio engineer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="vaasa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kotka')
def audio_engineer_tyopaikat13(page=1):

    job_list = job_obj.get_job("audio engineer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kotka")
	
@audio_engineer.route('/audio-engineer-tyopaikat-joensuu')
def audio_engineer_tyopaikat14(page=1):

    job_list = job_obj.get_job("audio engineer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="joensuu")
	
@audio_engineer.route('/audio-engineer-tyopaikat-hameenlinna')
def audio_engineer_tyopaikat15(page=1):

    job_list = job_obj.get_job("audio engineer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="hameenlinna")
	
@audio_engineer.route('/audio-engineer-tyopaikat-porvoo')
def audio_engineer_tyopaikat16(page=1):

    job_list = job_obj.get_job("audio engineer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="porvoo")
	
@audio_engineer.route('/audio-engineer-tyopaikat-mikkeli')
def audio_engineer_tyopaikat17(page=1):

    job_list = job_obj.get_job("audio engineer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="mikkeli")

@audio_engineer.route('/audio-engineer-tyopaikat-hyvinkaa')
def audio_engineer_tyopaikat18(page=1):

    job_list = job_obj.get_job("audio engineer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="hyvinkaa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-nurmijarvi')
def audio_engineer_tyopaikat19(page=1):

    job_list = job_obj.get_job("audio engineer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="nurmijarvi")

@audio_engineer.route('/audio-engineer-tyopaikat-jarvenpaa')
def audio_engineer_tyopaikat20(page=1):

    job_list = job_obj.get_job("audio engineer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="jarvenpaa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-rauma')
def audio_engineer_tyopaikat21(page=1):

    job_list = job_obj.get_job("audio engineer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="rauma")
	
@audio_engineer.route('/audio-engineer-tyopaikat-lohja')
def audio_engineer_tyopaikat22(page=1):

    job_list = job_obj.get_job("audio engineer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="lohja")
	
@audio_engineer.route('/audio-engineer-tyopaikat-karleby')
def audio_engineer_tyopaikat23(page=1):

    job_list = job_obj.get_job("audio engineer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="karleby")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kajaani')
def audio_engineer_tyopaikat24(page=1):

    job_list = job_obj.get_job("audio engineer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kajaani")
	
@audio_engineer.route('/audio-engineer-tyopaikat-rovaniemi')
def audio_engineer_tyopaikat25(page=1):

    job_list = job_obj.get_job("audio engineer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="rovaniemi")
	
@audio_engineer.route('/audio-engineer-tyopaikat-tuusula')
def audio_engineer_tyopaikat26(page=1):

    job_list = job_obj.get_job("audio engineer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="tuusula")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kirkkonummi')
def audio_engineer_tyopaikat27(page=1):

    job_list = job_obj.get_job("audio engineer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kirkkonummi")
	
@audio_engineer.route('/audio-engineer-tyopaikat-seinajoki')
def audio_engineer_tyopaikat28(page=1):

    job_list = job_obj.get_job("audio engineer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="seinajoki")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kerava')
def audio_engineer_tyopaikat29(page=1):

    job_list = job_obj.get_job("audio engineer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kerava")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kouvola')
def audio_engineer_tyopaikat30(page=1):

    job_list = job_obj.get_job("audio engineer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kouvola")
	
@audio_engineer.route('/audio-engineer-tyopaikat-imatra')
def audio_engineer_tyopaikat31(page=1):

    job_list = job_obj.get_job("audio engineer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="imatra")
	
@audio_engineer.route('/audio-engineer-tyopaikat-nokia')
def audio_engineer_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("audio engineer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="nokia")
	
@audio_engineer.route('/audio-engineer-tyopaikat-savonlinna')
def audio_engineer_tyopaikat32(page=1):

    job_list = job_obj.get_job("audio engineer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="savonlinna")
	
@audio_engineer.route('/audio-engineer-tyopaikat-riihimaki')
def audio_engineer_tyopaikat33(page=1):

    job_list = job_obj.get_job("audio engineer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="riihimaki")
	
@audio_engineer.route('/audio-engineer-tyopaikat-vihti')
def audio_engineer_tyopaikat34(page=1):

    job_list = job_obj.get_job("audio engineer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="vihti")
	
@audio_engineer.route('/audio-engineer-tyopaikat-salo')
def audio_engineer_tyopaikat35(page=1):

    job_list = job_obj.get_job("audio engineer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="salo")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kangasala')
def audio_engineer_tyopaikat36(page=1):

    job_list = job_obj.get_job("audio engineer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kangasala")
	
@audio_engineer.route('/audio-engineer-tyopaikat-raisio')
def audio_engineer_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("audio engineer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="raisio")
	
@audio_engineer.route('/audio-engineer-tyopaikat-karhula')
def audio_engineer_tyopaikat37(page=1):

    job_list = job_obj.get_job("audio engineer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="karhula")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kemi')
def audio_engineer_tyopaikat38(page=1):

    job_list = job_obj.get_job("audio engineer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kemi")
	
@audio_engineer.route('/audio-engineer-tyopaikat-iisalmi')
def audio_engineer_tyopaikat39(page=1):

    job_list = job_obj.get_job("audio engineer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="iisalmi")
	
@audio_engineer.route('/audio-engineer-tyopaikat-varkaus')
def audio_engineer_tyopaikat40(page=1):

    job_list = job_obj.get_job("audio engineer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="varkaus")
	
@audio_engineer.route('/audio-engineer-tyopaikat-raahe')
def audio_engineer_tyopaikat41(page=1):

    job_list = job_obj.get_job("audio engineer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="raahe")
	
@audio_engineer.route('/audio-engineer-tyopaikat-ylojarvi')
def audio_engineer_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("audio engineer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="ylojarvi")
	
@audio_engineer.route('/audio-engineer-tyopaikat-hamina')
def audio_engineer_tyopaikat42(page=1):

    job_list = job_obj.get_job("audio engineer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="hamina")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kaarina')
def audio_engineer_tyopaikat43(page=1):

    job_list = job_obj.get_job("audio engineer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kaarina")
	
@audio_engineer.route('/audio-engineer-tyopaikat-tornio')
def audio_engineer_tyopaikat44(page=1):

    job_list = job_obj.get_job("audio engineer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="tornio")
	
@audio_engineer.route('/audio-engineer-tyopaikat-heinola')
def audio_engineer_tyopaikat45(page=1):

    job_list = job_obj.get_job("audio engineer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="heinola")
	
@audio_engineer.route('/audio-engineer-tyopaikat-hollola')
def audio_engineer_tyopaikat46(page=1):

    job_list = job_obj.get_job("audio engineer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="hollola")
	
@audio_engineer.route('/audio-engineer-tyopaikat-valkeakoski')
def audio_engineer_tyopaikat47(page=1):

    job_list = job_obj.get_job("audio engineer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="valkeakoski")
	
@audio_engineer.route('/audio-engineer-tyopaikat-siilinjarvi')
def audio_engineer_tyopaikat48(page=1):

    job_list = job_obj.get_job("audio engineer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="siilinjarvi")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kuusankoski')
def audio_engineer_tyopaikat49(page=1):

    job_list = job_obj.get_job("audio engineer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kuusankoski")
	
@audio_engineer.route('/audio-engineer-tyopaikat-sibbo')
def audio_engineer_tyopaikat50(page=1):

    job_list = job_obj.get_job("audio engineer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="sibbo")
	
@audio_engineer.route('/audio-engineer-tyopaikat-jakostad')
def audio_engineer_tyopaikat51(page=1):

    job_list = job_obj.get_job("audio engineer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="jakostad")
	
@audio_engineer.route('/audio-engineer-tyopaikat-lempaala')
def audio_engineer_tyopaikat52(page=1):

    job_list = job_obj.get_job("audio engineer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="lempaala")
	
@audio_engineer.route('/audio-engineer-tyopaikat-mantsala')
def audio_engineer_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("audio engineer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="mantsala")
	
@audio_engineer.route('/audio-engineer-tyopaikat-forssa')
def audio_engineer_tyopaikat53(page=1):

    job_list = job_obj.get_job("audio engineer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="forssa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kuusamo')
def audio_engineer_tyopaikat54(page=1):

    job_list = job_obj.get_job("audio engineer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kuusamo")
	
@audio_engineer.route('/audio-engineer-tyopaikat-haukipudas')
def audio_engineer_tyopaikat55(page=1):

    job_list = job_obj.get_job("audio engineer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="haukipudas")
	
@audio_engineer.route('/audio-engineer-tyopaikat-korsholm')
def audio_engineer_tyopaikat56(page=1):

    job_list = job_obj.get_job("audio engineer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="korsholm")
	
@audio_engineer.route('/audio-engineer-tyopaikat-laukaa')
def audio_engineer_tyopaikat57(page=1):

    job_list = job_obj.get_job("audio engineer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="laukaa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-anjala')
def audio_engineer_tyopaikat58(page=1):

    job_list = job_obj.get_job("audio engineer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="anjala")
	
@audio_engineer.route('/audio-engineer-tyopaikat-uusikaupunki')
def audio_engineer_tyopaikat59(page=1):

    job_list = job_obj.get_job("audio engineer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="uusikaupunki")
	
@audio_engineer.route('/audio-engineer-tyopaikat-janakkala')
def audio_engineer_tyopaikat60(page=1):

    job_list = job_obj.get_job("audio engineer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="janakkala")
	
@audio_engineer.route('/audio-engineer-tyopaikat-pirkkala')
def audio_engineer_tyopaikat61(page=1):

    job_list = job_obj.get_job("audio engineer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="pirkkala")
	
@audio_engineer.route('/audio-engineer-tyopaikat-lansi-turunmaa')
def audio_engineer_tyopaikat62(page=1):

    job_list = job_obj.get_job("audio engineer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="lansi-turunmaa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-jamsa')
def audio_engineer_tyopaikat63(page=1):

    job_list = job_obj.get_job("audio engineer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="jamsa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-jamsa')
def audio_engineer_tyopaikat64(page=1):

    job_list = job_obj.get_job("audio engineer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="jamsa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-vammala')
def audio_engineer_tyopaikat65(page=1):

    job_list = job_obj.get_job("audio engineer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="vammala")
	
@audio_engineer.route('/audio-engineer-tyopaikat-nastola')
def audio_engineer_tyopaikat66(page=1):

    job_list = job_obj.get_job("audio engineer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="nastola")
	
@audio_engineer.route('/audio-engineer-tyopaikat-orimattila')
def audio_engineer_tyopaikat67(page=1):

    job_list = job_obj.get_job("audio engineer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="orimattila")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kauhajoki')
def audio_engineer_tyopaikat68(page=1):

    job_list = job_obj.get_job("audio engineer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kauhajoki")
	
@audio_engineer.route('/audio-engineer-tyopaikat-ekenas')
def audio_engineer_tyopaikat69(page=1):

    job_list = job_obj.get_job("audio engineer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="ekenas")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kempele')
def audio_engineer_tyopaikat70(page=1):

    job_list = job_obj.get_job("audio engineer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kempele")
	
@audio_engineer.route('/audio-engineer-tyopaikat-lapua')
def audio_engineer_tyopaikat71(page=1):

    job_list = job_obj.get_job("audio engineer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="lapua")
	
@audio_engineer.route('/audio-engineer-tyopaikat-lieksa')
def audio_engineer_tyopaikat72(page=1):

    job_list = job_obj.get_job("audio engineer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="lieksa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-naantali')
def audio_engineer_tyopaikat73(page=1):

    job_list = job_obj.get_job("audio engineer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="naantali")
	
@audio_engineer.route('/audio-engineer-tyopaikat-aanekoski')
def audio_engineer_tyopaikat74(page=1):

    job_list = job_obj.get_job("audio engineer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="aanekoski")
	
@audio_engineer.route('/audio-engineer-tyopaikat-ylivieska')
def audio_engineer_tyopaikat75(page=1):

    job_list = job_obj.get_job("audio engineer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="ylivieska")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kontiolahti')
def audio_engineer_tyopaikat76(page=1):

    job_list = job_obj.get_job("audio engineer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kontiolahti")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kankaanpaa')
def audio_engineer_tyopaikat77(page=1):

    job_list = job_obj.get_job("audio engineer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kankaanpaa")
	
@audio_engineer.route('/audio-engineer-tyopaikat-ulvila')
def audio_engineer_tyopaikat78(page=1):

    job_list = job_obj.get_job("audio engineer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="ulvila")
	
@audio_engineer.route('/audio-engineer-tyopaikat-pieksamaki')
def audio_engineer_tyopaikat79(page=1):

    job_list = job_obj.get_job("audio engineer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="pieksamaki")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kiiminki')
def audio_engineer_tyopaikat80(page=1):

    job_list = job_obj.get_job("audio engineer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kiiminki")
	
@audio_engineer.route('/audio-engineer-tyopaikat-pargas')
def audio_engineer_tyopaikat81(page=1):

    job_list = job_obj.get_job("audio engineer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="pargas")
	
@audio_engineer.route('/audio-engineer-tyopaikat-nurmo')
def audio_engineer_tyopaikat82(page=1):

    job_list = job_obj.get_job("audio engineer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="nurmo")
	
@audio_engineer.route('/audio-engineer-tyopaikat-ilmajoki')
def audio_engineer_tyopaikat83(page=1):

    job_list = job_obj.get_job("audio engineer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="ilmajoki")
	
@audio_engineer.route('/audio-engineer-tyopaikat-liperi')
def audio_engineer_tyopaikat84(page=1):

    job_list = job_obj.get_job("audio engineer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="liperi")
	
@audio_engineer.route('/audio-engineer-tyopaikat-keuruu')
def audio_engineer_tyopaikat85(page=1):

    job_list = job_obj.get_job("audio engineer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="keuruu")
	
@audio_engineer.route('/audio-engineer-tyopaikat-leppavirta')
def audio_engineer_tyopaikat86(page=1):

    job_list = job_obj.get_job("audio engineer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="leppavirta")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kurikka')
def audio_engineer_tyopaikat87(page=1):

    job_list = job_obj.get_job("audio engineer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kurikka")
	
@audio_engineer.route('/audio-engineer-tyopaikat-nivala')
def audio_engineer_tyopaikat88(page=1):

    job_list = job_obj.get_job("audio engineer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="nivala")
	
@audio_engineer.route('/audio-engineer-tyopaikat-joutseno')
def audio_engineer_tyopaikat89(page=1):

    job_list = job_obj.get_job("audio engineer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="joutseno")
	
@audio_engineer.route('/audio-engineer-tyopaikat-pedersore')
def audio_engineer_tyopaikat90(page=1):

    job_list = job_obj.get_job("audio engineer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="pedersore")
	
@audio_engineer.route('/audio-engineer-tyopaikat-sotkamo')
def audio_engineer_tyopaikat91(page=1):

    job_list = job_obj.get_job("audio engineer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="sotkamo")
	
@audio_engineer.route('/audio-engineer-tyopaikat-kuhmo')
def audio_engineer_tyopaikat92(page=1):

    job_list = job_obj.get_job("audio engineer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="kuhmo")
	
@audio_engineer.route('/audio-engineer-tyopaikat-paimio')
def audio_engineer_tyopaikat93(page=1):

    job_list = job_obj.get_job("audio engineer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="paimio")
	
@audio_engineer.route('/audio-engineer-tyopaikat-saarijarvi')
def audio_engineer_tyopaikat94(page=1):

    job_list = job_obj.get_job("audio engineer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer", location="saarijarvi")
	
@audio_engineer.route('/audio-engineer-tyopaikat-helsinki')
def audio_engineer_tyopaikat95(page=1):

    job_list = job_obj.get_job("audio engineer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="audio engineer  ", location="helsinki")
	  

