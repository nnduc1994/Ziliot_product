from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

animator = Blueprint('animator', __name__)
job_obj = Job()



####################################################################


@animator.route('/animator_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "animator" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@animator.route('/animator-avoimet-tyopaikat-espoo')
def animator_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("animator ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="espoo")

@animator.route('/animator-avoimet-tyopaikat-tampere')
def animator_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("animator ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="tampere")
	
@animator.route('/animator-avoimet-tyopaikat-vantaa')
def animator_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("animator ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vantaa")
	
@animator.route('/animator-avoimet-tyopaikat-turku')
def animator_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("animator ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="turku")
	
@animator.route('/animator-avoimet-tyopaikat-oulu')
def animator_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("animator ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="oulu")
	
@animator.route('/animator-avoimet-tyopaikat-lahti')
def animator_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("animator ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lahti")
	
@animator.route('/animator-avoimet-tyopaikat-kuopio')
def animator_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("animator ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuopio")
	
@animator.route('/animator-avoimet-tyopaikat-jyvvaskyla')
def animator_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("animator ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jyvvaskyla")

@animator.route('/animator-avoimet-tyopaikat-pori')
def animator_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("animator ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pori")

@animator.route('/animator-avoimet-tyopaikat-lappeenranta')
def animator_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("animator ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lappeenranta")	
	
@animator.route('/animator-avoimet-tyopaikat-vaasa')
def animator_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("animator ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vaasa")
	
@animator.route('/animator-avoimet-tyopaikat-kotka')
def animator_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("animator ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kotka")
	
@animator.route('/animator-avoimet-tyopaikat-joensuu')
def animator_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("animator ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="joensuu")
	
@animator.route('/animator-avoimet-tyopaikat-hameenlinna')
def animator_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("animator ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hameenlinna")
	
@animator.route('/animator-avoimet-tyopaikat-porvoo')
def animator_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("animator ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="porvoo")
	
@animator.route('/animator-avoimet-tyopaikat-mikkeli')
def animator_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("animator ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="mikkeli")

@animator.route('/animator-avoimet-tyopaikat-hyvinkaa')
def animator_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("animator ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hyvinkaa")
	
@animator.route('/animator-avoimet-tyopaikat-nurmijarvi')
def animator_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("animator ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nurmijarvi")

@animator.route('/animator-avoimet-tyopaikat-jarvenpaa')
def animator_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("animator ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jarvenpaa")
	
@animator.route('/animator-avoimet-tyopaikat-rauma')
def animator_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("animator ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="rauma")
	
@animator.route('/animator-avoimet-tyopaikat-lohja')
def animator_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("animator ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lohja")
	
@animator.route('/animator-avoimet-tyopaikat-karleby')
def animator_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("animator ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="karleby")
	
@animator.route('/animator-avoimet-tyopaikat-kajaani')
def animator_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("animator ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kajaani")
	
@animator.route('/animator-avoimet-tyopaikat-rovaniemi')
def animator_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("animator ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="rovaniemi")
	
@animator.route('/animator-avoimet-tyopaikat-tuusula')
def animator_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("animator ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="tuusula")
	
@animator.route('/animator-avoimet-tyopaikat-kirkkonummi')
def animator_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("animator ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kirkkonummi")
	
@animator.route('/animator-avoimet-tyopaikat-seinajoki')
def animator_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("animator ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="seinajoki")
	
@animator.route('/animator-avoimet-tyopaikat-kerava')
def animator_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("animator ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kerava")
	
@animator.route('/animator-avoimet-tyopaikat-kouvola')
def animator_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("animator ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kouvola")
	
@animator.route('/animator-avoimet-tyopaikat-imatra')
def animator_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("animator ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="imatra")
	
@animator.route('/animator-avoimet-tyopaikat-nokia')
def animator_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("animator ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nokia")
	
@animator.route('/animator-avoimet-tyopaikat-savonlinna')
def animator_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("animator ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="savonlinna")
	
@animator.route('/animator-avoimet-tyopaikat-riihimaki')
def animator_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("animator ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="riihimaki")
	
@animator.route('/animator-avoimet-tyopaikat-vihti')
def animator_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("animator ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vihti")
	
@animator.route('/animator-avoimet-tyopaikat-salo')
def animator_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("animator ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="salo")
	
@animator.route('/animator-avoimet-tyopaikat-kangasala')
def animator_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("animator ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kangasala")
	
@animator.route('/animator-avoimet-tyopaikat-raisio')
def animator_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("animator ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="raisio")
	
@animator.route('/animator-avoimet-tyopaikat-karhula')
def animator_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("animator ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="karhula")
	
@animator.route('/animator-avoimet-tyopaikat-kemi')
def animator_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("animator ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kemi")
	
@animator.route('/animator-avoimet-tyopaikat-iisalmi')
def animator_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("animator ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="iisalmi")
	
@animator.route('/animator-avoimet-tyopaikat-varkaus')
def animator_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("animator ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="varkaus")
	
@animator.route('/animator-avoimet-tyopaikat-raahe')
def animator_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("animator ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="raahe")
	
@animator.route('/animator-avoimet-tyopaikat-ylojarvi')
def animator_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("animator ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ylojarvi")
	
@animator.route('/animator-avoimet-tyopaikat-hamina')
def animator_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("animator ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hamina")
	
@animator.route('/animator-avoimet-tyopaikat-kaarina')
def animator_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("animator ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kaarina")
	
@animator.route('/animator-avoimet-tyopaikat-tornio')
def animator_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("animator ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="tornio")
	
@animator.route('/animator-avoimet-tyopaikat-heinola')
def animator_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("animator ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="heinola")
	
@animator.route('/animator-avoimet-tyopaikat-hollola')
def animator_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("animator ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hollola")
	
@animator.route('/animator-avoimet-tyopaikat-valkeakoski')
def animator_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("animator ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="valkeakoski")
	
@animator.route('/animator-avoimet-tyopaikat-siilinjarvi')
def animator_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("animator ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="siilinjarvi")
	
@animator.route('/animator-avoimet-tyopaikat-kuusankoski')
def animator_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("animator ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuusankoski")
	
@animator.route('/animator-avoimet-tyopaikat-sibbo')
def animator_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("animator ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="sibbo")
	
@animator.route('/animator-avoimet-tyopaikat-jakostad')
def animator_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("animator ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jakostad")
	
@animator.route('/animator-avoimet-tyopaikat-lempaala')
def animator_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("animator ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lempaala")
	
@animator.route('/animator-avoimet-tyopaikat-mantsala')
def animator_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("animator ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="mantsala")
	
@animator.route('/animator-avoimet-tyopaikat-forssa')
def animator_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("animator ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="forssa")
	
@animator.route('/animator-avoimet-tyopaikat-kuusamo')
def animator_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("animator ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuusamo")
	
@animator.route('/animator-avoimet-tyopaikat-haukipudas')
def animator_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("animator ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="haukipudas")
	
@animator.route('/animator-avoimet-tyopaikat-korsholm')
def animator_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("animator ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="korsholm")
	
@animator.route('/animator-avoimet-tyopaikat-laukaa')
def animator_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("animator ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="laukaa")
	
@animator.route('/animator-avoimet-tyopaikat-anjala')
def animator_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("animator ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="anjala")
	
@animator.route('/animator-avoimet-tyopaikat-uusikaupunki')
def animator_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("animator ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="uusikaupunki")
	
@animator.route('/animator-avoimet-tyopaikat-janakkala')
def animator_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("animator ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="janakkala")
	
@animator.route('/animator-avoimet-tyopaikat-pirkkala')
def animator_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("animator ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pirkkala")
	
@animator.route('/animator-avoimet-tyopaikat-lansi-turunmaa')
def animator_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("animator ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lansi-turunmaa")
	
@animator.route('/animator-avoimet-tyopaikat-jamsa')
def animator_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("animator ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jamsa")
	
@animator.route('/animator-avoimet-tyopaikat-jamsa')
def animator_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("animator ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jamsa")
	
@animator.route('/animator-avoimet-tyopaikat-vammala')
def animator_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("animator ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vammala")
	
@animator.route('/animator-avoimet-tyopaikat-nastola')
def animator_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("animator ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nastola")
	
@animator.route('/animator-avoimet-tyopaikat-orimattila')
def animator_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("animator ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="orimattila")
	
@animator.route('/animator-avoimet-tyopaikat-kauhajoki')
def animator_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("animator ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kauhajoki")
	
@animator.route('/animator-avoimet-tyopaikat-ekenas')
def animator_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("animator ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ekenas")
	
@animator.route('/animator-avoimet-tyopaikat-kempele')
def animator_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("animator ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kempele")
	
@animator.route('/animator-avoimet-tyopaikat-lapua')
def animator_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("animator ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lapua")
	
@animator.route('/animator-avoimet-tyopaikat-lieksa')
def animator_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("animator ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lieksa")
	
@animator.route('/animator-avoimet-tyopaikat-naantali')
def animator_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("animator ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="naantali")
	
@animator.route('/animator-avoimet-tyopaikat-aanekoski')
def animator_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("animator ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="aanekoski")
	
@animator.route('/animator-avoimet-tyopaikat-ylivieska')
def animator_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("animator ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ylivieska")
	
@animator.route('/animator-avoimet-tyopaikat-kontiolahti')
def animator_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("animator ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kontiolahti")
	
@animator.route('/animator-avoimet-tyopaikat-kankaanpaa')
def animator_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("animator ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kankaanpaa")
	
@animator.route('/animator-avoimet-tyopaikat-ulvila')
def animator_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("animator ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ulvila")
	
@animator.route('/animator-avoimet-tyopaikat-pieksamaki')
def animator_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("animator ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pieksamaki")
	
@animator.route('/animator-avoimet-tyopaikat-kiiminki')
def animator_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("animator ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kiiminki")
	
@animator.route('/animator-avoimet-tyopaikat-pargas')
def animator_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("animator ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pargas")
	
@animator.route('/animator-avoimet-tyopaikat-nurmo')
def animator_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("animator ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nurmo")
	
@animator.route('/animator-avoimet-tyopaikat-ilmajoki')
def animator_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("animator ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ilmajoki")
	
@animator.route('/animator-avoimet-tyopaikat-liperi')
def animator_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("animator ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="liperi")
	
@animator.route('/animator-avoimet-tyopaikat-keuruu')
def animator_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("animator ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="keuruu")
	
@animator.route('/animator-avoimet-tyopaikat-leppavirta')
def animator_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("animator ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="leppavirta")
	
@animator.route('/animator-avoimet-tyopaikat-kurikka')
def animator_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("animator ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kurikka")
	
@animator.route('/animator-avoimet-tyopaikat-nivala')
def animator_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("animator ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nivala")
	
@animator.route('/animator-avoimet-tyopaikat-joutseno')
def animator_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("animator ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="joutseno")
	
@animator.route('/animator-avoimet-tyopaikat-pedersore')
def animator_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("animator ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pedersore")
	
@animator.route('/animator-avoimet-tyopaikat-sotkamo')
def animator_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("animator ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="sotkamo")
	
@animator.route('/animator-avoimet-tyopaikat-kuhmo')
def animator_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("animator ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuhmo")
	
@animator.route('/animator-avoimet-tyopaikat-paimio')
def animator_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("animator ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="paimio")
	
@animator.route('/animator-avoimet-tyopaikat-saarijarvi')
def animator_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("animator ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="saarijarvi")
	
@animator.route('/animator-avoimet-tyopaikat-helsinki')
def animator_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("animator ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="helsinki")


####################################################################


##############################################
@animator.route('/animator-jobs-espoo')
def animator_jobs2(page=1):

    job_list = job_obj.get_job("animator ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="espoo")

@animator.route('/animator-jobs-tampere')
def animator_jobs3(page=1):

    job_list = job_obj.get_job("animator ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="tampere")
	
@animator.route('/animator-jobs-vantaa')
def animator_jobs4(page=1):

    job_list = job_obj.get_job("animator ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vantaa")
	
@animator.route('/animator-jobs-turku')
def animator_jobs5(page=1):

    job_list = job_obj.get_job("animator ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="turku")
	
@animator.route('/animator-jobs-oulu')
def animator_jobs6(page=1):

    job_list = job_obj.get_job("animator ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="oulu")
	
@animator.route('/animator-jobs-lahti')
def animator_jobs7(page=1):

    job_list = job_obj.get_job("animator ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lahti")
	
@animator.route('/animator-jobs-kuopio')
def animator_jobs8(page=1):

    job_list = job_obj.get_job("animator ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuopio")
	
@animator.route('/animator-jobs-jyvvaskyla')
def animator_jobs9(page=1):

    job_list = job_obj.get_job("animator ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jyvvaskyla")

@animator.route('/animator-jobs-pori')
def animator_jobs10(page=1):

    job_list = job_obj.get_job("animator ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pori")

@animator.route('/animator-jobs-lappeenranta')
def animator_jobs11(page=1):

    job_list = job_obj.get_job("animator ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lappeenranta")	
	
@animator.route('/animator-jobs-vaasa')
def animator_jobs12(page=1):

    job_list = job_obj.get_job("animator ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vaasa")
	
@animator.route('/animator-jobs-kotka')
def animator_jobs13(page=1):

    job_list = job_obj.get_job("animator ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kotka")
	
@animator.route('/animator-jobs-joensuu')
def animator_jobs14(page=1):

    job_list = job_obj.get_job("animator ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="joensuu")
	
@animator.route('/animator-jobs-hameenlinna')
def animator_jobs15(page=1):

    job_list = job_obj.get_job("animator ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hameenlinna")
	
@animator.route('/animator-jobs-porvoo')
def animator_jobs16(page=1):

    job_list = job_obj.get_job("animator ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="porvoo")
	
@animator.route('/animator-jobs-mikkeli')
def animator_jobs17(page=1):

    job_list = job_obj.get_job("animator ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="mikkeli")

@animator.route('/animator-jobs-hyvinkaa')
def animator_jobs18(page=1):

    job_list = job_obj.get_job("animator ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hyvinkaa")
	
@animator.route('/animator-jobs-nurmijarvi')
def animator_jobs19(page=1):

    job_list = job_obj.get_job("animator ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nurmijarvi")

@animator.route('/animator-jobs-jarvenpaa')
def animator_jobs20(page=1):

    job_list = job_obj.get_job("animator ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jarvenpaa")
	
@animator.route('/animator-jobs-rauma')
def animator_jobs21(page=1):

    job_list = job_obj.get_job("animator ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="rauma")
	
@animator.route('/animator-jobs-lohja')
def animator_jobs22(page=1):

    job_list = job_obj.get_job("animator ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lohja")
	
@animator.route('/animator-jobs-karleby')
def animator_jobs23(page=1):

    job_list = job_obj.get_job("animator ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="karleby")
	
@animator.route('/animator-jobs-kajaani')
def animator_jobs24(page=1):

    job_list = job_obj.get_job("animator ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kajaani")
	
@animator.route('/animator-jobs-rovaniemi')
def animator_jobs25(page=1):

    job_list = job_obj.get_job("animator ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="rovaniemi")
	
@animator.route('/animator-jobs-tuusula')
def animator_jobs26(page=1):

    job_list = job_obj.get_job("animator ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="tuusula")
	
@animator.route('/animator-jobs-kirkkonummi')
def animator_jobs27(page=1):

    job_list = job_obj.get_job("animator ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kirkkonummi")
	
@animator.route('/animator-jobs-seinajoki')
def animator_jobs28(page=1):

    job_list = job_obj.get_job("animator ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="seinajoki")
	
@animator.route('/animator-jobs-kerava')
def animator_jobs29(page=1):

    job_list = job_obj.get_job("animator ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kerava")
	
@animator.route('/animator-jobs-kouvola')
def animator_jobs30(page=1):

    job_list = job_obj.get_job("animator ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kouvola")
	
@animator.route('/animator-jobs-imatra')
def animator_jobs31(page=1):

    job_list = job_obj.get_job("animator ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="imatra")
	
@animator.route('/animator-jobs-nokia')
def animator_jobs32_1(page=1):

    job_list = job_obj.get_job("animator ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nokia")
	
@animator.route('/animator-jobs-savonlinna')
def animator_jobs32(page=1):

    job_list = job_obj.get_job("animator ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="savonlinna")
	
@animator.route('/animator-jobs-riihimaki')
def animator_jobs33(page=1):

    job_list = job_obj.get_job("animator ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="riihimaki")
	
@animator.route('/animator-jobs-vihti')
def animator_jobs34(page=1):

    job_list = job_obj.get_job("animator ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vihti")
	
@animator.route('/animator-jobs-salo')
def animator_jobs35(page=1):

    job_list = job_obj.get_job("animator ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="salo")
	
@animator.route('/animator-jobs-kangasala')
def animator_jobs36(page=1):

    job_list = job_obj.get_job("animator ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kangasala")
	
@animator.route('/animator-jobs-raisio')
def animator_jobs37_1(page=1):

    job_list = job_obj.get_job("animator ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="raisio")
	
@animator.route('/animator-jobs-karhula')
def animator_jobs37(page=1):

    job_list = job_obj.get_job("animator ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="karhula")
	
@animator.route('/animator-jobs-kemi')
def animator_jobs38(page=1):

    job_list = job_obj.get_job("animator ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kemi")
	
@animator.route('/animator-jobs-iisalmi')
def animator_jobs39(page=1):

    job_list = job_obj.get_job("animator ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="iisalmi")
	
@animator.route('/animator-jobs-varkaus')
def animator_jobs40(page=1):

    job_list = job_obj.get_job("animator ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="varkaus")
	
@animator.route('/animator-jobs-raahe')
def animator_jobs41(page=1):

    job_list = job_obj.get_job("animator ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="raahe")
	
@animator.route('/animator-jobs-ylojarvi')
def animator_jobs42_1(page=1):

    job_list = job_obj.get_job("animator ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ylojarvi")
	
@animator.route('/animator-jobs-hamina')
def animator_jobs42(page=1):

    job_list = job_obj.get_job("animator ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hamina")
	
@animator.route('/animator-jobs-kaarina')
def animator_jobs43(page=1):

    job_list = job_obj.get_job("animator ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kaarina")
	
@animator.route('/animator-jobs-tornio')
def animator_jobs44(page=1):

    job_list = job_obj.get_job("animator ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="tornio")
	
@animator.route('/animator-jobs-heinola')
def animator_jobs45(page=1):

    job_list = job_obj.get_job("animator ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="heinola")
	
@animator.route('/animator-jobs-hollola')
def animator_jobs46(page=1):

    job_list = job_obj.get_job("animator ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hollola")
	
@animator.route('/animator-jobs-valkeakoski')
def animator_jobs47(page=1):

    job_list = job_obj.get_job("animator ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="valkeakoski")
	
@animator.route('/animator-jobs-siilinjarvi')
def animator_jobs48(page=1):

    job_list = job_obj.get_job("animator ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="siilinjarvi")
	
@animator.route('/animator-jobs-kuusankoski')
def animator_jobs49(page=1):

    job_list = job_obj.get_job("animator ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuusankoski")
	
@animator.route('/animator-jobs-sibbo')
def animator_jobs50(page=1):

    job_list = job_obj.get_job("animator ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="sibbo")
	
@animator.route('/animator-jobs-jakostad')
def animator_jobs51(page=1):

    job_list = job_obj.get_job("animator ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jakostad")
	
@animator.route('/animator-jobs-lempaala')
def animator_jobs52(page=1):

    job_list = job_obj.get_job("animator ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lempaala")
	
@animator.route('/animator-jobs-mantsala')
def animator_jobs52_1(page=1):

    job_list = job_obj.get_job("animator ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="mantsala")
	
@animator.route('/animator-jobs-forssa')
def animator_jobs53(page=1):

    job_list = job_obj.get_job("animator ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="forssa")
	
@animator.route('/animator-jobs-kuusamo')
def animator_jobs54(page=1):

    job_list = job_obj.get_job("animator ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuusamo")
	
@animator.route('/animator-jobs-haukipudas')
def animator_jobs55(page=1):

    job_list = job_obj.get_job("animator ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="haukipudas")
	
@animator.route('/animator-jobs-korsholm')
def animator_jobs56(page=1):

    job_list = job_obj.get_job("animator ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="korsholm")
	
@animator.route('/animator-jobs-laukaa')
def animator_jobs57(page=1):

    job_list = job_obj.get_job("animator ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="laukaa")
	
@animator.route('/animator-jobs-anjala')
def animator_jobs58(page=1):

    job_list = job_obj.get_job("animator ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="anjala")
	
@animator.route('/animator-jobs-uusikaupunki')
def animator_jobs59(page=1):

    job_list = job_obj.get_job("animator ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="uusikaupunki")
	
@animator.route('/animator-jobs-janakkala')
def animator_jobs60(page=1):

    job_list = job_obj.get_job("animator ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="janakkala")
	
@animator.route('/animator-jobs-pirkkala')
def animator_jobs61(page=1):

    job_list = job_obj.get_job("animator ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pirkkala")
	
@animator.route('/animator-jobs-lansi-turunmaa')
def animator_jobs62(page=1):

    job_list = job_obj.get_job("animator ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lansi-turunmaa")
	
@animator.route('/animator-jobs-jamsa')
def animator_jobs63(page=1):

    job_list = job_obj.get_job("animator ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jamsa")
	
@animator.route('/animator-jobs-jamsa')
def animator_jobs64(page=1):

    job_list = job_obj.get_job("animator ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jamsa")
	
@animator.route('/animator-jobs-vammala')
def animator_jobs65(page=1):

    job_list = job_obj.get_job("animator ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vammala")
	
@animator.route('/animator-jobs-nastola')
def animator_jobs66(page=1):

    job_list = job_obj.get_job("animator ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nastola")
	
@animator.route('/animator-jobs-orimattila')
def animator_jobs67(page=1):

    job_list = job_obj.get_job("animator ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="orimattila")
	
@animator.route('/animator-jobs-kauhajoki')
def animator_jobs68(page=1):

    job_list = job_obj.get_job("animator ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kauhajoki")
	
@animator.route('/animator-jobs-ekenas')
def animator_jobs69(page=1):

    job_list = job_obj.get_job("animator ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ekenas")
	
@animator.route('/animator-jobs-kempele')
def animator_jobs70(page=1):

    job_list = job_obj.get_job("animator ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kempele")
	
@animator.route('/animator-jobs-lapua')
def animator_jobs71(page=1):

    job_list = job_obj.get_job("animator ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lapua")
	
@animator.route('/animator-jobs-lieksa')
def animator_jobs72(page=1):

    job_list = job_obj.get_job("animator ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lieksa")
	
@animator.route('/animator-jobs-naantali')
def animator_jobs73(page=1):

    job_list = job_obj.get_job("animator ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="naantali")
	
@animator.route('/animator-jobs-aanekoski')
def animator_jobs74(page=1):

    job_list = job_obj.get_job("animator ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="aanekoski")
	
@animator.route('/animator-jobs-ylivieska')
def animator_jobs75(page=1):

    job_list = job_obj.get_job("animator ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ylivieska")
	
@animator.route('/animator-jobs-kontiolahti')
def animator_jobs76(page=1):

    job_list = job_obj.get_job("animator ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kontiolahti")
	
@animator.route('/animator-jobs-kankaanpaa')
def animator_jobs77(page=1):

    job_list = job_obj.get_job("animator ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kankaanpaa")
	
@animator.route('/animator-jobs-ulvila')
def animator_jobs78(page=1):

    job_list = job_obj.get_job("animator ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ulvila")
	
@animator.route('/animator-jobs-pieksamaki')
def animator_jobs79(page=1):

    job_list = job_obj.get_job("animator ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pieksamaki")
	
@animator.route('/animator-jobs-kiiminki')
def animator_jobs80(page=1):

    job_list = job_obj.get_job("animator ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kiiminki")
	
@animator.route('/animator-jobs-pargas')
def animator_jobs81(page=1):

    job_list = job_obj.get_job("animator ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pargas")
	
@animator.route('/animator-jobs-nurmo')
def animator_jobs82(page=1):

    job_list = job_obj.get_job("animator ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nurmo")
	
@animator.route('/animator-jobs-ilmajoki')
def animator_jobs83(page=1):

    job_list = job_obj.get_job("animator ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ilmajoki")
	
@animator.route('/animator-jobs-liperi')
def animator_jobs84(page=1):

    job_list = job_obj.get_job("animator ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="liperi")
	
@animator.route('/animator-jobs-keuruu')
def animator_jobs85(page=1):

    job_list = job_obj.get_job("animator ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="keuruu")
	
@animator.route('/animator-jobs-leppavirta')
def animator_jobs86(page=1):

    job_list = job_obj.get_job("animator ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="leppavirta")
	
@animator.route('/animator-jobs-kurikka')
def animator_jobs87(page=1):

    job_list = job_obj.get_job("animator ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kurikka")
	
@animator.route('/animator-jobs-nivala')
def animator_jobs88(page=1):

    job_list = job_obj.get_job("animator ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nivala")
	
@animator.route('/animator-jobs-joutseno')
def animator_jobs89(page=1):

    job_list = job_obj.get_job("animator ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="joutseno")
	
@animator.route('/animator-jobs-pedersore')
def animator_jobs90(page=1):

    job_list = job_obj.get_job("animator ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pedersore")
	
@animator.route('/animator-jobs-sotkamo')
def animator_jobs91(page=1):

    job_list = job_obj.get_job("animator ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="sotkamo")
	
@animator.route('/animator-jobs-kuhmo')
def animator_jobs92(page=1):

    job_list = job_obj.get_job("animator ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuhmo")
	
@animator.route('/animator-jobs-paimio')
def animator_jobs93(page=1):

    job_list = job_obj.get_job("animator ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="paimio")
	
@animator.route('/animator-jobs-saarijarvi')
def animator_jobs94(page=1):

    job_list = job_obj.get_job("animator ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="saarijarvi")
	
@animator.route('/animator-jobs-helsinki')
def animator_jobs95(page=1):

    job_list = job_obj.get_job("animator ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="helsinki")


####################################################################
##############################################
@animator.route('/animator-tyopaikat-espoo')
def animator_tyopaikat2(page=1):

    job_list = job_obj.get_job("animator ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="espoo")

@animator.route('/animator-tyopaikat-tampere')
def animator_tyopaikat3(page=1):

    job_list = job_obj.get_job("animator ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="tampere")
	
@animator.route('/animator-tyopaikat-vantaa')
def animator_tyopaikat4(page=1):

    job_list = job_obj.get_job("animator ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vantaa")
	
@animator.route('/animator-tyopaikat-turku')
def animator_tyopaikat5(page=1):

    job_list = job_obj.get_job("animator ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="turku")
	
@animator.route('/animator-tyopaikat-oulu')
def animator_tyopaikat6(page=1):

    job_list = job_obj.get_job("animator ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="oulu")
	
@animator.route('/animator-tyopaikat-lahti')
def animator_tyopaikat7(page=1):

    job_list = job_obj.get_job("animator ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lahti")
	
@animator.route('/animator-tyopaikat-kuopio')
def animator_tyopaikat8(page=1):

    job_list = job_obj.get_job("animator ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuopio")
	
@animator.route('/animator-tyopaikat-jyvvaskyla')
def animator_tyopaikat9(page=1):

    job_list = job_obj.get_job("animator ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jyvvaskyla")

@animator.route('/animator-tyopaikat-pori')
def animator_tyopaikat10(page=1):

    job_list = job_obj.get_job("animator ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pori")

@animator.route('/animator-tyopaikat-lappeenranta')
def animator_tyopaikat11(page=1):

    job_list = job_obj.get_job("animator ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lappeenranta")	
	
@animator.route('/animator-tyopaikat-vaasa')
def animator_tyopaikat12(page=1):

    job_list = job_obj.get_job("animator ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vaasa")
	
@animator.route('/animator-tyopaikat-kotka')
def animator_tyopaikat13(page=1):

    job_list = job_obj.get_job("animator ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kotka")
	
@animator.route('/animator-tyopaikat-joensuu')
def animator_tyopaikat14(page=1):

    job_list = job_obj.get_job("animator ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="joensuu")
	
@animator.route('/animator-tyopaikat-hameenlinna')
def animator_tyopaikat15(page=1):

    job_list = job_obj.get_job("animator ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hameenlinna")
	
@animator.route('/animator-tyopaikat-porvoo')
def animator_tyopaikat16(page=1):

    job_list = job_obj.get_job("animator ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="porvoo")
	
@animator.route('/animator-tyopaikat-mikkeli')
def animator_tyopaikat17(page=1):

    job_list = job_obj.get_job("animator ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="mikkeli")

@animator.route('/animator-tyopaikat-hyvinkaa')
def animator_tyopaikat18(page=1):

    job_list = job_obj.get_job("animator ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hyvinkaa")
	
@animator.route('/animator-tyopaikat-nurmijarvi')
def animator_tyopaikat19(page=1):

    job_list = job_obj.get_job("animator ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nurmijarvi")

@animator.route('/animator-tyopaikat-jarvenpaa')
def animator_tyopaikat20(page=1):

    job_list = job_obj.get_job("animator ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jarvenpaa")
	
@animator.route('/animator-tyopaikat-rauma')
def animator_tyopaikat21(page=1):

    job_list = job_obj.get_job("animator ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="rauma")
	
@animator.route('/animator-tyopaikat-lohja')
def animator_tyopaikat22(page=1):

    job_list = job_obj.get_job("animator ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lohja")
	
@animator.route('/animator-tyopaikat-karleby')
def animator_tyopaikat23(page=1):

    job_list = job_obj.get_job("animator ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="karleby")
	
@animator.route('/animator-tyopaikat-kajaani')
def animator_tyopaikat24(page=1):

    job_list = job_obj.get_job("animator ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kajaani")
	
@animator.route('/animator-tyopaikat-rovaniemi')
def animator_tyopaikat25(page=1):

    job_list = job_obj.get_job("animator ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="rovaniemi")
	
@animator.route('/animator-tyopaikat-tuusula')
def animator_tyopaikat26(page=1):

    job_list = job_obj.get_job("animator ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="tuusula")
	
@animator.route('/animator-tyopaikat-kirkkonummi')
def animator_tyopaikat27(page=1):

    job_list = job_obj.get_job("animator ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kirkkonummi")
	
@animator.route('/animator-tyopaikat-seinajoki')
def animator_tyopaikat28(page=1):

    job_list = job_obj.get_job("animator ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="seinajoki")
	
@animator.route('/animator-tyopaikat-kerava')
def animator_tyopaikat29(page=1):

    job_list = job_obj.get_job("animator ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kerava")
	
@animator.route('/animator-tyopaikat-kouvola')
def animator_tyopaikat30(page=1):

    job_list = job_obj.get_job("animator ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kouvola")
	
@animator.route('/animator-tyopaikat-imatra')
def animator_tyopaikat31(page=1):

    job_list = job_obj.get_job("animator ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="imatra")
	
@animator.route('/animator-tyopaikat-nokia')
def animator_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("animator ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nokia")
	
@animator.route('/animator-tyopaikat-savonlinna')
def animator_tyopaikat32(page=1):

    job_list = job_obj.get_job("animator ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="savonlinna")
	
@animator.route('/animator-tyopaikat-riihimaki')
def animator_tyopaikat33(page=1):

    job_list = job_obj.get_job("animator ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="riihimaki")
	
@animator.route('/animator-tyopaikat-vihti')
def animator_tyopaikat34(page=1):

    job_list = job_obj.get_job("animator ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vihti")
	
@animator.route('/animator-tyopaikat-salo')
def animator_tyopaikat35(page=1):

    job_list = job_obj.get_job("animator ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="salo")
	
@animator.route('/animator-tyopaikat-kangasala')
def animator_tyopaikat36(page=1):

    job_list = job_obj.get_job("animator ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kangasala")
	
@animator.route('/animator-tyopaikat-raisio')
def animator_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("animator ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="raisio")
	
@animator.route('/animator-tyopaikat-karhula')
def animator_tyopaikat37(page=1):

    job_list = job_obj.get_job("animator ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="karhula")
	
@animator.route('/animator-tyopaikat-kemi')
def animator_tyopaikat38(page=1):

    job_list = job_obj.get_job("animator ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kemi")
	
@animator.route('/animator-tyopaikat-iisalmi')
def animator_tyopaikat39(page=1):

    job_list = job_obj.get_job("animator ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="iisalmi")
	
@animator.route('/animator-tyopaikat-varkaus')
def animator_tyopaikat40(page=1):

    job_list = job_obj.get_job("animator ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="varkaus")
	
@animator.route('/animator-tyopaikat-raahe')
def animator_tyopaikat41(page=1):

    job_list = job_obj.get_job("animator ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="raahe")
	
@animator.route('/animator-tyopaikat-ylojarvi')
def animator_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("animator ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ylojarvi")
	
@animator.route('/animator-tyopaikat-hamina')
def animator_tyopaikat42(page=1):

    job_list = job_obj.get_job("animator ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hamina")
	
@animator.route('/animator-tyopaikat-kaarina')
def animator_tyopaikat43(page=1):

    job_list = job_obj.get_job("animator ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kaarina")
	
@animator.route('/animator-tyopaikat-tornio')
def animator_tyopaikat44(page=1):

    job_list = job_obj.get_job("animator ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="tornio")
	
@animator.route('/animator-tyopaikat-heinola')
def animator_tyopaikat45(page=1):

    job_list = job_obj.get_job("animator ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="heinola")
	
@animator.route('/animator-tyopaikat-hollola')
def animator_tyopaikat46(page=1):

    job_list = job_obj.get_job("animator ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="hollola")
	
@animator.route('/animator-tyopaikat-valkeakoski')
def animator_tyopaikat47(page=1):

    job_list = job_obj.get_job("animator ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="valkeakoski")
	
@animator.route('/animator-tyopaikat-siilinjarvi')
def animator_tyopaikat48(page=1):

    job_list = job_obj.get_job("animator ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="siilinjarvi")
	
@animator.route('/animator-tyopaikat-kuusankoski')
def animator_tyopaikat49(page=1):

    job_list = job_obj.get_job("animator ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuusankoski")
	
@animator.route('/animator-tyopaikat-sibbo')
def animator_tyopaikat50(page=1):

    job_list = job_obj.get_job("animator ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="sibbo")
	
@animator.route('/animator-tyopaikat-jakostad')
def animator_tyopaikat51(page=1):

    job_list = job_obj.get_job("animator ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jakostad")
	
@animator.route('/animator-tyopaikat-lempaala')
def animator_tyopaikat52(page=1):

    job_list = job_obj.get_job("animator ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lempaala")
	
@animator.route('/animator-tyopaikat-mantsala')
def animator_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("animator ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="mantsala")
	
@animator.route('/animator-tyopaikat-forssa')
def animator_tyopaikat53(page=1):

    job_list = job_obj.get_job("animator ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="forssa")
	
@animator.route('/animator-tyopaikat-kuusamo')
def animator_tyopaikat54(page=1):

    job_list = job_obj.get_job("animator ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuusamo")
	
@animator.route('/animator-tyopaikat-haukipudas')
def animator_tyopaikat55(page=1):

    job_list = job_obj.get_job("animator ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="haukipudas")
	
@animator.route('/animator-tyopaikat-korsholm')
def animator_tyopaikat56(page=1):

    job_list = job_obj.get_job("animator ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="korsholm")
	
@animator.route('/animator-tyopaikat-laukaa')
def animator_tyopaikat57(page=1):

    job_list = job_obj.get_job("animator ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="laukaa")
	
@animator.route('/animator-tyopaikat-anjala')
def animator_tyopaikat58(page=1):

    job_list = job_obj.get_job("animator ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="anjala")
	
@animator.route('/animator-tyopaikat-uusikaupunki')
def animator_tyopaikat59(page=1):

    job_list = job_obj.get_job("animator ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="uusikaupunki")
	
@animator.route('/animator-tyopaikat-janakkala')
def animator_tyopaikat60(page=1):

    job_list = job_obj.get_job("animator ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="janakkala")
	
@animator.route('/animator-tyopaikat-pirkkala')
def animator_tyopaikat61(page=1):

    job_list = job_obj.get_job("animator ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pirkkala")
	
@animator.route('/animator-tyopaikat-lansi-turunmaa')
def animator_tyopaikat62(page=1):

    job_list = job_obj.get_job("animator ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lansi-turunmaa")
	
@animator.route('/animator-tyopaikat-jamsa')
def animator_tyopaikat63(page=1):

    job_list = job_obj.get_job("animator ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jamsa")
	
@animator.route('/animator-tyopaikat-jamsa')
def animator_tyopaikat64(page=1):

    job_list = job_obj.get_job("animator ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="jamsa")
	
@animator.route('/animator-tyopaikat-vammala')
def animator_tyopaikat65(page=1):

    job_list = job_obj.get_job("animator ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="vammala")
	
@animator.route('/animator-tyopaikat-nastola')
def animator_tyopaikat66(page=1):

    job_list = job_obj.get_job("animator ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nastola")
	
@animator.route('/animator-tyopaikat-orimattila')
def animator_tyopaikat67(page=1):

    job_list = job_obj.get_job("animator ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="orimattila")
	
@animator.route('/animator-tyopaikat-kauhajoki')
def animator_tyopaikat68(page=1):

    job_list = job_obj.get_job("animator ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kauhajoki")
	
@animator.route('/animator-tyopaikat-ekenas')
def animator_tyopaikat69(page=1):

    job_list = job_obj.get_job("animator ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ekenas")
	
@animator.route('/animator-tyopaikat-kempele')
def animator_tyopaikat70(page=1):

    job_list = job_obj.get_job("animator ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kempele")
	
@animator.route('/animator-tyopaikat-lapua')
def animator_tyopaikat71(page=1):

    job_list = job_obj.get_job("animator ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lapua")
	
@animator.route('/animator-tyopaikat-lieksa')
def animator_tyopaikat72(page=1):

    job_list = job_obj.get_job("animator ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="lieksa")
	
@animator.route('/animator-tyopaikat-naantali')
def animator_tyopaikat73(page=1):

    job_list = job_obj.get_job("animator ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="naantali")
	
@animator.route('/animator-tyopaikat-aanekoski')
def animator_tyopaikat74(page=1):

    job_list = job_obj.get_job("animator ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="aanekoski")
	
@animator.route('/animator-tyopaikat-ylivieska')
def animator_tyopaikat75(page=1):

    job_list = job_obj.get_job("animator ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ylivieska")
	
@animator.route('/animator-tyopaikat-kontiolahti')
def animator_tyopaikat76(page=1):

    job_list = job_obj.get_job("animator ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kontiolahti")
	
@animator.route('/animator-tyopaikat-kankaanpaa')
def animator_tyopaikat77(page=1):

    job_list = job_obj.get_job("animator ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kankaanpaa")
	
@animator.route('/animator-tyopaikat-ulvila')
def animator_tyopaikat78(page=1):

    job_list = job_obj.get_job("animator ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ulvila")
	
@animator.route('/animator-tyopaikat-pieksamaki')
def animator_tyopaikat79(page=1):

    job_list = job_obj.get_job("animator ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pieksamaki")
	
@animator.route('/animator-tyopaikat-kiiminki')
def animator_tyopaikat80(page=1):

    job_list = job_obj.get_job("animator ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kiiminki")
	
@animator.route('/animator-tyopaikat-pargas')
def animator_tyopaikat81(page=1):

    job_list = job_obj.get_job("animator ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pargas")
	
@animator.route('/animator-tyopaikat-nurmo')
def animator_tyopaikat82(page=1):

    job_list = job_obj.get_job("animator ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nurmo")
	
@animator.route('/animator-tyopaikat-ilmajoki')
def animator_tyopaikat83(page=1):

    job_list = job_obj.get_job("animator ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="ilmajoki")
	
@animator.route('/animator-tyopaikat-liperi')
def animator_tyopaikat84(page=1):

    job_list = job_obj.get_job("animator ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="liperi")
	
@animator.route('/animator-tyopaikat-keuruu')
def animator_tyopaikat85(page=1):

    job_list = job_obj.get_job("animator ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="keuruu")
	
@animator.route('/animator-tyopaikat-leppavirta')
def animator_tyopaikat86(page=1):

    job_list = job_obj.get_job("animator ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="leppavirta")
	
@animator.route('/animator-tyopaikat-kurikka')
def animator_tyopaikat87(page=1):

    job_list = job_obj.get_job("animator ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kurikka")
	
@animator.route('/animator-tyopaikat-nivala')
def animator_tyopaikat88(page=1):

    job_list = job_obj.get_job("animator ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="nivala")
	
@animator.route('/animator-tyopaikat-joutseno')
def animator_tyopaikat89(page=1):

    job_list = job_obj.get_job("animator ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="joutseno")
	
@animator.route('/animator-tyopaikat-pedersore')
def animator_tyopaikat90(page=1):

    job_list = job_obj.get_job("animator ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="pedersore")
	
@animator.route('/animator-tyopaikat-sotkamo')
def animator_tyopaikat91(page=1):

    job_list = job_obj.get_job("animator ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="sotkamo")
	
@animator.route('/animator-tyopaikat-kuhmo')
def animator_tyopaikat92(page=1):

    job_list = job_obj.get_job("animator ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="kuhmo")
	
@animator.route('/animator-tyopaikat-paimio')
def animator_tyopaikat93(page=1):

    job_list = job_obj.get_job("animator ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="paimio")
	
@animator.route('/animator-tyopaikat-saarijarvi')
def animator_tyopaikat94(page=1):

    job_list = job_obj.get_job("animator ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="saarijarvi")
	
@animator.route('/animator-tyopaikat-helsinki')
def animator_tyopaikat95(page=1):

    job_list = job_obj.get_job("animator ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="animator ", location="helsinki")


####################################################################

