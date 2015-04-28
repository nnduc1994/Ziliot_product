from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

creative_director = Blueprint('creative_director', __name__)
job_obj = Job()



####################################################################


@creative_director.route('/creative-director_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "creative-director" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@creative_director.route('/creative-director-avoimet-tyopaikat-espoo')
def creative_director_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("creative director ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="espoo")

@creative_director.route('/creative-director-avoimet-tyopaikat-tampere')
def creative_director_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("creative director ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="tampere")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-vantaa')
def creative_director_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("creative director ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="vantaa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-turku')
def creative_director_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("creative director ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="turku")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-oulu')
def creative_director_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("creative director ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="oulu")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-lahti')
def creative_director_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("creative director ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lahti")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kuopio')
def creative_director_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("creative director ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kuopio")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-jyvvaskyla')
def creative_director_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("creative director ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="jyvvaskyla")

@creative_director.route('/creative-director-avoimet-tyopaikat-pori')
def creative_director_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("creative director ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="pori")

@creative_director.route('/creative-director-avoimet-tyopaikat-lappeenranta')
def creative_director_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("creative director ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lappeenranta")	
	
@creative_director.route('/creative-director-avoimet-tyopaikat-vaasa')
def creative_director_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("creative director ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="vaasa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kotka')
def creative_director_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("creative director ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kotka")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-joensuu')
def creative_director_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("creative director ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="joensuu")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-hameenlinna')
def creative_director_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("creative director ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="hameenlinna")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-porvoo')
def creative_director_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("creative director ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="porvoo")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-mikkeli')
def creative_director_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("creative director ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="mikkeli")

@creative_director.route('/creative-director-avoimet-tyopaikat-hyvinkaa')
def creative_director_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("creative director ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="hyvinkaa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-nurmijarvi')
def creative_director_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("creative director ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="nurmijarvi")

@creative_director.route('/creative-director-avoimet-tyopaikat-jarvenpaa')
def creative_director_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("creative director ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="jarvenpaa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-rauma')
def creative_director_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("creative director ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="rauma")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-lohja')
def creative_director_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("creative director ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lohja")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-karleby')
def creative_director_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("creative director ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="karleby")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kajaani')
def creative_director_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("creative director ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kajaani")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-rovaniemi')
def creative_director_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("creative director ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="rovaniemi")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-tuusula')
def creative_director_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("creative director ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="tuusula")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kirkkonummi')
def creative_director_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("creative director ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kirkkonummi")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-seinajoki')
def creative_director_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("creative director ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="seinajoki")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kerava')
def creative_director_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("creative director ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kerava")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kouvola')
def creative_director_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("creative director ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kouvola")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-imatra')
def creative_director_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("creative director ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="imatra")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-nokia')
def creative_director_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("creative director ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="nokia")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-savonlinna')
def creative_director_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("creative director ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="savonlinna")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-riihimaki')
def creative_director_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("creative director ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="riihimaki")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-vihti')
def creative_director_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("creative director ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="vihti")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-salo')
def creative_director_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("creative director ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="salo")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kangasala')
def creative_director_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("creative director ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kangasala")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-raisio')
def creative_director_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("creative director ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="raisio")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-karhula')
def creative_director_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("creative director ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="karhula")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kemi')
def creative_director_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("creative director ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kemi")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-iisalmi')
def creative_director_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("creative director ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="iisalmi")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-varkaus')
def creative_director_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("creative director ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="varkaus")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-raahe')
def creative_director_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("creative director ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="raahe")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-ylojarvi')
def creative_director_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("creative director ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="ylojarvi")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-hamina')
def creative_director_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("creative director ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="hamina")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kaarina')
def creative_director_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("creative director ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kaarina")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-tornio')
def creative_director_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("creative director ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="tornio")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-heinola')
def creative_director_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("creative director ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="heinola")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-hollola')
def creative_director_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("creative director ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="hollola")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-valkeakoski')
def creative_director_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("creative director ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="valkeakoski")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-siilinjarvi')
def creative_director_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("creative director ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="siilinjarvi")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kuusankoski')
def creative_director_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("creative director ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kuusankoski")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-sibbo')
def creative_director_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("creative director ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="sibbo")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-jakostad')
def creative_director_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("creative director ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="jakostad")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-lempaala')
def creative_director_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("creative director ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lempaala")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-mantsala')
def creative_director_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("creative director ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="mantsala")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-forssa')
def creative_director_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("creative director ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="forssa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kuusamo')
def creative_director_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("creative director ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kuusamo")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-haukipudas')
def creative_director_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("creative director ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="haukipudas")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-korsholm')
def creative_director_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("creative director ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="korsholm")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-laukaa')
def creative_director_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("creative director ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="laukaa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-anjala')
def creative_director_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("creative director ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="anjala")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-uusikaupunki')
def creative_director_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("creative director ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="uusikaupunki")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-janakkala')
def creative_director_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("creative director ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="janakkala")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-pirkkala')
def creative_director_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("creative director ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="pirkkala")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-lansi-turunmaa')
def creative_director_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("creative director ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lansi-turunmaa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-jamsa')
def creative_director_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("creative director ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="jamsa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-jamsa')
def creative_director_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("creative director ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="jamsa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-vammala')
def creative_director_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("creative director ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="vammala")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-nastola')
def creative_director_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("creative director ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="nastola")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-orimattila')
def creative_director_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("creative director ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="orimattila")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kauhajoki')
def creative_director_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("creative director ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kauhajoki")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-ekenas')
def creative_director_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("creative director ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="ekenas")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kempele')
def creative_director_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("creative director ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kempele")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-lapua')
def creative_director_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("creative director ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lapua")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-lieksa')
def creative_director_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("creative director ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lieksa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-naantali')
def creative_director_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("creative director ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="naantali")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-aanekoski')
def creative_director_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("creative director ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="aanekoski")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-ylivieska')
def creative_director_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("creative director ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="ylivieska")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kontiolahti')
def creative_director_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("creative director ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kontiolahti")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kankaanpaa')
def creative_director_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("creative director ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kankaanpaa")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-ulvila')
def creative_director_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("creative director ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="ulvila")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-pieksamaki')
def creative_director_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("creative director ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="pieksamaki")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kiiminki')
def creative_director_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("creative director ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kiiminki")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-pargas')
def creative_director_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("creative director ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="pargas")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-nurmo')
def creative_director_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("creative director ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="nurmo")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-ilmajoki')
def creative_director_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("creative director ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="ilmajoki")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-liperi')
def creative_director_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("creative director ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="liperi")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-keuruu')
def creative_director_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("creative director ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="keuruu")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-leppavirta')
def creative_director_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("creative director ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="leppavirta")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kurikka')
def creative_director_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("creative director ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kurikka")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-nivala')
def creative_director_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("creative director ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="nivala")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-joutseno')
def creative_director_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("creative director ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="joutseno")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-pedersore')
def creative_director_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("creative director ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="pedersore")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-sotkamo')
def creative_director_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("creative director ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="sotkamo")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-kuhmo')
def creative_director_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("creative director ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kuhmo")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-paimio')
def creative_director_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("creative director ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="paimio")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-saarijarvi')
def creative_director_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("creative director ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="saarijarvi")
	
@creative_director.route('/creative-director-avoimet-tyopaikat-helsinki')
def creative_director_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("creative director ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="helsinki")


####################################################################


##############################################
@creative_director.route('/creative-director-jobs-espoo')
def creative_director_jobs2(page=1):

    job_list = job_obj.get_job("creative director ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="espoo")

@creative_director.route('/creative-director-jobs-tampere')
def creative_director_jobs3(page=1):

    job_list = job_obj.get_job("creative director ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="tampere")
	
@creative_director.route('/creative-director-jobs-vantaa')
def creative_director_jobs4(page=1):

    job_list = job_obj.get_job("creative director ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="vantaa")
	
@creative_director.route('/creative-director-jobs-turku')
def creative_director_jobs5(page=1):

    job_list = job_obj.get_job("creative director ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="turku")
	
@creative_director.route('/creative-director-jobs-oulu')
def creative_director_jobs6(page=1):

    job_list = job_obj.get_job("creative director ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="oulu")
	
@creative_director.route('/creative-director-jobs-lahti')
def creative_director_jobs7(page=1):

    job_list = job_obj.get_job("creative director ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lahti")
	
@creative_director.route('/creative-director-jobs-kuopio')
def creative_director_jobs8(page=1):

    job_list = job_obj.get_job("creative director ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kuopio")
	
@creative_director.route('/creative-director-jobs-jyvvaskyla')
def creative_director_jobs9(page=1):

    job_list = job_obj.get_job("creative director ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="jyvvaskyla")

@creative_director.route('/creative-director-jobs-pori')
def creative_director_jobs10(page=1):

    job_list = job_obj.get_job("creative director ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="pori")

@creative_director.route('/creative-director-jobs-lappeenranta')
def creative_director_jobs11(page=1):

    job_list = job_obj.get_job("creative director ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lappeenranta")	
	
@creative_director.route('/creative-director-jobs-vaasa')
def creative_director_jobs12(page=1):

    job_list = job_obj.get_job("creative director ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="vaasa")
	
@creative_director.route('/creative-director-jobs-kotka')
def creative_director_jobs13(page=1):

    job_list = job_obj.get_job("creative director ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kotka")
	
@creative_director.route('/creative-director-jobs-joensuu')
def creative_director_jobs14(page=1):

    job_list = job_obj.get_job("creative director ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="joensuu")
	
@creative_director.route('/creative-director-jobs-hameenlinna')
def creative_director_jobs15(page=1):

    job_list = job_obj.get_job("creative director ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="hameenlinna")
	
@creative_director.route('/creative-director-jobs-porvoo')
def creative_director_jobs16(page=1):

    job_list = job_obj.get_job("creative director ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="porvoo")
	
@creative_director.route('/creative-director-jobs-mikkeli')
def creative_director_jobs17(page=1):

    job_list = job_obj.get_job("creative director ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="mikkeli")

@creative_director.route('/creative-director-jobs-hyvinkaa')
def creative_director_jobs18(page=1):

    job_list = job_obj.get_job("creative director ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="hyvinkaa")
	
@creative_director.route('/creative-director-jobs-nurmijarvi')
def creative_director_jobs19(page=1):

    job_list = job_obj.get_job("creative director ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="nurmijarvi")

@creative_director.route('/creative-director-jobs-jarvenpaa')
def creative_director_jobs20(page=1):

    job_list = job_obj.get_job("creative director ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="jarvenpaa")
	
@creative_director.route('/creative-director-jobs-rauma')
def creative_director_jobs21(page=1):

    job_list = job_obj.get_job("creative director ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="rauma")
	
@creative_director.route('/creative-director-jobs-lohja')
def creative_director_jobs22(page=1):

    job_list = job_obj.get_job("creative director ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lohja")
	
@creative_director.route('/creative-director-jobs-karleby')
def creative_director_jobs23(page=1):

    job_list = job_obj.get_job("creative director ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="karleby")
	
@creative_director.route('/creative-director-jobs-kajaani')
def creative_director_jobs24(page=1):

    job_list = job_obj.get_job("creative director ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kajaani")
	
@creative_director.route('/creative-director-jobs-rovaniemi')
def creative_director_jobs25(page=1):

    job_list = job_obj.get_job("creative director ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="rovaniemi")
	
@creative_director.route('/creative-director-jobs-tuusula')
def creative_director_jobs26(page=1):

    job_list = job_obj.get_job("creative director ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="tuusula")
	
@creative_director.route('/creative-director-jobs-kirkkonummi')
def creative_director_jobs27(page=1):

    job_list = job_obj.get_job("creative director ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kirkkonummi")
	
@creative_director.route('/creative-director-jobs-seinajoki')
def creative_director_jobs28(page=1):

    job_list = job_obj.get_job("creative director ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="seinajoki")
	
@creative_director.route('/creative-director-jobs-kerava')
def creative_director_jobs29(page=1):

    job_list = job_obj.get_job("creative director ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kerava")
	
@creative_director.route('/creative-director-jobs-kouvola')
def creative_director_jobs30(page=1):

    job_list = job_obj.get_job("creative director ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kouvola")
	
@creative_director.route('/creative-director-jobs-imatra')
def creative_director_jobs31(page=1):

    job_list = job_obj.get_job("creative director ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="imatra")
	
@creative_director.route('/creative-director-jobs-nokia')
def creative_director_jobs32_1(page=1):

    job_list = job_obj.get_job("creative director ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="nokia")
	
@creative_director.route('/creative-director-jobs-savonlinna')
def creative_director_jobs32(page=1):

    job_list = job_obj.get_job("creative director ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="savonlinna")
	
@creative_director.route('/creative-director-jobs-riihimaki')
def creative_director_jobs33(page=1):

    job_list = job_obj.get_job("creative director ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="riihimaki")
	
@creative_director.route('/creative-director-jobs-vihti')
def creative_director_jobs34(page=1):

    job_list = job_obj.get_job("creative director ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="vihti")
	
@creative_director.route('/creative-director-jobs-salo')
def creative_director_jobs35(page=1):

    job_list = job_obj.get_job("creative director ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="salo")
	
@creative_director.route('/creative-director-jobs-kangasala')
def creative_director_jobs36(page=1):

    job_list = job_obj.get_job("creative director ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kangasala")
	
@creative_director.route('/creative-director-jobs-raisio')
def creative_director_jobs37_1(page=1):

    job_list = job_obj.get_job("creative director ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="raisio")
	
@creative_director.route('/creative-director-jobs-karhula')
def creative_director_jobs37(page=1):

    job_list = job_obj.get_job("creative director ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="karhula")
	
@creative_director.route('/creative-director-jobs-kemi')
def creative_director_jobs38(page=1):

    job_list = job_obj.get_job("creative director ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kemi")
	
@creative_director.route('/creative-director-jobs-iisalmi')
def creative_director_jobs39(page=1):

    job_list = job_obj.get_job("creative director ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="iisalmi")
	
@creative_director.route('/creative-director-jobs-varkaus')
def creative_director_jobs40(page=1):

    job_list = job_obj.get_job("creative director ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="varkaus")
	
@creative_director.route('/creative-director-jobs-raahe')
def creative_director_jobs41(page=1):

    job_list = job_obj.get_job("creative director ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="raahe")
	
@creative_director.route('/creative-director-jobs-ylojarvi')
def creative_director_jobs42_1(page=1):

    job_list = job_obj.get_job("creative director ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="ylojarvi")
	
@creative_director.route('/creative-director-jobs-hamina')
def creative_director_jobs42(page=1):

    job_list = job_obj.get_job("creative director ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="hamina")
	
@creative_director.route('/creative-director-jobs-kaarina')
def creative_director_jobs43(page=1):

    job_list = job_obj.get_job("creative director ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kaarina")
	
@creative_director.route('/creative-director-jobs-tornio')
def creative_director_jobs44(page=1):

    job_list = job_obj.get_job("creative director ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="tornio")
	
@creative_director.route('/creative-director-jobs-heinola')
def creative_director_jobs45(page=1):

    job_list = job_obj.get_job("creative director ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="heinola")
	
@creative_director.route('/creative-director-jobs-hollola')
def creative_director_jobs46(page=1):

    job_list = job_obj.get_job("creative director ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="hollola")
	
@creative_director.route('/creative-director-jobs-valkeakoski')
def creative_director_jobs47(page=1):

    job_list = job_obj.get_job("creative director ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="valkeakoski")
	
@creative_director.route('/creative-director-jobs-siilinjarvi')
def creative_director_jobs48(page=1):

    job_list = job_obj.get_job("creative director ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="siilinjarvi")
	
@creative_director.route('/creative-director-jobs-kuusankoski')
def creative_director_jobs49(page=1):

    job_list = job_obj.get_job("creative director ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kuusankoski")
	
@creative_director.route('/creative-director-jobs-sibbo')
def creative_director_jobs50(page=1):

    job_list = job_obj.get_job("creative director ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="sibbo")
	
@creative_director.route('/creative-director-jobs-jakostad')
def creative_director_jobs51(page=1):

    job_list = job_obj.get_job("creative director ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="jakostad")
	
@creative_director.route('/creative-director-jobs-lempaala')
def creative_director_jobs52(page=1):

    job_list = job_obj.get_job("creative director ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lempaala")
	
@creative_director.route('/creative-director-jobs-mantsala')
def creative_director_jobs52_1(page=1):

    job_list = job_obj.get_job("creative director ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="mantsala")
	
@creative_director.route('/creative-director-jobs-forssa')
def creative_director_jobs53(page=1):

    job_list = job_obj.get_job("creative director ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="forssa")
	
@creative_director.route('/creative-director-jobs-kuusamo')
def creative_director_jobs54(page=1):

    job_list = job_obj.get_job("creative director ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kuusamo")
	
@creative_director.route('/creative-director-jobs-haukipudas')
def creative_director_jobs55(page=1):

    job_list = job_obj.get_job("creative director ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="haukipudas")
	
@creative_director.route('/creative-director-jobs-korsholm')
def creative_director_jobs56(page=1):

    job_list = job_obj.get_job("creative director ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="korsholm")
	
@creative_director.route('/creative-director-jobs-laukaa')
def creative_director_jobs57(page=1):

    job_list = job_obj.get_job("creative director ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="laukaa")
	
@creative_director.route('/creative-director-jobs-anjala')
def creative_director_jobs58(page=1):

    job_list = job_obj.get_job("creative director ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="anjala")
	
@creative_director.route('/creative-director-jobs-uusikaupunki')
def creative_director_jobs59(page=1):

    job_list = job_obj.get_job("creative director ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="uusikaupunki")
	
@creative_director.route('/creative-director-jobs-janakkala')
def creative_director_jobs60(page=1):

    job_list = job_obj.get_job("creative director ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="janakkala")
	
@creative_director.route('/creative-director-jobs-pirkkala')
def creative_director_jobs61(page=1):

    job_list = job_obj.get_job("creative director ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="pirkkala")
	
@creative_director.route('/creative-director-jobs-lansi-turunmaa')
def creative_director_jobs62(page=1):

    job_list = job_obj.get_job("creative director ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lansi-turunmaa")
	
@creative_director.route('/creative-director-jobs-jamsa')
def creative_director_jobs63(page=1):

    job_list = job_obj.get_job("creative director ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="jamsa")
	
@creative_director.route('/creative-director-jobs-jamsa')
def creative_director_jobs64(page=1):

    job_list = job_obj.get_job("creative director ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="jamsa")
	
@creative_director.route('/creative-director-jobs-vammala')
def creative_director_jobs65(page=1):

    job_list = job_obj.get_job("creative director ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="vammala")
	
@creative_director.route('/creative-director-jobs-nastola')
def creative_director_jobs66(page=1):

    job_list = job_obj.get_job("creative director ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="nastola")
	
@creative_director.route('/creative-director-jobs-orimattila')
def creative_director_jobs67(page=1):

    job_list = job_obj.get_job("creative director ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="orimattila")
	
@creative_director.route('/creative-director-jobs-kauhajoki')
def creative_director_jobs68(page=1):

    job_list = job_obj.get_job("creative director ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kauhajoki")
	
@creative_director.route('/creative-director-jobs-ekenas')
def creative_director_jobs69(page=1):

    job_list = job_obj.get_job("creative director ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="ekenas")
	
@creative_director.route('/creative-director-jobs-kempele')
def creative_director_jobs70(page=1):

    job_list = job_obj.get_job("creative director ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kempele")
	
@creative_director.route('/creative-director-jobs-lapua')
def creative_director_jobs71(page=1):

    job_list = job_obj.get_job("creative director ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lapua")
	
@creative_director.route('/creative-director-jobs-lieksa')
def creative_director_jobs72(page=1):

    job_list = job_obj.get_job("creative director ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="lieksa")
	
@creative_director.route('/creative-director-jobs-naantali')
def creative_director_jobs73(page=1):

    job_list = job_obj.get_job("creative director ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="naantali")
	
@creative_director.route('/creative-director-jobs-aanekoski')
def creative_director_jobs74(page=1):

    job_list = job_obj.get_job("creative director ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="aanekoski")
	
@creative_director.route('/creative-director-jobs-ylivieska')
def creative_director_jobs75(page=1):

    job_list = job_obj.get_job("creative director ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="ylivieska")
	
@creative_director.route('/creative-director-jobs-kontiolahti')
def creative_director_jobs76(page=1):

    job_list = job_obj.get_job("creative director ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kontiolahti")
	
@creative_director.route('/creative-director-jobs-kankaanpaa')
def creative_director_jobs77(page=1):

    job_list = job_obj.get_job("creative director ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kankaanpaa")
	
@creative_director.route('/creative-director-jobs-ulvila')
def creative_director_jobs78(page=1):

    job_list = job_obj.get_job("creative director ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="ulvila")
	
@creative_director.route('/creative-director-jobs-pieksamaki')
def creative_director_jobs79(page=1):

    job_list = job_obj.get_job("creative director ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="pieksamaki")
	
@creative_director.route('/creative-director-jobs-kiiminki')
def creative_director_jobs80(page=1):

    job_list = job_obj.get_job("creative director ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kiiminki")
	
@creative_director.route('/creative-director-jobs-pargas')
def creative_director_jobs81(page=1):

    job_list = job_obj.get_job("creative director ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="pargas")
	
@creative_director.route('/creative-director-jobs-nurmo')
def creative_director_jobs82(page=1):

    job_list = job_obj.get_job("creative director ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="nurmo")
	
@creative_director.route('/creative-director-jobs-ilmajoki')
def creative_director_jobs83(page=1):

    job_list = job_obj.get_job("creative director ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="ilmajoki")
	
@creative_director.route('/creative-director-jobs-liperi')
def creative_director_jobs84(page=1):

    job_list = job_obj.get_job("creative director ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="liperi")
	
@creative_director.route('/creative-director-jobs-keuruu')
def creative_director_jobs85(page=1):

    job_list = job_obj.get_job("creative director ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="keuruu")
	
@creative_director.route('/creative-director-jobs-leppavirta')
def creative_director_jobs86(page=1):

    job_list = job_obj.get_job("creative director ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="leppavirta")
	
@creative_director.route('/creative-director-jobs-kurikka')
def creative_director_jobs87(page=1):

    job_list = job_obj.get_job("creative director ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kurikka")
	
@creative_director.route('/creative-director-jobs-nivala')
def creative_director_jobs88(page=1):

    job_list = job_obj.get_job("creative director ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="nivala")
	
@creative_director.route('/creative-director-jobs-joutseno')
def creative_director_jobs89(page=1):

    job_list = job_obj.get_job("creative director ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="joutseno")
	
@creative_director.route('/creative-director-jobs-pedersore')
def creative_director_jobs90(page=1):

    job_list = job_obj.get_job("creative director ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="pedersore")
	
@creative_director.route('/creative-director-jobs-sotkamo')
def creative_director_jobs91(page=1):

    job_list = job_obj.get_job("creative director ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="sotkamo")
	
@creative_director.route('/creative-director-jobs-kuhmo')
def creative_director_jobs92(page=1):

    job_list = job_obj.get_job("creative director ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="kuhmo")
	
@creative_director.route('/creative-director-jobs-paimio')
def creative_director_jobs93(page=1):

    job_list = job_obj.get_job("creative director ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="paimio")
	
@creative_director.route('/creative-director-jobs-saarijarvi')
def creative_director_jobs94(page=1):

    job_list = job_obj.get_job("creative director ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="saarijarvi")
	
@creative_director.route('/creative-director-jobs-helsinki')
def creative_director_jobs95(page=1):

    job_list = job_obj.get_job("creative director ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director ", location="helsinki")


####################################################################


##############################################
@creative_director.route('/creative-director-tyopaikat-espoo')
def creative_director_tyopaikat2(page=1):

    job_list = job_obj.get_job("creative director", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="espoo")

@creative_director.route('/creative-director-tyopaikat-tampere')
def creative_director_tyopaikat3(page=1):

    job_list = job_obj.get_job("creative director", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="tampere")
	
@creative_director.route('/creative-director-tyopaikat-vantaa')
def creative_director_tyopaikat4(page=1):

    job_list = job_obj.get_job("creative director", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="vantaa")
	
@creative_director.route('/creative-director-tyopaikat-turku')
def creative_director_tyopaikat5(page=1):

    job_list = job_obj.get_job("creative director", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="turku")
	
@creative_director.route('/creative-director-tyopaikat-oulu')
def creative_director_tyopaikat6(page=1):

    job_list = job_obj.get_job("creative director", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="oulu")
	
@creative_director.route('/creative-director-tyopaikat-lahti')
def creative_director_tyopaikat7(page=1):

    job_list = job_obj.get_job("creative director", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="lahti")
	
@creative_director.route('/creative-director-tyopaikat-kuopio')
def creative_director_tyopaikat8(page=1):

    job_list = job_obj.get_job("creative director", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kuopio")
	
@creative_director.route('/creative-director-tyopaikat-jyvvaskyla')
def creative_director_tyopaikat9(page=1):

    job_list = job_obj.get_job("creative director", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="jyvvaskyla")

@creative_director.route('/creative-director-tyopaikat-pori')
def creative_director_tyopaikat10(page=1):

    job_list = job_obj.get_job("creative director", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="pori")

@creative_director.route('/creative-director-tyopaikat-lappeenranta')
def creative_director_tyopaikat11(page=1):

    job_list = job_obj.get_job("creative director", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="lappeenranta")	
	
@creative_director.route('/creative-director-tyopaikat-vaasa')
def creative_director_tyopaikat12(page=1):

    job_list = job_obj.get_job("creative director", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="vaasa")
	
@creative_director.route('/creative-director-tyopaikat-kotka')
def creative_director_tyopaikat13(page=1):

    job_list = job_obj.get_job("creative director", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kotka")
	
@creative_director.route('/creative-director-tyopaikat-joensuu')
def creative_director_tyopaikat14(page=1):

    job_list = job_obj.get_job("creative director", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="joensuu")
	
@creative_director.route('/creative-director-tyopaikat-hameenlinna')
def creative_director_tyopaikat15(page=1):

    job_list = job_obj.get_job("creative director", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="hameenlinna")
	
@creative_director.route('/creative-director-tyopaikat-porvoo')
def creative_director_tyopaikat16(page=1):

    job_list = job_obj.get_job("creative director", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="porvoo")
	
@creative_director.route('/creative-director-tyopaikat-mikkeli')
def creative_director_tyopaikat17(page=1):

    job_list = job_obj.get_job("creative director", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="mikkeli")

@creative_director.route('/creative-director-tyopaikat-hyvinkaa')
def creative_director_tyopaikat18(page=1):

    job_list = job_obj.get_job("creative director", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="hyvinkaa")
	
@creative_director.route('/creative-director-tyopaikat-nurmijarvi')
def creative_director_tyopaikat19(page=1):

    job_list = job_obj.get_job("creative director", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="nurmijarvi")

@creative_director.route('/creative-director-tyopaikat-jarvenpaa')
def creative_director_tyopaikat20(page=1):

    job_list = job_obj.get_job("creative director", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="jarvenpaa")
	
@creative_director.route('/creative-director-tyopaikat-rauma')
def creative_director_tyopaikat21(page=1):

    job_list = job_obj.get_job("creative director", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="rauma")
	
@creative_director.route('/creative-director-tyopaikat-lohja')
def creative_director_tyopaikat22(page=1):

    job_list = job_obj.get_job("creative director", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="lohja")
	
@creative_director.route('/creative-director-tyopaikat-karleby')
def creative_director_tyopaikat23(page=1):

    job_list = job_obj.get_job("creative director", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="karleby")
	
@creative_director.route('/creative-director-tyopaikat-kajaani')
def creative_director_tyopaikat24(page=1):

    job_list = job_obj.get_job("creative director", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kajaani")
	
@creative_director.route('/creative-director-tyopaikat-rovaniemi')
def creative_director_tyopaikat25(page=1):

    job_list = job_obj.get_job("creative director", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="rovaniemi")
	
@creative_director.route('/creative-director-tyopaikat-tuusula')
def creative_director_tyopaikat26(page=1):

    job_list = job_obj.get_job("creative director", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="tuusula")
	
@creative_director.route('/creative-director-tyopaikat-kirkkonummi')
def creative_director_tyopaikat27(page=1):

    job_list = job_obj.get_job("creative director", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kirkkonummi")
	
@creative_director.route('/creative-director-tyopaikat-seinajoki')
def creative_director_tyopaikat28(page=1):

    job_list = job_obj.get_job("creative director", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="seinajoki")
	
@creative_director.route('/creative-director-tyopaikat-kerava')
def creative_director_tyopaikat29(page=1):

    job_list = job_obj.get_job("creative director", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kerava")
	
@creative_director.route('/creative-director-tyopaikat-kouvola')
def creative_director_tyopaikat30(page=1):

    job_list = job_obj.get_job("creative director", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kouvola")
	
@creative_director.route('/creative-director-tyopaikat-imatra')
def creative_director_tyopaikat31(page=1):

    job_list = job_obj.get_job("creative director", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="imatra")
	
@creative_director.route('/creative-director-tyopaikat-nokia')
def creative_director_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("creative director", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="nokia")
	
@creative_director.route('/creative-director-tyopaikat-savonlinna')
def creative_director_tyopaikat32(page=1):

    job_list = job_obj.get_job("creative director", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="savonlinna")
	
@creative_director.route('/creative-director-tyopaikat-riihimaki')
def creative_director_tyopaikat33(page=1):

    job_list = job_obj.get_job("creative director", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="riihimaki")
	
@creative_director.route('/creative-director-tyopaikat-vihti')
def creative_director_tyopaikat34(page=1):

    job_list = job_obj.get_job("creative director", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="vihti")
	
@creative_director.route('/creative-director-tyopaikat-salo')
def creative_director_tyopaikat35(page=1):

    job_list = job_obj.get_job("creative director", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="salo")
	
@creative_director.route('/creative-director-tyopaikat-kangasala')
def creative_director_tyopaikat36(page=1):

    job_list = job_obj.get_job("creative director", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kangasala")
	
@creative_director.route('/creative-director-tyopaikat-raisio')
def creative_director_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("creative director", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="raisio")
	
@creative_director.route('/creative-director-tyopaikat-karhula')
def creative_director_tyopaikat37(page=1):

    job_list = job_obj.get_job("creative director", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="karhula")
	
@creative_director.route('/creative-director-tyopaikat-kemi')
def creative_director_tyopaikat38(page=1):

    job_list = job_obj.get_job("creative director", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kemi")
	
@creative_director.route('/creative-director-tyopaikat-iisalmi')
def creative_director_tyopaikat39(page=1):

    job_list = job_obj.get_job("creative director", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="iisalmi")
	
@creative_director.route('/creative-director-tyopaikat-varkaus')
def creative_director_tyopaikat40(page=1):

    job_list = job_obj.get_job("creative director", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="varkaus")
	
@creative_director.route('/creative-director-tyopaikat-raahe')
def creative_director_tyopaikat41(page=1):

    job_list = job_obj.get_job("creative director", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="raahe")
	
@creative_director.route('/creative-director-tyopaikat-ylojarvi')
def creative_director_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("creative director", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="ylojarvi")
	
@creative_director.route('/creative-director-tyopaikat-hamina')
def creative_director_tyopaikat42(page=1):

    job_list = job_obj.get_job("creative director", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="hamina")
	
@creative_director.route('/creative-director-tyopaikat-kaarina')
def creative_director_tyopaikat43(page=1):

    job_list = job_obj.get_job("creative director", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kaarina")
	
@creative_director.route('/creative-director-tyopaikat-tornio')
def creative_director_tyopaikat44(page=1):

    job_list = job_obj.get_job("creative director", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="tornio")
	
@creative_director.route('/creative-director-tyopaikat-heinola')
def creative_director_tyopaikat45(page=1):

    job_list = job_obj.get_job("creative director", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="heinola")
	
@creative_director.route('/creative-director-tyopaikat-hollola')
def creative_director_tyopaikat46(page=1):

    job_list = job_obj.get_job("creative director", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="hollola")
	
@creative_director.route('/creative-director-tyopaikat-valkeakoski')
def creative_director_tyopaikat47(page=1):

    job_list = job_obj.get_job("creative director", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="valkeakoski")
	
@creative_director.route('/creative-director-tyopaikat-siilinjarvi')
def creative_director_tyopaikat48(page=1):

    job_list = job_obj.get_job("creative director", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="siilinjarvi")
	
@creative_director.route('/creative-director-tyopaikat-kuusankoski')
def creative_director_tyopaikat49(page=1):

    job_list = job_obj.get_job("creative director", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kuusankoski")
	
@creative_director.route('/creative-director-tyopaikat-sibbo')
def creative_director_tyopaikat50(page=1):

    job_list = job_obj.get_job("creative director", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="sibbo")
	
@creative_director.route('/creative-director-tyopaikat-jakostad')
def creative_director_tyopaikat51(page=1):

    job_list = job_obj.get_job("creative director", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="jakostad")
	
@creative_director.route('/creative-director-tyopaikat-lempaala')
def creative_director_tyopaikat52(page=1):

    job_list = job_obj.get_job("creative director", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="lempaala")
	
@creative_director.route('/creative-director-tyopaikat-mantsala')
def creative_director_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("creative director", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="mantsala")
	
@creative_director.route('/creative-director-tyopaikat-forssa')
def creative_director_tyopaikat53(page=1):

    job_list = job_obj.get_job("creative director", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="forssa")
	
@creative_director.route('/creative-director-tyopaikat-kuusamo')
def creative_director_tyopaikat54(page=1):

    job_list = job_obj.get_job("creative director", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kuusamo")
	
@creative_director.route('/creative-director-tyopaikat-haukipudas')
def creative_director_tyopaikat55(page=1):

    job_list = job_obj.get_job("creative director", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="haukipudas")
	
@creative_director.route('/creative-director-tyopaikat-korsholm')
def creative_director_tyopaikat56(page=1):

    job_list = job_obj.get_job("creative director", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="korsholm")
	
@creative_director.route('/creative-director-tyopaikat-laukaa')
def creative_director_tyopaikat57(page=1):

    job_list = job_obj.get_job("creative director", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="laukaa")
	
@creative_director.route('/creative-director-tyopaikat-anjala')
def creative_director_tyopaikat58(page=1):

    job_list = job_obj.get_job("creative director", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="anjala")
	
@creative_director.route('/creative-director-tyopaikat-uusikaupunki')
def creative_director_tyopaikat59(page=1):

    job_list = job_obj.get_job("creative director", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="uusikaupunki")
	
@creative_director.route('/creative-director-tyopaikat-janakkala')
def creative_director_tyopaikat60(page=1):

    job_list = job_obj.get_job("creative director", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="janakkala")
	
@creative_director.route('/creative-director-tyopaikat-pirkkala')
def creative_director_tyopaikat61(page=1):

    job_list = job_obj.get_job("creative director", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="pirkkala")
	
@creative_director.route('/creative-director-tyopaikat-lansi-turunmaa')
def creative_director_tyopaikat62(page=1):

    job_list = job_obj.get_job("creative director", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="lansi-turunmaa")
	
@creative_director.route('/creative-director-tyopaikat-jamsa')
def creative_director_tyopaikat63(page=1):

    job_list = job_obj.get_job("creative director", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="jamsa")
	
@creative_director.route('/creative-director-tyopaikat-jamsa')
def creative_director_tyopaikat64(page=1):

    job_list = job_obj.get_job("creative director", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="jamsa")
	
@creative_director.route('/creative-director-tyopaikat-vammala')
def creative_director_tyopaikat65(page=1):

    job_list = job_obj.get_job("creative director", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="vammala")
	
@creative_director.route('/creative-director-tyopaikat-nastola')
def creative_director_tyopaikat66(page=1):

    job_list = job_obj.get_job("creative director", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="nastola")
	
@creative_director.route('/creative-director-tyopaikat-orimattila')
def creative_director_tyopaikat67(page=1):

    job_list = job_obj.get_job("creative director", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="orimattila")
	
@creative_director.route('/creative-director-tyopaikat-kauhajoki')
def creative_director_tyopaikat68(page=1):

    job_list = job_obj.get_job("creative director", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kauhajoki")
	
@creative_director.route('/creative-director-tyopaikat-ekenas')
def creative_director_tyopaikat69(page=1):

    job_list = job_obj.get_job("creative director", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="ekenas")
	
@creative_director.route('/creative-director-tyopaikat-kempele')
def creative_director_tyopaikat70(page=1):

    job_list = job_obj.get_job("creative director", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kempele")
	
@creative_director.route('/creative-director-tyopaikat-lapua')
def creative_director_tyopaikat71(page=1):

    job_list = job_obj.get_job("creative director", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="lapua")
	
@creative_director.route('/creative-director-tyopaikat-lieksa')
def creative_director_tyopaikat72(page=1):

    job_list = job_obj.get_job("creative director", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="lieksa")
	
@creative_director.route('/creative-director-tyopaikat-naantali')
def creative_director_tyopaikat73(page=1):

    job_list = job_obj.get_job("creative director", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="naantali")
	
@creative_director.route('/creative-director-tyopaikat-aanekoski')
def creative_director_tyopaikat74(page=1):

    job_list = job_obj.get_job("creative director", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="aanekoski")
	
@creative_director.route('/creative-director-tyopaikat-ylivieska')
def creative_director_tyopaikat75(page=1):

    job_list = job_obj.get_job("creative director", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="ylivieska")
	
@creative_director.route('/creative-director-tyopaikat-kontiolahti')
def creative_director_tyopaikat76(page=1):

    job_list = job_obj.get_job("creative director", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kontiolahti")
	
@creative_director.route('/creative-director-tyopaikat-kankaanpaa')
def creative_director_tyopaikat77(page=1):

    job_list = job_obj.get_job("creative director", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kankaanpaa")
	
@creative_director.route('/creative-director-tyopaikat-ulvila')
def creative_director_tyopaikat78(page=1):

    job_list = job_obj.get_job("creative director", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="ulvila")
	
@creative_director.route('/creative-director-tyopaikat-pieksamaki')
def creative_director_tyopaikat79(page=1):

    job_list = job_obj.get_job("creative director", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="pieksamaki")
	
@creative_director.route('/creative-director-tyopaikat-kiiminki')
def creative_director_tyopaikat80(page=1):

    job_list = job_obj.get_job("creative director", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kiiminki")
	
@creative_director.route('/creative-director-tyopaikat-pargas')
def creative_director_tyopaikat81(page=1):

    job_list = job_obj.get_job("creative director", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="pargas")
	
@creative_director.route('/creative-director-tyopaikat-nurmo')
def creative_director_tyopaikat82(page=1):

    job_list = job_obj.get_job("creative director", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="nurmo")
	
@creative_director.route('/creative-director-tyopaikat-ilmajoki')
def creative_director_tyopaikat83(page=1):

    job_list = job_obj.get_job("creative director", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="ilmajoki")
	
@creative_director.route('/creative-director-tyopaikat-liperi')
def creative_director_tyopaikat84(page=1):

    job_list = job_obj.get_job("creative director", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="liperi")
	
@creative_director.route('/creative-director-tyopaikat-keuruu')
def creative_director_tyopaikat85(page=1):

    job_list = job_obj.get_job("creative director", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="keuruu")
	
@creative_director.route('/creative-director-tyopaikat-leppavirta')
def creative_director_tyopaikat86(page=1):

    job_list = job_obj.get_job("creative director", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="leppavirta")
	
@creative_director.route('/creative-director-tyopaikat-kurikka')
def creative_director_tyopaikat87(page=1):

    job_list = job_obj.get_job("creative director", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kurikka")
	
@creative_director.route('/creative-director-tyopaikat-nivala')
def creative_director_tyopaikat88(page=1):

    job_list = job_obj.get_job("creative director", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="nivala")
	
@creative_director.route('/creative-director-tyopaikat-joutseno')
def creative_director_tyopaikat89(page=1):

    job_list = job_obj.get_job("creative director", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="joutseno")
	
@creative_director.route('/creative-director-tyopaikat-pedersore')
def creative_director_tyopaikat90(page=1):

    job_list = job_obj.get_job("creative director", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="pedersore")
	
@creative_director.route('/creative-director-tyopaikat-sotkamo')
def creative_director_tyopaikat91(page=1):

    job_list = job_obj.get_job("creative director", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="sotkamo")
	
@creative_director.route('/creative-director-tyopaikat-kuhmo')
def creative_director_tyopaikat92(page=1):

    job_list = job_obj.get_job("creative director", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="kuhmo")
	
@creative_director.route('/creative-director-tyopaikat-paimio')
def creative_director_tyopaikat93(page=1):

    job_list = job_obj.get_job("creative director", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="paimio")
	
@creative_director.route('/creative-director-tyopaikat-saarijarvi')
def creative_director_tyopaikat94(page=1):

    job_list = job_obj.get_job("creative director", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director", location="saarijarvi")
	
@creative_director.route('/creative-director-tyopaikat-helsinki')
def creative_director_tyopaikat95(page=1):

    job_list = job_obj.get_job("creative director", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="creative director  ", location="helsinki")
	  

