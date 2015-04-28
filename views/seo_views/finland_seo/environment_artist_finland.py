from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

environment_artist = Blueprint('environment_artist', __name__)
job_obj = Job()



####################################################################


@environment_artist.route('/environment-artist_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "environment-artist" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@environment_artist.route('/environment-artist-avoimet-tyopaikat-espoo')
def environment_artist_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("environment artist ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="espoo")

@environment_artist.route('/environment-artist-avoimet-tyopaikat-tampere')
def environment_artist_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("environment artist ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="tampere")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-vantaa')
def environment_artist_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("environment artist ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="vantaa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-turku')
def environment_artist_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("environment artist ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="turku")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-oulu')
def environment_artist_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("environment artist ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="oulu")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-lahti')
def environment_artist_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("environment artist ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lahti")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kuopio')
def environment_artist_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("environment artist ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kuopio")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-jyvvaskyla')
def environment_artist_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("environment artist ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="jyvvaskyla")

@environment_artist.route('/environment-artist-avoimet-tyopaikat-pori')
def environment_artist_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("environment artist ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="pori")

@environment_artist.route('/environment-artist-avoimet-tyopaikat-lappeenranta')
def environment_artist_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("environment artist ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lappeenranta")	
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-vaasa')
def environment_artist_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("environment artist ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="vaasa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kotka')
def environment_artist_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("environment artist ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kotka")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-joensuu')
def environment_artist_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("environment artist ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="joensuu")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-hameenlinna')
def environment_artist_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("environment artist ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="hameenlinna")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-porvoo')
def environment_artist_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("environment artist ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="porvoo")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-mikkeli')
def environment_artist_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("environment artist ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="mikkeli")

@environment_artist.route('/environment-artist-avoimet-tyopaikat-hyvinkaa')
def environment_artist_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("environment artist ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="hyvinkaa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-nurmijarvi')
def environment_artist_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("environment artist ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="nurmijarvi")

@environment_artist.route('/environment-artist-avoimet-tyopaikat-jarvenpaa')
def environment_artist_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("environment artist ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="jarvenpaa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-rauma')
def environment_artist_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("environment artist ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="rauma")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-lohja')
def environment_artist_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("environment artist ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lohja")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-karleby')
def environment_artist_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("environment artist ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="karleby")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kajaani')
def environment_artist_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("environment artist ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kajaani")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-rovaniemi')
def environment_artist_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("environment artist ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="rovaniemi")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-tuusula')
def environment_artist_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("environment artist ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="tuusula")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kirkkonummi')
def environment_artist_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("environment artist ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kirkkonummi")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-seinajoki')
def environment_artist_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("environment artist ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="seinajoki")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kerava')
def environment_artist_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("environment artist ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kerava")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kouvola')
def environment_artist_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("environment artist ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kouvola")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-imatra')
def environment_artist_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("environment artist ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="imatra")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-nokia')
def environment_artist_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("environment artist ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="nokia")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-savonlinna')
def environment_artist_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("environment artist ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="savonlinna")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-riihimaki')
def environment_artist_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("environment artist ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="riihimaki")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-vihti')
def environment_artist_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("environment artist ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="vihti")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-salo')
def environment_artist_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("environment artist ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="salo")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kangasala')
def environment_artist_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("environment artist ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kangasala")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-raisio')
def environment_artist_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("environment artist ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="raisio")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-karhula')
def environment_artist_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("environment artist ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="karhula")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kemi')
def environment_artist_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("environment artist ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kemi")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-iisalmi')
def environment_artist_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("environment artist ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="iisalmi")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-varkaus')
def environment_artist_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("environment artist ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="varkaus")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-raahe')
def environment_artist_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("environment artist ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="raahe")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-ylojarvi')
def environment_artist_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("environment artist ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="ylojarvi")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-hamina')
def environment_artist_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("environment artist ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="hamina")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kaarina')
def environment_artist_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("environment artist ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kaarina")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-tornio')
def environment_artist_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("environment artist ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="tornio")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-heinola')
def environment_artist_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("environment artist ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="heinola")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-hollola')
def environment_artist_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("environment artist ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="hollola")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-valkeakoski')
def environment_artist_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("environment artist ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="valkeakoski")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-siilinjarvi')
def environment_artist_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("environment artist ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="siilinjarvi")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kuusankoski')
def environment_artist_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("environment artist ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kuusankoski")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-sibbo')
def environment_artist_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("environment artist ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="sibbo")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-jakostad')
def environment_artist_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("environment artist ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="jakostad")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-lempaala')
def environment_artist_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("environment artist ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lempaala")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-mantsala')
def environment_artist_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("environment artist ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="mantsala")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-forssa')
def environment_artist_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("environment artist ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="forssa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kuusamo')
def environment_artist_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("environment artist ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kuusamo")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-haukipudas')
def environment_artist_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("environment artist ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="haukipudas")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-korsholm')
def environment_artist_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("environment artist ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="korsholm")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-laukaa')
def environment_artist_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("environment artist ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="laukaa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-anjala')
def environment_artist_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("environment artist ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="anjala")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-uusikaupunki')
def environment_artist_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("environment artist ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="uusikaupunki")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-janakkala')
def environment_artist_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("environment artist ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="janakkala")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-pirkkala')
def environment_artist_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("environment artist ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="pirkkala")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-lansi-turunmaa')
def environment_artist_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("environment artist ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lansi-turunmaa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-jamsa')
def environment_artist_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("environment artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="jamsa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-jamsa')
def environment_artist_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("environment artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="jamsa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-vammala')
def environment_artist_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("environment artist ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="vammala")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-nastola')
def environment_artist_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("environment artist ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="nastola")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-orimattila')
def environment_artist_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("environment artist ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="orimattila")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kauhajoki')
def environment_artist_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("environment artist ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kauhajoki")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-ekenas')
def environment_artist_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("environment artist ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="ekenas")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kempele')
def environment_artist_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("environment artist ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kempele")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-lapua')
def environment_artist_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("environment artist ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lapua")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-lieksa')
def environment_artist_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("environment artist ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lieksa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-naantali')
def environment_artist_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("environment artist ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="naantali")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-aanekoski')
def environment_artist_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("environment artist ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="aanekoski")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-ylivieska')
def environment_artist_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("environment artist ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="ylivieska")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kontiolahti')
def environment_artist_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("environment artist ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kontiolahti")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kankaanpaa')
def environment_artist_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("environment artist ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kankaanpaa")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-ulvila')
def environment_artist_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("environment artist ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="ulvila")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-pieksamaki')
def environment_artist_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("environment artist ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="pieksamaki")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kiiminki')
def environment_artist_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("environment artist ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kiiminki")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-pargas')
def environment_artist_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("environment artist ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="pargas")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-nurmo')
def environment_artist_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("environment artist ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="nurmo")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-ilmajoki')
def environment_artist_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("environment artist ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="ilmajoki")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-liperi')
def environment_artist_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("environment artist ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="liperi")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-keuruu')
def environment_artist_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("environment artist ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="keuruu")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-leppavirta')
def environment_artist_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("environment artist ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="leppavirta")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kurikka')
def environment_artist_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("environment artist ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kurikka")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-nivala')
def environment_artist_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("environment artist ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="nivala")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-joutseno')
def environment_artist_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("environment artist ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="joutseno")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-pedersore')
def environment_artist_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("environment artist ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="pedersore")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-sotkamo')
def environment_artist_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("environment artist ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="sotkamo")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-kuhmo')
def environment_artist_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("environment artist ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kuhmo")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-paimio')
def environment_artist_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("environment artist ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="paimio")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-saarijarvi')
def environment_artist_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("environment artist ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="saarijarvi")
	
@environment_artist.route('/environment-artist-avoimet-tyopaikat-helsinki')
def environment_artist_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("environment artist ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="helsinki")


####################################################################


##############################################
@environment_artist.route('/environment-artist-jobs-espoo')
def environment_artist_jobs2(page=1):

    job_list = job_obj.get_job("environment artist ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="espoo")

@environment_artist.route('/environment-artist-jobs-tampere')
def environment_artist_jobs3(page=1):

    job_list = job_obj.get_job("environment artist ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="tampere")
	
@environment_artist.route('/environment-artist-jobs-vantaa')
def environment_artist_jobs4(page=1):

    job_list = job_obj.get_job("environment artist ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="vantaa")
	
@environment_artist.route('/environment-artist-jobs-turku')
def environment_artist_jobs5(page=1):

    job_list = job_obj.get_job("environment artist ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="turku")
	
@environment_artist.route('/environment-artist-jobs-oulu')
def environment_artist_jobs6(page=1):

    job_list = job_obj.get_job("environment artist ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="oulu")
	
@environment_artist.route('/environment-artist-jobs-lahti')
def environment_artist_jobs7(page=1):

    job_list = job_obj.get_job("environment artist ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lahti")
	
@environment_artist.route('/environment-artist-jobs-kuopio')
def environment_artist_jobs8(page=1):

    job_list = job_obj.get_job("environment artist ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kuopio")
	
@environment_artist.route('/environment-artist-jobs-jyvvaskyla')
def environment_artist_jobs9(page=1):

    job_list = job_obj.get_job("environment artist ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="jyvvaskyla")

@environment_artist.route('/environment-artist-jobs-pori')
def environment_artist_jobs10(page=1):

    job_list = job_obj.get_job("environment artist ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="pori")

@environment_artist.route('/environment-artist-jobs-lappeenranta')
def environment_artist_jobs11(page=1):

    job_list = job_obj.get_job("environment artist ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lappeenranta")	
	
@environment_artist.route('/environment-artist-jobs-vaasa')
def environment_artist_jobs12(page=1):

    job_list = job_obj.get_job("environment artist ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="vaasa")
	
@environment_artist.route('/environment-artist-jobs-kotka')
def environment_artist_jobs13(page=1):

    job_list = job_obj.get_job("environment artist ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kotka")
	
@environment_artist.route('/environment-artist-jobs-joensuu')
def environment_artist_jobs14(page=1):

    job_list = job_obj.get_job("environment artist ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="joensuu")
	
@environment_artist.route('/environment-artist-jobs-hameenlinna')
def environment_artist_jobs15(page=1):

    job_list = job_obj.get_job("environment artist ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="hameenlinna")
	
@environment_artist.route('/environment-artist-jobs-porvoo')
def environment_artist_jobs16(page=1):

    job_list = job_obj.get_job("environment artist ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="porvoo")
	
@environment_artist.route('/environment-artist-jobs-mikkeli')
def environment_artist_jobs17(page=1):

    job_list = job_obj.get_job("environment artist ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="mikkeli")

@environment_artist.route('/environment-artist-jobs-hyvinkaa')
def environment_artist_jobs18(page=1):

    job_list = job_obj.get_job("environment artist ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="hyvinkaa")
	
@environment_artist.route('/environment-artist-jobs-nurmijarvi')
def environment_artist_jobs19(page=1):

    job_list = job_obj.get_job("environment artist ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="nurmijarvi")

@environment_artist.route('/environment-artist-jobs-jarvenpaa')
def environment_artist_jobs20(page=1):

    job_list = job_obj.get_job("environment artist ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="jarvenpaa")
	
@environment_artist.route('/environment-artist-jobs-rauma')
def environment_artist_jobs21(page=1):

    job_list = job_obj.get_job("environment artist ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="rauma")
	
@environment_artist.route('/environment-artist-jobs-lohja')
def environment_artist_jobs22(page=1):

    job_list = job_obj.get_job("environment artist ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lohja")
	
@environment_artist.route('/environment-artist-jobs-karleby')
def environment_artist_jobs23(page=1):

    job_list = job_obj.get_job("environment artist ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="karleby")
	
@environment_artist.route('/environment-artist-jobs-kajaani')
def environment_artist_jobs24(page=1):

    job_list = job_obj.get_job("environment artist ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kajaani")
	
@environment_artist.route('/environment-artist-jobs-rovaniemi')
def environment_artist_jobs25(page=1):

    job_list = job_obj.get_job("environment artist ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="rovaniemi")
	
@environment_artist.route('/environment-artist-jobs-tuusula')
def environment_artist_jobs26(page=1):

    job_list = job_obj.get_job("environment artist ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="tuusula")
	
@environment_artist.route('/environment-artist-jobs-kirkkonummi')
def environment_artist_jobs27(page=1):

    job_list = job_obj.get_job("environment artist ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kirkkonummi")
	
@environment_artist.route('/environment-artist-jobs-seinajoki')
def environment_artist_jobs28(page=1):

    job_list = job_obj.get_job("environment artist ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="seinajoki")
	
@environment_artist.route('/environment-artist-jobs-kerava')
def environment_artist_jobs29(page=1):

    job_list = job_obj.get_job("environment artist ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kerava")
	
@environment_artist.route('/environment-artist-jobs-kouvola')
def environment_artist_jobs30(page=1):

    job_list = job_obj.get_job("environment artist ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kouvola")
	
@environment_artist.route('/environment-artist-jobs-imatra')
def environment_artist_jobs31(page=1):

    job_list = job_obj.get_job("environment artist ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="imatra")
	
@environment_artist.route('/environment-artist-jobs-nokia')
def environment_artist_jobs32_1(page=1):

    job_list = job_obj.get_job("environment artist ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="nokia")
	
@environment_artist.route('/environment-artist-jobs-savonlinna')
def environment_artist_jobs32(page=1):

    job_list = job_obj.get_job("environment artist ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="savonlinna")
	
@environment_artist.route('/environment-artist-jobs-riihimaki')
def environment_artist_jobs33(page=1):

    job_list = job_obj.get_job("environment artist ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="riihimaki")
	
@environment_artist.route('/environment-artist-jobs-vihti')
def environment_artist_jobs34(page=1):

    job_list = job_obj.get_job("environment artist ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="vihti")
	
@environment_artist.route('/environment-artist-jobs-salo')
def environment_artist_jobs35(page=1):

    job_list = job_obj.get_job("environment artist ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="salo")
	
@environment_artist.route('/environment-artist-jobs-kangasala')
def environment_artist_jobs36(page=1):

    job_list = job_obj.get_job("environment artist ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kangasala")
	
@environment_artist.route('/environment-artist-jobs-raisio')
def environment_artist_jobs37_1(page=1):

    job_list = job_obj.get_job("environment artist ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="raisio")
	
@environment_artist.route('/environment-artist-jobs-karhula')
def environment_artist_jobs37(page=1):

    job_list = job_obj.get_job("environment artist ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="karhula")
	
@environment_artist.route('/environment-artist-jobs-kemi')
def environment_artist_jobs38(page=1):

    job_list = job_obj.get_job("environment artist ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kemi")
	
@environment_artist.route('/environment-artist-jobs-iisalmi')
def environment_artist_jobs39(page=1):

    job_list = job_obj.get_job("environment artist ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="iisalmi")
	
@environment_artist.route('/environment-artist-jobs-varkaus')
def environment_artist_jobs40(page=1):

    job_list = job_obj.get_job("environment artist ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="varkaus")
	
@environment_artist.route('/environment-artist-jobs-raahe')
def environment_artist_jobs41(page=1):

    job_list = job_obj.get_job("environment artist ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="raahe")
	
@environment_artist.route('/environment-artist-jobs-ylojarvi')
def environment_artist_jobs42_1(page=1):

    job_list = job_obj.get_job("environment artist ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="ylojarvi")
	
@environment_artist.route('/environment-artist-jobs-hamina')
def environment_artist_jobs42(page=1):

    job_list = job_obj.get_job("environment artist ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="hamina")
	
@environment_artist.route('/environment-artist-jobs-kaarina')
def environment_artist_jobs43(page=1):

    job_list = job_obj.get_job("environment artist ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kaarina")
	
@environment_artist.route('/environment-artist-jobs-tornio')
def environment_artist_jobs44(page=1):

    job_list = job_obj.get_job("environment artist ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="tornio")
	
@environment_artist.route('/environment-artist-jobs-heinola')
def environment_artist_jobs45(page=1):

    job_list = job_obj.get_job("environment artist ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="heinola")
	
@environment_artist.route('/environment-artist-jobs-hollola')
def environment_artist_jobs46(page=1):

    job_list = job_obj.get_job("environment artist ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="hollola")
	
@environment_artist.route('/environment-artist-jobs-valkeakoski')
def environment_artist_jobs47(page=1):

    job_list = job_obj.get_job("environment artist ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="valkeakoski")
	
@environment_artist.route('/environment-artist-jobs-siilinjarvi')
def environment_artist_jobs48(page=1):

    job_list = job_obj.get_job("environment artist ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="siilinjarvi")
	
@environment_artist.route('/environment-artist-jobs-kuusankoski')
def environment_artist_jobs49(page=1):

    job_list = job_obj.get_job("environment artist ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kuusankoski")
	
@environment_artist.route('/environment-artist-jobs-sibbo')
def environment_artist_jobs50(page=1):

    job_list = job_obj.get_job("environment artist ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="sibbo")
	
@environment_artist.route('/environment-artist-jobs-jakostad')
def environment_artist_jobs51(page=1):

    job_list = job_obj.get_job("environment artist ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="jakostad")
	
@environment_artist.route('/environment-artist-jobs-lempaala')
def environment_artist_jobs52(page=1):

    job_list = job_obj.get_job("environment artist ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lempaala")
	
@environment_artist.route('/environment-artist-jobs-mantsala')
def environment_artist_jobs52_1(page=1):

    job_list = job_obj.get_job("environment artist ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="mantsala")
	
@environment_artist.route('/environment-artist-jobs-forssa')
def environment_artist_jobs53(page=1):

    job_list = job_obj.get_job("environment artist ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="forssa")
	
@environment_artist.route('/environment-artist-jobs-kuusamo')
def environment_artist_jobs54(page=1):

    job_list = job_obj.get_job("environment artist ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kuusamo")
	
@environment_artist.route('/environment-artist-jobs-haukipudas')
def environment_artist_jobs55(page=1):

    job_list = job_obj.get_job("environment artist ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="haukipudas")
	
@environment_artist.route('/environment-artist-jobs-korsholm')
def environment_artist_jobs56(page=1):

    job_list = job_obj.get_job("environment artist ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="korsholm")
	
@environment_artist.route('/environment-artist-jobs-laukaa')
def environment_artist_jobs57(page=1):

    job_list = job_obj.get_job("environment artist ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="laukaa")
	
@environment_artist.route('/environment-artist-jobs-anjala')
def environment_artist_jobs58(page=1):

    job_list = job_obj.get_job("environment artist ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="anjala")
	
@environment_artist.route('/environment-artist-jobs-uusikaupunki')
def environment_artist_jobs59(page=1):

    job_list = job_obj.get_job("environment artist ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="uusikaupunki")
	
@environment_artist.route('/environment-artist-jobs-janakkala')
def environment_artist_jobs60(page=1):

    job_list = job_obj.get_job("environment artist ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="janakkala")
	
@environment_artist.route('/environment-artist-jobs-pirkkala')
def environment_artist_jobs61(page=1):

    job_list = job_obj.get_job("environment artist ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="pirkkala")
	
@environment_artist.route('/environment-artist-jobs-lansi-turunmaa')
def environment_artist_jobs62(page=1):

    job_list = job_obj.get_job("environment artist ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lansi-turunmaa")
	
@environment_artist.route('/environment-artist-jobs-jamsa')
def environment_artist_jobs63(page=1):

    job_list = job_obj.get_job("environment artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="jamsa")
	
@environment_artist.route('/environment-artist-jobs-jamsa')
def environment_artist_jobs64(page=1):

    job_list = job_obj.get_job("environment artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="jamsa")
	
@environment_artist.route('/environment-artist-jobs-vammala')
def environment_artist_jobs65(page=1):

    job_list = job_obj.get_job("environment artist ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="vammala")
	
@environment_artist.route('/environment-artist-jobs-nastola')
def environment_artist_jobs66(page=1):

    job_list = job_obj.get_job("environment artist ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="nastola")
	
@environment_artist.route('/environment-artist-jobs-orimattila')
def environment_artist_jobs67(page=1):

    job_list = job_obj.get_job("environment artist ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="orimattila")
	
@environment_artist.route('/environment-artist-jobs-kauhajoki')
def environment_artist_jobs68(page=1):

    job_list = job_obj.get_job("environment artist ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kauhajoki")
	
@environment_artist.route('/environment-artist-jobs-ekenas')
def environment_artist_jobs69(page=1):

    job_list = job_obj.get_job("environment artist ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="ekenas")
	
@environment_artist.route('/environment-artist-jobs-kempele')
def environment_artist_jobs70(page=1):

    job_list = job_obj.get_job("environment artist ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kempele")
	
@environment_artist.route('/environment-artist-jobs-lapua')
def environment_artist_jobs71(page=1):

    job_list = job_obj.get_job("environment artist ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lapua")
	
@environment_artist.route('/environment-artist-jobs-lieksa')
def environment_artist_jobs72(page=1):

    job_list = job_obj.get_job("environment artist ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="lieksa")
	
@environment_artist.route('/environment-artist-jobs-naantali')
def environment_artist_jobs73(page=1):

    job_list = job_obj.get_job("environment artist ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="naantali")
	
@environment_artist.route('/environment-artist-jobs-aanekoski')
def environment_artist_jobs74(page=1):

    job_list = job_obj.get_job("environment artist ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="aanekoski")
	
@environment_artist.route('/environment-artist-jobs-ylivieska')
def environment_artist_jobs75(page=1):

    job_list = job_obj.get_job("environment artist ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="ylivieska")
	
@environment_artist.route('/environment-artist-jobs-kontiolahti')
def environment_artist_jobs76(page=1):

    job_list = job_obj.get_job("environment artist ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kontiolahti")
	
@environment_artist.route('/environment-artist-jobs-kankaanpaa')
def environment_artist_jobs77(page=1):

    job_list = job_obj.get_job("environment artist ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kankaanpaa")
	
@environment_artist.route('/environment-artist-jobs-ulvila')
def environment_artist_jobs78(page=1):

    job_list = job_obj.get_job("environment artist ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="ulvila")
	
@environment_artist.route('/environment-artist-jobs-pieksamaki')
def environment_artist_jobs79(page=1):

    job_list = job_obj.get_job("environment artist ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="pieksamaki")
	
@environment_artist.route('/environment-artist-jobs-kiiminki')
def environment_artist_jobs80(page=1):

    job_list = job_obj.get_job("environment artist ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kiiminki")
	
@environment_artist.route('/environment-artist-jobs-pargas')
def environment_artist_jobs81(page=1):

    job_list = job_obj.get_job("environment artist ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="pargas")
	
@environment_artist.route('/environment-artist-jobs-nurmo')
def environment_artist_jobs82(page=1):

    job_list = job_obj.get_job("environment artist ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="nurmo")
	
@environment_artist.route('/environment-artist-jobs-ilmajoki')
def environment_artist_jobs83(page=1):

    job_list = job_obj.get_job("environment artist ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="ilmajoki")
	
@environment_artist.route('/environment-artist-jobs-liperi')
def environment_artist_jobs84(page=1):

    job_list = job_obj.get_job("environment artist ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="liperi")
	
@environment_artist.route('/environment-artist-jobs-keuruu')
def environment_artist_jobs85(page=1):

    job_list = job_obj.get_job("environment artist ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="keuruu")
	
@environment_artist.route('/environment-artist-jobs-leppavirta')
def environment_artist_jobs86(page=1):

    job_list = job_obj.get_job("environment artist ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="leppavirta")
	
@environment_artist.route('/environment-artist-jobs-kurikka')
def environment_artist_jobs87(page=1):

    job_list = job_obj.get_job("environment artist ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kurikka")
	
@environment_artist.route('/environment-artist-jobs-nivala')
def environment_artist_jobs88(page=1):

    job_list = job_obj.get_job("environment artist ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="nivala")
	
@environment_artist.route('/environment-artist-jobs-joutseno')
def environment_artist_jobs89(page=1):

    job_list = job_obj.get_job("environment artist ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="joutseno")
	
@environment_artist.route('/environment-artist-jobs-pedersore')
def environment_artist_jobs90(page=1):

    job_list = job_obj.get_job("environment artist ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="pedersore")
	
@environment_artist.route('/environment-artist-jobs-sotkamo')
def environment_artist_jobs91(page=1):

    job_list = job_obj.get_job("environment artist ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="sotkamo")
	
@environment_artist.route('/environment-artist-jobs-kuhmo')
def environment_artist_jobs92(page=1):

    job_list = job_obj.get_job("environment artist ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="kuhmo")
	
@environment_artist.route('/environment-artist-jobs-paimio')
def environment_artist_jobs93(page=1):

    job_list = job_obj.get_job("environment artist ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="paimio")
	
@environment_artist.route('/environment-artist-jobs-saarijarvi')
def environment_artist_jobs94(page=1):

    job_list = job_obj.get_job("environment artist ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="saarijarvi")
	
@environment_artist.route('/environment-artist-jobs-helsinki')
def environment_artist_jobs95(page=1):

    job_list = job_obj.get_job("environment artist ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist ", location="helsinki")


####################################################################


##############################################
@environment_artist.route('/environment-artist-tyopaikat-espoo')
def environment_artist_tyopaikat2(page=1):

    job_list = job_obj.get_job("environment artist", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="espoo")

@environment_artist.route('/environment-artist-tyopaikat-tampere')
def environment_artist_tyopaikat3(page=1):

    job_list = job_obj.get_job("environment artist", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="tampere")
	
@environment_artist.route('/environment-artist-tyopaikat-vantaa')
def environment_artist_tyopaikat4(page=1):

    job_list = job_obj.get_job("environment artist", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="vantaa")
	
@environment_artist.route('/environment-artist-tyopaikat-turku')
def environment_artist_tyopaikat5(page=1):

    job_list = job_obj.get_job("environment artist", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="turku")
	
@environment_artist.route('/environment-artist-tyopaikat-oulu')
def environment_artist_tyopaikat6(page=1):

    job_list = job_obj.get_job("environment artist", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="oulu")
	
@environment_artist.route('/environment-artist-tyopaikat-lahti')
def environment_artist_tyopaikat7(page=1):

    job_list = job_obj.get_job("environment artist", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="lahti")
	
@environment_artist.route('/environment-artist-tyopaikat-kuopio')
def environment_artist_tyopaikat8(page=1):

    job_list = job_obj.get_job("environment artist", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kuopio")
	
@environment_artist.route('/environment-artist-tyopaikat-jyvvaskyla')
def environment_artist_tyopaikat9(page=1):

    job_list = job_obj.get_job("environment artist", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="jyvvaskyla")

@environment_artist.route('/environment-artist-tyopaikat-pori')
def environment_artist_tyopaikat10(page=1):

    job_list = job_obj.get_job("environment artist", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="pori")

@environment_artist.route('/environment-artist-tyopaikat-lappeenranta')
def environment_artist_tyopaikat11(page=1):

    job_list = job_obj.get_job("environment artist", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="lappeenranta")	
	
@environment_artist.route('/environment-artist-tyopaikat-vaasa')
def environment_artist_tyopaikat12(page=1):

    job_list = job_obj.get_job("environment artist", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="vaasa")
	
@environment_artist.route('/environment-artist-tyopaikat-kotka')
def environment_artist_tyopaikat13(page=1):

    job_list = job_obj.get_job("environment artist", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kotka")
	
@environment_artist.route('/environment-artist-tyopaikat-joensuu')
def environment_artist_tyopaikat14(page=1):

    job_list = job_obj.get_job("environment artist", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="joensuu")
	
@environment_artist.route('/environment-artist-tyopaikat-hameenlinna')
def environment_artist_tyopaikat15(page=1):

    job_list = job_obj.get_job("environment artist", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="hameenlinna")
	
@environment_artist.route('/environment-artist-tyopaikat-porvoo')
def environment_artist_tyopaikat16(page=1):

    job_list = job_obj.get_job("environment artist", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="porvoo")
	
@environment_artist.route('/environment-artist-tyopaikat-mikkeli')
def environment_artist_tyopaikat17(page=1):

    job_list = job_obj.get_job("environment artist", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="mikkeli")

@environment_artist.route('/environment-artist-tyopaikat-hyvinkaa')
def environment_artist_tyopaikat18(page=1):

    job_list = job_obj.get_job("environment artist", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="hyvinkaa")
	
@environment_artist.route('/environment-artist-tyopaikat-nurmijarvi')
def environment_artist_tyopaikat19(page=1):

    job_list = job_obj.get_job("environment artist", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="nurmijarvi")

@environment_artist.route('/environment-artist-tyopaikat-jarvenpaa')
def environment_artist_tyopaikat20(page=1):

    job_list = job_obj.get_job("environment artist", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="jarvenpaa")
	
@environment_artist.route('/environment-artist-tyopaikat-rauma')
def environment_artist_tyopaikat21(page=1):

    job_list = job_obj.get_job("environment artist", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="rauma")
	
@environment_artist.route('/environment-artist-tyopaikat-lohja')
def environment_artist_tyopaikat22(page=1):

    job_list = job_obj.get_job("environment artist", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="lohja")
	
@environment_artist.route('/environment-artist-tyopaikat-karleby')
def environment_artist_tyopaikat23(page=1):

    job_list = job_obj.get_job("environment artist", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="karleby")
	
@environment_artist.route('/environment-artist-tyopaikat-kajaani')
def environment_artist_tyopaikat24(page=1):

    job_list = job_obj.get_job("environment artist", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kajaani")
	
@environment_artist.route('/environment-artist-tyopaikat-rovaniemi')
def environment_artist_tyopaikat25(page=1):

    job_list = job_obj.get_job("environment artist", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="rovaniemi")
	
@environment_artist.route('/environment-artist-tyopaikat-tuusula')
def environment_artist_tyopaikat26(page=1):

    job_list = job_obj.get_job("environment artist", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="tuusula")
	
@environment_artist.route('/environment-artist-tyopaikat-kirkkonummi')
def environment_artist_tyopaikat27(page=1):

    job_list = job_obj.get_job("environment artist", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kirkkonummi")
	
@environment_artist.route('/environment-artist-tyopaikat-seinajoki')
def environment_artist_tyopaikat28(page=1):

    job_list = job_obj.get_job("environment artist", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="seinajoki")
	
@environment_artist.route('/environment-artist-tyopaikat-kerava')
def environment_artist_tyopaikat29(page=1):

    job_list = job_obj.get_job("environment artist", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kerava")
	
@environment_artist.route('/environment-artist-tyopaikat-kouvola')
def environment_artist_tyopaikat30(page=1):

    job_list = job_obj.get_job("environment artist", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kouvola")
	
@environment_artist.route('/environment-artist-tyopaikat-imatra')
def environment_artist_tyopaikat31(page=1):

    job_list = job_obj.get_job("environment artist", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="imatra")
	
@environment_artist.route('/environment-artist-tyopaikat-nokia')
def environment_artist_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("environment artist", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="nokia")
	
@environment_artist.route('/environment-artist-tyopaikat-savonlinna')
def environment_artist_tyopaikat32(page=1):

    job_list = job_obj.get_job("environment artist", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="savonlinna")
	
@environment_artist.route('/environment-artist-tyopaikat-riihimaki')
def environment_artist_tyopaikat33(page=1):

    job_list = job_obj.get_job("environment artist", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="riihimaki")
	
@environment_artist.route('/environment-artist-tyopaikat-vihti')
def environment_artist_tyopaikat34(page=1):

    job_list = job_obj.get_job("environment artist", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="vihti")
	
@environment_artist.route('/environment-artist-tyopaikat-salo')
def environment_artist_tyopaikat35(page=1):

    job_list = job_obj.get_job("environment artist", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="salo")
	
@environment_artist.route('/environment-artist-tyopaikat-kangasala')
def environment_artist_tyopaikat36(page=1):

    job_list = job_obj.get_job("environment artist", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kangasala")
	
@environment_artist.route('/environment-artist-tyopaikat-raisio')
def environment_artist_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("environment artist", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="raisio")
	
@environment_artist.route('/environment-artist-tyopaikat-karhula')
def environment_artist_tyopaikat37(page=1):

    job_list = job_obj.get_job("environment artist", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="karhula")
	
@environment_artist.route('/environment-artist-tyopaikat-kemi')
def environment_artist_tyopaikat38(page=1):

    job_list = job_obj.get_job("environment artist", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kemi")
	
@environment_artist.route('/environment-artist-tyopaikat-iisalmi')
def environment_artist_tyopaikat39(page=1):

    job_list = job_obj.get_job("environment artist", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="iisalmi")
	
@environment_artist.route('/environment-artist-tyopaikat-varkaus')
def environment_artist_tyopaikat40(page=1):

    job_list = job_obj.get_job("environment artist", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="varkaus")
	
@environment_artist.route('/environment-artist-tyopaikat-raahe')
def environment_artist_tyopaikat41(page=1):

    job_list = job_obj.get_job("environment artist", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="raahe")
	
@environment_artist.route('/environment-artist-tyopaikat-ylojarvi')
def environment_artist_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("environment artist", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="ylojarvi")
	
@environment_artist.route('/environment-artist-tyopaikat-hamina')
def environment_artist_tyopaikat42(page=1):

    job_list = job_obj.get_job("environment artist", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="hamina")
	
@environment_artist.route('/environment-artist-tyopaikat-kaarina')
def environment_artist_tyopaikat43(page=1):

    job_list = job_obj.get_job("environment artist", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kaarina")
	
@environment_artist.route('/environment-artist-tyopaikat-tornio')
def environment_artist_tyopaikat44(page=1):

    job_list = job_obj.get_job("environment artist", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="tornio")
	
@environment_artist.route('/environment-artist-tyopaikat-heinola')
def environment_artist_tyopaikat45(page=1):

    job_list = job_obj.get_job("environment artist", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="heinola")
	
@environment_artist.route('/environment-artist-tyopaikat-hollola')
def environment_artist_tyopaikat46(page=1):

    job_list = job_obj.get_job("environment artist", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="hollola")
	
@environment_artist.route('/environment-artist-tyopaikat-valkeakoski')
def environment_artist_tyopaikat47(page=1):

    job_list = job_obj.get_job("environment artist", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="valkeakoski")
	
@environment_artist.route('/environment-artist-tyopaikat-siilinjarvi')
def environment_artist_tyopaikat48(page=1):

    job_list = job_obj.get_job("environment artist", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="siilinjarvi")
	
@environment_artist.route('/environment-artist-tyopaikat-kuusankoski')
def environment_artist_tyopaikat49(page=1):

    job_list = job_obj.get_job("environment artist", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kuusankoski")
	
@environment_artist.route('/environment-artist-tyopaikat-sibbo')
def environment_artist_tyopaikat50(page=1):

    job_list = job_obj.get_job("environment artist", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="sibbo")
	
@environment_artist.route('/environment-artist-tyopaikat-jakostad')
def environment_artist_tyopaikat51(page=1):

    job_list = job_obj.get_job("environment artist", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="jakostad")
	
@environment_artist.route('/environment-artist-tyopaikat-lempaala')
def environment_artist_tyopaikat52(page=1):

    job_list = job_obj.get_job("environment artist", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="lempaala")
	
@environment_artist.route('/environment-artist-tyopaikat-mantsala')
def environment_artist_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("environment artist", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="mantsala")
	
@environment_artist.route('/environment-artist-tyopaikat-forssa')
def environment_artist_tyopaikat53(page=1):

    job_list = job_obj.get_job("environment artist", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="forssa")
	
@environment_artist.route('/environment-artist-tyopaikat-kuusamo')
def environment_artist_tyopaikat54(page=1):

    job_list = job_obj.get_job("environment artist", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kuusamo")
	
@environment_artist.route('/environment-artist-tyopaikat-haukipudas')
def environment_artist_tyopaikat55(page=1):

    job_list = job_obj.get_job("environment artist", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="haukipudas")
	
@environment_artist.route('/environment-artist-tyopaikat-korsholm')
def environment_artist_tyopaikat56(page=1):

    job_list = job_obj.get_job("environment artist", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="korsholm")
	
@environment_artist.route('/environment-artist-tyopaikat-laukaa')
def environment_artist_tyopaikat57(page=1):

    job_list = job_obj.get_job("environment artist", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="laukaa")
	
@environment_artist.route('/environment-artist-tyopaikat-anjala')
def environment_artist_tyopaikat58(page=1):

    job_list = job_obj.get_job("environment artist", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="anjala")
	
@environment_artist.route('/environment-artist-tyopaikat-uusikaupunki')
def environment_artist_tyopaikat59(page=1):

    job_list = job_obj.get_job("environment artist", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="uusikaupunki")
	
@environment_artist.route('/environment-artist-tyopaikat-janakkala')
def environment_artist_tyopaikat60(page=1):

    job_list = job_obj.get_job("environment artist", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="janakkala")
	
@environment_artist.route('/environment-artist-tyopaikat-pirkkala')
def environment_artist_tyopaikat61(page=1):

    job_list = job_obj.get_job("environment artist", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="pirkkala")
	
@environment_artist.route('/environment-artist-tyopaikat-lansi-turunmaa')
def environment_artist_tyopaikat62(page=1):

    job_list = job_obj.get_job("environment artist", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="lansi-turunmaa")
	
@environment_artist.route('/environment-artist-tyopaikat-jamsa')
def environment_artist_tyopaikat63(page=1):

    job_list = job_obj.get_job("environment artist", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="jamsa")
	
@environment_artist.route('/environment-artist-tyopaikat-jamsa')
def environment_artist_tyopaikat64(page=1):

    job_list = job_obj.get_job("environment artist", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="jamsa")
	
@environment_artist.route('/environment-artist-tyopaikat-vammala')
def environment_artist_tyopaikat65(page=1):

    job_list = job_obj.get_job("environment artist", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="vammala")
	
@environment_artist.route('/environment-artist-tyopaikat-nastola')
def environment_artist_tyopaikat66(page=1):

    job_list = job_obj.get_job("environment artist", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="nastola")
	
@environment_artist.route('/environment-artist-tyopaikat-orimattila')
def environment_artist_tyopaikat67(page=1):

    job_list = job_obj.get_job("environment artist", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="orimattila")
	
@environment_artist.route('/environment-artist-tyopaikat-kauhajoki')
def environment_artist_tyopaikat68(page=1):

    job_list = job_obj.get_job("environment artist", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kauhajoki")
	
@environment_artist.route('/environment-artist-tyopaikat-ekenas')
def environment_artist_tyopaikat69(page=1):

    job_list = job_obj.get_job("environment artist", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="ekenas")
	
@environment_artist.route('/environment-artist-tyopaikat-kempele')
def environment_artist_tyopaikat70(page=1):

    job_list = job_obj.get_job("environment artist", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kempele")
	
@environment_artist.route('/environment-artist-tyopaikat-lapua')
def environment_artist_tyopaikat71(page=1):

    job_list = job_obj.get_job("environment artist", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="lapua")
	
@environment_artist.route('/environment-artist-tyopaikat-lieksa')
def environment_artist_tyopaikat72(page=1):

    job_list = job_obj.get_job("environment artist", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="lieksa")
	
@environment_artist.route('/environment-artist-tyopaikat-naantali')
def environment_artist_tyopaikat73(page=1):

    job_list = job_obj.get_job("environment artist", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="naantali")
	
@environment_artist.route('/environment-artist-tyopaikat-aanekoski')
def environment_artist_tyopaikat74(page=1):

    job_list = job_obj.get_job("environment artist", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="aanekoski")
	
@environment_artist.route('/environment-artist-tyopaikat-ylivieska')
def environment_artist_tyopaikat75(page=1):

    job_list = job_obj.get_job("environment artist", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="ylivieska")
	
@environment_artist.route('/environment-artist-tyopaikat-kontiolahti')
def environment_artist_tyopaikat76(page=1):

    job_list = job_obj.get_job("environment artist", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kontiolahti")
	
@environment_artist.route('/environment-artist-tyopaikat-kankaanpaa')
def environment_artist_tyopaikat77(page=1):

    job_list = job_obj.get_job("environment artist", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kankaanpaa")
	
@environment_artist.route('/environment-artist-tyopaikat-ulvila')
def environment_artist_tyopaikat78(page=1):

    job_list = job_obj.get_job("environment artist", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="ulvila")
	
@environment_artist.route('/environment-artist-tyopaikat-pieksamaki')
def environment_artist_tyopaikat79(page=1):

    job_list = job_obj.get_job("environment artist", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="pieksamaki")
	
@environment_artist.route('/environment-artist-tyopaikat-kiiminki')
def environment_artist_tyopaikat80(page=1):

    job_list = job_obj.get_job("environment artist", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kiiminki")
	
@environment_artist.route('/environment-artist-tyopaikat-pargas')
def environment_artist_tyopaikat81(page=1):

    job_list = job_obj.get_job("environment artist", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="pargas")
	
@environment_artist.route('/environment-artist-tyopaikat-nurmo')
def environment_artist_tyopaikat82(page=1):

    job_list = job_obj.get_job("environment artist", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="nurmo")
	
@environment_artist.route('/environment-artist-tyopaikat-ilmajoki')
def environment_artist_tyopaikat83(page=1):

    job_list = job_obj.get_job("environment artist", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="ilmajoki")
	
@environment_artist.route('/environment-artist-tyopaikat-liperi')
def environment_artist_tyopaikat84(page=1):

    job_list = job_obj.get_job("environment artist", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="liperi")
	
@environment_artist.route('/environment-artist-tyopaikat-keuruu')
def environment_artist_tyopaikat85(page=1):

    job_list = job_obj.get_job("environment artist", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="keuruu")
	
@environment_artist.route('/environment-artist-tyopaikat-leppavirta')
def environment_artist_tyopaikat86(page=1):

    job_list = job_obj.get_job("environment artist", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="leppavirta")
	
@environment_artist.route('/environment-artist-tyopaikat-kurikka')
def environment_artist_tyopaikat87(page=1):

    job_list = job_obj.get_job("environment artist", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kurikka")
	
@environment_artist.route('/environment-artist-tyopaikat-nivala')
def environment_artist_tyopaikat88(page=1):

    job_list = job_obj.get_job("environment artist", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="nivala")
	
@environment_artist.route('/environment-artist-tyopaikat-joutseno')
def environment_artist_tyopaikat89(page=1):

    job_list = job_obj.get_job("environment artist", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="joutseno")
	
@environment_artist.route('/environment-artist-tyopaikat-pedersore')
def environment_artist_tyopaikat90(page=1):

    job_list = job_obj.get_job("environment artist", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="pedersore")
	
@environment_artist.route('/environment-artist-tyopaikat-sotkamo')
def environment_artist_tyopaikat91(page=1):

    job_list = job_obj.get_job("environment artist", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="sotkamo")
	
@environment_artist.route('/environment-artist-tyopaikat-kuhmo')
def environment_artist_tyopaikat92(page=1):

    job_list = job_obj.get_job("environment artist", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="kuhmo")
	
@environment_artist.route('/environment-artist-tyopaikat-paimio')
def environment_artist_tyopaikat93(page=1):

    job_list = job_obj.get_job("environment artist", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="paimio")
	
@environment_artist.route('/environment-artist-tyopaikat-saarijarvi')
def environment_artist_tyopaikat94(page=1):

    job_list = job_obj.get_job("environment artist", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist", location="saarijarvi")
	
@environment_artist.route('/environment-artist-tyopaikat-helsinki')
def environment_artist_tyopaikat95(page=1):

    job_list = job_obj.get_job("environment artist", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="environment artist  ", location="helsinki")
	  

