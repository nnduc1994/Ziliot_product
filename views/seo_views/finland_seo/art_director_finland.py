from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

art_director = Blueprint('art_director', __name__)
job_obj = Job()



####################################################################


@art_director.route('/art-director_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "art-director" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@art_director.route('/art-director-avoimet-tyopaikat-espoo')
def art_director_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("art director ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="espoo")

@art_director.route('/art-director-avoimet-tyopaikat-tampere')
def art_director_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("art director ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="tampere")
	
@art_director.route('/art-director-avoimet-tyopaikat-vantaa')
def art_director_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("art director ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="vantaa")
	
@art_director.route('/art-director-avoimet-tyopaikat-turku')
def art_director_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("art director ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="turku")
	
@art_director.route('/art-director-avoimet-tyopaikat-oulu')
def art_director_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("art director ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="oulu")
	
@art_director.route('/art-director-avoimet-tyopaikat-lahti')
def art_director_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("art director ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lahti")
	
@art_director.route('/art-director-avoimet-tyopaikat-kuopio')
def art_director_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("art director ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kuopio")
	
@art_director.route('/art-director-avoimet-tyopaikat-jyvvaskyla')
def art_director_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("art director ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="jyvvaskyla")

@art_director.route('/art-director-avoimet-tyopaikat-pori')
def art_director_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("art director ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="pori")

@art_director.route('/art-director-avoimet-tyopaikat-lappeenranta')
def art_director_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("art director ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lappeenranta")	
	
@art_director.route('/art-director-avoimet-tyopaikat-vaasa')
def art_director_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("art director ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="vaasa")
	
@art_director.route('/art-director-avoimet-tyopaikat-kotka')
def art_director_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("art director ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kotka")
	
@art_director.route('/art-director-avoimet-tyopaikat-joensuu')
def art_director_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("art director ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="joensuu")
	
@art_director.route('/art-director-avoimet-tyopaikat-hameenlinna')
def art_director_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("art director ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="hameenlinna")
	
@art_director.route('/art-director-avoimet-tyopaikat-porvoo')
def art_director_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("art director ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="porvoo")
	
@art_director.route('/art-director-avoimet-tyopaikat-mikkeli')
def art_director_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("art director ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="mikkeli")

@art_director.route('/art-director-avoimet-tyopaikat-hyvinkaa')
def art_director_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("art director ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="hyvinkaa")
	
@art_director.route('/art-director-avoimet-tyopaikat-nurmijarvi')
def art_director_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("art director ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="nurmijarvi")

@art_director.route('/art-director-avoimet-tyopaikat-jarvenpaa')
def art_director_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("art director ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="jarvenpaa")
	
@art_director.route('/art-director-avoimet-tyopaikat-rauma')
def art_director_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("art director ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="rauma")
	
@art_director.route('/art-director-avoimet-tyopaikat-lohja')
def art_director_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("art director ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lohja")
	
@art_director.route('/art-director-avoimet-tyopaikat-karleby')
def art_director_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("art director ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="karleby")
	
@art_director.route('/art-director-avoimet-tyopaikat-kajaani')
def art_director_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("art director ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kajaani")
	
@art_director.route('/art-director-avoimet-tyopaikat-rovaniemi')
def art_director_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("art director ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="rovaniemi")
	
@art_director.route('/art-director-avoimet-tyopaikat-tuusula')
def art_director_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("art director ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="tuusula")
	
@art_director.route('/art-director-avoimet-tyopaikat-kirkkonummi')
def art_director_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("art director ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kirkkonummi")
	
@art_director.route('/art-director-avoimet-tyopaikat-seinajoki')
def art_director_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("art director ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="seinajoki")
	
@art_director.route('/art-director-avoimet-tyopaikat-kerava')
def art_director_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("art director ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kerava")
	
@art_director.route('/art-director-avoimet-tyopaikat-kouvola')
def art_director_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("art director ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kouvola")
	
@art_director.route('/art-director-avoimet-tyopaikat-imatra')
def art_director_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("art director ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="imatra")
	
@art_director.route('/art-director-avoimet-tyopaikat-nokia')
def art_director_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("art director ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="nokia")
	
@art_director.route('/art-director-avoimet-tyopaikat-savonlinna')
def art_director_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("art director ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="savonlinna")
	
@art_director.route('/art-director-avoimet-tyopaikat-riihimaki')
def art_director_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("art director ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="riihimaki")
	
@art_director.route('/art-director-avoimet-tyopaikat-vihti')
def art_director_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("art director ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="vihti")
	
@art_director.route('/art-director-avoimet-tyopaikat-salo')
def art_director_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("art director ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="salo")
	
@art_director.route('/art-director-avoimet-tyopaikat-kangasala')
def art_director_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("art director ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kangasala")
	
@art_director.route('/art-director-avoimet-tyopaikat-raisio')
def art_director_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("art director ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="raisio")
	
@art_director.route('/art-director-avoimet-tyopaikat-karhula')
def art_director_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("art director ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="karhula")
	
@art_director.route('/art-director-avoimet-tyopaikat-kemi')
def art_director_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("art director ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kemi")
	
@art_director.route('/art-director-avoimet-tyopaikat-iisalmi')
def art_director_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("art director ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="iisalmi")
	
@art_director.route('/art-director-avoimet-tyopaikat-varkaus')
def art_director_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("art director ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="varkaus")
	
@art_director.route('/art-director-avoimet-tyopaikat-raahe')
def art_director_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("art director ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="raahe")
	
@art_director.route('/art-director-avoimet-tyopaikat-ylojarvi')
def art_director_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("art director ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="ylojarvi")
	
@art_director.route('/art-director-avoimet-tyopaikat-hamina')
def art_director_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("art director ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="hamina")
	
@art_director.route('/art-director-avoimet-tyopaikat-kaarina')
def art_director_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("art director ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kaarina")
	
@art_director.route('/art-director-avoimet-tyopaikat-tornio')
def art_director_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("art director ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="tornio")
	
@art_director.route('/art-director-avoimet-tyopaikat-heinola')
def art_director_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("art director ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="heinola")
	
@art_director.route('/art-director-avoimet-tyopaikat-hollola')
def art_director_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("art director ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="hollola")
	
@art_director.route('/art-director-avoimet-tyopaikat-valkeakoski')
def art_director_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("art director ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="valkeakoski")
	
@art_director.route('/art-director-avoimet-tyopaikat-siilinjarvi')
def art_director_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("art director ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="siilinjarvi")
	
@art_director.route('/art-director-avoimet-tyopaikat-kuusankoski')
def art_director_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("art director ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kuusankoski")
	
@art_director.route('/art-director-avoimet-tyopaikat-sibbo')
def art_director_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("art director ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="sibbo")
	
@art_director.route('/art-director-avoimet-tyopaikat-jakostad')
def art_director_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("art director ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="jakostad")
	
@art_director.route('/art-director-avoimet-tyopaikat-lempaala')
def art_director_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("art director ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lempaala")
	
@art_director.route('/art-director-avoimet-tyopaikat-mantsala')
def art_director_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("art director ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="mantsala")
	
@art_director.route('/art-director-avoimet-tyopaikat-forssa')
def art_director_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("art director ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="forssa")
	
@art_director.route('/art-director-avoimet-tyopaikat-kuusamo')
def art_director_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("art director ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kuusamo")
	
@art_director.route('/art-director-avoimet-tyopaikat-haukipudas')
def art_director_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("art director ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="haukipudas")
	
@art_director.route('/art-director-avoimet-tyopaikat-korsholm')
def art_director_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("art director ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="korsholm")
	
@art_director.route('/art-director-avoimet-tyopaikat-laukaa')
def art_director_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("art director ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="laukaa")
	
@art_director.route('/art-director-avoimet-tyopaikat-anjala')
def art_director_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("art director ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="anjala")
	
@art_director.route('/art-director-avoimet-tyopaikat-uusikaupunki')
def art_director_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("art director ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="uusikaupunki")
	
@art_director.route('/art-director-avoimet-tyopaikat-janakkala')
def art_director_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("art director ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="janakkala")
	
@art_director.route('/art-director-avoimet-tyopaikat-pirkkala')
def art_director_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("art director ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="pirkkala")
	
@art_director.route('/art-director-avoimet-tyopaikat-lansi-turunmaa')
def art_director_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("art director ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lansi-turunmaa")
	
@art_director.route('/art-director-avoimet-tyopaikat-jamsa')
def art_director_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("art director ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="jamsa")
	
@art_director.route('/art-director-avoimet-tyopaikat-jamsa')
def art_director_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("art director ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="jamsa")
	
@art_director.route('/art-director-avoimet-tyopaikat-vammala')
def art_director_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("art director ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="vammala")
	
@art_director.route('/art-director-avoimet-tyopaikat-nastola')
def art_director_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("art director ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="nastola")
	
@art_director.route('/art-director-avoimet-tyopaikat-orimattila')
def art_director_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("art director ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="orimattila")
	
@art_director.route('/art-director-avoimet-tyopaikat-kauhajoki')
def art_director_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("art director ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kauhajoki")
	
@art_director.route('/art-director-avoimet-tyopaikat-ekenas')
def art_director_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("art director ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="ekenas")
	
@art_director.route('/art-director-avoimet-tyopaikat-kempele')
def art_director_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("art director ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kempele")
	
@art_director.route('/art-director-avoimet-tyopaikat-lapua')
def art_director_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("art director ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lapua")
	
@art_director.route('/art-director-avoimet-tyopaikat-lieksa')
def art_director_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("art director ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lieksa")
	
@art_director.route('/art-director-avoimet-tyopaikat-naantali')
def art_director_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("art director ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="naantali")
	
@art_director.route('/art-director-avoimet-tyopaikat-aanekoski')
def art_director_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("art director ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="aanekoski")
	
@art_director.route('/art-director-avoimet-tyopaikat-ylivieska')
def art_director_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("art director ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="ylivieska")
	
@art_director.route('/art-director-avoimet-tyopaikat-kontiolahti')
def art_director_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("art director ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kontiolahti")
	
@art_director.route('/art-director-avoimet-tyopaikat-kankaanpaa')
def art_director_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("art director ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kankaanpaa")
	
@art_director.route('/art-director-avoimet-tyopaikat-ulvila')
def art_director_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("art director ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="ulvila")
	
@art_director.route('/art-director-avoimet-tyopaikat-pieksamaki')
def art_director_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("art director ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="pieksamaki")
	
@art_director.route('/art-director-avoimet-tyopaikat-kiiminki')
def art_director_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("art director ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kiiminki")
	
@art_director.route('/art-director-avoimet-tyopaikat-pargas')
def art_director_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("art director ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="pargas")
	
@art_director.route('/art-director-avoimet-tyopaikat-nurmo')
def art_director_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("art director ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="nurmo")
	
@art_director.route('/art-director-avoimet-tyopaikat-ilmajoki')
def art_director_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("art director ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="ilmajoki")
	
@art_director.route('/art-director-avoimet-tyopaikat-liperi')
def art_director_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("art director ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="liperi")
	
@art_director.route('/art-director-avoimet-tyopaikat-keuruu')
def art_director_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("art director ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="keuruu")
	
@art_director.route('/art-director-avoimet-tyopaikat-leppavirta')
def art_director_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("art director ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="leppavirta")
	
@art_director.route('/art-director-avoimet-tyopaikat-kurikka')
def art_director_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("art director ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kurikka")
	
@art_director.route('/art-director-avoimet-tyopaikat-nivala')
def art_director_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("art director ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="nivala")
	
@art_director.route('/art-director-avoimet-tyopaikat-joutseno')
def art_director_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("art director ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="joutseno")
	
@art_director.route('/art-director-avoimet-tyopaikat-pedersore')
def art_director_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("art director ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="pedersore")
	
@art_director.route('/art-director-avoimet-tyopaikat-sotkamo')
def art_director_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("art director ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="sotkamo")
	
@art_director.route('/art-director-avoimet-tyopaikat-kuhmo')
def art_director_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("art director ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kuhmo")
	
@art_director.route('/art-director-avoimet-tyopaikat-paimio')
def art_director_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("art director ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="paimio")
	
@art_director.route('/art-director-avoimet-tyopaikat-saarijarvi')
def art_director_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("art director ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="saarijarvi")
	
@art_director.route('/art-director-avoimet-tyopaikat-helsinki')
def art_director_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("art director ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="helsinki")


####################################################################


##############################################
@art_director.route('/art-director-jobs-espoo')
def art_director_jobs2(page=1):

    job_list = job_obj.get_job("art director ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="espoo")

@art_director.route('/art-director-jobs-tampere')
def art_director_jobs3(page=1):

    job_list = job_obj.get_job("art director ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="tampere")
	
@art_director.route('/art-director-jobs-vantaa')
def art_director_jobs4(page=1):

    job_list = job_obj.get_job("art director ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="vantaa")
	
@art_director.route('/art-director-jobs-turku')
def art_director_jobs5(page=1):

    job_list = job_obj.get_job("art director ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="turku")
	
@art_director.route('/art-director-jobs-oulu')
def art_director_jobs6(page=1):

    job_list = job_obj.get_job("art director ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="oulu")
	
@art_director.route('/art-director-jobs-lahti')
def art_director_jobs7(page=1):

    job_list = job_obj.get_job("art director ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lahti")
	
@art_director.route('/art-director-jobs-kuopio')
def art_director_jobs8(page=1):

    job_list = job_obj.get_job("art director ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kuopio")
	
@art_director.route('/art-director-jobs-jyvvaskyla')
def art_director_jobs9(page=1):

    job_list = job_obj.get_job("art director ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="jyvvaskyla")

@art_director.route('/art-director-jobs-pori')
def art_director_jobs10(page=1):

    job_list = job_obj.get_job("art director ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="pori")

@art_director.route('/art-director-jobs-lappeenranta')
def art_director_jobs11(page=1):

    job_list = job_obj.get_job("art director ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lappeenranta")	
	
@art_director.route('/art-director-jobs-vaasa')
def art_director_jobs12(page=1):

    job_list = job_obj.get_job("art director ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="vaasa")
	
@art_director.route('/art-director-jobs-kotka')
def art_director_jobs13(page=1):

    job_list = job_obj.get_job("art director ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kotka")
	
@art_director.route('/art-director-jobs-joensuu')
def art_director_jobs14(page=1):

    job_list = job_obj.get_job("art director ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="joensuu")
	
@art_director.route('/art-director-jobs-hameenlinna')
def art_director_jobs15(page=1):

    job_list = job_obj.get_job("art director ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="hameenlinna")
	
@art_director.route('/art-director-jobs-porvoo')
def art_director_jobs16(page=1):

    job_list = job_obj.get_job("art director ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="porvoo")
	
@art_director.route('/art-director-jobs-mikkeli')
def art_director_jobs17(page=1):

    job_list = job_obj.get_job("art director ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="mikkeli")

@art_director.route('/art-director-jobs-hyvinkaa')
def art_director_jobs18(page=1):

    job_list = job_obj.get_job("art director ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="hyvinkaa")
	
@art_director.route('/art-director-jobs-nurmijarvi')
def art_director_jobs19(page=1):

    job_list = job_obj.get_job("art director ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="nurmijarvi")

@art_director.route('/art-director-jobs-jarvenpaa')
def art_director_jobs20(page=1):

    job_list = job_obj.get_job("art director ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="jarvenpaa")
	
@art_director.route('/art-director-jobs-rauma')
def art_director_jobs21(page=1):

    job_list = job_obj.get_job("art director ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="rauma")
	
@art_director.route('/art-director-jobs-lohja')
def art_director_jobs22(page=1):

    job_list = job_obj.get_job("art director ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lohja")
	
@art_director.route('/art-director-jobs-karleby')
def art_director_jobs23(page=1):

    job_list = job_obj.get_job("art director ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="karleby")
	
@art_director.route('/art-director-jobs-kajaani')
def art_director_jobs24(page=1):

    job_list = job_obj.get_job("art director ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kajaani")
	
@art_director.route('/art-director-jobs-rovaniemi')
def art_director_jobs25(page=1):

    job_list = job_obj.get_job("art director ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="rovaniemi")
	
@art_director.route('/art-director-jobs-tuusula')
def art_director_jobs26(page=1):

    job_list = job_obj.get_job("art director ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="tuusula")
	
@art_director.route('/art-director-jobs-kirkkonummi')
def art_director_jobs27(page=1):

    job_list = job_obj.get_job("art director ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kirkkonummi")
	
@art_director.route('/art-director-jobs-seinajoki')
def art_director_jobs28(page=1):

    job_list = job_obj.get_job("art director ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="seinajoki")
	
@art_director.route('/art-director-jobs-kerava')
def art_director_jobs29(page=1):

    job_list = job_obj.get_job("art director ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kerava")
	
@art_director.route('/art-director-jobs-kouvola')
def art_director_jobs30(page=1):

    job_list = job_obj.get_job("art director ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kouvola")
	
@art_director.route('/art-director-jobs-imatra')
def art_director_jobs31(page=1):

    job_list = job_obj.get_job("art director ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="imatra")
	
@art_director.route('/art-director-jobs-nokia')
def art_director_jobs32_1(page=1):

    job_list = job_obj.get_job("art director ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="nokia")
	
@art_director.route('/art-director-jobs-savonlinna')
def art_director_jobs32(page=1):

    job_list = job_obj.get_job("art director ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="savonlinna")
	
@art_director.route('/art-director-jobs-riihimaki')
def art_director_jobs33(page=1):

    job_list = job_obj.get_job("art director ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="riihimaki")
	
@art_director.route('/art-director-jobs-vihti')
def art_director_jobs34(page=1):

    job_list = job_obj.get_job("art director ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="vihti")
	
@art_director.route('/art-director-jobs-salo')
def art_director_jobs35(page=1):

    job_list = job_obj.get_job("art director ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="salo")
	
@art_director.route('/art-director-jobs-kangasala')
def art_director_jobs36(page=1):

    job_list = job_obj.get_job("art director ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kangasala")
	
@art_director.route('/art-director-jobs-raisio')
def art_director_jobs37_1(page=1):

    job_list = job_obj.get_job("art director ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="raisio")
	
@art_director.route('/art-director-jobs-karhula')
def art_director_jobs37(page=1):

    job_list = job_obj.get_job("art director ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="karhula")
	
@art_director.route('/art-director-jobs-kemi')
def art_director_jobs38(page=1):

    job_list = job_obj.get_job("art director ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kemi")
	
@art_director.route('/art-director-jobs-iisalmi')
def art_director_jobs39(page=1):

    job_list = job_obj.get_job("art director ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="iisalmi")
	
@art_director.route('/art-director-jobs-varkaus')
def art_director_jobs40(page=1):

    job_list = job_obj.get_job("art director ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="varkaus")
	
@art_director.route('/art-director-jobs-raahe')
def art_director_jobs41(page=1):

    job_list = job_obj.get_job("art director ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="raahe")
	
@art_director.route('/art-director-jobs-ylojarvi')
def art_director_jobs42_1(page=1):

    job_list = job_obj.get_job("art director ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="ylojarvi")
	
@art_director.route('/art-director-jobs-hamina')
def art_director_jobs42(page=1):

    job_list = job_obj.get_job("art director ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="hamina")
	
@art_director.route('/art-director-jobs-kaarina')
def art_director_jobs43(page=1):

    job_list = job_obj.get_job("art director ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kaarina")
	
@art_director.route('/art-director-jobs-tornio')
def art_director_jobs44(page=1):

    job_list = job_obj.get_job("art director ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="tornio")
	
@art_director.route('/art-director-jobs-heinola')
def art_director_jobs45(page=1):

    job_list = job_obj.get_job("art director ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="heinola")
	
@art_director.route('/art-director-jobs-hollola')
def art_director_jobs46(page=1):

    job_list = job_obj.get_job("art director ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="hollola")
	
@art_director.route('/art-director-jobs-valkeakoski')
def art_director_jobs47(page=1):

    job_list = job_obj.get_job("art director ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="valkeakoski")
	
@art_director.route('/art-director-jobs-siilinjarvi')
def art_director_jobs48(page=1):

    job_list = job_obj.get_job("art director ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="siilinjarvi")
	
@art_director.route('/art-director-jobs-kuusankoski')
def art_director_jobs49(page=1):

    job_list = job_obj.get_job("art director ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kuusankoski")
	
@art_director.route('/art-director-jobs-sibbo')
def art_director_jobs50(page=1):

    job_list = job_obj.get_job("art director ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="sibbo")
	
@art_director.route('/art-director-jobs-jakostad')
def art_director_jobs51(page=1):

    job_list = job_obj.get_job("art director ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="jakostad")
	
@art_director.route('/art-director-jobs-lempaala')
def art_director_jobs52(page=1):

    job_list = job_obj.get_job("art director ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lempaala")
	
@art_director.route('/art-director-jobs-mantsala')
def art_director_jobs52_1(page=1):

    job_list = job_obj.get_job("art director ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="mantsala")
	
@art_director.route('/art-director-jobs-forssa')
def art_director_jobs53(page=1):

    job_list = job_obj.get_job("art director ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="forssa")
	
@art_director.route('/art-director-jobs-kuusamo')
def art_director_jobs54(page=1):

    job_list = job_obj.get_job("art director ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kuusamo")
	
@art_director.route('/art-director-jobs-haukipudas')
def art_director_jobs55(page=1):

    job_list = job_obj.get_job("art director ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="haukipudas")
	
@art_director.route('/art-director-jobs-korsholm')
def art_director_jobs56(page=1):

    job_list = job_obj.get_job("art director ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="korsholm")
	
@art_director.route('/art-director-jobs-laukaa')
def art_director_jobs57(page=1):

    job_list = job_obj.get_job("art director ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="laukaa")
	
@art_director.route('/art-director-jobs-anjala')
def art_director_jobs58(page=1):

    job_list = job_obj.get_job("art director ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="anjala")
	
@art_director.route('/art-director-jobs-uusikaupunki')
def art_director_jobs59(page=1):

    job_list = job_obj.get_job("art director ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="uusikaupunki")
	
@art_director.route('/art-director-jobs-janakkala')
def art_director_jobs60(page=1):

    job_list = job_obj.get_job("art director ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="janakkala")
	
@art_director.route('/art-director-jobs-pirkkala')
def art_director_jobs61(page=1):

    job_list = job_obj.get_job("art director ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="pirkkala")
	
@art_director.route('/art-director-jobs-lansi-turunmaa')
def art_director_jobs62(page=1):

    job_list = job_obj.get_job("art director ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lansi-turunmaa")
	
@art_director.route('/art-director-jobs-jamsa')
def art_director_jobs63(page=1):

    job_list = job_obj.get_job("art director ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="jamsa")
	
@art_director.route('/art-director-jobs-jamsa')
def art_director_jobs64(page=1):

    job_list = job_obj.get_job("art director ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="jamsa")
	
@art_director.route('/art-director-jobs-vammala')
def art_director_jobs65(page=1):

    job_list = job_obj.get_job("art director ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="vammala")
	
@art_director.route('/art-director-jobs-nastola')
def art_director_jobs66(page=1):

    job_list = job_obj.get_job("art director ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="nastola")
	
@art_director.route('/art-director-jobs-orimattila')
def art_director_jobs67(page=1):

    job_list = job_obj.get_job("art director ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="orimattila")
	
@art_director.route('/art-director-jobs-kauhajoki')
def art_director_jobs68(page=1):

    job_list = job_obj.get_job("art director ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kauhajoki")
	
@art_director.route('/art-director-jobs-ekenas')
def art_director_jobs69(page=1):

    job_list = job_obj.get_job("art director ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="ekenas")
	
@art_director.route('/art-director-jobs-kempele')
def art_director_jobs70(page=1):

    job_list = job_obj.get_job("art director ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kempele")
	
@art_director.route('/art-director-jobs-lapua')
def art_director_jobs71(page=1):

    job_list = job_obj.get_job("art director ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lapua")
	
@art_director.route('/art-director-jobs-lieksa')
def art_director_jobs72(page=1):

    job_list = job_obj.get_job("art director ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="lieksa")
	
@art_director.route('/art-director-jobs-naantali')
def art_director_jobs73(page=1):

    job_list = job_obj.get_job("art director ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="naantali")
	
@art_director.route('/art-director-jobs-aanekoski')
def art_director_jobs74(page=1):

    job_list = job_obj.get_job("art director ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="aanekoski")
	
@art_director.route('/art-director-jobs-ylivieska')
def art_director_jobs75(page=1):

    job_list = job_obj.get_job("art director ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="ylivieska")
	
@art_director.route('/art-director-jobs-kontiolahti')
def art_director_jobs76(page=1):

    job_list = job_obj.get_job("art director ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kontiolahti")
	
@art_director.route('/art-director-jobs-kankaanpaa')
def art_director_jobs77(page=1):

    job_list = job_obj.get_job("art director ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kankaanpaa")
	
@art_director.route('/art-director-jobs-ulvila')
def art_director_jobs78(page=1):

    job_list = job_obj.get_job("art director ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="ulvila")
	
@art_director.route('/art-director-jobs-pieksamaki')
def art_director_jobs79(page=1):

    job_list = job_obj.get_job("art director ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="pieksamaki")
	
@art_director.route('/art-director-jobs-kiiminki')
def art_director_jobs80(page=1):

    job_list = job_obj.get_job("art director ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kiiminki")
	
@art_director.route('/art-director-jobs-pargas')
def art_director_jobs81(page=1):

    job_list = job_obj.get_job("art director ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="pargas")
	
@art_director.route('/art-director-jobs-nurmo')
def art_director_jobs82(page=1):

    job_list = job_obj.get_job("art director ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="nurmo")
	
@art_director.route('/art-director-jobs-ilmajoki')
def art_director_jobs83(page=1):

    job_list = job_obj.get_job("art director ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="ilmajoki")
	
@art_director.route('/art-director-jobs-liperi')
def art_director_jobs84(page=1):

    job_list = job_obj.get_job("art director ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="liperi")
	
@art_director.route('/art-director-jobs-keuruu')
def art_director_jobs85(page=1):

    job_list = job_obj.get_job("art director ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="keuruu")
	
@art_director.route('/art-director-jobs-leppavirta')
def art_director_jobs86(page=1):

    job_list = job_obj.get_job("art director ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="leppavirta")
	
@art_director.route('/art-director-jobs-kurikka')
def art_director_jobs87(page=1):

    job_list = job_obj.get_job("art director ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kurikka")
	
@art_director.route('/art-director-jobs-nivala')
def art_director_jobs88(page=1):

    job_list = job_obj.get_job("art director ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="nivala")
	
@art_director.route('/art-director-jobs-joutseno')
def art_director_jobs89(page=1):

    job_list = job_obj.get_job("art director ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="joutseno")
	
@art_director.route('/art-director-jobs-pedersore')
def art_director_jobs90(page=1):

    job_list = job_obj.get_job("art director ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="pedersore")
	
@art_director.route('/art-director-jobs-sotkamo')
def art_director_jobs91(page=1):

    job_list = job_obj.get_job("art director ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="sotkamo")
	
@art_director.route('/art-director-jobs-kuhmo')
def art_director_jobs92(page=1):

    job_list = job_obj.get_job("art director ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="kuhmo")
	
@art_director.route('/art-director-jobs-paimio')
def art_director_jobs93(page=1):

    job_list = job_obj.get_job("art director ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="paimio")
	
@art_director.route('/art-director-jobs-saarijarvi')
def art_director_jobs94(page=1):

    job_list = job_obj.get_job("art director ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="saarijarvi")
	
@art_director.route('/art-director-jobs-helsinki')
def art_director_jobs95(page=1):

    job_list = job_obj.get_job("art director ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director ", location="helsinki")


####################################################################


##############################################
@art_director.route('/art-director-tyopaikat-espoo')
def art_director_tyopaikat2(page=1):

    job_list = job_obj.get_job("art director", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="espoo")

@art_director.route('/art-director-tyopaikat-tampere')
def art_director_tyopaikat3(page=1):

    job_list = job_obj.get_job("art director", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="tampere")
	
@art_director.route('/art-director-tyopaikat-vantaa')
def art_director_tyopaikat4(page=1):

    job_list = job_obj.get_job("art director", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="vantaa")
	
@art_director.route('/art-director-tyopaikat-turku')
def art_director_tyopaikat5(page=1):

    job_list = job_obj.get_job("art director", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="turku")
	
@art_director.route('/art-director-tyopaikat-oulu')
def art_director_tyopaikat6(page=1):

    job_list = job_obj.get_job("art director", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="oulu")
	
@art_director.route('/art-director-tyopaikat-lahti')
def art_director_tyopaikat7(page=1):

    job_list = job_obj.get_job("art director", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="lahti")
	
@art_director.route('/art-director-tyopaikat-kuopio')
def art_director_tyopaikat8(page=1):

    job_list = job_obj.get_job("art director", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kuopio")
	
@art_director.route('/art-director-tyopaikat-jyvvaskyla')
def art_director_tyopaikat9(page=1):

    job_list = job_obj.get_job("art director", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="jyvvaskyla")

@art_director.route('/art-director-tyopaikat-pori')
def art_director_tyopaikat10(page=1):

    job_list = job_obj.get_job("art director", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="pori")

@art_director.route('/art-director-tyopaikat-lappeenranta')
def art_director_tyopaikat11(page=1):

    job_list = job_obj.get_job("art director", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="lappeenranta")	
	
@art_director.route('/art-director-tyopaikat-vaasa')
def art_director_tyopaikat12(page=1):

    job_list = job_obj.get_job("art director", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="vaasa")
	
@art_director.route('/art-director-tyopaikat-kotka')
def art_director_tyopaikat13(page=1):

    job_list = job_obj.get_job("art director", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kotka")
	
@art_director.route('/art-director-tyopaikat-joensuu')
def art_director_tyopaikat14(page=1):

    job_list = job_obj.get_job("art director", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="joensuu")
	
@art_director.route('/art-director-tyopaikat-hameenlinna')
def art_director_tyopaikat15(page=1):

    job_list = job_obj.get_job("art director", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="hameenlinna")
	
@art_director.route('/art-director-tyopaikat-porvoo')
def art_director_tyopaikat16(page=1):

    job_list = job_obj.get_job("art director", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="porvoo")
	
@art_director.route('/art-director-tyopaikat-mikkeli')
def art_director_tyopaikat17(page=1):

    job_list = job_obj.get_job("art director", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="mikkeli")

@art_director.route('/art-director-tyopaikat-hyvinkaa')
def art_director_tyopaikat18(page=1):

    job_list = job_obj.get_job("art director", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="hyvinkaa")
	
@art_director.route('/art-director-tyopaikat-nurmijarvi')
def art_director_tyopaikat19(page=1):

    job_list = job_obj.get_job("art director", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="nurmijarvi")

@art_director.route('/art-director-tyopaikat-jarvenpaa')
def art_director_tyopaikat20(page=1):

    job_list = job_obj.get_job("art director", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="jarvenpaa")
	
@art_director.route('/art-director-tyopaikat-rauma')
def art_director_tyopaikat21(page=1):

    job_list = job_obj.get_job("art director", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="rauma")
	
@art_director.route('/art-director-tyopaikat-lohja')
def art_director_tyopaikat22(page=1):

    job_list = job_obj.get_job("art director", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="lohja")
	
@art_director.route('/art-director-tyopaikat-karleby')
def art_director_tyopaikat23(page=1):

    job_list = job_obj.get_job("art director", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="karleby")
	
@art_director.route('/art-director-tyopaikat-kajaani')
def art_director_tyopaikat24(page=1):

    job_list = job_obj.get_job("art director", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kajaani")
	
@art_director.route('/art-director-tyopaikat-rovaniemi')
def art_director_tyopaikat25(page=1):

    job_list = job_obj.get_job("art director", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="rovaniemi")
	
@art_director.route('/art-director-tyopaikat-tuusula')
def art_director_tyopaikat26(page=1):

    job_list = job_obj.get_job("art director", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="tuusula")
	
@art_director.route('/art-director-tyopaikat-kirkkonummi')
def art_director_tyopaikat27(page=1):

    job_list = job_obj.get_job("art director", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kirkkonummi")
	
@art_director.route('/art-director-tyopaikat-seinajoki')
def art_director_tyopaikat28(page=1):

    job_list = job_obj.get_job("art director", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="seinajoki")
	
@art_director.route('/art-director-tyopaikat-kerava')
def art_director_tyopaikat29(page=1):

    job_list = job_obj.get_job("art director", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kerava")
	
@art_director.route('/art-director-tyopaikat-kouvola')
def art_director_tyopaikat30(page=1):

    job_list = job_obj.get_job("art director", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kouvola")
	
@art_director.route('/art-director-tyopaikat-imatra')
def art_director_tyopaikat31(page=1):

    job_list = job_obj.get_job("art director", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="imatra")
	
@art_director.route('/art-director-tyopaikat-nokia')
def art_director_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("art director", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="nokia")
	
@art_director.route('/art-director-tyopaikat-savonlinna')
def art_director_tyopaikat32(page=1):

    job_list = job_obj.get_job("art director", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="savonlinna")
	
@art_director.route('/art-director-tyopaikat-riihimaki')
def art_director_tyopaikat33(page=1):

    job_list = job_obj.get_job("art director", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="riihimaki")
	
@art_director.route('/art-director-tyopaikat-vihti')
def art_director_tyopaikat34(page=1):

    job_list = job_obj.get_job("art director", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="vihti")
	
@art_director.route('/art-director-tyopaikat-salo')
def art_director_tyopaikat35(page=1):

    job_list = job_obj.get_job("art director", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="salo")
	
@art_director.route('/art-director-tyopaikat-kangasala')
def art_director_tyopaikat36(page=1):

    job_list = job_obj.get_job("art director", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kangasala")
	
@art_director.route('/art-director-tyopaikat-raisio')
def art_director_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("art director", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="raisio")
	
@art_director.route('/art-director-tyopaikat-karhula')
def art_director_tyopaikat37(page=1):

    job_list = job_obj.get_job("art director", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="karhula")
	
@art_director.route('/art-director-tyopaikat-kemi')
def art_director_tyopaikat38(page=1):

    job_list = job_obj.get_job("art director", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kemi")
	
@art_director.route('/art-director-tyopaikat-iisalmi')
def art_director_tyopaikat39(page=1):

    job_list = job_obj.get_job("art director", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="iisalmi")
	
@art_director.route('/art-director-tyopaikat-varkaus')
def art_director_tyopaikat40(page=1):

    job_list = job_obj.get_job("art director", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="varkaus")
	
@art_director.route('/art-director-tyopaikat-raahe')
def art_director_tyopaikat41(page=1):

    job_list = job_obj.get_job("art director", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="raahe")
	
@art_director.route('/art-director-tyopaikat-ylojarvi')
def art_director_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("art director", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="ylojarvi")
	
@art_director.route('/art-director-tyopaikat-hamina')
def art_director_tyopaikat42(page=1):

    job_list = job_obj.get_job("art director", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="hamina")
	
@art_director.route('/art-director-tyopaikat-kaarina')
def art_director_tyopaikat43(page=1):

    job_list = job_obj.get_job("art director", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kaarina")
	
@art_director.route('/art-director-tyopaikat-tornio')
def art_director_tyopaikat44(page=1):

    job_list = job_obj.get_job("art director", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="tornio")
	
@art_director.route('/art-director-tyopaikat-heinola')
def art_director_tyopaikat45(page=1):

    job_list = job_obj.get_job("art director", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="heinola")
	
@art_director.route('/art-director-tyopaikat-hollola')
def art_director_tyopaikat46(page=1):

    job_list = job_obj.get_job("art director", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="hollola")
	
@art_director.route('/art-director-tyopaikat-valkeakoski')
def art_director_tyopaikat47(page=1):

    job_list = job_obj.get_job("art director", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="valkeakoski")
	
@art_director.route('/art-director-tyopaikat-siilinjarvi')
def art_director_tyopaikat48(page=1):

    job_list = job_obj.get_job("art director", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="siilinjarvi")
	
@art_director.route('/art-director-tyopaikat-kuusankoski')
def art_director_tyopaikat49(page=1):

    job_list = job_obj.get_job("art director", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kuusankoski")
	
@art_director.route('/art-director-tyopaikat-sibbo')
def art_director_tyopaikat50(page=1):

    job_list = job_obj.get_job("art director", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="sibbo")
	
@art_director.route('/art-director-tyopaikat-jakostad')
def art_director_tyopaikat51(page=1):

    job_list = job_obj.get_job("art director", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="jakostad")
	
@art_director.route('/art-director-tyopaikat-lempaala')
def art_director_tyopaikat52(page=1):

    job_list = job_obj.get_job("art director", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="lempaala")
	
@art_director.route('/art-director-tyopaikat-mantsala')
def art_director_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("art director", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="mantsala")
	
@art_director.route('/art-director-tyopaikat-forssa')
def art_director_tyopaikat53(page=1):

    job_list = job_obj.get_job("art director", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="forssa")
	
@art_director.route('/art-director-tyopaikat-kuusamo')
def art_director_tyopaikat54(page=1):

    job_list = job_obj.get_job("art director", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kuusamo")
	
@art_director.route('/art-director-tyopaikat-haukipudas')
def art_director_tyopaikat55(page=1):

    job_list = job_obj.get_job("art director", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="haukipudas")
	
@art_director.route('/art-director-tyopaikat-korsholm')
def art_director_tyopaikat56(page=1):

    job_list = job_obj.get_job("art director", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="korsholm")
	
@art_director.route('/art-director-tyopaikat-laukaa')
def art_director_tyopaikat57(page=1):

    job_list = job_obj.get_job("art director", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="laukaa")
	
@art_director.route('/art-director-tyopaikat-anjala')
def art_director_tyopaikat58(page=1):

    job_list = job_obj.get_job("art director", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="anjala")
	
@art_director.route('/art-director-tyopaikat-uusikaupunki')
def art_director_tyopaikat59(page=1):

    job_list = job_obj.get_job("art director", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="uusikaupunki")
	
@art_director.route('/art-director-tyopaikat-janakkala')
def art_director_tyopaikat60(page=1):

    job_list = job_obj.get_job("art director", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="janakkala")
	
@art_director.route('/art-director-tyopaikat-pirkkala')
def art_director_tyopaikat61(page=1):

    job_list = job_obj.get_job("art director", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="pirkkala")
	
@art_director.route('/art-director-tyopaikat-lansi-turunmaa')
def art_director_tyopaikat62(page=1):

    job_list = job_obj.get_job("art director", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="lansi-turunmaa")
	
@art_director.route('/art-director-tyopaikat-jamsa')
def art_director_tyopaikat63(page=1):

    job_list = job_obj.get_job("art director", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="jamsa")
	
@art_director.route('/art-director-tyopaikat-jamsa')
def art_director_tyopaikat64(page=1):

    job_list = job_obj.get_job("art director", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="jamsa")
	
@art_director.route('/art-director-tyopaikat-vammala')
def art_director_tyopaikat65(page=1):

    job_list = job_obj.get_job("art director", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="vammala")
	
@art_director.route('/art-director-tyopaikat-nastola')
def art_director_tyopaikat66(page=1):

    job_list = job_obj.get_job("art director", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="nastola")
	
@art_director.route('/art-director-tyopaikat-orimattila')
def art_director_tyopaikat67(page=1):

    job_list = job_obj.get_job("art director", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="orimattila")
	
@art_director.route('/art-director-tyopaikat-kauhajoki')
def art_director_tyopaikat68(page=1):

    job_list = job_obj.get_job("art director", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kauhajoki")
	
@art_director.route('/art-director-tyopaikat-ekenas')
def art_director_tyopaikat69(page=1):

    job_list = job_obj.get_job("art director", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="ekenas")
	
@art_director.route('/art-director-tyopaikat-kempele')
def art_director_tyopaikat70(page=1):

    job_list = job_obj.get_job("art director", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kempele")
	
@art_director.route('/art-director-tyopaikat-lapua')
def art_director_tyopaikat71(page=1):

    job_list = job_obj.get_job("art director", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="lapua")
	
@art_director.route('/art-director-tyopaikat-lieksa')
def art_director_tyopaikat72(page=1):

    job_list = job_obj.get_job("art director", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="lieksa")
	
@art_director.route('/art-director-tyopaikat-naantali')
def art_director_tyopaikat73(page=1):

    job_list = job_obj.get_job("art director", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="naantali")
	
@art_director.route('/art-director-tyopaikat-aanekoski')
def art_director_tyopaikat74(page=1):

    job_list = job_obj.get_job("art director", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="aanekoski")
	
@art_director.route('/art-director-tyopaikat-ylivieska')
def art_director_tyopaikat75(page=1):

    job_list = job_obj.get_job("art director", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="ylivieska")
	
@art_director.route('/art-director-tyopaikat-kontiolahti')
def art_director_tyopaikat76(page=1):

    job_list = job_obj.get_job("art director", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kontiolahti")
	
@art_director.route('/art-director-tyopaikat-kankaanpaa')
def art_director_tyopaikat77(page=1):

    job_list = job_obj.get_job("art director", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kankaanpaa")
	
@art_director.route('/art-director-tyopaikat-ulvila')
def art_director_tyopaikat78(page=1):

    job_list = job_obj.get_job("art director", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="ulvila")
	
@art_director.route('/art-director-tyopaikat-pieksamaki')
def art_director_tyopaikat79(page=1):

    job_list = job_obj.get_job("art director", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="pieksamaki")
	
@art_director.route('/art-director-tyopaikat-kiiminki')
def art_director_tyopaikat80(page=1):

    job_list = job_obj.get_job("art director", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kiiminki")
	
@art_director.route('/art-director-tyopaikat-pargas')
def art_director_tyopaikat81(page=1):

    job_list = job_obj.get_job("art director", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="pargas")
	
@art_director.route('/art-director-tyopaikat-nurmo')
def art_director_tyopaikat82(page=1):

    job_list = job_obj.get_job("art director", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="nurmo")
	
@art_director.route('/art-director-tyopaikat-ilmajoki')
def art_director_tyopaikat83(page=1):

    job_list = job_obj.get_job("art director", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="ilmajoki")
	
@art_director.route('/art-director-tyopaikat-liperi')
def art_director_tyopaikat84(page=1):

    job_list = job_obj.get_job("art director", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="liperi")
	
@art_director.route('/art-director-tyopaikat-keuruu')
def art_director_tyopaikat85(page=1):

    job_list = job_obj.get_job("art director", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="keuruu")
	
@art_director.route('/art-director-tyopaikat-leppavirta')
def art_director_tyopaikat86(page=1):

    job_list = job_obj.get_job("art director", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="leppavirta")
	
@art_director.route('/art-director-tyopaikat-kurikka')
def art_director_tyopaikat87(page=1):

    job_list = job_obj.get_job("art director", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kurikka")
	
@art_director.route('/art-director-tyopaikat-nivala')
def art_director_tyopaikat88(page=1):

    job_list = job_obj.get_job("art director", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="nivala")
	
@art_director.route('/art-director-tyopaikat-joutseno')
def art_director_tyopaikat89(page=1):

    job_list = job_obj.get_job("art director", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="joutseno")
	
@art_director.route('/art-director-tyopaikat-pedersore')
def art_director_tyopaikat90(page=1):

    job_list = job_obj.get_job("art director", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="pedersore")
	
@art_director.route('/art-director-tyopaikat-sotkamo')
def art_director_tyopaikat91(page=1):

    job_list = job_obj.get_job("art director", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="sotkamo")
	
@art_director.route('/art-director-tyopaikat-kuhmo')
def art_director_tyopaikat92(page=1):

    job_list = job_obj.get_job("art director", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="kuhmo")
	
@art_director.route('/art-director-tyopaikat-paimio')
def art_director_tyopaikat93(page=1):

    job_list = job_obj.get_job("art director", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="paimio")
	
@art_director.route('/art-director-tyopaikat-saarijarvi')
def art_director_tyopaikat94(page=1):

    job_list = job_obj.get_job("art director", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director", location="saarijarvi")
	
@art_director.route('/art-director-tyopaikat-helsinki')
def art_director_tyopaikat95(page=1):

    job_list = job_obj.get_job("art director", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="art director  ", location="helsinki")
	  

