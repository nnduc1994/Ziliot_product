from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

concept_artist = Blueprint('concept_artist', __name__)
job_obj = Job()



####################################################################


@concept_artist.route('/concept-artist_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "concept-artist" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@concept_artist.route('/concept-artist-avoimet-tyopaikat-espoo')
def concept_artist_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("concept artist ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="espoo")

@concept_artist.route('/concept-artist-avoimet-tyopaikat-tampere')
def concept_artist_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("concept artist ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="tampere")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-vantaa')
def concept_artist_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("concept artist ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="vantaa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-turku')
def concept_artist_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("concept artist ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="turku")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-oulu')
def concept_artist_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("concept artist ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="oulu")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-lahti')
def concept_artist_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("concept artist ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lahti")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kuopio')
def concept_artist_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("concept artist ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kuopio")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-jyvvaskyla')
def concept_artist_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("concept artist ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="jyvvaskyla")

@concept_artist.route('/concept-artist-avoimet-tyopaikat-pori')
def concept_artist_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("concept artist ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="pori")

@concept_artist.route('/concept-artist-avoimet-tyopaikat-lappeenranta')
def concept_artist_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("concept artist ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lappeenranta")	
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-vaasa')
def concept_artist_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("concept artist ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="vaasa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kotka')
def concept_artist_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("concept artist ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kotka")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-joensuu')
def concept_artist_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("concept artist ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="joensuu")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-hameenlinna')
def concept_artist_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("concept artist ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="hameenlinna")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-porvoo')
def concept_artist_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("concept artist ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="porvoo")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-mikkeli')
def concept_artist_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("concept artist ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="mikkeli")

@concept_artist.route('/concept-artist-avoimet-tyopaikat-hyvinkaa')
def concept_artist_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("concept artist ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="hyvinkaa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-nurmijarvi')
def concept_artist_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("concept artist ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="nurmijarvi")

@concept_artist.route('/concept-artist-avoimet-tyopaikat-jarvenpaa')
def concept_artist_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("concept artist ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="jarvenpaa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-rauma')
def concept_artist_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("concept artist ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="rauma")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-lohja')
def concept_artist_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("concept artist ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lohja")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-karleby')
def concept_artist_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("concept artist ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="karleby")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kajaani')
def concept_artist_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("concept artist ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kajaani")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-rovaniemi')
def concept_artist_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("concept artist ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="rovaniemi")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-tuusula')
def concept_artist_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("concept artist ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="tuusula")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kirkkonummi')
def concept_artist_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("concept artist ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kirkkonummi")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-seinajoki')
def concept_artist_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("concept artist ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="seinajoki")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kerava')
def concept_artist_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("concept artist ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kerava")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kouvola')
def concept_artist_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("concept artist ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kouvola")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-imatra')
def concept_artist_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("concept artist ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="imatra")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-nokia')
def concept_artist_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("concept artist ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="nokia")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-savonlinna')
def concept_artist_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("concept artist ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="savonlinna")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-riihimaki')
def concept_artist_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("concept artist ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="riihimaki")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-vihti')
def concept_artist_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("concept artist ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="vihti")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-salo')
def concept_artist_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("concept artist ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="salo")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kangasala')
def concept_artist_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("concept artist ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kangasala")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-raisio')
def concept_artist_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("concept artist ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="raisio")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-karhula')
def concept_artist_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("concept artist ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="karhula")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kemi')
def concept_artist_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("concept artist ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kemi")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-iisalmi')
def concept_artist_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("concept artist ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="iisalmi")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-varkaus')
def concept_artist_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("concept artist ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="varkaus")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-raahe')
def concept_artist_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("concept artist ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="raahe")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-ylojarvi')
def concept_artist_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("concept artist ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="ylojarvi")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-hamina')
def concept_artist_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("concept artist ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="hamina")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kaarina')
def concept_artist_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("concept artist ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kaarina")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-tornio')
def concept_artist_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("concept artist ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="tornio")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-heinola')
def concept_artist_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("concept artist ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="heinola")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-hollola')
def concept_artist_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("concept artist ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="hollola")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-valkeakoski')
def concept_artist_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("concept artist ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="valkeakoski")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-siilinjarvi')
def concept_artist_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("concept artist ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="siilinjarvi")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kuusankoski')
def concept_artist_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("concept artist ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kuusankoski")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-sibbo')
def concept_artist_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("concept artist ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="sibbo")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-jakostad')
def concept_artist_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("concept artist ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="jakostad")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-lempaala')
def concept_artist_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("concept artist ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lempaala")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-mantsala')
def concept_artist_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("concept artist ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="mantsala")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-forssa')
def concept_artist_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("concept artist ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="forssa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kuusamo')
def concept_artist_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("concept artist ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kuusamo")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-haukipudas')
def concept_artist_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("concept artist ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="haukipudas")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-korsholm')
def concept_artist_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("concept artist ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="korsholm")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-laukaa')
def concept_artist_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("concept artist ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="laukaa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-anjala')
def concept_artist_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("concept artist ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="anjala")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-uusikaupunki')
def concept_artist_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("concept artist ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="uusikaupunki")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-janakkala')
def concept_artist_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("concept artist ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="janakkala")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-pirkkala')
def concept_artist_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("concept artist ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="pirkkala")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-lansi-turunmaa')
def concept_artist_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("concept artist ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lansi-turunmaa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-jamsa')
def concept_artist_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("concept artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="jamsa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-jamsa')
def concept_artist_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("concept artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="jamsa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-vammala')
def concept_artist_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("concept artist ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="vammala")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-nastola')
def concept_artist_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("concept artist ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="nastola")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-orimattila')
def concept_artist_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("concept artist ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="orimattila")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kauhajoki')
def concept_artist_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("concept artist ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kauhajoki")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-ekenas')
def concept_artist_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("concept artist ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="ekenas")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kempele')
def concept_artist_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("concept artist ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kempele")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-lapua')
def concept_artist_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("concept artist ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lapua")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-lieksa')
def concept_artist_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("concept artist ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lieksa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-naantali')
def concept_artist_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("concept artist ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="naantali")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-aanekoski')
def concept_artist_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("concept artist ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="aanekoski")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-ylivieska')
def concept_artist_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("concept artist ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="ylivieska")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kontiolahti')
def concept_artist_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("concept artist ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kontiolahti")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kankaanpaa')
def concept_artist_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("concept artist ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kankaanpaa")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-ulvila')
def concept_artist_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("concept artist ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="ulvila")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-pieksamaki')
def concept_artist_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("concept artist ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="pieksamaki")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kiiminki')
def concept_artist_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("concept artist ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kiiminki")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-pargas')
def concept_artist_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("concept artist ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="pargas")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-nurmo')
def concept_artist_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("concept artist ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="nurmo")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-ilmajoki')
def concept_artist_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("concept artist ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="ilmajoki")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-liperi')
def concept_artist_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("concept artist ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="liperi")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-keuruu')
def concept_artist_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("concept artist ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="keuruu")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-leppavirta')
def concept_artist_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("concept artist ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="leppavirta")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kurikka')
def concept_artist_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("concept artist ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kurikka")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-nivala')
def concept_artist_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("concept artist ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="nivala")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-joutseno')
def concept_artist_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("concept artist ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="joutseno")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-pedersore')
def concept_artist_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("concept artist ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="pedersore")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-sotkamo')
def concept_artist_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("concept artist ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="sotkamo")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-kuhmo')
def concept_artist_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("concept artist ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kuhmo")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-paimio')
def concept_artist_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("concept artist ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="paimio")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-saarijarvi')
def concept_artist_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("concept artist ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="saarijarvi")
	
@concept_artist.route('/concept-artist-avoimet-tyopaikat-helsinki')
def concept_artist_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("concept artist ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="helsinki")


####################################################################


##############################################
@concept_artist.route('/concept-artist-jobs-espoo')
def concept_artist_jobs2(page=1):

    job_list = job_obj.get_job("concept artist ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="espoo")

@concept_artist.route('/concept-artist-jobs-tampere')
def concept_artist_jobs3(page=1):

    job_list = job_obj.get_job("concept artist ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="tampere")
	
@concept_artist.route('/concept-artist-jobs-vantaa')
def concept_artist_jobs4(page=1):

    job_list = job_obj.get_job("concept artist ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="vantaa")
	
@concept_artist.route('/concept-artist-jobs-turku')
def concept_artist_jobs5(page=1):

    job_list = job_obj.get_job("concept artist ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="turku")
	
@concept_artist.route('/concept-artist-jobs-oulu')
def concept_artist_jobs6(page=1):

    job_list = job_obj.get_job("concept artist ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="oulu")
	
@concept_artist.route('/concept-artist-jobs-lahti')
def concept_artist_jobs7(page=1):

    job_list = job_obj.get_job("concept artist ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lahti")
	
@concept_artist.route('/concept-artist-jobs-kuopio')
def concept_artist_jobs8(page=1):

    job_list = job_obj.get_job("concept artist ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kuopio")
	
@concept_artist.route('/concept-artist-jobs-jyvvaskyla')
def concept_artist_jobs9(page=1):

    job_list = job_obj.get_job("concept artist ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="jyvvaskyla")

@concept_artist.route('/concept-artist-jobs-pori')
def concept_artist_jobs10(page=1):

    job_list = job_obj.get_job("concept artist ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="pori")

@concept_artist.route('/concept-artist-jobs-lappeenranta')
def concept_artist_jobs11(page=1):

    job_list = job_obj.get_job("concept artist ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lappeenranta")	
	
@concept_artist.route('/concept-artist-jobs-vaasa')
def concept_artist_jobs12(page=1):

    job_list = job_obj.get_job("concept artist ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="vaasa")
	
@concept_artist.route('/concept-artist-jobs-kotka')
def concept_artist_jobs13(page=1):

    job_list = job_obj.get_job("concept artist ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kotka")
	
@concept_artist.route('/concept-artist-jobs-joensuu')
def concept_artist_jobs14(page=1):

    job_list = job_obj.get_job("concept artist ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="joensuu")
	
@concept_artist.route('/concept-artist-jobs-hameenlinna')
def concept_artist_jobs15(page=1):

    job_list = job_obj.get_job("concept artist ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="hameenlinna")
	
@concept_artist.route('/concept-artist-jobs-porvoo')
def concept_artist_jobs16(page=1):

    job_list = job_obj.get_job("concept artist ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="porvoo")
	
@concept_artist.route('/concept-artist-jobs-mikkeli')
def concept_artist_jobs17(page=1):

    job_list = job_obj.get_job("concept artist ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="mikkeli")

@concept_artist.route('/concept-artist-jobs-hyvinkaa')
def concept_artist_jobs18(page=1):

    job_list = job_obj.get_job("concept artist ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="hyvinkaa")
	
@concept_artist.route('/concept-artist-jobs-nurmijarvi')
def concept_artist_jobs19(page=1):

    job_list = job_obj.get_job("concept artist ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="nurmijarvi")

@concept_artist.route('/concept-artist-jobs-jarvenpaa')
def concept_artist_jobs20(page=1):

    job_list = job_obj.get_job("concept artist ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="jarvenpaa")
	
@concept_artist.route('/concept-artist-jobs-rauma')
def concept_artist_jobs21(page=1):

    job_list = job_obj.get_job("concept artist ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="rauma")
	
@concept_artist.route('/concept-artist-jobs-lohja')
def concept_artist_jobs22(page=1):

    job_list = job_obj.get_job("concept artist ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lohja")
	
@concept_artist.route('/concept-artist-jobs-karleby')
def concept_artist_jobs23(page=1):

    job_list = job_obj.get_job("concept artist ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="karleby")
	
@concept_artist.route('/concept-artist-jobs-kajaani')
def concept_artist_jobs24(page=1):

    job_list = job_obj.get_job("concept artist ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kajaani")
	
@concept_artist.route('/concept-artist-jobs-rovaniemi')
def concept_artist_jobs25(page=1):

    job_list = job_obj.get_job("concept artist ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="rovaniemi")
	
@concept_artist.route('/concept-artist-jobs-tuusula')
def concept_artist_jobs26(page=1):

    job_list = job_obj.get_job("concept artist ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="tuusula")
	
@concept_artist.route('/concept-artist-jobs-kirkkonummi')
def concept_artist_jobs27(page=1):

    job_list = job_obj.get_job("concept artist ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kirkkonummi")
	
@concept_artist.route('/concept-artist-jobs-seinajoki')
def concept_artist_jobs28(page=1):

    job_list = job_obj.get_job("concept artist ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="seinajoki")
	
@concept_artist.route('/concept-artist-jobs-kerava')
def concept_artist_jobs29(page=1):

    job_list = job_obj.get_job("concept artist ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kerava")
	
@concept_artist.route('/concept-artist-jobs-kouvola')
def concept_artist_jobs30(page=1):

    job_list = job_obj.get_job("concept artist ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kouvola")
	
@concept_artist.route('/concept-artist-jobs-imatra')
def concept_artist_jobs31(page=1):

    job_list = job_obj.get_job("concept artist ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="imatra")
	
@concept_artist.route('/concept-artist-jobs-nokia')
def concept_artist_jobs32_1(page=1):

    job_list = job_obj.get_job("concept artist ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="nokia")
	
@concept_artist.route('/concept-artist-jobs-savonlinna')
def concept_artist_jobs32(page=1):

    job_list = job_obj.get_job("concept artist ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="savonlinna")
	
@concept_artist.route('/concept-artist-jobs-riihimaki')
def concept_artist_jobs33(page=1):

    job_list = job_obj.get_job("concept artist ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="riihimaki")
	
@concept_artist.route('/concept-artist-jobs-vihti')
def concept_artist_jobs34(page=1):

    job_list = job_obj.get_job("concept artist ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="vihti")
	
@concept_artist.route('/concept-artist-jobs-salo')
def concept_artist_jobs35(page=1):

    job_list = job_obj.get_job("concept artist ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="salo")
	
@concept_artist.route('/concept-artist-jobs-kangasala')
def concept_artist_jobs36(page=1):

    job_list = job_obj.get_job("concept artist ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kangasala")
	
@concept_artist.route('/concept-artist-jobs-raisio')
def concept_artist_jobs37_1(page=1):

    job_list = job_obj.get_job("concept artist ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="raisio")
	
@concept_artist.route('/concept-artist-jobs-karhula')
def concept_artist_jobs37(page=1):

    job_list = job_obj.get_job("concept artist ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="karhula")
	
@concept_artist.route('/concept-artist-jobs-kemi')
def concept_artist_jobs38(page=1):

    job_list = job_obj.get_job("concept artist ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kemi")
	
@concept_artist.route('/concept-artist-jobs-iisalmi')
def concept_artist_jobs39(page=1):

    job_list = job_obj.get_job("concept artist ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="iisalmi")
	
@concept_artist.route('/concept-artist-jobs-varkaus')
def concept_artist_jobs40(page=1):

    job_list = job_obj.get_job("concept artist ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="varkaus")
	
@concept_artist.route('/concept-artist-jobs-raahe')
def concept_artist_jobs41(page=1):

    job_list = job_obj.get_job("concept artist ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="raahe")
	
@concept_artist.route('/concept-artist-jobs-ylojarvi')
def concept_artist_jobs42_1(page=1):

    job_list = job_obj.get_job("concept artist ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="ylojarvi")
	
@concept_artist.route('/concept-artist-jobs-hamina')
def concept_artist_jobs42(page=1):

    job_list = job_obj.get_job("concept artist ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="hamina")
	
@concept_artist.route('/concept-artist-jobs-kaarina')
def concept_artist_jobs43(page=1):

    job_list = job_obj.get_job("concept artist ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kaarina")
	
@concept_artist.route('/concept-artist-jobs-tornio')
def concept_artist_jobs44(page=1):

    job_list = job_obj.get_job("concept artist ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="tornio")
	
@concept_artist.route('/concept-artist-jobs-heinola')
def concept_artist_jobs45(page=1):

    job_list = job_obj.get_job("concept artist ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="heinola")
	
@concept_artist.route('/concept-artist-jobs-hollola')
def concept_artist_jobs46(page=1):

    job_list = job_obj.get_job("concept artist ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="hollola")
	
@concept_artist.route('/concept-artist-jobs-valkeakoski')
def concept_artist_jobs47(page=1):

    job_list = job_obj.get_job("concept artist ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="valkeakoski")
	
@concept_artist.route('/concept-artist-jobs-siilinjarvi')
def concept_artist_jobs48(page=1):

    job_list = job_obj.get_job("concept artist ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="siilinjarvi")
	
@concept_artist.route('/concept-artist-jobs-kuusankoski')
def concept_artist_jobs49(page=1):

    job_list = job_obj.get_job("concept artist ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kuusankoski")
	
@concept_artist.route('/concept-artist-jobs-sibbo')
def concept_artist_jobs50(page=1):

    job_list = job_obj.get_job("concept artist ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="sibbo")
	
@concept_artist.route('/concept-artist-jobs-jakostad')
def concept_artist_jobs51(page=1):

    job_list = job_obj.get_job("concept artist ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="jakostad")
	
@concept_artist.route('/concept-artist-jobs-lempaala')
def concept_artist_jobs52(page=1):

    job_list = job_obj.get_job("concept artist ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lempaala")
	
@concept_artist.route('/concept-artist-jobs-mantsala')
def concept_artist_jobs52_1(page=1):

    job_list = job_obj.get_job("concept artist ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="mantsala")
	
@concept_artist.route('/concept-artist-jobs-forssa')
def concept_artist_jobs53(page=1):

    job_list = job_obj.get_job("concept artist ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="forssa")
	
@concept_artist.route('/concept-artist-jobs-kuusamo')
def concept_artist_jobs54(page=1):

    job_list = job_obj.get_job("concept artist ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kuusamo")
	
@concept_artist.route('/concept-artist-jobs-haukipudas')
def concept_artist_jobs55(page=1):

    job_list = job_obj.get_job("concept artist ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="haukipudas")
	
@concept_artist.route('/concept-artist-jobs-korsholm')
def concept_artist_jobs56(page=1):

    job_list = job_obj.get_job("concept artist ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="korsholm")
	
@concept_artist.route('/concept-artist-jobs-laukaa')
def concept_artist_jobs57(page=1):

    job_list = job_obj.get_job("concept artist ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="laukaa")
	
@concept_artist.route('/concept-artist-jobs-anjala')
def concept_artist_jobs58(page=1):

    job_list = job_obj.get_job("concept artist ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="anjala")
	
@concept_artist.route('/concept-artist-jobs-uusikaupunki')
def concept_artist_jobs59(page=1):

    job_list = job_obj.get_job("concept artist ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="uusikaupunki")
	
@concept_artist.route('/concept-artist-jobs-janakkala')
def concept_artist_jobs60(page=1):

    job_list = job_obj.get_job("concept artist ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="janakkala")
	
@concept_artist.route('/concept-artist-jobs-pirkkala')
def concept_artist_jobs61(page=1):

    job_list = job_obj.get_job("concept artist ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="pirkkala")
	
@concept_artist.route('/concept-artist-jobs-lansi-turunmaa')
def concept_artist_jobs62(page=1):

    job_list = job_obj.get_job("concept artist ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lansi-turunmaa")
	
@concept_artist.route('/concept-artist-jobs-jamsa')
def concept_artist_jobs63(page=1):

    job_list = job_obj.get_job("concept artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="jamsa")
	
@concept_artist.route('/concept-artist-jobs-jamsa')
def concept_artist_jobs64(page=1):

    job_list = job_obj.get_job("concept artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="jamsa")
	
@concept_artist.route('/concept-artist-jobs-vammala')
def concept_artist_jobs65(page=1):

    job_list = job_obj.get_job("concept artist ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="vammala")
	
@concept_artist.route('/concept-artist-jobs-nastola')
def concept_artist_jobs66(page=1):

    job_list = job_obj.get_job("concept artist ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="nastola")
	
@concept_artist.route('/concept-artist-jobs-orimattila')
def concept_artist_jobs67(page=1):

    job_list = job_obj.get_job("concept artist ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="orimattila")
	
@concept_artist.route('/concept-artist-jobs-kauhajoki')
def concept_artist_jobs68(page=1):

    job_list = job_obj.get_job("concept artist ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kauhajoki")
	
@concept_artist.route('/concept-artist-jobs-ekenas')
def concept_artist_jobs69(page=1):

    job_list = job_obj.get_job("concept artist ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="ekenas")
	
@concept_artist.route('/concept-artist-jobs-kempele')
def concept_artist_jobs70(page=1):

    job_list = job_obj.get_job("concept artist ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kempele")
	
@concept_artist.route('/concept-artist-jobs-lapua')
def concept_artist_jobs71(page=1):

    job_list = job_obj.get_job("concept artist ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lapua")
	
@concept_artist.route('/concept-artist-jobs-lieksa')
def concept_artist_jobs72(page=1):

    job_list = job_obj.get_job("concept artist ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="lieksa")
	
@concept_artist.route('/concept-artist-jobs-naantali')
def concept_artist_jobs73(page=1):

    job_list = job_obj.get_job("concept artist ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="naantali")
	
@concept_artist.route('/concept-artist-jobs-aanekoski')
def concept_artist_jobs74(page=1):

    job_list = job_obj.get_job("concept artist ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="aanekoski")
	
@concept_artist.route('/concept-artist-jobs-ylivieska')
def concept_artist_jobs75(page=1):

    job_list = job_obj.get_job("concept artist ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="ylivieska")
	
@concept_artist.route('/concept-artist-jobs-kontiolahti')
def concept_artist_jobs76(page=1):

    job_list = job_obj.get_job("concept artist ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kontiolahti")
	
@concept_artist.route('/concept-artist-jobs-kankaanpaa')
def concept_artist_jobs77(page=1):

    job_list = job_obj.get_job("concept artist ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kankaanpaa")
	
@concept_artist.route('/concept-artist-jobs-ulvila')
def concept_artist_jobs78(page=1):

    job_list = job_obj.get_job("concept artist ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="ulvila")
	
@concept_artist.route('/concept-artist-jobs-pieksamaki')
def concept_artist_jobs79(page=1):

    job_list = job_obj.get_job("concept artist ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="pieksamaki")
	
@concept_artist.route('/concept-artist-jobs-kiiminki')
def concept_artist_jobs80(page=1):

    job_list = job_obj.get_job("concept artist ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kiiminki")
	
@concept_artist.route('/concept-artist-jobs-pargas')
def concept_artist_jobs81(page=1):

    job_list = job_obj.get_job("concept artist ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="pargas")
	
@concept_artist.route('/concept-artist-jobs-nurmo')
def concept_artist_jobs82(page=1):

    job_list = job_obj.get_job("concept artist ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="nurmo")
	
@concept_artist.route('/concept-artist-jobs-ilmajoki')
def concept_artist_jobs83(page=1):

    job_list = job_obj.get_job("concept artist ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="ilmajoki")
	
@concept_artist.route('/concept-artist-jobs-liperi')
def concept_artist_jobs84(page=1):

    job_list = job_obj.get_job("concept artist ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="liperi")
	
@concept_artist.route('/concept-artist-jobs-keuruu')
def concept_artist_jobs85(page=1):

    job_list = job_obj.get_job("concept artist ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="keuruu")
	
@concept_artist.route('/concept-artist-jobs-leppavirta')
def concept_artist_jobs86(page=1):

    job_list = job_obj.get_job("concept artist ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="leppavirta")
	
@concept_artist.route('/concept-artist-jobs-kurikka')
def concept_artist_jobs87(page=1):

    job_list = job_obj.get_job("concept artist ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kurikka")
	
@concept_artist.route('/concept-artist-jobs-nivala')
def concept_artist_jobs88(page=1):

    job_list = job_obj.get_job("concept artist ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="nivala")
	
@concept_artist.route('/concept-artist-jobs-joutseno')
def concept_artist_jobs89(page=1):

    job_list = job_obj.get_job("concept artist ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="joutseno")
	
@concept_artist.route('/concept-artist-jobs-pedersore')
def concept_artist_jobs90(page=1):

    job_list = job_obj.get_job("concept artist ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="pedersore")
	
@concept_artist.route('/concept-artist-jobs-sotkamo')
def concept_artist_jobs91(page=1):

    job_list = job_obj.get_job("concept artist ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="sotkamo")
	
@concept_artist.route('/concept-artist-jobs-kuhmo')
def concept_artist_jobs92(page=1):

    job_list = job_obj.get_job("concept artist ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="kuhmo")
	
@concept_artist.route('/concept-artist-jobs-paimio')
def concept_artist_jobs93(page=1):

    job_list = job_obj.get_job("concept artist ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="paimio")
	
@concept_artist.route('/concept-artist-jobs-saarijarvi')
def concept_artist_jobs94(page=1):

    job_list = job_obj.get_job("concept artist ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="saarijarvi")
	
@concept_artist.route('/concept-artist-jobs-helsinki')
def concept_artist_jobs95(page=1):

    job_list = job_obj.get_job("concept artist ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist ", location="helsinki")


####################################################################


##############################################
@concept_artist.route('/concept-artist-tyopaikat-espoo')
def concept_artist_tyopaikat2(page=1):

    job_list = job_obj.get_job("concept artist", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="espoo")

@concept_artist.route('/concept-artist-tyopaikat-tampere')
def concept_artist_tyopaikat3(page=1):

    job_list = job_obj.get_job("concept artist", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="tampere")
	
@concept_artist.route('/concept-artist-tyopaikat-vantaa')
def concept_artist_tyopaikat4(page=1):

    job_list = job_obj.get_job("concept artist", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="vantaa")
	
@concept_artist.route('/concept-artist-tyopaikat-turku')
def concept_artist_tyopaikat5(page=1):

    job_list = job_obj.get_job("concept artist", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="turku")
	
@concept_artist.route('/concept-artist-tyopaikat-oulu')
def concept_artist_tyopaikat6(page=1):

    job_list = job_obj.get_job("concept artist", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="oulu")
	
@concept_artist.route('/concept-artist-tyopaikat-lahti')
def concept_artist_tyopaikat7(page=1):

    job_list = job_obj.get_job("concept artist", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="lahti")
	
@concept_artist.route('/concept-artist-tyopaikat-kuopio')
def concept_artist_tyopaikat8(page=1):

    job_list = job_obj.get_job("concept artist", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kuopio")
	
@concept_artist.route('/concept-artist-tyopaikat-jyvvaskyla')
def concept_artist_tyopaikat9(page=1):

    job_list = job_obj.get_job("concept artist", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="jyvvaskyla")

@concept_artist.route('/concept-artist-tyopaikat-pori')
def concept_artist_tyopaikat10(page=1):

    job_list = job_obj.get_job("concept artist", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="pori")

@concept_artist.route('/concept-artist-tyopaikat-lappeenranta')
def concept_artist_tyopaikat11(page=1):

    job_list = job_obj.get_job("concept artist", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="lappeenranta")	
	
@concept_artist.route('/concept-artist-tyopaikat-vaasa')
def concept_artist_tyopaikat12(page=1):

    job_list = job_obj.get_job("concept artist", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="vaasa")
	
@concept_artist.route('/concept-artist-tyopaikat-kotka')
def concept_artist_tyopaikat13(page=1):

    job_list = job_obj.get_job("concept artist", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kotka")
	
@concept_artist.route('/concept-artist-tyopaikat-joensuu')
def concept_artist_tyopaikat14(page=1):

    job_list = job_obj.get_job("concept artist", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="joensuu")
	
@concept_artist.route('/concept-artist-tyopaikat-hameenlinna')
def concept_artist_tyopaikat15(page=1):

    job_list = job_obj.get_job("concept artist", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="hameenlinna")
	
@concept_artist.route('/concept-artist-tyopaikat-porvoo')
def concept_artist_tyopaikat16(page=1):

    job_list = job_obj.get_job("concept artist", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="porvoo")
	
@concept_artist.route('/concept-artist-tyopaikat-mikkeli')
def concept_artist_tyopaikat17(page=1):

    job_list = job_obj.get_job("concept artist", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="mikkeli")

@concept_artist.route('/concept-artist-tyopaikat-hyvinkaa')
def concept_artist_tyopaikat18(page=1):

    job_list = job_obj.get_job("concept artist", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="hyvinkaa")
	
@concept_artist.route('/concept-artist-tyopaikat-nurmijarvi')
def concept_artist_tyopaikat19(page=1):

    job_list = job_obj.get_job("concept artist", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="nurmijarvi")

@concept_artist.route('/concept-artist-tyopaikat-jarvenpaa')
def concept_artist_tyopaikat20(page=1):

    job_list = job_obj.get_job("concept artist", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="jarvenpaa")
	
@concept_artist.route('/concept-artist-tyopaikat-rauma')
def concept_artist_tyopaikat21(page=1):

    job_list = job_obj.get_job("concept artist", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="rauma")
	
@concept_artist.route('/concept-artist-tyopaikat-lohja')
def concept_artist_tyopaikat22(page=1):

    job_list = job_obj.get_job("concept artist", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="lohja")
	
@concept_artist.route('/concept-artist-tyopaikat-karleby')
def concept_artist_tyopaikat23(page=1):

    job_list = job_obj.get_job("concept artist", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="karleby")
	
@concept_artist.route('/concept-artist-tyopaikat-kajaani')
def concept_artist_tyopaikat24(page=1):

    job_list = job_obj.get_job("concept artist", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kajaani")
	
@concept_artist.route('/concept-artist-tyopaikat-rovaniemi')
def concept_artist_tyopaikat25(page=1):

    job_list = job_obj.get_job("concept artist", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="rovaniemi")
	
@concept_artist.route('/concept-artist-tyopaikat-tuusula')
def concept_artist_tyopaikat26(page=1):

    job_list = job_obj.get_job("concept artist", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="tuusula")
	
@concept_artist.route('/concept-artist-tyopaikat-kirkkonummi')
def concept_artist_tyopaikat27(page=1):

    job_list = job_obj.get_job("concept artist", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kirkkonummi")
	
@concept_artist.route('/concept-artist-tyopaikat-seinajoki')
def concept_artist_tyopaikat28(page=1):

    job_list = job_obj.get_job("concept artist", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="seinajoki")
	
@concept_artist.route('/concept-artist-tyopaikat-kerava')
def concept_artist_tyopaikat29(page=1):

    job_list = job_obj.get_job("concept artist", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kerava")
	
@concept_artist.route('/concept-artist-tyopaikat-kouvola')
def concept_artist_tyopaikat30(page=1):

    job_list = job_obj.get_job("concept artist", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kouvola")
	
@concept_artist.route('/concept-artist-tyopaikat-imatra')
def concept_artist_tyopaikat31(page=1):

    job_list = job_obj.get_job("concept artist", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="imatra")
	
@concept_artist.route('/concept-artist-tyopaikat-nokia')
def concept_artist_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("concept artist", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="nokia")
	
@concept_artist.route('/concept-artist-tyopaikat-savonlinna')
def concept_artist_tyopaikat32(page=1):

    job_list = job_obj.get_job("concept artist", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="savonlinna")
	
@concept_artist.route('/concept-artist-tyopaikat-riihimaki')
def concept_artist_tyopaikat33(page=1):

    job_list = job_obj.get_job("concept artist", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="riihimaki")
	
@concept_artist.route('/concept-artist-tyopaikat-vihti')
def concept_artist_tyopaikat34(page=1):

    job_list = job_obj.get_job("concept artist", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="vihti")
	
@concept_artist.route('/concept-artist-tyopaikat-salo')
def concept_artist_tyopaikat35(page=1):

    job_list = job_obj.get_job("concept artist", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="salo")
	
@concept_artist.route('/concept-artist-tyopaikat-kangasala')
def concept_artist_tyopaikat36(page=1):

    job_list = job_obj.get_job("concept artist", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kangasala")
	
@concept_artist.route('/concept-artist-tyopaikat-raisio')
def concept_artist_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("concept artist", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="raisio")
	
@concept_artist.route('/concept-artist-tyopaikat-karhula')
def concept_artist_tyopaikat37(page=1):

    job_list = job_obj.get_job("concept artist", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="karhula")
	
@concept_artist.route('/concept-artist-tyopaikat-kemi')
def concept_artist_tyopaikat38(page=1):

    job_list = job_obj.get_job("concept artist", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kemi")
	
@concept_artist.route('/concept-artist-tyopaikat-iisalmi')
def concept_artist_tyopaikat39(page=1):

    job_list = job_obj.get_job("concept artist", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="iisalmi")
	
@concept_artist.route('/concept-artist-tyopaikat-varkaus')
def concept_artist_tyopaikat40(page=1):

    job_list = job_obj.get_job("concept artist", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="varkaus")
	
@concept_artist.route('/concept-artist-tyopaikat-raahe')
def concept_artist_tyopaikat41(page=1):

    job_list = job_obj.get_job("concept artist", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="raahe")
	
@concept_artist.route('/concept-artist-tyopaikat-ylojarvi')
def concept_artist_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("concept artist", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="ylojarvi")
	
@concept_artist.route('/concept-artist-tyopaikat-hamina')
def concept_artist_tyopaikat42(page=1):

    job_list = job_obj.get_job("concept artist", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="hamina")
	
@concept_artist.route('/concept-artist-tyopaikat-kaarina')
def concept_artist_tyopaikat43(page=1):

    job_list = job_obj.get_job("concept artist", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kaarina")
	
@concept_artist.route('/concept-artist-tyopaikat-tornio')
def concept_artist_tyopaikat44(page=1):

    job_list = job_obj.get_job("concept artist", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="tornio")
	
@concept_artist.route('/concept-artist-tyopaikat-heinola')
def concept_artist_tyopaikat45(page=1):

    job_list = job_obj.get_job("concept artist", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="heinola")
	
@concept_artist.route('/concept-artist-tyopaikat-hollola')
def concept_artist_tyopaikat46(page=1):

    job_list = job_obj.get_job("concept artist", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="hollola")
	
@concept_artist.route('/concept-artist-tyopaikat-valkeakoski')
def concept_artist_tyopaikat47(page=1):

    job_list = job_obj.get_job("concept artist", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="valkeakoski")
	
@concept_artist.route('/concept-artist-tyopaikat-siilinjarvi')
def concept_artist_tyopaikat48(page=1):

    job_list = job_obj.get_job("concept artist", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="siilinjarvi")
	
@concept_artist.route('/concept-artist-tyopaikat-kuusankoski')
def concept_artist_tyopaikat49(page=1):

    job_list = job_obj.get_job("concept artist", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kuusankoski")
	
@concept_artist.route('/concept-artist-tyopaikat-sibbo')
def concept_artist_tyopaikat50(page=1):

    job_list = job_obj.get_job("concept artist", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="sibbo")
	
@concept_artist.route('/concept-artist-tyopaikat-jakostad')
def concept_artist_tyopaikat51(page=1):

    job_list = job_obj.get_job("concept artist", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="jakostad")
	
@concept_artist.route('/concept-artist-tyopaikat-lempaala')
def concept_artist_tyopaikat52(page=1):

    job_list = job_obj.get_job("concept artist", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="lempaala")
	
@concept_artist.route('/concept-artist-tyopaikat-mantsala')
def concept_artist_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("concept artist", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="mantsala")
	
@concept_artist.route('/concept-artist-tyopaikat-forssa')
def concept_artist_tyopaikat53(page=1):

    job_list = job_obj.get_job("concept artist", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="forssa")
	
@concept_artist.route('/concept-artist-tyopaikat-kuusamo')
def concept_artist_tyopaikat54(page=1):

    job_list = job_obj.get_job("concept artist", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kuusamo")
	
@concept_artist.route('/concept-artist-tyopaikat-haukipudas')
def concept_artist_tyopaikat55(page=1):

    job_list = job_obj.get_job("concept artist", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="haukipudas")
	
@concept_artist.route('/concept-artist-tyopaikat-korsholm')
def concept_artist_tyopaikat56(page=1):

    job_list = job_obj.get_job("concept artist", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="korsholm")
	
@concept_artist.route('/concept-artist-tyopaikat-laukaa')
def concept_artist_tyopaikat57(page=1):

    job_list = job_obj.get_job("concept artist", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="laukaa")
	
@concept_artist.route('/concept-artist-tyopaikat-anjala')
def concept_artist_tyopaikat58(page=1):

    job_list = job_obj.get_job("concept artist", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="anjala")
	
@concept_artist.route('/concept-artist-tyopaikat-uusikaupunki')
def concept_artist_tyopaikat59(page=1):

    job_list = job_obj.get_job("concept artist", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="uusikaupunki")
	
@concept_artist.route('/concept-artist-tyopaikat-janakkala')
def concept_artist_tyopaikat60(page=1):

    job_list = job_obj.get_job("concept artist", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="janakkala")
	
@concept_artist.route('/concept-artist-tyopaikat-pirkkala')
def concept_artist_tyopaikat61(page=1):

    job_list = job_obj.get_job("concept artist", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="pirkkala")
	
@concept_artist.route('/concept-artist-tyopaikat-lansi-turunmaa')
def concept_artist_tyopaikat62(page=1):

    job_list = job_obj.get_job("concept artist", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="lansi-turunmaa")
	
@concept_artist.route('/concept-artist-tyopaikat-jamsa')
def concept_artist_tyopaikat63(page=1):

    job_list = job_obj.get_job("concept artist", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="jamsa")
	
@concept_artist.route('/concept-artist-tyopaikat-jamsa')
def concept_artist_tyopaikat64(page=1):

    job_list = job_obj.get_job("concept artist", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="jamsa")
	
@concept_artist.route('/concept-artist-tyopaikat-vammala')
def concept_artist_tyopaikat65(page=1):

    job_list = job_obj.get_job("concept artist", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="vammala")
	
@concept_artist.route('/concept-artist-tyopaikat-nastola')
def concept_artist_tyopaikat66(page=1):

    job_list = job_obj.get_job("concept artist", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="nastola")
	
@concept_artist.route('/concept-artist-tyopaikat-orimattila')
def concept_artist_tyopaikat67(page=1):

    job_list = job_obj.get_job("concept artist", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="orimattila")
	
@concept_artist.route('/concept-artist-tyopaikat-kauhajoki')
def concept_artist_tyopaikat68(page=1):

    job_list = job_obj.get_job("concept artist", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kauhajoki")
	
@concept_artist.route('/concept-artist-tyopaikat-ekenas')
def concept_artist_tyopaikat69(page=1):

    job_list = job_obj.get_job("concept artist", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="ekenas")
	
@concept_artist.route('/concept-artist-tyopaikat-kempele')
def concept_artist_tyopaikat70(page=1):

    job_list = job_obj.get_job("concept artist", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kempele")
	
@concept_artist.route('/concept-artist-tyopaikat-lapua')
def concept_artist_tyopaikat71(page=1):

    job_list = job_obj.get_job("concept artist", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="lapua")
	
@concept_artist.route('/concept-artist-tyopaikat-lieksa')
def concept_artist_tyopaikat72(page=1):

    job_list = job_obj.get_job("concept artist", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="lieksa")
	
@concept_artist.route('/concept-artist-tyopaikat-naantali')
def concept_artist_tyopaikat73(page=1):

    job_list = job_obj.get_job("concept artist", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="naantali")
	
@concept_artist.route('/concept-artist-tyopaikat-aanekoski')
def concept_artist_tyopaikat74(page=1):

    job_list = job_obj.get_job("concept artist", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="aanekoski")
	
@concept_artist.route('/concept-artist-tyopaikat-ylivieska')
def concept_artist_tyopaikat75(page=1):

    job_list = job_obj.get_job("concept artist", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="ylivieska")
	
@concept_artist.route('/concept-artist-tyopaikat-kontiolahti')
def concept_artist_tyopaikat76(page=1):

    job_list = job_obj.get_job("concept artist", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kontiolahti")
	
@concept_artist.route('/concept-artist-tyopaikat-kankaanpaa')
def concept_artist_tyopaikat77(page=1):

    job_list = job_obj.get_job("concept artist", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kankaanpaa")
	
@concept_artist.route('/concept-artist-tyopaikat-ulvila')
def concept_artist_tyopaikat78(page=1):

    job_list = job_obj.get_job("concept artist", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="ulvila")
	
@concept_artist.route('/concept-artist-tyopaikat-pieksamaki')
def concept_artist_tyopaikat79(page=1):

    job_list = job_obj.get_job("concept artist", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="pieksamaki")
	
@concept_artist.route('/concept-artist-tyopaikat-kiiminki')
def concept_artist_tyopaikat80(page=1):

    job_list = job_obj.get_job("concept artist", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kiiminki")
	
@concept_artist.route('/concept-artist-tyopaikat-pargas')
def concept_artist_tyopaikat81(page=1):

    job_list = job_obj.get_job("concept artist", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="pargas")
	
@concept_artist.route('/concept-artist-tyopaikat-nurmo')
def concept_artist_tyopaikat82(page=1):

    job_list = job_obj.get_job("concept artist", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="nurmo")
	
@concept_artist.route('/concept-artist-tyopaikat-ilmajoki')
def concept_artist_tyopaikat83(page=1):

    job_list = job_obj.get_job("concept artist", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="ilmajoki")
	
@concept_artist.route('/concept-artist-tyopaikat-liperi')
def concept_artist_tyopaikat84(page=1):

    job_list = job_obj.get_job("concept artist", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="liperi")
	
@concept_artist.route('/concept-artist-tyopaikat-keuruu')
def concept_artist_tyopaikat85(page=1):

    job_list = job_obj.get_job("concept artist", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="keuruu")
	
@concept_artist.route('/concept-artist-tyopaikat-leppavirta')
def concept_artist_tyopaikat86(page=1):

    job_list = job_obj.get_job("concept artist", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="leppavirta")
	
@concept_artist.route('/concept-artist-tyopaikat-kurikka')
def concept_artist_tyopaikat87(page=1):

    job_list = job_obj.get_job("concept artist", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kurikka")
	
@concept_artist.route('/concept-artist-tyopaikat-nivala')
def concept_artist_tyopaikat88(page=1):

    job_list = job_obj.get_job("concept artist", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="nivala")
	
@concept_artist.route('/concept-artist-tyopaikat-joutseno')
def concept_artist_tyopaikat89(page=1):

    job_list = job_obj.get_job("concept artist", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="joutseno")
	
@concept_artist.route('/concept-artist-tyopaikat-pedersore')
def concept_artist_tyopaikat90(page=1):

    job_list = job_obj.get_job("concept artist", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="pedersore")
	
@concept_artist.route('/concept-artist-tyopaikat-sotkamo')
def concept_artist_tyopaikat91(page=1):

    job_list = job_obj.get_job("concept artist", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="sotkamo")
	
@concept_artist.route('/concept-artist-tyopaikat-kuhmo')
def concept_artist_tyopaikat92(page=1):

    job_list = job_obj.get_job("concept artist", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="kuhmo")
	
@concept_artist.route('/concept-artist-tyopaikat-paimio')
def concept_artist_tyopaikat93(page=1):

    job_list = job_obj.get_job("concept artist", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="paimio")
	
@concept_artist.route('/concept-artist-tyopaikat-saarijarvi')
def concept_artist_tyopaikat94(page=1):

    job_list = job_obj.get_job("concept artist", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist", location="saarijarvi")
	
@concept_artist.route('/concept-artist-tyopaikat-helsinki')
def concept_artist_tyopaikat95(page=1):

    job_list = job_obj.get_job("concept artist", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="concept artist  ", location="helsinki")
	  

