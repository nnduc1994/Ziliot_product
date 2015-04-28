from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

principal_artist = Blueprint('principal_artist', __name__)
job_obj = Job()



####################################################################


@principal_artist.route('/principal-artist_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "principal-artist" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@principal_artist.route('/principal-artist-avoimet-tyopaikat-espoo')
def principal_artist_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("principal artist ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="espoo")

@principal_artist.route('/principal-artist-avoimet-tyopaikat-tampere')
def principal_artist_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("principal artist ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="tampere")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-vantaa')
def principal_artist_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("principal artist ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="vantaa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-turku')
def principal_artist_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("principal artist ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="turku")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-oulu')
def principal_artist_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("principal artist ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="oulu")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-lahti')
def principal_artist_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("principal artist ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lahti")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kuopio')
def principal_artist_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("principal artist ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kuopio")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-jyvvaskyla')
def principal_artist_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("principal artist ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="jyvvaskyla")

@principal_artist.route('/principal-artist-avoimet-tyopaikat-pori')
def principal_artist_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("principal artist ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="pori")

@principal_artist.route('/principal-artist-avoimet-tyopaikat-lappeenranta')
def principal_artist_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("principal artist ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lappeenranta")	
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-vaasa')
def principal_artist_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("principal artist ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="vaasa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kotka')
def principal_artist_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("principal artist ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kotka")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-joensuu')
def principal_artist_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("principal artist ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="joensuu")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-hameenlinna')
def principal_artist_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("principal artist ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="hameenlinna")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-porvoo')
def principal_artist_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("principal artist ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="porvoo")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-mikkeli')
def principal_artist_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("principal artist ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="mikkeli")

@principal_artist.route('/principal-artist-avoimet-tyopaikat-hyvinkaa')
def principal_artist_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("principal artist ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="hyvinkaa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-nurmijarvi')
def principal_artist_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("principal artist ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="nurmijarvi")

@principal_artist.route('/principal-artist-avoimet-tyopaikat-jarvenpaa')
def principal_artist_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("principal artist ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="jarvenpaa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-rauma')
def principal_artist_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("principal artist ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="rauma")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-lohja')
def principal_artist_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("principal artist ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lohja")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-karleby')
def principal_artist_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("principal artist ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="karleby")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kajaani')
def principal_artist_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("principal artist ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kajaani")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-rovaniemi')
def principal_artist_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("principal artist ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="rovaniemi")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-tuusula')
def principal_artist_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("principal artist ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="tuusula")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kirkkonummi')
def principal_artist_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("principal artist ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kirkkonummi")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-seinajoki')
def principal_artist_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("principal artist ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="seinajoki")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kerava')
def principal_artist_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("principal artist ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kerava")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kouvola')
def principal_artist_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("principal artist ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kouvola")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-imatra')
def principal_artist_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("principal artist ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="imatra")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-nokia')
def principal_artist_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("principal artist ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="nokia")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-savonlinna')
def principal_artist_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("principal artist ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="savonlinna")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-riihimaki')
def principal_artist_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("principal artist ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="riihimaki")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-vihti')
def principal_artist_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("principal artist ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="vihti")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-salo')
def principal_artist_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("principal artist ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="salo")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kangasala')
def principal_artist_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("principal artist ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kangasala")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-raisio')
def principal_artist_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("principal artist ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="raisio")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-karhula')
def principal_artist_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("principal artist ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="karhula")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kemi')
def principal_artist_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("principal artist ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kemi")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-iisalmi')
def principal_artist_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("principal artist ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="iisalmi")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-varkaus')
def principal_artist_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("principal artist ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="varkaus")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-raahe')
def principal_artist_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("principal artist ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="raahe")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-ylojarvi')
def principal_artist_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("principal artist ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="ylojarvi")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-hamina')
def principal_artist_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("principal artist ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="hamina")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kaarina')
def principal_artist_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("principal artist ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kaarina")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-tornio')
def principal_artist_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("principal artist ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="tornio")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-heinola')
def principal_artist_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("principal artist ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="heinola")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-hollola')
def principal_artist_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("principal artist ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="hollola")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-valkeakoski')
def principal_artist_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("principal artist ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="valkeakoski")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-siilinjarvi')
def principal_artist_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("principal artist ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="siilinjarvi")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kuusankoski')
def principal_artist_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("principal artist ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kuusankoski")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-sibbo')
def principal_artist_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("principal artist ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="sibbo")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-jakostad')
def principal_artist_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("principal artist ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="jakostad")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-lempaala')
def principal_artist_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("principal artist ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lempaala")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-mantsala')
def principal_artist_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("principal artist ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="mantsala")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-forssa')
def principal_artist_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("principal artist ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="forssa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kuusamo')
def principal_artist_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("principal artist ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kuusamo")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-haukipudas')
def principal_artist_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("principal artist ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="haukipudas")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-korsholm')
def principal_artist_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("principal artist ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="korsholm")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-laukaa')
def principal_artist_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("principal artist ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="laukaa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-anjala')
def principal_artist_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("principal artist ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="anjala")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-uusikaupunki')
def principal_artist_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("principal artist ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="uusikaupunki")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-janakkala')
def principal_artist_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("principal artist ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="janakkala")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-pirkkala')
def principal_artist_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("principal artist ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="pirkkala")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-lansi-turunmaa')
def principal_artist_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("principal artist ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lansi-turunmaa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-jamsa')
def principal_artist_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("principal artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="jamsa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-jamsa')
def principal_artist_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("principal artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="jamsa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-vammala')
def principal_artist_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("principal artist ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="vammala")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-nastola')
def principal_artist_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("principal artist ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="nastola")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-orimattila')
def principal_artist_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("principal artist ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="orimattila")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kauhajoki')
def principal_artist_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("principal artist ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kauhajoki")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-ekenas')
def principal_artist_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("principal artist ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="ekenas")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kempele')
def principal_artist_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("principal artist ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kempele")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-lapua')
def principal_artist_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("principal artist ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lapua")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-lieksa')
def principal_artist_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("principal artist ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lieksa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-naantali')
def principal_artist_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("principal artist ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="naantali")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-aanekoski')
def principal_artist_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("principal artist ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="aanekoski")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-ylivieska')
def principal_artist_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("principal artist ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="ylivieska")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kontiolahti')
def principal_artist_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("principal artist ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kontiolahti")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kankaanpaa')
def principal_artist_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("principal artist ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kankaanpaa")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-ulvila')
def principal_artist_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("principal artist ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="ulvila")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-pieksamaki')
def principal_artist_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("principal artist ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="pieksamaki")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kiiminki')
def principal_artist_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("principal artist ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kiiminki")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-pargas')
def principal_artist_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("principal artist ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="pargas")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-nurmo')
def principal_artist_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("principal artist ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="nurmo")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-ilmajoki')
def principal_artist_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("principal artist ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="ilmajoki")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-liperi')
def principal_artist_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("principal artist ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="liperi")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-keuruu')
def principal_artist_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("principal artist ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="keuruu")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-leppavirta')
def principal_artist_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("principal artist ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="leppavirta")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kurikka')
def principal_artist_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("principal artist ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kurikka")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-nivala')
def principal_artist_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("principal artist ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="nivala")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-joutseno')
def principal_artist_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("principal artist ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="joutseno")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-pedersore')
def principal_artist_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("principal artist ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="pedersore")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-sotkamo')
def principal_artist_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("principal artist ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="sotkamo")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-kuhmo')
def principal_artist_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("principal artist ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kuhmo")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-paimio')
def principal_artist_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("principal artist ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="paimio")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-saarijarvi')
def principal_artist_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("principal artist ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="saarijarvi")
	
@principal_artist.route('/principal-artist-avoimet-tyopaikat-helsinki')
def principal_artist_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("principal artist ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="helsinki")


####################################################################


##############################################
@principal_artist.route('/principal-artist-jobs-espoo')
def principal_artist_jobs2(page=1):

    job_list = job_obj.get_job("principal artist ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="espoo")

@principal_artist.route('/principal-artist-jobs-tampere')
def principal_artist_jobs3(page=1):

    job_list = job_obj.get_job("principal artist ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="tampere")
	
@principal_artist.route('/principal-artist-jobs-vantaa')
def principal_artist_jobs4(page=1):

    job_list = job_obj.get_job("principal artist ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="vantaa")
	
@principal_artist.route('/principal-artist-jobs-turku')
def principal_artist_jobs5(page=1):

    job_list = job_obj.get_job("principal artist ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="turku")
	
@principal_artist.route('/principal-artist-jobs-oulu')
def principal_artist_jobs6(page=1):

    job_list = job_obj.get_job("principal artist ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="oulu")
	
@principal_artist.route('/principal-artist-jobs-lahti')
def principal_artist_jobs7(page=1):

    job_list = job_obj.get_job("principal artist ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lahti")
	
@principal_artist.route('/principal-artist-jobs-kuopio')
def principal_artist_jobs8(page=1):

    job_list = job_obj.get_job("principal artist ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kuopio")
	
@principal_artist.route('/principal-artist-jobs-jyvvaskyla')
def principal_artist_jobs9(page=1):

    job_list = job_obj.get_job("principal artist ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="jyvvaskyla")

@principal_artist.route('/principal-artist-jobs-pori')
def principal_artist_jobs10(page=1):

    job_list = job_obj.get_job("principal artist ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="pori")

@principal_artist.route('/principal-artist-jobs-lappeenranta')
def principal_artist_jobs11(page=1):

    job_list = job_obj.get_job("principal artist ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lappeenranta")	
	
@principal_artist.route('/principal-artist-jobs-vaasa')
def principal_artist_jobs12(page=1):

    job_list = job_obj.get_job("principal artist ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="vaasa")
	
@principal_artist.route('/principal-artist-jobs-kotka')
def principal_artist_jobs13(page=1):

    job_list = job_obj.get_job("principal artist ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kotka")
	
@principal_artist.route('/principal-artist-jobs-joensuu')
def principal_artist_jobs14(page=1):

    job_list = job_obj.get_job("principal artist ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="joensuu")
	
@principal_artist.route('/principal-artist-jobs-hameenlinna')
def principal_artist_jobs15(page=1):

    job_list = job_obj.get_job("principal artist ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="hameenlinna")
	
@principal_artist.route('/principal-artist-jobs-porvoo')
def principal_artist_jobs16(page=1):

    job_list = job_obj.get_job("principal artist ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="porvoo")
	
@principal_artist.route('/principal-artist-jobs-mikkeli')
def principal_artist_jobs17(page=1):

    job_list = job_obj.get_job("principal artist ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="mikkeli")

@principal_artist.route('/principal-artist-jobs-hyvinkaa')
def principal_artist_jobs18(page=1):

    job_list = job_obj.get_job("principal artist ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="hyvinkaa")
	
@principal_artist.route('/principal-artist-jobs-nurmijarvi')
def principal_artist_jobs19(page=1):

    job_list = job_obj.get_job("principal artist ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="nurmijarvi")

@principal_artist.route('/principal-artist-jobs-jarvenpaa')
def principal_artist_jobs20(page=1):

    job_list = job_obj.get_job("principal artist ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="jarvenpaa")
	
@principal_artist.route('/principal-artist-jobs-rauma')
def principal_artist_jobs21(page=1):

    job_list = job_obj.get_job("principal artist ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="rauma")
	
@principal_artist.route('/principal-artist-jobs-lohja')
def principal_artist_jobs22(page=1):

    job_list = job_obj.get_job("principal artist ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lohja")
	
@principal_artist.route('/principal-artist-jobs-karleby')
def principal_artist_jobs23(page=1):

    job_list = job_obj.get_job("principal artist ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="karleby")
	
@principal_artist.route('/principal-artist-jobs-kajaani')
def principal_artist_jobs24(page=1):

    job_list = job_obj.get_job("principal artist ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kajaani")
	
@principal_artist.route('/principal-artist-jobs-rovaniemi')
def principal_artist_jobs25(page=1):

    job_list = job_obj.get_job("principal artist ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="rovaniemi")
	
@principal_artist.route('/principal-artist-jobs-tuusula')
def principal_artist_jobs26(page=1):

    job_list = job_obj.get_job("principal artist ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="tuusula")
	
@principal_artist.route('/principal-artist-jobs-kirkkonummi')
def principal_artist_jobs27(page=1):

    job_list = job_obj.get_job("principal artist ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kirkkonummi")
	
@principal_artist.route('/principal-artist-jobs-seinajoki')
def principal_artist_jobs28(page=1):

    job_list = job_obj.get_job("principal artist ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="seinajoki")
	
@principal_artist.route('/principal-artist-jobs-kerava')
def principal_artist_jobs29(page=1):

    job_list = job_obj.get_job("principal artist ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kerava")
	
@principal_artist.route('/principal-artist-jobs-kouvola')
def principal_artist_jobs30(page=1):

    job_list = job_obj.get_job("principal artist ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kouvola")
	
@principal_artist.route('/principal-artist-jobs-imatra')
def principal_artist_jobs31(page=1):

    job_list = job_obj.get_job("principal artist ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="imatra")
	
@principal_artist.route('/principal-artist-jobs-nokia')
def principal_artist_jobs32_1(page=1):

    job_list = job_obj.get_job("principal artist ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="nokia")
	
@principal_artist.route('/principal-artist-jobs-savonlinna')
def principal_artist_jobs32(page=1):

    job_list = job_obj.get_job("principal artist ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="savonlinna")
	
@principal_artist.route('/principal-artist-jobs-riihimaki')
def principal_artist_jobs33(page=1):

    job_list = job_obj.get_job("principal artist ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="riihimaki")
	
@principal_artist.route('/principal-artist-jobs-vihti')
def principal_artist_jobs34(page=1):

    job_list = job_obj.get_job("principal artist ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="vihti")
	
@principal_artist.route('/principal-artist-jobs-salo')
def principal_artist_jobs35(page=1):

    job_list = job_obj.get_job("principal artist ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="salo")
	
@principal_artist.route('/principal-artist-jobs-kangasala')
def principal_artist_jobs36(page=1):

    job_list = job_obj.get_job("principal artist ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kangasala")
	
@principal_artist.route('/principal-artist-jobs-raisio')
def principal_artist_jobs37_1(page=1):

    job_list = job_obj.get_job("principal artist ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="raisio")
	
@principal_artist.route('/principal-artist-jobs-karhula')
def principal_artist_jobs37(page=1):

    job_list = job_obj.get_job("principal artist ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="karhula")
	
@principal_artist.route('/principal-artist-jobs-kemi')
def principal_artist_jobs38(page=1):

    job_list = job_obj.get_job("principal artist ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kemi")
	
@principal_artist.route('/principal-artist-jobs-iisalmi')
def principal_artist_jobs39(page=1):

    job_list = job_obj.get_job("principal artist ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="iisalmi")
	
@principal_artist.route('/principal-artist-jobs-varkaus')
def principal_artist_jobs40(page=1):

    job_list = job_obj.get_job("principal artist ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="varkaus")
	
@principal_artist.route('/principal-artist-jobs-raahe')
def principal_artist_jobs41(page=1):

    job_list = job_obj.get_job("principal artist ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="raahe")
	
@principal_artist.route('/principal-artist-jobs-ylojarvi')
def principal_artist_jobs42_1(page=1):

    job_list = job_obj.get_job("principal artist ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="ylojarvi")
	
@principal_artist.route('/principal-artist-jobs-hamina')
def principal_artist_jobs42(page=1):

    job_list = job_obj.get_job("principal artist ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="hamina")
	
@principal_artist.route('/principal-artist-jobs-kaarina')
def principal_artist_jobs43(page=1):

    job_list = job_obj.get_job("principal artist ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kaarina")
	
@principal_artist.route('/principal-artist-jobs-tornio')
def principal_artist_jobs44(page=1):

    job_list = job_obj.get_job("principal artist ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="tornio")
	
@principal_artist.route('/principal-artist-jobs-heinola')
def principal_artist_jobs45(page=1):

    job_list = job_obj.get_job("principal artist ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="heinola")
	
@principal_artist.route('/principal-artist-jobs-hollola')
def principal_artist_jobs46(page=1):

    job_list = job_obj.get_job("principal artist ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="hollola")
	
@principal_artist.route('/principal-artist-jobs-valkeakoski')
def principal_artist_jobs47(page=1):

    job_list = job_obj.get_job("principal artist ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="valkeakoski")
	
@principal_artist.route('/principal-artist-jobs-siilinjarvi')
def principal_artist_jobs48(page=1):

    job_list = job_obj.get_job("principal artist ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="siilinjarvi")
	
@principal_artist.route('/principal-artist-jobs-kuusankoski')
def principal_artist_jobs49(page=1):

    job_list = job_obj.get_job("principal artist ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kuusankoski")
	
@principal_artist.route('/principal-artist-jobs-sibbo')
def principal_artist_jobs50(page=1):

    job_list = job_obj.get_job("principal artist ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="sibbo")
	
@principal_artist.route('/principal-artist-jobs-jakostad')
def principal_artist_jobs51(page=1):

    job_list = job_obj.get_job("principal artist ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="jakostad")
	
@principal_artist.route('/principal-artist-jobs-lempaala')
def principal_artist_jobs52(page=1):

    job_list = job_obj.get_job("principal artist ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lempaala")
	
@principal_artist.route('/principal-artist-jobs-mantsala')
def principal_artist_jobs52_1(page=1):

    job_list = job_obj.get_job("principal artist ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="mantsala")
	
@principal_artist.route('/principal-artist-jobs-forssa')
def principal_artist_jobs53(page=1):

    job_list = job_obj.get_job("principal artist ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="forssa")
	
@principal_artist.route('/principal-artist-jobs-kuusamo')
def principal_artist_jobs54(page=1):

    job_list = job_obj.get_job("principal artist ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kuusamo")
	
@principal_artist.route('/principal-artist-jobs-haukipudas')
def principal_artist_jobs55(page=1):

    job_list = job_obj.get_job("principal artist ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="haukipudas")
	
@principal_artist.route('/principal-artist-jobs-korsholm')
def principal_artist_jobs56(page=1):

    job_list = job_obj.get_job("principal artist ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="korsholm")
	
@principal_artist.route('/principal-artist-jobs-laukaa')
def principal_artist_jobs57(page=1):

    job_list = job_obj.get_job("principal artist ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="laukaa")
	
@principal_artist.route('/principal-artist-jobs-anjala')
def principal_artist_jobs58(page=1):

    job_list = job_obj.get_job("principal artist ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="anjala")
	
@principal_artist.route('/principal-artist-jobs-uusikaupunki')
def principal_artist_jobs59(page=1):

    job_list = job_obj.get_job("principal artist ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="uusikaupunki")
	
@principal_artist.route('/principal-artist-jobs-janakkala')
def principal_artist_jobs60(page=1):

    job_list = job_obj.get_job("principal artist ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="janakkala")
	
@principal_artist.route('/principal-artist-jobs-pirkkala')
def principal_artist_jobs61(page=1):

    job_list = job_obj.get_job("principal artist ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="pirkkala")
	
@principal_artist.route('/principal-artist-jobs-lansi-turunmaa')
def principal_artist_jobs62(page=1):

    job_list = job_obj.get_job("principal artist ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lansi-turunmaa")
	
@principal_artist.route('/principal-artist-jobs-jamsa')
def principal_artist_jobs63(page=1):

    job_list = job_obj.get_job("principal artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="jamsa")
	
@principal_artist.route('/principal-artist-jobs-jamsa')
def principal_artist_jobs64(page=1):

    job_list = job_obj.get_job("principal artist ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="jamsa")
	
@principal_artist.route('/principal-artist-jobs-vammala')
def principal_artist_jobs65(page=1):

    job_list = job_obj.get_job("principal artist ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="vammala")
	
@principal_artist.route('/principal-artist-jobs-nastola')
def principal_artist_jobs66(page=1):

    job_list = job_obj.get_job("principal artist ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="nastola")
	
@principal_artist.route('/principal-artist-jobs-orimattila')
def principal_artist_jobs67(page=1):

    job_list = job_obj.get_job("principal artist ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="orimattila")
	
@principal_artist.route('/principal-artist-jobs-kauhajoki')
def principal_artist_jobs68(page=1):

    job_list = job_obj.get_job("principal artist ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kauhajoki")
	
@principal_artist.route('/principal-artist-jobs-ekenas')
def principal_artist_jobs69(page=1):

    job_list = job_obj.get_job("principal artist ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="ekenas")
	
@principal_artist.route('/principal-artist-jobs-kempele')
def principal_artist_jobs70(page=1):

    job_list = job_obj.get_job("principal artist ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kempele")
	
@principal_artist.route('/principal-artist-jobs-lapua')
def principal_artist_jobs71(page=1):

    job_list = job_obj.get_job("principal artist ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lapua")
	
@principal_artist.route('/principal-artist-jobs-lieksa')
def principal_artist_jobs72(page=1):

    job_list = job_obj.get_job("principal artist ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="lieksa")
	
@principal_artist.route('/principal-artist-jobs-naantali')
def principal_artist_jobs73(page=1):

    job_list = job_obj.get_job("principal artist ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="naantali")
	
@principal_artist.route('/principal-artist-jobs-aanekoski')
def principal_artist_jobs74(page=1):

    job_list = job_obj.get_job("principal artist ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="aanekoski")
	
@principal_artist.route('/principal-artist-jobs-ylivieska')
def principal_artist_jobs75(page=1):

    job_list = job_obj.get_job("principal artist ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="ylivieska")
	
@principal_artist.route('/principal-artist-jobs-kontiolahti')
def principal_artist_jobs76(page=1):

    job_list = job_obj.get_job("principal artist ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kontiolahti")
	
@principal_artist.route('/principal-artist-jobs-kankaanpaa')
def principal_artist_jobs77(page=1):

    job_list = job_obj.get_job("principal artist ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kankaanpaa")
	
@principal_artist.route('/principal-artist-jobs-ulvila')
def principal_artist_jobs78(page=1):

    job_list = job_obj.get_job("principal artist ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="ulvila")
	
@principal_artist.route('/principal-artist-jobs-pieksamaki')
def principal_artist_jobs79(page=1):

    job_list = job_obj.get_job("principal artist ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="pieksamaki")
	
@principal_artist.route('/principal-artist-jobs-kiiminki')
def principal_artist_jobs80(page=1):

    job_list = job_obj.get_job("principal artist ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kiiminki")
	
@principal_artist.route('/principal-artist-jobs-pargas')
def principal_artist_jobs81(page=1):

    job_list = job_obj.get_job("principal artist ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="pargas")
	
@principal_artist.route('/principal-artist-jobs-nurmo')
def principal_artist_jobs82(page=1):

    job_list = job_obj.get_job("principal artist ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="nurmo")
	
@principal_artist.route('/principal-artist-jobs-ilmajoki')
def principal_artist_jobs83(page=1):

    job_list = job_obj.get_job("principal artist ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="ilmajoki")
	
@principal_artist.route('/principal-artist-jobs-liperi')
def principal_artist_jobs84(page=1):

    job_list = job_obj.get_job("principal artist ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="liperi")
	
@principal_artist.route('/principal-artist-jobs-keuruu')
def principal_artist_jobs85(page=1):

    job_list = job_obj.get_job("principal artist ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="keuruu")
	
@principal_artist.route('/principal-artist-jobs-leppavirta')
def principal_artist_jobs86(page=1):

    job_list = job_obj.get_job("principal artist ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="leppavirta")
	
@principal_artist.route('/principal-artist-jobs-kurikka')
def principal_artist_jobs87(page=1):

    job_list = job_obj.get_job("principal artist ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kurikka")
	
@principal_artist.route('/principal-artist-jobs-nivala')
def principal_artist_jobs88(page=1):

    job_list = job_obj.get_job("principal artist ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="nivala")
	
@principal_artist.route('/principal-artist-jobs-joutseno')
def principal_artist_jobs89(page=1):

    job_list = job_obj.get_job("principal artist ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="joutseno")
	
@principal_artist.route('/principal-artist-jobs-pedersore')
def principal_artist_jobs90(page=1):

    job_list = job_obj.get_job("principal artist ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="pedersore")
	
@principal_artist.route('/principal-artist-jobs-sotkamo')
def principal_artist_jobs91(page=1):

    job_list = job_obj.get_job("principal artist ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="sotkamo")
	
@principal_artist.route('/principal-artist-jobs-kuhmo')
def principal_artist_jobs92(page=1):

    job_list = job_obj.get_job("principal artist ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="kuhmo")
	
@principal_artist.route('/principal-artist-jobs-paimio')
def principal_artist_jobs93(page=1):

    job_list = job_obj.get_job("principal artist ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="paimio")
	
@principal_artist.route('/principal-artist-jobs-saarijarvi')
def principal_artist_jobs94(page=1):

    job_list = job_obj.get_job("principal artist ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="saarijarvi")
	
@principal_artist.route('/principal-artist-jobs-helsinki')
def principal_artist_jobs95(page=1):

    job_list = job_obj.get_job("principal artist ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist ", location="helsinki")


####################################################################


##############################################
@principal_artist.route('/principal-artist-tyopaikat-espoo')
def principal_artist_tyopaikat2(page=1):

    job_list = job_obj.get_job("principal artist", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="espoo")

@principal_artist.route('/principal-artist-tyopaikat-tampere')
def principal_artist_tyopaikat3(page=1):

    job_list = job_obj.get_job("principal artist", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="tampere")
	
@principal_artist.route('/principal-artist-tyopaikat-vantaa')
def principal_artist_tyopaikat4(page=1):

    job_list = job_obj.get_job("principal artist", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="vantaa")
	
@principal_artist.route('/principal-artist-tyopaikat-turku')
def principal_artist_tyopaikat5(page=1):

    job_list = job_obj.get_job("principal artist", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="turku")
	
@principal_artist.route('/principal-artist-tyopaikat-oulu')
def principal_artist_tyopaikat6(page=1):

    job_list = job_obj.get_job("principal artist", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="oulu")
	
@principal_artist.route('/principal-artist-tyopaikat-lahti')
def principal_artist_tyopaikat7(page=1):

    job_list = job_obj.get_job("principal artist", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="lahti")
	
@principal_artist.route('/principal-artist-tyopaikat-kuopio')
def principal_artist_tyopaikat8(page=1):

    job_list = job_obj.get_job("principal artist", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kuopio")
	
@principal_artist.route('/principal-artist-tyopaikat-jyvvaskyla')
def principal_artist_tyopaikat9(page=1):

    job_list = job_obj.get_job("principal artist", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="jyvvaskyla")

@principal_artist.route('/principal-artist-tyopaikat-pori')
def principal_artist_tyopaikat10(page=1):

    job_list = job_obj.get_job("principal artist", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="pori")

@principal_artist.route('/principal-artist-tyopaikat-lappeenranta')
def principal_artist_tyopaikat11(page=1):

    job_list = job_obj.get_job("principal artist", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="lappeenranta")	
	
@principal_artist.route('/principal-artist-tyopaikat-vaasa')
def principal_artist_tyopaikat12(page=1):

    job_list = job_obj.get_job("principal artist", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="vaasa")
	
@principal_artist.route('/principal-artist-tyopaikat-kotka')
def principal_artist_tyopaikat13(page=1):

    job_list = job_obj.get_job("principal artist", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kotka")
	
@principal_artist.route('/principal-artist-tyopaikat-joensuu')
def principal_artist_tyopaikat14(page=1):

    job_list = job_obj.get_job("principal artist", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="joensuu")
	
@principal_artist.route('/principal-artist-tyopaikat-hameenlinna')
def principal_artist_tyopaikat15(page=1):

    job_list = job_obj.get_job("principal artist", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="hameenlinna")
	
@principal_artist.route('/principal-artist-tyopaikat-porvoo')
def principal_artist_tyopaikat16(page=1):

    job_list = job_obj.get_job("principal artist", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="porvoo")
	
@principal_artist.route('/principal-artist-tyopaikat-mikkeli')
def principal_artist_tyopaikat17(page=1):

    job_list = job_obj.get_job("principal artist", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="mikkeli")

@principal_artist.route('/principal-artist-tyopaikat-hyvinkaa')
def principal_artist_tyopaikat18(page=1):

    job_list = job_obj.get_job("principal artist", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="hyvinkaa")
	
@principal_artist.route('/principal-artist-tyopaikat-nurmijarvi')
def principal_artist_tyopaikat19(page=1):

    job_list = job_obj.get_job("principal artist", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="nurmijarvi")

@principal_artist.route('/principal-artist-tyopaikat-jarvenpaa')
def principal_artist_tyopaikat20(page=1):

    job_list = job_obj.get_job("principal artist", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="jarvenpaa")
	
@principal_artist.route('/principal-artist-tyopaikat-rauma')
def principal_artist_tyopaikat21(page=1):

    job_list = job_obj.get_job("principal artist", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="rauma")
	
@principal_artist.route('/principal-artist-tyopaikat-lohja')
def principal_artist_tyopaikat22(page=1):

    job_list = job_obj.get_job("principal artist", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="lohja")
	
@principal_artist.route('/principal-artist-tyopaikat-karleby')
def principal_artist_tyopaikat23(page=1):

    job_list = job_obj.get_job("principal artist", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="karleby")
	
@principal_artist.route('/principal-artist-tyopaikat-kajaani')
def principal_artist_tyopaikat24(page=1):

    job_list = job_obj.get_job("principal artist", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kajaani")
	
@principal_artist.route('/principal-artist-tyopaikat-rovaniemi')
def principal_artist_tyopaikat25(page=1):

    job_list = job_obj.get_job("principal artist", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="rovaniemi")
	
@principal_artist.route('/principal-artist-tyopaikat-tuusula')
def principal_artist_tyopaikat26(page=1):

    job_list = job_obj.get_job("principal artist", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="tuusula")
	
@principal_artist.route('/principal-artist-tyopaikat-kirkkonummi')
def principal_artist_tyopaikat27(page=1):

    job_list = job_obj.get_job("principal artist", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kirkkonummi")
	
@principal_artist.route('/principal-artist-tyopaikat-seinajoki')
def principal_artist_tyopaikat28(page=1):

    job_list = job_obj.get_job("principal artist", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="seinajoki")
	
@principal_artist.route('/principal-artist-tyopaikat-kerava')
def principal_artist_tyopaikat29(page=1):

    job_list = job_obj.get_job("principal artist", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kerava")
	
@principal_artist.route('/principal-artist-tyopaikat-kouvola')
def principal_artist_tyopaikat30(page=1):

    job_list = job_obj.get_job("principal artist", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kouvola")
	
@principal_artist.route('/principal-artist-tyopaikat-imatra')
def principal_artist_tyopaikat31(page=1):

    job_list = job_obj.get_job("principal artist", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="imatra")
	
@principal_artist.route('/principal-artist-tyopaikat-nokia')
def principal_artist_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("principal artist", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="nokia")
	
@principal_artist.route('/principal-artist-tyopaikat-savonlinna')
def principal_artist_tyopaikat32(page=1):

    job_list = job_obj.get_job("principal artist", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="savonlinna")
	
@principal_artist.route('/principal-artist-tyopaikat-riihimaki')
def principal_artist_tyopaikat33(page=1):

    job_list = job_obj.get_job("principal artist", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="riihimaki")
	
@principal_artist.route('/principal-artist-tyopaikat-vihti')
def principal_artist_tyopaikat34(page=1):

    job_list = job_obj.get_job("principal artist", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="vihti")
	
@principal_artist.route('/principal-artist-tyopaikat-salo')
def principal_artist_tyopaikat35(page=1):

    job_list = job_obj.get_job("principal artist", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="salo")
	
@principal_artist.route('/principal-artist-tyopaikat-kangasala')
def principal_artist_tyopaikat36(page=1):

    job_list = job_obj.get_job("principal artist", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kangasala")
	
@principal_artist.route('/principal-artist-tyopaikat-raisio')
def principal_artist_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("principal artist", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="raisio")
	
@principal_artist.route('/principal-artist-tyopaikat-karhula')
def principal_artist_tyopaikat37(page=1):

    job_list = job_obj.get_job("principal artist", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="karhula")
	
@principal_artist.route('/principal-artist-tyopaikat-kemi')
def principal_artist_tyopaikat38(page=1):

    job_list = job_obj.get_job("principal artist", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kemi")
	
@principal_artist.route('/principal-artist-tyopaikat-iisalmi')
def principal_artist_tyopaikat39(page=1):

    job_list = job_obj.get_job("principal artist", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="iisalmi")
	
@principal_artist.route('/principal-artist-tyopaikat-varkaus')
def principal_artist_tyopaikat40(page=1):

    job_list = job_obj.get_job("principal artist", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="varkaus")
	
@principal_artist.route('/principal-artist-tyopaikat-raahe')
def principal_artist_tyopaikat41(page=1):

    job_list = job_obj.get_job("principal artist", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="raahe")
	
@principal_artist.route('/principal-artist-tyopaikat-ylojarvi')
def principal_artist_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("principal artist", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="ylojarvi")
	
@principal_artist.route('/principal-artist-tyopaikat-hamina')
def principal_artist_tyopaikat42(page=1):

    job_list = job_obj.get_job("principal artist", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="hamina")
	
@principal_artist.route('/principal-artist-tyopaikat-kaarina')
def principal_artist_tyopaikat43(page=1):

    job_list = job_obj.get_job("principal artist", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kaarina")
	
@principal_artist.route('/principal-artist-tyopaikat-tornio')
def principal_artist_tyopaikat44(page=1):

    job_list = job_obj.get_job("principal artist", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="tornio")
	
@principal_artist.route('/principal-artist-tyopaikat-heinola')
def principal_artist_tyopaikat45(page=1):

    job_list = job_obj.get_job("principal artist", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="heinola")
	
@principal_artist.route('/principal-artist-tyopaikat-hollola')
def principal_artist_tyopaikat46(page=1):

    job_list = job_obj.get_job("principal artist", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="hollola")
	
@principal_artist.route('/principal-artist-tyopaikat-valkeakoski')
def principal_artist_tyopaikat47(page=1):

    job_list = job_obj.get_job("principal artist", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="valkeakoski")
	
@principal_artist.route('/principal-artist-tyopaikat-siilinjarvi')
def principal_artist_tyopaikat48(page=1):

    job_list = job_obj.get_job("principal artist", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="siilinjarvi")
	
@principal_artist.route('/principal-artist-tyopaikat-kuusankoski')
def principal_artist_tyopaikat49(page=1):

    job_list = job_obj.get_job("principal artist", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kuusankoski")
	
@principal_artist.route('/principal-artist-tyopaikat-sibbo')
def principal_artist_tyopaikat50(page=1):

    job_list = job_obj.get_job("principal artist", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="sibbo")
	
@principal_artist.route('/principal-artist-tyopaikat-jakostad')
def principal_artist_tyopaikat51(page=1):

    job_list = job_obj.get_job("principal artist", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="jakostad")
	
@principal_artist.route('/principal-artist-tyopaikat-lempaala')
def principal_artist_tyopaikat52(page=1):

    job_list = job_obj.get_job("principal artist", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="lempaala")
	
@principal_artist.route('/principal-artist-tyopaikat-mantsala')
def principal_artist_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("principal artist", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="mantsala")
	
@principal_artist.route('/principal-artist-tyopaikat-forssa')
def principal_artist_tyopaikat53(page=1):

    job_list = job_obj.get_job("principal artist", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="forssa")
	
@principal_artist.route('/principal-artist-tyopaikat-kuusamo')
def principal_artist_tyopaikat54(page=1):

    job_list = job_obj.get_job("principal artist", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kuusamo")
	
@principal_artist.route('/principal-artist-tyopaikat-haukipudas')
def principal_artist_tyopaikat55(page=1):

    job_list = job_obj.get_job("principal artist", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="haukipudas")
	
@principal_artist.route('/principal-artist-tyopaikat-korsholm')
def principal_artist_tyopaikat56(page=1):

    job_list = job_obj.get_job("principal artist", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="korsholm")
	
@principal_artist.route('/principal-artist-tyopaikat-laukaa')
def principal_artist_tyopaikat57(page=1):

    job_list = job_obj.get_job("principal artist", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="laukaa")
	
@principal_artist.route('/principal-artist-tyopaikat-anjala')
def principal_artist_tyopaikat58(page=1):

    job_list = job_obj.get_job("principal artist", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="anjala")
	
@principal_artist.route('/principal-artist-tyopaikat-uusikaupunki')
def principal_artist_tyopaikat59(page=1):

    job_list = job_obj.get_job("principal artist", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="uusikaupunki")
	
@principal_artist.route('/principal-artist-tyopaikat-janakkala')
def principal_artist_tyopaikat60(page=1):

    job_list = job_obj.get_job("principal artist", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="janakkala")
	
@principal_artist.route('/principal-artist-tyopaikat-pirkkala')
def principal_artist_tyopaikat61(page=1):

    job_list = job_obj.get_job("principal artist", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="pirkkala")
	
@principal_artist.route('/principal-artist-tyopaikat-lansi-turunmaa')
def principal_artist_tyopaikat62(page=1):

    job_list = job_obj.get_job("principal artist", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="lansi-turunmaa")
	
@principal_artist.route('/principal-artist-tyopaikat-jamsa')
def principal_artist_tyopaikat63(page=1):

    job_list = job_obj.get_job("principal artist", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="jamsa")
	
@principal_artist.route('/principal-artist-tyopaikat-jamsa')
def principal_artist_tyopaikat64(page=1):

    job_list = job_obj.get_job("principal artist", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="jamsa")
	
@principal_artist.route('/principal-artist-tyopaikat-vammala')
def principal_artist_tyopaikat65(page=1):

    job_list = job_obj.get_job("principal artist", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="vammala")
	
@principal_artist.route('/principal-artist-tyopaikat-nastola')
def principal_artist_tyopaikat66(page=1):

    job_list = job_obj.get_job("principal artist", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="nastola")
	
@principal_artist.route('/principal-artist-tyopaikat-orimattila')
def principal_artist_tyopaikat67(page=1):

    job_list = job_obj.get_job("principal artist", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="orimattila")
	
@principal_artist.route('/principal-artist-tyopaikat-kauhajoki')
def principal_artist_tyopaikat68(page=1):

    job_list = job_obj.get_job("principal artist", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kauhajoki")
	
@principal_artist.route('/principal-artist-tyopaikat-ekenas')
def principal_artist_tyopaikat69(page=1):

    job_list = job_obj.get_job("principal artist", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="ekenas")
	
@principal_artist.route('/principal-artist-tyopaikat-kempele')
def principal_artist_tyopaikat70(page=1):

    job_list = job_obj.get_job("principal artist", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kempele")
	
@principal_artist.route('/principal-artist-tyopaikat-lapua')
def principal_artist_tyopaikat71(page=1):

    job_list = job_obj.get_job("principal artist", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="lapua")
	
@principal_artist.route('/principal-artist-tyopaikat-lieksa')
def principal_artist_tyopaikat72(page=1):

    job_list = job_obj.get_job("principal artist", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="lieksa")
	
@principal_artist.route('/principal-artist-tyopaikat-naantali')
def principal_artist_tyopaikat73(page=1):

    job_list = job_obj.get_job("principal artist", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="naantali")
	
@principal_artist.route('/principal-artist-tyopaikat-aanekoski')
def principal_artist_tyopaikat74(page=1):

    job_list = job_obj.get_job("principal artist", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="aanekoski")
	
@principal_artist.route('/principal-artist-tyopaikat-ylivieska')
def principal_artist_tyopaikat75(page=1):

    job_list = job_obj.get_job("principal artist", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="ylivieska")
	
@principal_artist.route('/principal-artist-tyopaikat-kontiolahti')
def principal_artist_tyopaikat76(page=1):

    job_list = job_obj.get_job("principal artist", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kontiolahti")
	
@principal_artist.route('/principal-artist-tyopaikat-kankaanpaa')
def principal_artist_tyopaikat77(page=1):

    job_list = job_obj.get_job("principal artist", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kankaanpaa")
	
@principal_artist.route('/principal-artist-tyopaikat-ulvila')
def principal_artist_tyopaikat78(page=1):

    job_list = job_obj.get_job("principal artist", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="ulvila")
	
@principal_artist.route('/principal-artist-tyopaikat-pieksamaki')
def principal_artist_tyopaikat79(page=1):

    job_list = job_obj.get_job("principal artist", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="pieksamaki")
	
@principal_artist.route('/principal-artist-tyopaikat-kiiminki')
def principal_artist_tyopaikat80(page=1):

    job_list = job_obj.get_job("principal artist", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kiiminki")
	
@principal_artist.route('/principal-artist-tyopaikat-pargas')
def principal_artist_tyopaikat81(page=1):

    job_list = job_obj.get_job("principal artist", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="pargas")
	
@principal_artist.route('/principal-artist-tyopaikat-nurmo')
def principal_artist_tyopaikat82(page=1):

    job_list = job_obj.get_job("principal artist", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="nurmo")
	
@principal_artist.route('/principal-artist-tyopaikat-ilmajoki')
def principal_artist_tyopaikat83(page=1):

    job_list = job_obj.get_job("principal artist", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="ilmajoki")
	
@principal_artist.route('/principal-artist-tyopaikat-liperi')
def principal_artist_tyopaikat84(page=1):

    job_list = job_obj.get_job("principal artist", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="liperi")
	
@principal_artist.route('/principal-artist-tyopaikat-keuruu')
def principal_artist_tyopaikat85(page=1):

    job_list = job_obj.get_job("principal artist", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="keuruu")
	
@principal_artist.route('/principal-artist-tyopaikat-leppavirta')
def principal_artist_tyopaikat86(page=1):

    job_list = job_obj.get_job("principal artist", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="leppavirta")
	
@principal_artist.route('/principal-artist-tyopaikat-kurikka')
def principal_artist_tyopaikat87(page=1):

    job_list = job_obj.get_job("principal artist", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kurikka")
	
@principal_artist.route('/principal-artist-tyopaikat-nivala')
def principal_artist_tyopaikat88(page=1):

    job_list = job_obj.get_job("principal artist", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="nivala")
	
@principal_artist.route('/principal-artist-tyopaikat-joutseno')
def principal_artist_tyopaikat89(page=1):

    job_list = job_obj.get_job("principal artist", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="joutseno")
	
@principal_artist.route('/principal-artist-tyopaikat-pedersore')
def principal_artist_tyopaikat90(page=1):

    job_list = job_obj.get_job("principal artist", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="pedersore")
	
@principal_artist.route('/principal-artist-tyopaikat-sotkamo')
def principal_artist_tyopaikat91(page=1):

    job_list = job_obj.get_job("principal artist", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="sotkamo")
	
@principal_artist.route('/principal-artist-tyopaikat-kuhmo')
def principal_artist_tyopaikat92(page=1):

    job_list = job_obj.get_job("principal artist", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="kuhmo")
	
@principal_artist.route('/principal-artist-tyopaikat-paimio')
def principal_artist_tyopaikat93(page=1):

    job_list = job_obj.get_job("principal artist", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="paimio")
	
@principal_artist.route('/principal-artist-tyopaikat-saarijarvi')
def principal_artist_tyopaikat94(page=1):

    job_list = job_obj.get_job("principal artist", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist", location="saarijarvi")
	
@principal_artist.route('/principal-artist-tyopaikat-helsinki')
def principal_artist_tyopaikat95(page=1):

    job_list = job_obj.get_job("principal artist", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="principal artist  ", location="helsinki")
	  

