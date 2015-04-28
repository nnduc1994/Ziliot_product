from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

three_d_artist = Blueprint('three_d_artist', __name__)
job_obj = Job()



####################################################################


@three_d_artist.route('/3d-artist_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "3d-artist" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-espoo')
def three_d_artist_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("3d artist ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="espoo")

@three_d_artist.route('/3d-artist-avoimet-tyopaikat-tampere')
def three_d_artist_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("3d artist ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="tampere")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-vantaa')
def three_d_artist_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("3d artist ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="vantaa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-turku')
def three_d_artist_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("3d artist ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="turku")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-oulu')
def three_d_artist_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("3d artist ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="oulu")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-lahti')
def three_d_artist_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("3d artist ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lahti")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kuopio')
def three_d_artist_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("3d artist ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kuopio")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-jyvvaskyla')
def three_d_artist_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("3d artist ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="jyvvaskyla")

@three_d_artist.route('/3d-artist-avoimet-tyopaikat-pori')
def three_d_artist_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("3d artist ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="pori")

@three_d_artist.route('/3d-artist-avoimet-tyopaikat-lappeenranta')
def three_d_artist_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("3d artist ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lappeenranta")	
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-vaasa')
def three_d_artist_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("3d artist ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="vaasa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kotka')
def three_d_artist_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("3d artist ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kotka")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-joensuu')
def three_d_artist_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("3d artist ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="joensuu")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-hameenlinna')
def three_d_artist_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("3d artist ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="hameenlinna")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-porvoo')
def three_d_artist_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("3d artist ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="porvoo")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-mikkeli')
def three_d_artist_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("3d artist ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="mikkeli")

@three_d_artist.route('/3d-artist-avoimet-tyopaikat-hyvinkaa')
def three_d_artist_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("3d artist ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="hyvinkaa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-nurmijarvi')
def three_d_artist_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("3d artist ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="nurmijarvi")

@three_d_artist.route('/3d-artist-avoimet-tyopaikat-jarvenpaa')
def three_d_artist_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("3d artist ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="jarvenpaa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-rauma')
def three_d_artist_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("3d artist ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="rauma")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-lohja')
def three_d_artist_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("3d artist ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lohja")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-karleby')
def three_d_artist_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("3d artist ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="karleby")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kajaani')
def three_d_artist_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("3d artist ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kajaani")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-rovaniemi')
def three_d_artist_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("3d artist ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="rovaniemi")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-tuusula')
def three_d_artist_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("3d artist ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="tuusula")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kirkkonummi')
def three_d_artist_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("3d artist ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kirkkonummi")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-seinajoki')
def three_d_artist_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("3d artist ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="seinajoki")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kerava')
def three_d_artist_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("3d artist ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kerava")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kouvola')
def three_d_artist_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("3d artist ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kouvola")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-imatra')
def three_d_artist_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("3d artist ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="imatra")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-nokia')
def three_d_artist_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("3d artist ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="nokia")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-savonlinna')
def three_d_artist_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("3d artist ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="savonlinna")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-riihimaki')
def three_d_artist_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("3d artist ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="riihimaki")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-vihti')
def three_d_artist_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("3d artist ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="vihti")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-salo')
def three_d_artist_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("3d artist ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="salo")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kangasala')
def three_d_artist_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("3d artist ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kangasala")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-raisio')
def three_d_artist_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("3d artist ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="raisio")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-karhula')
def three_d_artist_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("3d artist ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="karhula")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kemi')
def three_d_artist_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("3d artist ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kemi")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-iisalmi')
def three_d_artist_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("3d artist ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="iisalmi")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-varkaus')
def three_d_artist_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("3d artist ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="varkaus")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-raahe')
def three_d_artist_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("3d artist ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="raahe")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-ylojarvi')
def three_d_artist_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("3d artist ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="ylojarvi")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-hamina')
def three_d_artist_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("3d artist ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="hamina")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kaarina')
def three_d_artist_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("3d artist ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kaarina")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-tornio')
def three_d_artist_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("3d artist ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="tornio")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-heinola')
def three_d_artist_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("3d artist ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="heinola")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-hollola')
def three_d_artist_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("3d artist ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="hollola")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-valkeakoski')
def three_d_artist_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("3d artist ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="valkeakoski")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-siilinjarvi')
def three_d_artist_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("3d artist ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="siilinjarvi")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kuusankoski')
def three_d_artist_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("3d artist ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kuusankoski")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-sibbo')
def three_d_artist_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("3d artist ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="sibbo")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-jakostad')
def three_d_artist_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("3d artist ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="jakostad")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-lempaala')
def three_d_artist_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("3d artist ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lempaala")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-mantsala')
def three_d_artist_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("3d artist ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="mantsala")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-forssa')
def three_d_artist_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("3d artist ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="forssa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kuusamo')
def three_d_artist_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("3d artist ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kuusamo")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-haukipudas')
def three_d_artist_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("3d artist ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="haukipudas")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-korsholm')
def three_d_artist_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("3d artist ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="korsholm")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-laukaa')
def three_d_artist_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("3d artist ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="laukaa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-anjala')
def three_d_artist_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("3d artist ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="anjala")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-uusikaupunki')
def three_d_artist_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("3d artist ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="uusikaupunki")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-janakkala')
def three_d_artist_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("3d artist ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="janakkala")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-pirkkala')
def three_d_artist_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("3d artist ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="pirkkala")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-lansi-turunmaa')
def three_d_artist_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("3d artist ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lansi-turunmaa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-jamsa')
def three_d_artist_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("3d artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="jamsa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-jamsa')
def three_d_artist_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("3d artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="jamsa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-vammala')
def three_d_artist_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("3d artist ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="vammala")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-nastola')
def three_d_artist_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("3d artist ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="nastola")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-orimattila')
def three_d_artist_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("3d artist ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="orimattila")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kauhajoki')
def three_d_artist_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("3d artist ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kauhajoki")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-ekenas')
def three_d_artist_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("3d artist ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="ekenas")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kempele')
def three_d_artist_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("3d artist ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kempele")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-lapua')
def three_d_artist_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("3d artist ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lapua")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-lieksa')
def three_d_artist_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("3d artist ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lieksa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-naantali')
def three_d_artist_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("3d artist ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="naantali")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-aanekoski')
def three_d_artist_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("3d artist ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="aanekoski")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-ylivieska')
def three_d_artist_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("3d artist ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="ylivieska")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kontiolahti')
def three_d_artist_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("3d artist ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kontiolahti")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kankaanpaa')
def three_d_artist_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("3d artist ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kankaanpaa")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-ulvila')
def three_d_artist_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("3d artist ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="ulvila")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-pieksamaki')
def three_d_artist_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("3d artist ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="pieksamaki")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kiiminki')
def three_d_artist_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("3d artist ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kiiminki")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-pargas')
def three_d_artist_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("3d artist ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="pargas")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-nurmo')
def three_d_artist_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("3d artist ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="nurmo")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-ilmajoki')
def three_d_artist_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("3d artist ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="ilmajoki")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-liperi')
def three_d_artist_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("3d artist ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="liperi")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-keuruu')
def three_d_artist_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("3d artist ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="keuruu")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-leppavirta')
def three_d_artist_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("3d artist ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="leppavirta")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kurikka')
def three_d_artist_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("3d artist ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kurikka")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-nivala')
def three_d_artist_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("3d artist ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="nivala")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-joutseno')
def three_d_artist_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("3d artist ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="joutseno")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-pedersore')
def three_d_artist_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("3d artist ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="pedersore")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-sotkamo')
def three_d_artist_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("3d artist ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="sotkamo")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-kuhmo')
def three_d_artist_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("3d artist ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kuhmo")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-paimio')
def three_d_artist_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("3d artist ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="paimio")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-saarijarvi')
def three_d_artist_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("3d artist ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="saarijarvi")
	
@three_d_artist.route('/3d-artist-avoimet-tyopaikat-helsinki')
def three_d_artist_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("3d artist ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="helsinki")


####################################################################


##############################################
@three_d_artist.route('/3d-artist-jobs-espoo')
def three_d_artist_jobs2(page=1):

    job_list = job_obj.get_job("3d artist ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="espoo")

@three_d_artist.route('/3d-artist-jobs-tampere')
def three_d_artist_jobs3(page=1):

    job_list = job_obj.get_job("3d artist ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="tampere")
	
@three_d_artist.route('/3d-artist-jobs-vantaa')
def three_d_artist_jobs4(page=1):

    job_list = job_obj.get_job("3d artist ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="vantaa")
	
@three_d_artist.route('/3d-artist-jobs-turku')
def three_d_artist_jobs5(page=1):

    job_list = job_obj.get_job("3d artist ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="turku")
	
@three_d_artist.route('/3d-artist-jobs-oulu')
def three_d_artist_jobs6(page=1):

    job_list = job_obj.get_job("3d artist ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="oulu")
	
@three_d_artist.route('/3d-artist-jobs-lahti')
def three_d_artist_jobs7(page=1):

    job_list = job_obj.get_job("3d artist ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lahti")
	
@three_d_artist.route('/3d-artist-jobs-kuopio')
def three_d_artist_jobs8(page=1):

    job_list = job_obj.get_job("3d artist ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kuopio")
	
@three_d_artist.route('/3d-artist-jobs-jyvvaskyla')
def three_d_artist_jobs9(page=1):

    job_list = job_obj.get_job("3d artist ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="jyvvaskyla")

@three_d_artist.route('/3d-artist-jobs-pori')
def three_d_artist_jobs10(page=1):

    job_list = job_obj.get_job("3d artist ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="pori")

@three_d_artist.route('/3d-artist-jobs-lappeenranta')
def three_d_artist_jobs11(page=1):

    job_list = job_obj.get_job("3d artist ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lappeenranta")	
	
@three_d_artist.route('/3d-artist-jobs-vaasa')
def three_d_artist_jobs12(page=1):

    job_list = job_obj.get_job("3d artist ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="vaasa")
	
@three_d_artist.route('/3d-artist-jobs-kotka')
def three_d_artist_jobs13(page=1):

    job_list = job_obj.get_job("3d artist ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kotka")
	
@three_d_artist.route('/3d-artist-jobs-joensuu')
def three_d_artist_jobs14(page=1):

    job_list = job_obj.get_job("3d artist ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="joensuu")
	
@three_d_artist.route('/3d-artist-jobs-hameenlinna')
def three_d_artist_jobs15(page=1):

    job_list = job_obj.get_job("3d artist ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="hameenlinna")
	
@three_d_artist.route('/3d-artist-jobs-porvoo')
def three_d_artist_jobs16(page=1):

    job_list = job_obj.get_job("3d artist ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="porvoo")
	
@three_d_artist.route('/3d-artist-jobs-mikkeli')
def three_d_artist_jobs17(page=1):

    job_list = job_obj.get_job("3d artist ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="mikkeli")

@three_d_artist.route('/3d-artist-jobs-hyvinkaa')
def three_d_artist_jobs18(page=1):

    job_list = job_obj.get_job("3d artist ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="hyvinkaa")
	
@three_d_artist.route('/3d-artist-jobs-nurmijarvi')
def three_d_artist_jobs19(page=1):

    job_list = job_obj.get_job("3d artist ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="nurmijarvi")

@three_d_artist.route('/3d-artist-jobs-jarvenpaa')
def three_d_artist_jobs20(page=1):

    job_list = job_obj.get_job("3d artist ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="jarvenpaa")
	
@three_d_artist.route('/3d-artist-jobs-rauma')
def three_d_artist_jobs21(page=1):

    job_list = job_obj.get_job("3d artist ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="rauma")
	
@three_d_artist.route('/3d-artist-jobs-lohja')
def three_d_artist_jobs22(page=1):

    job_list = job_obj.get_job("3d artist ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lohja")
	
@three_d_artist.route('/3d-artist-jobs-karleby')
def three_d_artist_jobs23(page=1):

    job_list = job_obj.get_job("3d artist ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="karleby")
	
@three_d_artist.route('/3d-artist-jobs-kajaani')
def three_d_artist_jobs24(page=1):

    job_list = job_obj.get_job("3d artist ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kajaani")
	
@three_d_artist.route('/3d-artist-jobs-rovaniemi')
def three_d_artist_jobs25(page=1):

    job_list = job_obj.get_job("3d artist ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="rovaniemi")
	
@three_d_artist.route('/3d-artist-jobs-tuusula')
def three_d_artist_jobs26(page=1):

    job_list = job_obj.get_job("3d artist ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="tuusula")
	
@three_d_artist.route('/3d-artist-jobs-kirkkonummi')
def three_d_artist_jobs27(page=1):

    job_list = job_obj.get_job("3d artist ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kirkkonummi")
	
@three_d_artist.route('/3d-artist-jobs-seinajoki')
def three_d_artist_jobs28(page=1):

    job_list = job_obj.get_job("3d artist ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="seinajoki")
	
@three_d_artist.route('/3d-artist-jobs-kerava')
def three_d_artist_jobs29(page=1):

    job_list = job_obj.get_job("3d artist ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kerava")
	
@three_d_artist.route('/3d-artist-jobs-kouvola')
def three_d_artist_jobs30(page=1):

    job_list = job_obj.get_job("3d artist ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kouvola")
	
@three_d_artist.route('/3d-artist-jobs-imatra')
def three_d_artist_jobs31(page=1):

    job_list = job_obj.get_job("3d artist ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="imatra")
	
@three_d_artist.route('/3d-artist-jobs-nokia')
def three_d_artist_jobs32_1(page=1):

    job_list = job_obj.get_job("3d artist ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="nokia")
	
@three_d_artist.route('/3d-artist-jobs-savonlinna')
def three_d_artist_jobs32(page=1):

    job_list = job_obj.get_job("3d artist ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="savonlinna")
	
@three_d_artist.route('/3d-artist-jobs-riihimaki')
def three_d_artist_jobs33(page=1):

    job_list = job_obj.get_job("3d artist ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="riihimaki")
	
@three_d_artist.route('/3d-artist-jobs-vihti')
def three_d_artist_jobs34(page=1):

    job_list = job_obj.get_job("3d artist ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="vihti")
	
@three_d_artist.route('/3d-artist-jobs-salo')
def three_d_artist_jobs35(page=1):

    job_list = job_obj.get_job("3d artist ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="salo")
	
@three_d_artist.route('/3d-artist-jobs-kangasala')
def three_d_artist_jobs36(page=1):

    job_list = job_obj.get_job("3d artist ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kangasala")
	
@three_d_artist.route('/3d-artist-jobs-raisio')
def three_d_artist_jobs37_1(page=1):

    job_list = job_obj.get_job("3d artist ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="raisio")
	
@three_d_artist.route('/3d-artist-jobs-karhula')
def three_d_artist_jobs37(page=1):

    job_list = job_obj.get_job("3d artist ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="karhula")
	
@three_d_artist.route('/3d-artist-jobs-kemi')
def three_d_artist_jobs38(page=1):

    job_list = job_obj.get_job("3d artist ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kemi")
	
@three_d_artist.route('/3d-artist-jobs-iisalmi')
def three_d_artist_jobs39(page=1):

    job_list = job_obj.get_job("3d artist ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="iisalmi")
	
@three_d_artist.route('/3d-artist-jobs-varkaus')
def three_d_artist_jobs40(page=1):

    job_list = job_obj.get_job("3d artist ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="varkaus")
	
@three_d_artist.route('/3d-artist-jobs-raahe')
def three_d_artist_jobs41(page=1):

    job_list = job_obj.get_job("3d artist ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="raahe")
	
@three_d_artist.route('/3d-artist-jobs-ylojarvi')
def three_d_artist_jobs42_1(page=1):

    job_list = job_obj.get_job("3d artist ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="ylojarvi")
	
@three_d_artist.route('/3d-artist-jobs-hamina')
def three_d_artist_jobs42(page=1):

    job_list = job_obj.get_job("3d artist ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="hamina")
	
@three_d_artist.route('/3d-artist-jobs-kaarina')
def three_d_artist_jobs43(page=1):

    job_list = job_obj.get_job("3d artist ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kaarina")
	
@three_d_artist.route('/3d-artist-jobs-tornio')
def three_d_artist_jobs44(page=1):

    job_list = job_obj.get_job("3d artist ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="tornio")
	
@three_d_artist.route('/3d-artist-jobs-heinola')
def three_d_artist_jobs45(page=1):

    job_list = job_obj.get_job("3d artist ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="heinola")
	
@three_d_artist.route('/3d-artist-jobs-hollola')
def three_d_artist_jobs46(page=1):

    job_list = job_obj.get_job("3d artist ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="hollola")
	
@three_d_artist.route('/3d-artist-jobs-valkeakoski')
def three_d_artist_jobs47(page=1):

    job_list = job_obj.get_job("3d artist ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="valkeakoski")
	
@three_d_artist.route('/3d-artist-jobs-siilinjarvi')
def three_d_artist_jobs48(page=1):

    job_list = job_obj.get_job("3d artist ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="siilinjarvi")
	
@three_d_artist.route('/3d-artist-jobs-kuusankoski')
def three_d_artist_jobs49(page=1):

    job_list = job_obj.get_job("3d artist ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kuusankoski")
	
@three_d_artist.route('/3d-artist-jobs-sibbo')
def three_d_artist_jobs50(page=1):

    job_list = job_obj.get_job("3d artist ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="sibbo")
	
@three_d_artist.route('/3d-artist-jobs-jakostad')
def three_d_artist_jobs51(page=1):

    job_list = job_obj.get_job("3d artist ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="jakostad")
	
@three_d_artist.route('/3d-artist-jobs-lempaala')
def three_d_artist_jobs52(page=1):

    job_list = job_obj.get_job("3d artist ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lempaala")
	
@three_d_artist.route('/3d-artist-jobs-mantsala')
def three_d_artist_jobs52_1(page=1):

    job_list = job_obj.get_job("3d artist ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="mantsala")
	
@three_d_artist.route('/3d-artist-jobs-forssa')
def three_d_artist_jobs53(page=1):

    job_list = job_obj.get_job("3d artist ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="forssa")
	
@three_d_artist.route('/3d-artist-jobs-kuusamo')
def three_d_artist_jobs54(page=1):

    job_list = job_obj.get_job("3d artist ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kuusamo")
	
@three_d_artist.route('/3d-artist-jobs-haukipudas')
def three_d_artist_jobs55(page=1):

    job_list = job_obj.get_job("3d artist ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="haukipudas")
	
@three_d_artist.route('/3d-artist-jobs-korsholm')
def three_d_artist_jobs56(page=1):

    job_list = job_obj.get_job("3d artist ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="korsholm")
	
@three_d_artist.route('/3d-artist-jobs-laukaa')
def three_d_artist_jobs57(page=1):

    job_list = job_obj.get_job("3d artist ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="laukaa")
	
@three_d_artist.route('/3d-artist-jobs-anjala')
def three_d_artist_jobs58(page=1):

    job_list = job_obj.get_job("3d artist ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="anjala")
	
@three_d_artist.route('/3d-artist-jobs-uusikaupunki')
def three_d_artist_jobs59(page=1):

    job_list = job_obj.get_job("3d artist ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="uusikaupunki")
	
@three_d_artist.route('/3d-artist-jobs-janakkala')
def three_d_artist_jobs60(page=1):

    job_list = job_obj.get_job("3d artist ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="janakkala")
	
@three_d_artist.route('/3d-artist-jobs-pirkkala')
def three_d_artist_jobs61(page=1):

    job_list = job_obj.get_job("3d artist ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="pirkkala")
	
@three_d_artist.route('/3d-artist-jobs-lansi-turunmaa')
def three_d_artist_jobs62(page=1):

    job_list = job_obj.get_job("3d artist ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lansi-turunmaa")
	
@three_d_artist.route('/3d-artist-jobs-jamsa')
def three_d_artist_jobs63(page=1):

    job_list = job_obj.get_job("3d artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="jamsa")
	
@three_d_artist.route('/3d-artist-jobs-jamsa')
def three_d_artist_jobs64(page=1):

    job_list = job_obj.get_job("3d artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="jamsa")
	
@three_d_artist.route('/3d-artist-jobs-vammala')
def three_d_artist_jobs65(page=1):

    job_list = job_obj.get_job("3d artist ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="vammala")
	
@three_d_artist.route('/3d-artist-jobs-nastola')
def three_d_artist_jobs66(page=1):

    job_list = job_obj.get_job("3d artist ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="nastola")
	
@three_d_artist.route('/3d-artist-jobs-orimattila')
def three_d_artist_jobs67(page=1):

    job_list = job_obj.get_job("3d artist ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="orimattila")
	
@three_d_artist.route('/3d-artist-jobs-kauhajoki')
def three_d_artist_jobs68(page=1):

    job_list = job_obj.get_job("3d artist ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kauhajoki")
	
@three_d_artist.route('/3d-artist-jobs-ekenas')
def three_d_artist_jobs69(page=1):

    job_list = job_obj.get_job("3d artist ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="ekenas")
	
@three_d_artist.route('/3d-artist-jobs-kempele')
def three_d_artist_jobs70(page=1):

    job_list = job_obj.get_job("3d artist ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kempele")
	
@three_d_artist.route('/3d-artist-jobs-lapua')
def three_d_artist_jobs71(page=1):

    job_list = job_obj.get_job("3d artist ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lapua")
	
@three_d_artist.route('/3d-artist-jobs-lieksa')
def three_d_artist_jobs72(page=1):

    job_list = job_obj.get_job("3d artist ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="lieksa")
	
@three_d_artist.route('/3d-artist-jobs-naantali')
def three_d_artist_jobs73(page=1):

    job_list = job_obj.get_job("3d artist ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="naantali")
	
@three_d_artist.route('/3d-artist-jobs-aanekoski')
def three_d_artist_jobs74(page=1):

    job_list = job_obj.get_job("3d artist ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="aanekoski")
	
@three_d_artist.route('/3d-artist-jobs-ylivieska')
def three_d_artist_jobs75(page=1):

    job_list = job_obj.get_job("3d artist ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="ylivieska")
	
@three_d_artist.route('/3d-artist-jobs-kontiolahti')
def three_d_artist_jobs76(page=1):

    job_list = job_obj.get_job("3d artist ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kontiolahti")
	
@three_d_artist.route('/3d-artist-jobs-kankaanpaa')
def three_d_artist_jobs77(page=1):

    job_list = job_obj.get_job("3d artist ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kankaanpaa")
	
@three_d_artist.route('/3d-artist-jobs-ulvila')
def three_d_artist_jobs78(page=1):

    job_list = job_obj.get_job("3d artist ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="ulvila")
	
@three_d_artist.route('/3d-artist-jobs-pieksamaki')
def three_d_artist_jobs79(page=1):

    job_list = job_obj.get_job("3d artist ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="pieksamaki")
	
@three_d_artist.route('/3d-artist-jobs-kiiminki')
def three_d_artist_jobs80(page=1):

    job_list = job_obj.get_job("3d artist ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kiiminki")
	
@three_d_artist.route('/3d-artist-jobs-pargas')
def three_d_artist_jobs81(page=1):

    job_list = job_obj.get_job("3d artist ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="pargas")
	
@three_d_artist.route('/3d-artist-jobs-nurmo')
def three_d_artist_jobs82(page=1):

    job_list = job_obj.get_job("3d artist ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="nurmo")
	
@three_d_artist.route('/3d-artist-jobs-ilmajoki')
def three_d_artist_jobs83(page=1):

    job_list = job_obj.get_job("3d artist ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="ilmajoki")
	
@three_d_artist.route('/3d-artist-jobs-liperi')
def three_d_artist_jobs84(page=1):

    job_list = job_obj.get_job("3d artist ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="liperi")
	
@three_d_artist.route('/3d-artist-jobs-keuruu')
def three_d_artist_jobs85(page=1):

    job_list = job_obj.get_job("3d artist ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="keuruu")
	
@three_d_artist.route('/3d-artist-jobs-leppavirta')
def three_d_artist_jobs86(page=1):

    job_list = job_obj.get_job("3d artist ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="leppavirta")
	
@three_d_artist.route('/3d-artist-jobs-kurikka')
def three_d_artist_jobs87(page=1):

    job_list = job_obj.get_job("3d artist ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kurikka")
	
@three_d_artist.route('/3d-artist-jobs-nivala')
def three_d_artist_jobs88(page=1):

    job_list = job_obj.get_job("3d artist ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="nivala")
	
@three_d_artist.route('/3d-artist-jobs-joutseno')
def three_d_artist_jobs89(page=1):

    job_list = job_obj.get_job("3d artist ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="joutseno")
	
@three_d_artist.route('/3d-artist-jobs-pedersore')
def three_d_artist_jobs90(page=1):

    job_list = job_obj.get_job("3d artist ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="pedersore")
	
@three_d_artist.route('/3d-artist-jobs-sotkamo')
def three_d_artist_jobs91(page=1):

    job_list = job_obj.get_job("3d artist ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="sotkamo")
	
@three_d_artist.route('/3d-artist-jobs-kuhmo')
def three_d_artist_jobs92(page=1):

    job_list = job_obj.get_job("3d artist ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="kuhmo")
	
@three_d_artist.route('/3d-artist-jobs-paimio')
def three_d_artist_jobs93(page=1):

    job_list = job_obj.get_job("3d artist ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="paimio")
	
@three_d_artist.route('/3d-artist-jobs-saarijarvi')
def three_d_artist_jobs94(page=1):

    job_list = job_obj.get_job("3d artist ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="saarijarvi")
	
@three_d_artist.route('/3d-artist-jobs-helsinki')
def three_d_artist_jobs95(page=1):

    job_list = job_obj.get_job("3d artist ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist ", location="helsinki")


####################################################################


##############################################
@three_d_artist.route('/3d-artist-tyopaikat-espoo')
def three_d_artist_tyopaikat2(page=1):

    job_list = job_obj.get_job("3d artist", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="espoo")

@three_d_artist.route('/3d-artist-tyopaikat-tampere')
def three_d_artist_tyopaikat3(page=1):

    job_list = job_obj.get_job("3d artist", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="tampere")
	
@three_d_artist.route('/3d-artist-tyopaikat-vantaa')
def three_d_artist_tyopaikat4(page=1):

    job_list = job_obj.get_job("3d artist", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="vantaa")
	
@three_d_artist.route('/3d-artist-tyopaikat-turku')
def three_d_artist_tyopaikat5(page=1):

    job_list = job_obj.get_job("3d artist", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="turku")
	
@three_d_artist.route('/3d-artist-tyopaikat-oulu')
def three_d_artist_tyopaikat6(page=1):

    job_list = job_obj.get_job("3d artist", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="oulu")
	
@three_d_artist.route('/3d-artist-tyopaikat-lahti')
def three_d_artist_tyopaikat7(page=1):

    job_list = job_obj.get_job("3d artist", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="lahti")
	
@three_d_artist.route('/3d-artist-tyopaikat-kuopio')
def three_d_artist_tyopaikat8(page=1):

    job_list = job_obj.get_job("3d artist", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kuopio")
	
@three_d_artist.route('/3d-artist-tyopaikat-jyvvaskyla')
def three_d_artist_tyopaikat9(page=1):

    job_list = job_obj.get_job("3d artist", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="jyvvaskyla")

@three_d_artist.route('/3d-artist-tyopaikat-pori')
def three_d_artist_tyopaikat10(page=1):

    job_list = job_obj.get_job("3d artist", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="pori")

@three_d_artist.route('/3d-artist-tyopaikat-lappeenranta')
def three_d_artist_tyopaikat11(page=1):

    job_list = job_obj.get_job("3d artist", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="lappeenranta")	
	
@three_d_artist.route('/3d-artist-tyopaikat-vaasa')
def three_d_artist_tyopaikat12(page=1):

    job_list = job_obj.get_job("3d artist", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="vaasa")
	
@three_d_artist.route('/3d-artist-tyopaikat-kotka')
def three_d_artist_tyopaikat13(page=1):

    job_list = job_obj.get_job("3d artist", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kotka")
	
@three_d_artist.route('/3d-artist-tyopaikat-joensuu')
def three_d_artist_tyopaikat14(page=1):

    job_list = job_obj.get_job("3d artist", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="joensuu")
	
@three_d_artist.route('/3d-artist-tyopaikat-hameenlinna')
def three_d_artist_tyopaikat15(page=1):

    job_list = job_obj.get_job("3d artist", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="hameenlinna")
	
@three_d_artist.route('/3d-artist-tyopaikat-porvoo')
def three_d_artist_tyopaikat16(page=1):

    job_list = job_obj.get_job("3d artist", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="porvoo")
	
@three_d_artist.route('/3d-artist-tyopaikat-mikkeli')
def three_d_artist_tyopaikat17(page=1):

    job_list = job_obj.get_job("3d artist", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="mikkeli")

@three_d_artist.route('/3d-artist-tyopaikat-hyvinkaa')
def three_d_artist_tyopaikat18(page=1):

    job_list = job_obj.get_job("3d artist", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="hyvinkaa")
	
@three_d_artist.route('/3d-artist-tyopaikat-nurmijarvi')
def three_d_artist_tyopaikat19(page=1):

    job_list = job_obj.get_job("3d artist", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="nurmijarvi")

@three_d_artist.route('/3d-artist-tyopaikat-jarvenpaa')
def three_d_artist_tyopaikat20(page=1):

    job_list = job_obj.get_job("3d artist", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="jarvenpaa")
	
@three_d_artist.route('/3d-artist-tyopaikat-rauma')
def three_d_artist_tyopaikat21(page=1):

    job_list = job_obj.get_job("3d artist", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="rauma")
	
@three_d_artist.route('/3d-artist-tyopaikat-lohja')
def three_d_artist_tyopaikat22(page=1):

    job_list = job_obj.get_job("3d artist", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="lohja")
	
@three_d_artist.route('/3d-artist-tyopaikat-karleby')
def three_d_artist_tyopaikat23(page=1):

    job_list = job_obj.get_job("3d artist", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="karleby")
	
@three_d_artist.route('/3d-artist-tyopaikat-kajaani')
def three_d_artist_tyopaikat24(page=1):

    job_list = job_obj.get_job("3d artist", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kajaani")
	
@three_d_artist.route('/3d-artist-tyopaikat-rovaniemi')
def three_d_artist_tyopaikat25(page=1):

    job_list = job_obj.get_job("3d artist", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="rovaniemi")
	
@three_d_artist.route('/3d-artist-tyopaikat-tuusula')
def three_d_artist_tyopaikat26(page=1):

    job_list = job_obj.get_job("3d artist", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="tuusula")
	
@three_d_artist.route('/3d-artist-tyopaikat-kirkkonummi')
def three_d_artist_tyopaikat27(page=1):

    job_list = job_obj.get_job("3d artist", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kirkkonummi")
	
@three_d_artist.route('/3d-artist-tyopaikat-seinajoki')
def three_d_artist_tyopaikat28(page=1):

    job_list = job_obj.get_job("3d artist", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="seinajoki")
	
@three_d_artist.route('/3d-artist-tyopaikat-kerava')
def three_d_artist_tyopaikat29(page=1):

    job_list = job_obj.get_job("3d artist", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kerava")
	
@three_d_artist.route('/3d-artist-tyopaikat-kouvola')
def three_d_artist_tyopaikat30(page=1):

    job_list = job_obj.get_job("3d artist", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kouvola")
	
@three_d_artist.route('/3d-artist-tyopaikat-imatra')
def three_d_artist_tyopaikat31(page=1):

    job_list = job_obj.get_job("3d artist", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="imatra")
	
@three_d_artist.route('/3d-artist-tyopaikat-nokia')
def three_d_artist_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("3d artist", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="nokia")
	
@three_d_artist.route('/3d-artist-tyopaikat-savonlinna')
def three_d_artist_tyopaikat32(page=1):

    job_list = job_obj.get_job("3d artist", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="savonlinna")
	
@three_d_artist.route('/3d-artist-tyopaikat-riihimaki')
def three_d_artist_tyopaikat33(page=1):

    job_list = job_obj.get_job("3d artist", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="riihimaki")
	
@three_d_artist.route('/3d-artist-tyopaikat-vihti')
def three_d_artist_tyopaikat34(page=1):

    job_list = job_obj.get_job("3d artist", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="vihti")
	
@three_d_artist.route('/3d-artist-tyopaikat-salo')
def three_d_artist_tyopaikat35(page=1):

    job_list = job_obj.get_job("3d artist", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="salo")
	
@three_d_artist.route('/3d-artist-tyopaikat-kangasala')
def three_d_artist_tyopaikat36(page=1):

    job_list = job_obj.get_job("3d artist", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kangasala")
	
@three_d_artist.route('/3d-artist-tyopaikat-raisio')
def three_d_artist_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("3d artist", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="raisio")
	
@three_d_artist.route('/3d-artist-tyopaikat-karhula')
def three_d_artist_tyopaikat37(page=1):

    job_list = job_obj.get_job("3d artist", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="karhula")
	
@three_d_artist.route('/3d-artist-tyopaikat-kemi')
def three_d_artist_tyopaikat38(page=1):

    job_list = job_obj.get_job("3d artist", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kemi")
	
@three_d_artist.route('/3d-artist-tyopaikat-iisalmi')
def three_d_artist_tyopaikat39(page=1):

    job_list = job_obj.get_job("3d artist", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="iisalmi")
	
@three_d_artist.route('/3d-artist-tyopaikat-varkaus')
def three_d_artist_tyopaikat40(page=1):

    job_list = job_obj.get_job("3d artist", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="varkaus")
	
@three_d_artist.route('/3d-artist-tyopaikat-raahe')
def three_d_artist_tyopaikat41(page=1):

    job_list = job_obj.get_job("3d artist", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="raahe")
	
@three_d_artist.route('/3d-artist-tyopaikat-ylojarvi')
def three_d_artist_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("3d artist", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="ylojarvi")
	
@three_d_artist.route('/3d-artist-tyopaikat-hamina')
def three_d_artist_tyopaikat42(page=1):

    job_list = job_obj.get_job("3d artist", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="hamina")
	
@three_d_artist.route('/3d-artist-tyopaikat-kaarina')
def three_d_artist_tyopaikat43(page=1):

    job_list = job_obj.get_job("3d artist", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kaarina")
	
@three_d_artist.route('/3d-artist-tyopaikat-tornio')
def three_d_artist_tyopaikat44(page=1):

    job_list = job_obj.get_job("3d artist", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="tornio")
	
@three_d_artist.route('/3d-artist-tyopaikat-heinola')
def three_d_artist_tyopaikat45(page=1):

    job_list = job_obj.get_job("3d artist", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="heinola")
	
@three_d_artist.route('/3d-artist-tyopaikat-hollola')
def three_d_artist_tyopaikat46(page=1):

    job_list = job_obj.get_job("3d artist", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="hollola")
	
@three_d_artist.route('/3d-artist-tyopaikat-valkeakoski')
def three_d_artist_tyopaikat47(page=1):

    job_list = job_obj.get_job("3d artist", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="valkeakoski")
	
@three_d_artist.route('/3d-artist-tyopaikat-siilinjarvi')
def three_d_artist_tyopaikat48(page=1):

    job_list = job_obj.get_job("3d artist", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="siilinjarvi")
	
@three_d_artist.route('/3d-artist-tyopaikat-kuusankoski')
def three_d_artist_tyopaikat49(page=1):

    job_list = job_obj.get_job("3d artist", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kuusankoski")
	
@three_d_artist.route('/3d-artist-tyopaikat-sibbo')
def three_d_artist_tyopaikat50(page=1):

    job_list = job_obj.get_job("3d artist", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="sibbo")
	
@three_d_artist.route('/3d-artist-tyopaikat-jakostad')
def three_d_artist_tyopaikat51(page=1):

    job_list = job_obj.get_job("3d artist", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="jakostad")
	
@three_d_artist.route('/3d-artist-tyopaikat-lempaala')
def three_d_artist_tyopaikat52(page=1):

    job_list = job_obj.get_job("3d artist", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="lempaala")
	
@three_d_artist.route('/3d-artist-tyopaikat-mantsala')
def three_d_artist_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("3d artist", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="mantsala")
	
@three_d_artist.route('/3d-artist-tyopaikat-forssa')
def three_d_artist_tyopaikat53(page=1):

    job_list = job_obj.get_job("3d artist", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="forssa")
	
@three_d_artist.route('/3d-artist-tyopaikat-kuusamo')
def three_d_artist_tyopaikat54(page=1):

    job_list = job_obj.get_job("3d artist", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kuusamo")
	
@three_d_artist.route('/3d-artist-tyopaikat-haukipudas')
def three_d_artist_tyopaikat55(page=1):

    job_list = job_obj.get_job("3d artist", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="haukipudas")
	
@three_d_artist.route('/3d-artist-tyopaikat-korsholm')
def three_d_artist_tyopaikat56(page=1):

    job_list = job_obj.get_job("3d artist", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="korsholm")
	
@three_d_artist.route('/3d-artist-tyopaikat-laukaa')
def three_d_artist_tyopaikat57(page=1):

    job_list = job_obj.get_job("3d artist", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="laukaa")
	
@three_d_artist.route('/3d-artist-tyopaikat-anjala')
def three_d_artist_tyopaikat58(page=1):

    job_list = job_obj.get_job("3d artist", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="anjala")
	
@three_d_artist.route('/3d-artist-tyopaikat-uusikaupunki')
def three_d_artist_tyopaikat59(page=1):

    job_list = job_obj.get_job("3d artist", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="uusikaupunki")
	
@three_d_artist.route('/3d-artist-tyopaikat-janakkala')
def three_d_artist_tyopaikat60(page=1):

    job_list = job_obj.get_job("3d artist", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="janakkala")
	
@three_d_artist.route('/3d-artist-tyopaikat-pirkkala')
def three_d_artist_tyopaikat61(page=1):

    job_list = job_obj.get_job("3d artist", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="pirkkala")
	
@three_d_artist.route('/3d-artist-tyopaikat-lansi-turunmaa')
def three_d_artist_tyopaikat62(page=1):

    job_list = job_obj.get_job("3d artist", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="lansi-turunmaa")
	
@three_d_artist.route('/3d-artist-tyopaikat-jamsa')
def three_d_artist_tyopaikat63(page=1):

    job_list = job_obj.get_job("3d artist", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="jamsa")
	
@three_d_artist.route('/3d-artist-tyopaikat-jamsa')
def three_d_artist_tyopaikat64(page=1):

    job_list = job_obj.get_job("3d artist", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="jamsa")
	
@three_d_artist.route('/3d-artist-tyopaikat-vammala')
def three_d_artist_tyopaikat65(page=1):

    job_list = job_obj.get_job("3d artist", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="vammala")
	
@three_d_artist.route('/3d-artist-tyopaikat-nastola')
def three_d_artist_tyopaikat66(page=1):

    job_list = job_obj.get_job("3d artist", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="nastola")
	
@three_d_artist.route('/3d-artist-tyopaikat-orimattila')
def three_d_artist_tyopaikat67(page=1):

    job_list = job_obj.get_job("3d artist", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="orimattila")
	
@three_d_artist.route('/3d-artist-tyopaikat-kauhajoki')
def three_d_artist_tyopaikat68(page=1):

    job_list = job_obj.get_job("3d artist", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kauhajoki")
	
@three_d_artist.route('/3d-artist-tyopaikat-ekenas')
def three_d_artist_tyopaikat69(page=1):

    job_list = job_obj.get_job("3d artist", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="ekenas")
	
@three_d_artist.route('/3d-artist-tyopaikat-kempele')
def three_d_artist_tyopaikat70(page=1):

    job_list = job_obj.get_job("3d artist", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kempele")
	
@three_d_artist.route('/3d-artist-tyopaikat-lapua')
def three_d_artist_tyopaikat71(page=1):

    job_list = job_obj.get_job("3d artist", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="lapua")
	
@three_d_artist.route('/3d-artist-tyopaikat-lieksa')
def three_d_artist_tyopaikat72(page=1):

    job_list = job_obj.get_job("3d artist", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="lieksa")
	
@three_d_artist.route('/3d-artist-tyopaikat-naantali')
def three_d_artist_tyopaikat73(page=1):

    job_list = job_obj.get_job("3d artist", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="naantali")
	
@three_d_artist.route('/3d-artist-tyopaikat-aanekoski')
def three_d_artist_tyopaikat74(page=1):

    job_list = job_obj.get_job("3d artist", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="aanekoski")
	
@three_d_artist.route('/3d-artist-tyopaikat-ylivieska')
def three_d_artist_tyopaikat75(page=1):

    job_list = job_obj.get_job("3d artist", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="ylivieska")
	
@three_d_artist.route('/3d-artist-tyopaikat-kontiolahti')
def three_d_artist_tyopaikat76(page=1):

    job_list = job_obj.get_job("3d artist", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kontiolahti")
	
@three_d_artist.route('/3d-artist-tyopaikat-kankaanpaa')
def three_d_artist_tyopaikat77(page=1):

    job_list = job_obj.get_job("3d artist", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kankaanpaa")
	
@three_d_artist.route('/3d-artist-tyopaikat-ulvila')
def three_d_artist_tyopaikat78(page=1):

    job_list = job_obj.get_job("3d artist", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="ulvila")
	
@three_d_artist.route('/3d-artist-tyopaikat-pieksamaki')
def three_d_artist_tyopaikat79(page=1):

    job_list = job_obj.get_job("3d artist", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="pieksamaki")
	
@three_d_artist.route('/3d-artist-tyopaikat-kiiminki')
def three_d_artist_tyopaikat80(page=1):

    job_list = job_obj.get_job("3d artist", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kiiminki")
	
@three_d_artist.route('/3d-artist-tyopaikat-pargas')
def three_d_artist_tyopaikat81(page=1):

    job_list = job_obj.get_job("3d artist", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="pargas")
	
@three_d_artist.route('/3d-artist-tyopaikat-nurmo')
def three_d_artist_tyopaikat82(page=1):

    job_list = job_obj.get_job("3d artist", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="nurmo")
	
@three_d_artist.route('/3d-artist-tyopaikat-ilmajoki')
def three_d_artist_tyopaikat83(page=1):

    job_list = job_obj.get_job("3d artist", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="ilmajoki")
	
@three_d_artist.route('/3d-artist-tyopaikat-liperi')
def three_d_artist_tyopaikat84(page=1):

    job_list = job_obj.get_job("3d artist", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="liperi")
	
@three_d_artist.route('/3d-artist-tyopaikat-keuruu')
def three_d_artist_tyopaikat85(page=1):

    job_list = job_obj.get_job("3d artist", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="keuruu")
	
@three_d_artist.route('/3d-artist-tyopaikat-leppavirta')
def three_d_artist_tyopaikat86(page=1):

    job_list = job_obj.get_job("3d artist", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="leppavirta")
	
@three_d_artist.route('/3d-artist-tyopaikat-kurikka')
def three_d_artist_tyopaikat87(page=1):

    job_list = job_obj.get_job("3d artist", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kurikka")
	
@three_d_artist.route('/3d-artist-tyopaikat-nivala')
def three_d_artist_tyopaikat88(page=1):

    job_list = job_obj.get_job("3d artist", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="nivala")
	
@three_d_artist.route('/3d-artist-tyopaikat-joutseno')
def three_d_artist_tyopaikat89(page=1):

    job_list = job_obj.get_job("3d artist", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="joutseno")
	
@three_d_artist.route('/3d-artist-tyopaikat-pedersore')
def three_d_artist_tyopaikat90(page=1):

    job_list = job_obj.get_job("3d artist", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="pedersore")
	
@three_d_artist.route('/3d-artist-tyopaikat-sotkamo')
def three_d_artist_tyopaikat91(page=1):

    job_list = job_obj.get_job("3d artist", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="sotkamo")
	
@three_d_artist.route('/3d-artist-tyopaikat-kuhmo')
def three_d_artist_tyopaikat92(page=1):

    job_list = job_obj.get_job("3d artist", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="kuhmo")
	
@three_d_artist.route('/3d-artist-tyopaikat-paimio')
def three_d_artist_tyopaikat93(page=1):

    job_list = job_obj.get_job("3d artist", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="paimio")
	
@three_d_artist.route('/3d-artist-tyopaikat-saarijarvi')
def three_d_artist_tyopaikat94(page=1):

    job_list = job_obj.get_job("3d artist", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist", location="saarijarvi")
	
@three_d_artist.route('/3d-artist-tyopaikat-helsinki')
def three_d_artist_tyopaikat95(page=1):

    job_list = job_obj.get_job("3d artist", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="3d artist  ", location="helsinki")
	  

