from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

senior_designer = Blueprint('senior_designer', __name__)
job_obj = Job()



####################################################################


@senior_designer.route('/senior-designer_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "senior-designer" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@senior_designer.route('/senior-designer-avoimet-tyopaikat-espoo')
def senior_designer_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("senior designer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="espoo")

@senior_designer.route('/senior-designer-avoimet-tyopaikat-tampere')
def senior_designer_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("senior designer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="tampere")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-vantaa')
def senior_designer_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("senior designer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="vantaa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-turku')
def senior_designer_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("senior designer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="turku")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-oulu')
def senior_designer_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("senior designer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="oulu")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-lahti')
def senior_designer_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("senior designer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lahti")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kuopio')
def senior_designer_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("senior designer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kuopio")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-jyvvaskyla')
def senior_designer_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("senior designer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="jyvvaskyla")

@senior_designer.route('/senior-designer-avoimet-tyopaikat-pori')
def senior_designer_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("senior designer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="pori")

@senior_designer.route('/senior-designer-avoimet-tyopaikat-lappeenranta')
def senior_designer_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("senior designer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lappeenranta")	
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-vaasa')
def senior_designer_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("senior designer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="vaasa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kotka')
def senior_designer_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("senior designer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kotka")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-joensuu')
def senior_designer_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("senior designer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="joensuu")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-hameenlinna')
def senior_designer_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("senior designer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="hameenlinna")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-porvoo')
def senior_designer_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("senior designer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="porvoo")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-mikkeli')
def senior_designer_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("senior designer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="mikkeli")

@senior_designer.route('/senior-designer-avoimet-tyopaikat-hyvinkaa')
def senior_designer_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("senior designer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="hyvinkaa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-nurmijarvi')
def senior_designer_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("senior designer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="nurmijarvi")

@senior_designer.route('/senior-designer-avoimet-tyopaikat-jarvenpaa')
def senior_designer_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("senior designer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="jarvenpaa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-rauma')
def senior_designer_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("senior designer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="rauma")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-lohja')
def senior_designer_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("senior designer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lohja")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-karleby')
def senior_designer_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("senior designer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="karleby")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kajaani')
def senior_designer_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("senior designer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kajaani")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-rovaniemi')
def senior_designer_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("senior designer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="rovaniemi")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-tuusula')
def senior_designer_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("senior designer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="tuusula")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kirkkonummi')
def senior_designer_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("senior designer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kirkkonummi")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-seinajoki')
def senior_designer_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("senior designer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="seinajoki")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kerava')
def senior_designer_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("senior designer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kerava")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kouvola')
def senior_designer_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("senior designer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kouvola")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-imatra')
def senior_designer_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("senior designer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="imatra")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-nokia')
def senior_designer_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("senior designer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="nokia")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-savonlinna')
def senior_designer_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("senior designer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="savonlinna")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-riihimaki')
def senior_designer_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("senior designer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="riihimaki")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-vihti')
def senior_designer_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("senior designer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="vihti")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-salo')
def senior_designer_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("senior designer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="salo")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kangasala')
def senior_designer_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("senior designer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kangasala")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-raisio')
def senior_designer_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("senior designer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="raisio")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-karhula')
def senior_designer_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("senior designer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="karhula")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kemi')
def senior_designer_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("senior designer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kemi")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-iisalmi')
def senior_designer_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("senior designer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="iisalmi")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-varkaus')
def senior_designer_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("senior designer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="varkaus")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-raahe')
def senior_designer_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("senior designer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="raahe")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-ylojarvi')
def senior_designer_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("senior designer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="ylojarvi")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-hamina')
def senior_designer_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("senior designer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="hamina")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kaarina')
def senior_designer_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("senior designer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kaarina")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-tornio')
def senior_designer_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("senior designer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="tornio")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-heinola')
def senior_designer_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("senior designer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="heinola")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-hollola')
def senior_designer_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("senior designer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="hollola")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-valkeakoski')
def senior_designer_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("senior designer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="valkeakoski")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-siilinjarvi')
def senior_designer_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("senior designer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="siilinjarvi")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kuusankoski')
def senior_designer_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("senior designer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kuusankoski")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-sibbo')
def senior_designer_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("senior designer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="sibbo")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-jakostad')
def senior_designer_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("senior designer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="jakostad")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-lempaala')
def senior_designer_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("senior designer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lempaala")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-mantsala')
def senior_designer_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("senior designer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="mantsala")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-forssa')
def senior_designer_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("senior designer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="forssa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kuusamo')
def senior_designer_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("senior designer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kuusamo")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-haukipudas')
def senior_designer_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("senior designer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="haukipudas")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-korsholm')
def senior_designer_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("senior designer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="korsholm")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-laukaa')
def senior_designer_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("senior designer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="laukaa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-anjala')
def senior_designer_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("senior designer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="anjala")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-uusikaupunki')
def senior_designer_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("senior designer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="uusikaupunki")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-janakkala')
def senior_designer_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("senior designer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="janakkala")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-pirkkala')
def senior_designer_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("senior designer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="pirkkala")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-lansi-turunmaa')
def senior_designer_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("senior designer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lansi-turunmaa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-jamsa')
def senior_designer_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("senior designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="jamsa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-jamsa')
def senior_designer_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("senior designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="jamsa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-vammala')
def senior_designer_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("senior designer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="vammala")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-nastola')
def senior_designer_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("senior designer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="nastola")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-orimattila')
def senior_designer_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("senior designer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="orimattila")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kauhajoki')
def senior_designer_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("senior designer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kauhajoki")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-ekenas')
def senior_designer_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("senior designer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="ekenas")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kempele')
def senior_designer_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("senior designer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kempele")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-lapua')
def senior_designer_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("senior designer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lapua")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-lieksa')
def senior_designer_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("senior designer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lieksa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-naantali')
def senior_designer_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("senior designer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="naantali")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-aanekoski')
def senior_designer_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("senior designer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="aanekoski")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-ylivieska')
def senior_designer_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("senior designer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="ylivieska")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kontiolahti')
def senior_designer_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("senior designer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kontiolahti")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kankaanpaa')
def senior_designer_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("senior designer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kankaanpaa")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-ulvila')
def senior_designer_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("senior designer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="ulvila")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-pieksamaki')
def senior_designer_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("senior designer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="pieksamaki")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kiiminki')
def senior_designer_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("senior designer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kiiminki")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-pargas')
def senior_designer_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("senior designer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="pargas")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-nurmo')
def senior_designer_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("senior designer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="nurmo")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-ilmajoki')
def senior_designer_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("senior designer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="ilmajoki")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-liperi')
def senior_designer_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("senior designer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="liperi")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-keuruu')
def senior_designer_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("senior designer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="keuruu")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-leppavirta')
def senior_designer_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("senior designer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="leppavirta")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kurikka')
def senior_designer_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("senior designer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kurikka")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-nivala')
def senior_designer_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("senior designer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="nivala")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-joutseno')
def senior_designer_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("senior designer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="joutseno")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-pedersore')
def senior_designer_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("senior designer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="pedersore")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-sotkamo')
def senior_designer_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("senior designer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="sotkamo")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-kuhmo')
def senior_designer_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("senior designer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kuhmo")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-paimio')
def senior_designer_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("senior designer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="paimio")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-saarijarvi')
def senior_designer_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("senior designer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="saarijarvi")
	
@senior_designer.route('/senior-designer-avoimet-tyopaikat-helsinki')
def senior_designer_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("senior designer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="helsinki")


####################################################################


##############################################
@senior_designer.route('/senior-designer-jobs-espoo')
def senior_designer_jobs2(page=1):

    job_list = job_obj.get_job("senior designer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="espoo")

@senior_designer.route('/senior-designer-jobs-tampere')
def senior_designer_jobs3(page=1):

    job_list = job_obj.get_job("senior designer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="tampere")
	
@senior_designer.route('/senior-designer-jobs-vantaa')
def senior_designer_jobs4(page=1):

    job_list = job_obj.get_job("senior designer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="vantaa")
	
@senior_designer.route('/senior-designer-jobs-turku')
def senior_designer_jobs5(page=1):

    job_list = job_obj.get_job("senior designer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="turku")
	
@senior_designer.route('/senior-designer-jobs-oulu')
def senior_designer_jobs6(page=1):

    job_list = job_obj.get_job("senior designer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="oulu")
	
@senior_designer.route('/senior-designer-jobs-lahti')
def senior_designer_jobs7(page=1):

    job_list = job_obj.get_job("senior designer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lahti")
	
@senior_designer.route('/senior-designer-jobs-kuopio')
def senior_designer_jobs8(page=1):

    job_list = job_obj.get_job("senior designer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kuopio")
	
@senior_designer.route('/senior-designer-jobs-jyvvaskyla')
def senior_designer_jobs9(page=1):

    job_list = job_obj.get_job("senior designer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="jyvvaskyla")

@senior_designer.route('/senior-designer-jobs-pori')
def senior_designer_jobs10(page=1):

    job_list = job_obj.get_job("senior designer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="pori")

@senior_designer.route('/senior-designer-jobs-lappeenranta')
def senior_designer_jobs11(page=1):

    job_list = job_obj.get_job("senior designer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lappeenranta")	
	
@senior_designer.route('/senior-designer-jobs-vaasa')
def senior_designer_jobs12(page=1):

    job_list = job_obj.get_job("senior designer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="vaasa")
	
@senior_designer.route('/senior-designer-jobs-kotka')
def senior_designer_jobs13(page=1):

    job_list = job_obj.get_job("senior designer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kotka")
	
@senior_designer.route('/senior-designer-jobs-joensuu')
def senior_designer_jobs14(page=1):

    job_list = job_obj.get_job("senior designer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="joensuu")
	
@senior_designer.route('/senior-designer-jobs-hameenlinna')
def senior_designer_jobs15(page=1):

    job_list = job_obj.get_job("senior designer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="hameenlinna")
	
@senior_designer.route('/senior-designer-jobs-porvoo')
def senior_designer_jobs16(page=1):

    job_list = job_obj.get_job("senior designer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="porvoo")
	
@senior_designer.route('/senior-designer-jobs-mikkeli')
def senior_designer_jobs17(page=1):

    job_list = job_obj.get_job("senior designer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="mikkeli")

@senior_designer.route('/senior-designer-jobs-hyvinkaa')
def senior_designer_jobs18(page=1):

    job_list = job_obj.get_job("senior designer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="hyvinkaa")
	
@senior_designer.route('/senior-designer-jobs-nurmijarvi')
def senior_designer_jobs19(page=1):

    job_list = job_obj.get_job("senior designer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="nurmijarvi")

@senior_designer.route('/senior-designer-jobs-jarvenpaa')
def senior_designer_jobs20(page=1):

    job_list = job_obj.get_job("senior designer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="jarvenpaa")
	
@senior_designer.route('/senior-designer-jobs-rauma')
def senior_designer_jobs21(page=1):

    job_list = job_obj.get_job("senior designer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="rauma")
	
@senior_designer.route('/senior-designer-jobs-lohja')
def senior_designer_jobs22(page=1):

    job_list = job_obj.get_job("senior designer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lohja")
	
@senior_designer.route('/senior-designer-jobs-karleby')
def senior_designer_jobs23(page=1):

    job_list = job_obj.get_job("senior designer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="karleby")
	
@senior_designer.route('/senior-designer-jobs-kajaani')
def senior_designer_jobs24(page=1):

    job_list = job_obj.get_job("senior designer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kajaani")
	
@senior_designer.route('/senior-designer-jobs-rovaniemi')
def senior_designer_jobs25(page=1):

    job_list = job_obj.get_job("senior designer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="rovaniemi")
	
@senior_designer.route('/senior-designer-jobs-tuusula')
def senior_designer_jobs26(page=1):

    job_list = job_obj.get_job("senior designer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="tuusula")
	
@senior_designer.route('/senior-designer-jobs-kirkkonummi')
def senior_designer_jobs27(page=1):

    job_list = job_obj.get_job("senior designer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kirkkonummi")
	
@senior_designer.route('/senior-designer-jobs-seinajoki')
def senior_designer_jobs28(page=1):

    job_list = job_obj.get_job("senior designer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="seinajoki")
	
@senior_designer.route('/senior-designer-jobs-kerava')
def senior_designer_jobs29(page=1):

    job_list = job_obj.get_job("senior designer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kerava")
	
@senior_designer.route('/senior-designer-jobs-kouvola')
def senior_designer_jobs30(page=1):

    job_list = job_obj.get_job("senior designer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kouvola")
	
@senior_designer.route('/senior-designer-jobs-imatra')
def senior_designer_jobs31(page=1):

    job_list = job_obj.get_job("senior designer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="imatra")
	
@senior_designer.route('/senior-designer-jobs-nokia')
def senior_designer_jobs32_1(page=1):

    job_list = job_obj.get_job("senior designer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="nokia")
	
@senior_designer.route('/senior-designer-jobs-savonlinna')
def senior_designer_jobs32(page=1):

    job_list = job_obj.get_job("senior designer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="savonlinna")
	
@senior_designer.route('/senior-designer-jobs-riihimaki')
def senior_designer_jobs33(page=1):

    job_list = job_obj.get_job("senior designer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="riihimaki")
	
@senior_designer.route('/senior-designer-jobs-vihti')
def senior_designer_jobs34(page=1):

    job_list = job_obj.get_job("senior designer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="vihti")
	
@senior_designer.route('/senior-designer-jobs-salo')
def senior_designer_jobs35(page=1):

    job_list = job_obj.get_job("senior designer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="salo")
	
@senior_designer.route('/senior-designer-jobs-kangasala')
def senior_designer_jobs36(page=1):

    job_list = job_obj.get_job("senior designer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kangasala")
	
@senior_designer.route('/senior-designer-jobs-raisio')
def senior_designer_jobs37_1(page=1):

    job_list = job_obj.get_job("senior designer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="raisio")
	
@senior_designer.route('/senior-designer-jobs-karhula')
def senior_designer_jobs37(page=1):

    job_list = job_obj.get_job("senior designer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="karhula")
	
@senior_designer.route('/senior-designer-jobs-kemi')
def senior_designer_jobs38(page=1):

    job_list = job_obj.get_job("senior designer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kemi")
	
@senior_designer.route('/senior-designer-jobs-iisalmi')
def senior_designer_jobs39(page=1):

    job_list = job_obj.get_job("senior designer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="iisalmi")
	
@senior_designer.route('/senior-designer-jobs-varkaus')
def senior_designer_jobs40(page=1):

    job_list = job_obj.get_job("senior designer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="varkaus")
	
@senior_designer.route('/senior-designer-jobs-raahe')
def senior_designer_jobs41(page=1):

    job_list = job_obj.get_job("senior designer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="raahe")
	
@senior_designer.route('/senior-designer-jobs-ylojarvi')
def senior_designer_jobs42_1(page=1):

    job_list = job_obj.get_job("senior designer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="ylojarvi")
	
@senior_designer.route('/senior-designer-jobs-hamina')
def senior_designer_jobs42(page=1):

    job_list = job_obj.get_job("senior designer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="hamina")
	
@senior_designer.route('/senior-designer-jobs-kaarina')
def senior_designer_jobs43(page=1):

    job_list = job_obj.get_job("senior designer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kaarina")
	
@senior_designer.route('/senior-designer-jobs-tornio')
def senior_designer_jobs44(page=1):

    job_list = job_obj.get_job("senior designer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="tornio")
	
@senior_designer.route('/senior-designer-jobs-heinola')
def senior_designer_jobs45(page=1):

    job_list = job_obj.get_job("senior designer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="heinola")
	
@senior_designer.route('/senior-designer-jobs-hollola')
def senior_designer_jobs46(page=1):

    job_list = job_obj.get_job("senior designer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="hollola")
	
@senior_designer.route('/senior-designer-jobs-valkeakoski')
def senior_designer_jobs47(page=1):

    job_list = job_obj.get_job("senior designer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="valkeakoski")
	
@senior_designer.route('/senior-designer-jobs-siilinjarvi')
def senior_designer_jobs48(page=1):

    job_list = job_obj.get_job("senior designer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="siilinjarvi")
	
@senior_designer.route('/senior-designer-jobs-kuusankoski')
def senior_designer_jobs49(page=1):

    job_list = job_obj.get_job("senior designer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kuusankoski")
	
@senior_designer.route('/senior-designer-jobs-sibbo')
def senior_designer_jobs50(page=1):

    job_list = job_obj.get_job("senior designer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="sibbo")
	
@senior_designer.route('/senior-designer-jobs-jakostad')
def senior_designer_jobs51(page=1):

    job_list = job_obj.get_job("senior designer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="jakostad")
	
@senior_designer.route('/senior-designer-jobs-lempaala')
def senior_designer_jobs52(page=1):

    job_list = job_obj.get_job("senior designer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lempaala")
	
@senior_designer.route('/senior-designer-jobs-mantsala')
def senior_designer_jobs52_1(page=1):

    job_list = job_obj.get_job("senior designer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="mantsala")
	
@senior_designer.route('/senior-designer-jobs-forssa')
def senior_designer_jobs53(page=1):

    job_list = job_obj.get_job("senior designer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="forssa")
	
@senior_designer.route('/senior-designer-jobs-kuusamo')
def senior_designer_jobs54(page=1):

    job_list = job_obj.get_job("senior designer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kuusamo")
	
@senior_designer.route('/senior-designer-jobs-haukipudas')
def senior_designer_jobs55(page=1):

    job_list = job_obj.get_job("senior designer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="haukipudas")
	
@senior_designer.route('/senior-designer-jobs-korsholm')
def senior_designer_jobs56(page=1):

    job_list = job_obj.get_job("senior designer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="korsholm")
	
@senior_designer.route('/senior-designer-jobs-laukaa')
def senior_designer_jobs57(page=1):

    job_list = job_obj.get_job("senior designer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="laukaa")
	
@senior_designer.route('/senior-designer-jobs-anjala')
def senior_designer_jobs58(page=1):

    job_list = job_obj.get_job("senior designer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="anjala")
	
@senior_designer.route('/senior-designer-jobs-uusikaupunki')
def senior_designer_jobs59(page=1):

    job_list = job_obj.get_job("senior designer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="uusikaupunki")
	
@senior_designer.route('/senior-designer-jobs-janakkala')
def senior_designer_jobs60(page=1):

    job_list = job_obj.get_job("senior designer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="janakkala")
	
@senior_designer.route('/senior-designer-jobs-pirkkala')
def senior_designer_jobs61(page=1):

    job_list = job_obj.get_job("senior designer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="pirkkala")
	
@senior_designer.route('/senior-designer-jobs-lansi-turunmaa')
def senior_designer_jobs62(page=1):

    job_list = job_obj.get_job("senior designer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lansi-turunmaa")
	
@senior_designer.route('/senior-designer-jobs-jamsa')
def senior_designer_jobs63(page=1):

    job_list = job_obj.get_job("senior designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="jamsa")
	
@senior_designer.route('/senior-designer-jobs-jamsa')
def senior_designer_jobs64(page=1):

    job_list = job_obj.get_job("senior designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="jamsa")
	
@senior_designer.route('/senior-designer-jobs-vammala')
def senior_designer_jobs65(page=1):

    job_list = job_obj.get_job("senior designer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="vammala")
	
@senior_designer.route('/senior-designer-jobs-nastola')
def senior_designer_jobs66(page=1):

    job_list = job_obj.get_job("senior designer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="nastola")
	
@senior_designer.route('/senior-designer-jobs-orimattila')
def senior_designer_jobs67(page=1):

    job_list = job_obj.get_job("senior designer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="orimattila")
	
@senior_designer.route('/senior-designer-jobs-kauhajoki')
def senior_designer_jobs68(page=1):

    job_list = job_obj.get_job("senior designer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kauhajoki")
	
@senior_designer.route('/senior-designer-jobs-ekenas')
def senior_designer_jobs69(page=1):

    job_list = job_obj.get_job("senior designer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="ekenas")
	
@senior_designer.route('/senior-designer-jobs-kempele')
def senior_designer_jobs70(page=1):

    job_list = job_obj.get_job("senior designer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kempele")
	
@senior_designer.route('/senior-designer-jobs-lapua')
def senior_designer_jobs71(page=1):

    job_list = job_obj.get_job("senior designer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lapua")
	
@senior_designer.route('/senior-designer-jobs-lieksa')
def senior_designer_jobs72(page=1):

    job_list = job_obj.get_job("senior designer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="lieksa")
	
@senior_designer.route('/senior-designer-jobs-naantali')
def senior_designer_jobs73(page=1):

    job_list = job_obj.get_job("senior designer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="naantali")
	
@senior_designer.route('/senior-designer-jobs-aanekoski')
def senior_designer_jobs74(page=1):

    job_list = job_obj.get_job("senior designer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="aanekoski")
	
@senior_designer.route('/senior-designer-jobs-ylivieska')
def senior_designer_jobs75(page=1):

    job_list = job_obj.get_job("senior designer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="ylivieska")
	
@senior_designer.route('/senior-designer-jobs-kontiolahti')
def senior_designer_jobs76(page=1):

    job_list = job_obj.get_job("senior designer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kontiolahti")
	
@senior_designer.route('/senior-designer-jobs-kankaanpaa')
def senior_designer_jobs77(page=1):

    job_list = job_obj.get_job("senior designer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kankaanpaa")
	
@senior_designer.route('/senior-designer-jobs-ulvila')
def senior_designer_jobs78(page=1):

    job_list = job_obj.get_job("senior designer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="ulvila")
	
@senior_designer.route('/senior-designer-jobs-pieksamaki')
def senior_designer_jobs79(page=1):

    job_list = job_obj.get_job("senior designer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="pieksamaki")
	
@senior_designer.route('/senior-designer-jobs-kiiminki')
def senior_designer_jobs80(page=1):

    job_list = job_obj.get_job("senior designer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kiiminki")
	
@senior_designer.route('/senior-designer-jobs-pargas')
def senior_designer_jobs81(page=1):

    job_list = job_obj.get_job("senior designer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="pargas")
	
@senior_designer.route('/senior-designer-jobs-nurmo')
def senior_designer_jobs82(page=1):

    job_list = job_obj.get_job("senior designer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="nurmo")
	
@senior_designer.route('/senior-designer-jobs-ilmajoki')
def senior_designer_jobs83(page=1):

    job_list = job_obj.get_job("senior designer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="ilmajoki")
	
@senior_designer.route('/senior-designer-jobs-liperi')
def senior_designer_jobs84(page=1):

    job_list = job_obj.get_job("senior designer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="liperi")
	
@senior_designer.route('/senior-designer-jobs-keuruu')
def senior_designer_jobs85(page=1):

    job_list = job_obj.get_job("senior designer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="keuruu")
	
@senior_designer.route('/senior-designer-jobs-leppavirta')
def senior_designer_jobs86(page=1):

    job_list = job_obj.get_job("senior designer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="leppavirta")
	
@senior_designer.route('/senior-designer-jobs-kurikka')
def senior_designer_jobs87(page=1):

    job_list = job_obj.get_job("senior designer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kurikka")
	
@senior_designer.route('/senior-designer-jobs-nivala')
def senior_designer_jobs88(page=1):

    job_list = job_obj.get_job("senior designer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="nivala")
	
@senior_designer.route('/senior-designer-jobs-joutseno')
def senior_designer_jobs89(page=1):

    job_list = job_obj.get_job("senior designer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="joutseno")
	
@senior_designer.route('/senior-designer-jobs-pedersore')
def senior_designer_jobs90(page=1):

    job_list = job_obj.get_job("senior designer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="pedersore")
	
@senior_designer.route('/senior-designer-jobs-sotkamo')
def senior_designer_jobs91(page=1):

    job_list = job_obj.get_job("senior designer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="sotkamo")
	
@senior_designer.route('/senior-designer-jobs-kuhmo')
def senior_designer_jobs92(page=1):

    job_list = job_obj.get_job("senior designer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="kuhmo")
	
@senior_designer.route('/senior-designer-jobs-paimio')
def senior_designer_jobs93(page=1):

    job_list = job_obj.get_job("senior designer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="paimio")
	
@senior_designer.route('/senior-designer-jobs-saarijarvi')
def senior_designer_jobs94(page=1):

    job_list = job_obj.get_job("senior designer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="saarijarvi")
	
@senior_designer.route('/senior-designer-jobs-helsinki')
def senior_designer_jobs95(page=1):

    job_list = job_obj.get_job("senior designer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer ", location="helsinki")


####################################################################


##############################################
@senior_designer.route('/senior-designer-tyopaikat-espoo')
def senior_designer_tyopaikat2(page=1):

    job_list = job_obj.get_job("senior designer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="espoo")

@senior_designer.route('/senior-designer-tyopaikat-tampere')
def senior_designer_tyopaikat3(page=1):

    job_list = job_obj.get_job("senior designer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="tampere")
	
@senior_designer.route('/senior-designer-tyopaikat-vantaa')
def senior_designer_tyopaikat4(page=1):

    job_list = job_obj.get_job("senior designer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="vantaa")
	
@senior_designer.route('/senior-designer-tyopaikat-turku')
def senior_designer_tyopaikat5(page=1):

    job_list = job_obj.get_job("senior designer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="turku")
	
@senior_designer.route('/senior-designer-tyopaikat-oulu')
def senior_designer_tyopaikat6(page=1):

    job_list = job_obj.get_job("senior designer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="oulu")
	
@senior_designer.route('/senior-designer-tyopaikat-lahti')
def senior_designer_tyopaikat7(page=1):

    job_list = job_obj.get_job("senior designer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="lahti")
	
@senior_designer.route('/senior-designer-tyopaikat-kuopio')
def senior_designer_tyopaikat8(page=1):

    job_list = job_obj.get_job("senior designer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kuopio")
	
@senior_designer.route('/senior-designer-tyopaikat-jyvvaskyla')
def senior_designer_tyopaikat9(page=1):

    job_list = job_obj.get_job("senior designer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="jyvvaskyla")

@senior_designer.route('/senior-designer-tyopaikat-pori')
def senior_designer_tyopaikat10(page=1):

    job_list = job_obj.get_job("senior designer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="pori")

@senior_designer.route('/senior-designer-tyopaikat-lappeenranta')
def senior_designer_tyopaikat11(page=1):

    job_list = job_obj.get_job("senior designer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="lappeenranta")	
	
@senior_designer.route('/senior-designer-tyopaikat-vaasa')
def senior_designer_tyopaikat12(page=1):

    job_list = job_obj.get_job("senior designer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="vaasa")
	
@senior_designer.route('/senior-designer-tyopaikat-kotka')
def senior_designer_tyopaikat13(page=1):

    job_list = job_obj.get_job("senior designer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kotka")
	
@senior_designer.route('/senior-designer-tyopaikat-joensuu')
def senior_designer_tyopaikat14(page=1):

    job_list = job_obj.get_job("senior designer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="joensuu")
	
@senior_designer.route('/senior-designer-tyopaikat-hameenlinna')
def senior_designer_tyopaikat15(page=1):

    job_list = job_obj.get_job("senior designer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="hameenlinna")
	
@senior_designer.route('/senior-designer-tyopaikat-porvoo')
def senior_designer_tyopaikat16(page=1):

    job_list = job_obj.get_job("senior designer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="porvoo")
	
@senior_designer.route('/senior-designer-tyopaikat-mikkeli')
def senior_designer_tyopaikat17(page=1):

    job_list = job_obj.get_job("senior designer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="mikkeli")

@senior_designer.route('/senior-designer-tyopaikat-hyvinkaa')
def senior_designer_tyopaikat18(page=1):

    job_list = job_obj.get_job("senior designer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="hyvinkaa")
	
@senior_designer.route('/senior-designer-tyopaikat-nurmijarvi')
def senior_designer_tyopaikat19(page=1):

    job_list = job_obj.get_job("senior designer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="nurmijarvi")

@senior_designer.route('/senior-designer-tyopaikat-jarvenpaa')
def senior_designer_tyopaikat20(page=1):

    job_list = job_obj.get_job("senior designer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="jarvenpaa")
	
@senior_designer.route('/senior-designer-tyopaikat-rauma')
def senior_designer_tyopaikat21(page=1):

    job_list = job_obj.get_job("senior designer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="rauma")
	
@senior_designer.route('/senior-designer-tyopaikat-lohja')
def senior_designer_tyopaikat22(page=1):

    job_list = job_obj.get_job("senior designer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="lohja")
	
@senior_designer.route('/senior-designer-tyopaikat-karleby')
def senior_designer_tyopaikat23(page=1):

    job_list = job_obj.get_job("senior designer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="karleby")
	
@senior_designer.route('/senior-designer-tyopaikat-kajaani')
def senior_designer_tyopaikat24(page=1):

    job_list = job_obj.get_job("senior designer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kajaani")
	
@senior_designer.route('/senior-designer-tyopaikat-rovaniemi')
def senior_designer_tyopaikat25(page=1):

    job_list = job_obj.get_job("senior designer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="rovaniemi")
	
@senior_designer.route('/senior-designer-tyopaikat-tuusula')
def senior_designer_tyopaikat26(page=1):

    job_list = job_obj.get_job("senior designer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="tuusula")
	
@senior_designer.route('/senior-designer-tyopaikat-kirkkonummi')
def senior_designer_tyopaikat27(page=1):

    job_list = job_obj.get_job("senior designer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kirkkonummi")
	
@senior_designer.route('/senior-designer-tyopaikat-seinajoki')
def senior_designer_tyopaikat28(page=1):

    job_list = job_obj.get_job("senior designer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="seinajoki")
	
@senior_designer.route('/senior-designer-tyopaikat-kerava')
def senior_designer_tyopaikat29(page=1):

    job_list = job_obj.get_job("senior designer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kerava")
	
@senior_designer.route('/senior-designer-tyopaikat-kouvola')
def senior_designer_tyopaikat30(page=1):

    job_list = job_obj.get_job("senior designer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kouvola")
	
@senior_designer.route('/senior-designer-tyopaikat-imatra')
def senior_designer_tyopaikat31(page=1):

    job_list = job_obj.get_job("senior designer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="imatra")
	
@senior_designer.route('/senior-designer-tyopaikat-nokia')
def senior_designer_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("senior designer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="nokia")
	
@senior_designer.route('/senior-designer-tyopaikat-savonlinna')
def senior_designer_tyopaikat32(page=1):

    job_list = job_obj.get_job("senior designer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="savonlinna")
	
@senior_designer.route('/senior-designer-tyopaikat-riihimaki')
def senior_designer_tyopaikat33(page=1):

    job_list = job_obj.get_job("senior designer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="riihimaki")
	
@senior_designer.route('/senior-designer-tyopaikat-vihti')
def senior_designer_tyopaikat34(page=1):

    job_list = job_obj.get_job("senior designer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="vihti")
	
@senior_designer.route('/senior-designer-tyopaikat-salo')
def senior_designer_tyopaikat35(page=1):

    job_list = job_obj.get_job("senior designer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="salo")
	
@senior_designer.route('/senior-designer-tyopaikat-kangasala')
def senior_designer_tyopaikat36(page=1):

    job_list = job_obj.get_job("senior designer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kangasala")
	
@senior_designer.route('/senior-designer-tyopaikat-raisio')
def senior_designer_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("senior designer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="raisio")
	
@senior_designer.route('/senior-designer-tyopaikat-karhula')
def senior_designer_tyopaikat37(page=1):

    job_list = job_obj.get_job("senior designer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="karhula")
	
@senior_designer.route('/senior-designer-tyopaikat-kemi')
def senior_designer_tyopaikat38(page=1):

    job_list = job_obj.get_job("senior designer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kemi")
	
@senior_designer.route('/senior-designer-tyopaikat-iisalmi')
def senior_designer_tyopaikat39(page=1):

    job_list = job_obj.get_job("senior designer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="iisalmi")
	
@senior_designer.route('/senior-designer-tyopaikat-varkaus')
def senior_designer_tyopaikat40(page=1):

    job_list = job_obj.get_job("senior designer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="varkaus")
	
@senior_designer.route('/senior-designer-tyopaikat-raahe')
def senior_designer_tyopaikat41(page=1):

    job_list = job_obj.get_job("senior designer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="raahe")
	
@senior_designer.route('/senior-designer-tyopaikat-ylojarvi')
def senior_designer_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("senior designer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="ylojarvi")
	
@senior_designer.route('/senior-designer-tyopaikat-hamina')
def senior_designer_tyopaikat42(page=1):

    job_list = job_obj.get_job("senior designer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="hamina")
	
@senior_designer.route('/senior-designer-tyopaikat-kaarina')
def senior_designer_tyopaikat43(page=1):

    job_list = job_obj.get_job("senior designer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kaarina")
	
@senior_designer.route('/senior-designer-tyopaikat-tornio')
def senior_designer_tyopaikat44(page=1):

    job_list = job_obj.get_job("senior designer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="tornio")
	
@senior_designer.route('/senior-designer-tyopaikat-heinola')
def senior_designer_tyopaikat45(page=1):

    job_list = job_obj.get_job("senior designer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="heinola")
	
@senior_designer.route('/senior-designer-tyopaikat-hollola')
def senior_designer_tyopaikat46(page=1):

    job_list = job_obj.get_job("senior designer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="hollola")
	
@senior_designer.route('/senior-designer-tyopaikat-valkeakoski')
def senior_designer_tyopaikat47(page=1):

    job_list = job_obj.get_job("senior designer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="valkeakoski")
	
@senior_designer.route('/senior-designer-tyopaikat-siilinjarvi')
def senior_designer_tyopaikat48(page=1):

    job_list = job_obj.get_job("senior designer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="siilinjarvi")
	
@senior_designer.route('/senior-designer-tyopaikat-kuusankoski')
def senior_designer_tyopaikat49(page=1):

    job_list = job_obj.get_job("senior designer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kuusankoski")
	
@senior_designer.route('/senior-designer-tyopaikat-sibbo')
def senior_designer_tyopaikat50(page=1):

    job_list = job_obj.get_job("senior designer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="sibbo")
	
@senior_designer.route('/senior-designer-tyopaikat-jakostad')
def senior_designer_tyopaikat51(page=1):

    job_list = job_obj.get_job("senior designer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="jakostad")
	
@senior_designer.route('/senior-designer-tyopaikat-lempaala')
def senior_designer_tyopaikat52(page=1):

    job_list = job_obj.get_job("senior designer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="lempaala")
	
@senior_designer.route('/senior-designer-tyopaikat-mantsala')
def senior_designer_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("senior designer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="mantsala")
	
@senior_designer.route('/senior-designer-tyopaikat-forssa')
def senior_designer_tyopaikat53(page=1):

    job_list = job_obj.get_job("senior designer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="forssa")
	
@senior_designer.route('/senior-designer-tyopaikat-kuusamo')
def senior_designer_tyopaikat54(page=1):

    job_list = job_obj.get_job("senior designer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kuusamo")
	
@senior_designer.route('/senior-designer-tyopaikat-haukipudas')
def senior_designer_tyopaikat55(page=1):

    job_list = job_obj.get_job("senior designer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="haukipudas")
	
@senior_designer.route('/senior-designer-tyopaikat-korsholm')
def senior_designer_tyopaikat56(page=1):

    job_list = job_obj.get_job("senior designer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="korsholm")
	
@senior_designer.route('/senior-designer-tyopaikat-laukaa')
def senior_designer_tyopaikat57(page=1):

    job_list = job_obj.get_job("senior designer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="laukaa")
	
@senior_designer.route('/senior-designer-tyopaikat-anjala')
def senior_designer_tyopaikat58(page=1):

    job_list = job_obj.get_job("senior designer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="anjala")
	
@senior_designer.route('/senior-designer-tyopaikat-uusikaupunki')
def senior_designer_tyopaikat59(page=1):

    job_list = job_obj.get_job("senior designer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="uusikaupunki")
	
@senior_designer.route('/senior-designer-tyopaikat-janakkala')
def senior_designer_tyopaikat60(page=1):

    job_list = job_obj.get_job("senior designer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="janakkala")
	
@senior_designer.route('/senior-designer-tyopaikat-pirkkala')
def senior_designer_tyopaikat61(page=1):

    job_list = job_obj.get_job("senior designer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="pirkkala")
	
@senior_designer.route('/senior-designer-tyopaikat-lansi-turunmaa')
def senior_designer_tyopaikat62(page=1):

    job_list = job_obj.get_job("senior designer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="lansi-turunmaa")
	
@senior_designer.route('/senior-designer-tyopaikat-jamsa')
def senior_designer_tyopaikat63(page=1):

    job_list = job_obj.get_job("senior designer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="jamsa")
	
@senior_designer.route('/senior-designer-tyopaikat-jamsa')
def senior_designer_tyopaikat64(page=1):

    job_list = job_obj.get_job("senior designer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="jamsa")
	
@senior_designer.route('/senior-designer-tyopaikat-vammala')
def senior_designer_tyopaikat65(page=1):

    job_list = job_obj.get_job("senior designer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="vammala")
	
@senior_designer.route('/senior-designer-tyopaikat-nastola')
def senior_designer_tyopaikat66(page=1):

    job_list = job_obj.get_job("senior designer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="nastola")
	
@senior_designer.route('/senior-designer-tyopaikat-orimattila')
def senior_designer_tyopaikat67(page=1):

    job_list = job_obj.get_job("senior designer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="orimattila")
	
@senior_designer.route('/senior-designer-tyopaikat-kauhajoki')
def senior_designer_tyopaikat68(page=1):

    job_list = job_obj.get_job("senior designer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kauhajoki")
	
@senior_designer.route('/senior-designer-tyopaikat-ekenas')
def senior_designer_tyopaikat69(page=1):

    job_list = job_obj.get_job("senior designer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="ekenas")
	
@senior_designer.route('/senior-designer-tyopaikat-kempele')
def senior_designer_tyopaikat70(page=1):

    job_list = job_obj.get_job("senior designer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kempele")
	
@senior_designer.route('/senior-designer-tyopaikat-lapua')
def senior_designer_tyopaikat71(page=1):

    job_list = job_obj.get_job("senior designer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="lapua")
	
@senior_designer.route('/senior-designer-tyopaikat-lieksa')
def senior_designer_tyopaikat72(page=1):

    job_list = job_obj.get_job("senior designer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="lieksa")
	
@senior_designer.route('/senior-designer-tyopaikat-naantali')
def senior_designer_tyopaikat73(page=1):

    job_list = job_obj.get_job("senior designer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="naantali")
	
@senior_designer.route('/senior-designer-tyopaikat-aanekoski')
def senior_designer_tyopaikat74(page=1):

    job_list = job_obj.get_job("senior designer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="aanekoski")
	
@senior_designer.route('/senior-designer-tyopaikat-ylivieska')
def senior_designer_tyopaikat75(page=1):

    job_list = job_obj.get_job("senior designer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="ylivieska")
	
@senior_designer.route('/senior-designer-tyopaikat-kontiolahti')
def senior_designer_tyopaikat76(page=1):

    job_list = job_obj.get_job("senior designer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kontiolahti")
	
@senior_designer.route('/senior-designer-tyopaikat-kankaanpaa')
def senior_designer_tyopaikat77(page=1):

    job_list = job_obj.get_job("senior designer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kankaanpaa")
	
@senior_designer.route('/senior-designer-tyopaikat-ulvila')
def senior_designer_tyopaikat78(page=1):

    job_list = job_obj.get_job("senior designer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="ulvila")
	
@senior_designer.route('/senior-designer-tyopaikat-pieksamaki')
def senior_designer_tyopaikat79(page=1):

    job_list = job_obj.get_job("senior designer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="pieksamaki")
	
@senior_designer.route('/senior-designer-tyopaikat-kiiminki')
def senior_designer_tyopaikat80(page=1):

    job_list = job_obj.get_job("senior designer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kiiminki")
	
@senior_designer.route('/senior-designer-tyopaikat-pargas')
def senior_designer_tyopaikat81(page=1):

    job_list = job_obj.get_job("senior designer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="pargas")
	
@senior_designer.route('/senior-designer-tyopaikat-nurmo')
def senior_designer_tyopaikat82(page=1):

    job_list = job_obj.get_job("senior designer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="nurmo")
	
@senior_designer.route('/senior-designer-tyopaikat-ilmajoki')
def senior_designer_tyopaikat83(page=1):

    job_list = job_obj.get_job("senior designer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="ilmajoki")
	
@senior_designer.route('/senior-designer-tyopaikat-liperi')
def senior_designer_tyopaikat84(page=1):

    job_list = job_obj.get_job("senior designer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="liperi")
	
@senior_designer.route('/senior-designer-tyopaikat-keuruu')
def senior_designer_tyopaikat85(page=1):

    job_list = job_obj.get_job("senior designer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="keuruu")
	
@senior_designer.route('/senior-designer-tyopaikat-leppavirta')
def senior_designer_tyopaikat86(page=1):

    job_list = job_obj.get_job("senior designer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="leppavirta")
	
@senior_designer.route('/senior-designer-tyopaikat-kurikka')
def senior_designer_tyopaikat87(page=1):

    job_list = job_obj.get_job("senior designer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kurikka")
	
@senior_designer.route('/senior-designer-tyopaikat-nivala')
def senior_designer_tyopaikat88(page=1):

    job_list = job_obj.get_job("senior designer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="nivala")
	
@senior_designer.route('/senior-designer-tyopaikat-joutseno')
def senior_designer_tyopaikat89(page=1):

    job_list = job_obj.get_job("senior designer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="joutseno")
	
@senior_designer.route('/senior-designer-tyopaikat-pedersore')
def senior_designer_tyopaikat90(page=1):

    job_list = job_obj.get_job("senior designer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="pedersore")
	
@senior_designer.route('/senior-designer-tyopaikat-sotkamo')
def senior_designer_tyopaikat91(page=1):

    job_list = job_obj.get_job("senior designer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="sotkamo")
	
@senior_designer.route('/senior-designer-tyopaikat-kuhmo')
def senior_designer_tyopaikat92(page=1):

    job_list = job_obj.get_job("senior designer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="kuhmo")
	
@senior_designer.route('/senior-designer-tyopaikat-paimio')
def senior_designer_tyopaikat93(page=1):

    job_list = job_obj.get_job("senior designer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="paimio")
	
@senior_designer.route('/senior-designer-tyopaikat-saarijarvi')
def senior_designer_tyopaikat94(page=1):

    job_list = job_obj.get_job("senior designer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer", location="saarijarvi")
	
@senior_designer.route('/senior-designer-tyopaikat-helsinki')
def senior_designer_tyopaikat95(page=1):

    job_list = job_obj.get_job("senior designer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="senior designer  ", location="helsinki")
	  

