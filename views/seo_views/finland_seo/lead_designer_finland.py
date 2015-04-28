from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

lead_designer = Blueprint('lead_designer', __name__)
job_obj = Job()



####################################################################


@lead_designer.route('/lead-designer_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "lead-designer" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@lead_designer.route('/lead-designer-avoimet-tyopaikat-espoo')
def lead_designer_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("lead designer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="espoo")

@lead_designer.route('/lead-designer-avoimet-tyopaikat-tampere')
def lead_designer_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("lead designer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="tampere")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-vantaa')
def lead_designer_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("lead designer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="vantaa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-turku')
def lead_designer_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("lead designer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="turku")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-oulu')
def lead_designer_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("lead designer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="oulu")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-lahti')
def lead_designer_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("lead designer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lahti")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kuopio')
def lead_designer_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("lead designer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kuopio")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-jyvvaskyla')
def lead_designer_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("lead designer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="jyvvaskyla")

@lead_designer.route('/lead-designer-avoimet-tyopaikat-pori')
def lead_designer_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("lead designer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="pori")

@lead_designer.route('/lead-designer-avoimet-tyopaikat-lappeenranta')
def lead_designer_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("lead designer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lappeenranta")	
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-vaasa')
def lead_designer_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("lead designer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="vaasa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kotka')
def lead_designer_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("lead designer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kotka")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-joensuu')
def lead_designer_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("lead designer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="joensuu")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-hameenlinna')
def lead_designer_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("lead designer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="hameenlinna")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-porvoo')
def lead_designer_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("lead designer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="porvoo")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-mikkeli')
def lead_designer_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("lead designer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="mikkeli")

@lead_designer.route('/lead-designer-avoimet-tyopaikat-hyvinkaa')
def lead_designer_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("lead designer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="hyvinkaa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-nurmijarvi')
def lead_designer_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("lead designer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="nurmijarvi")

@lead_designer.route('/lead-designer-avoimet-tyopaikat-jarvenpaa')
def lead_designer_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("lead designer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="jarvenpaa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-rauma')
def lead_designer_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("lead designer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="rauma")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-lohja')
def lead_designer_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("lead designer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lohja")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-karleby')
def lead_designer_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("lead designer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="karleby")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kajaani')
def lead_designer_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("lead designer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kajaani")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-rovaniemi')
def lead_designer_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("lead designer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="rovaniemi")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-tuusula')
def lead_designer_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("lead designer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="tuusula")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kirkkonummi')
def lead_designer_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("lead designer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kirkkonummi")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-seinajoki')
def lead_designer_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("lead designer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="seinajoki")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kerava')
def lead_designer_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("lead designer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kerava")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kouvola')
def lead_designer_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("lead designer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kouvola")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-imatra')
def lead_designer_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("lead designer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="imatra")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-nokia')
def lead_designer_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("lead designer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="nokia")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-savonlinna')
def lead_designer_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("lead designer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="savonlinna")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-riihimaki')
def lead_designer_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("lead designer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="riihimaki")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-vihti')
def lead_designer_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("lead designer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="vihti")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-salo')
def lead_designer_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("lead designer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="salo")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kangasala')
def lead_designer_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("lead designer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kangasala")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-raisio')
def lead_designer_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("lead designer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="raisio")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-karhula')
def lead_designer_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("lead designer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="karhula")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kemi')
def lead_designer_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("lead designer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kemi")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-iisalmi')
def lead_designer_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("lead designer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="iisalmi")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-varkaus')
def lead_designer_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("lead designer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="varkaus")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-raahe')
def lead_designer_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("lead designer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="raahe")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-ylojarvi')
def lead_designer_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("lead designer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="ylojarvi")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-hamina')
def lead_designer_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("lead designer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="hamina")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kaarina')
def lead_designer_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("lead designer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kaarina")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-tornio')
def lead_designer_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("lead designer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="tornio")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-heinola')
def lead_designer_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("lead designer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="heinola")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-hollola')
def lead_designer_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("lead designer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="hollola")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-valkeakoski')
def lead_designer_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("lead designer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="valkeakoski")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-siilinjarvi')
def lead_designer_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("lead designer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="siilinjarvi")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kuusankoski')
def lead_designer_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("lead designer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kuusankoski")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-sibbo')
def lead_designer_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("lead designer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="sibbo")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-jakostad')
def lead_designer_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("lead designer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="jakostad")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-lempaala')
def lead_designer_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("lead designer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lempaala")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-mantsala')
def lead_designer_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("lead designer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="mantsala")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-forssa')
def lead_designer_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("lead designer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="forssa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kuusamo')
def lead_designer_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("lead designer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kuusamo")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-haukipudas')
def lead_designer_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("lead designer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="haukipudas")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-korsholm')
def lead_designer_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("lead designer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="korsholm")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-laukaa')
def lead_designer_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("lead designer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="laukaa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-anjala')
def lead_designer_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("lead designer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="anjala")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-uusikaupunki')
def lead_designer_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("lead designer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="uusikaupunki")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-janakkala')
def lead_designer_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("lead designer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="janakkala")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-pirkkala')
def lead_designer_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("lead designer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="pirkkala")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-lansi-turunmaa')
def lead_designer_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("lead designer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lansi-turunmaa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-jamsa')
def lead_designer_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("lead designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="jamsa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-jamsa')
def lead_designer_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("lead designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="jamsa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-vammala')
def lead_designer_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("lead designer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="vammala")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-nastola')
def lead_designer_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("lead designer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="nastola")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-orimattila')
def lead_designer_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("lead designer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="orimattila")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kauhajoki')
def lead_designer_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("lead designer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kauhajoki")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-ekenas')
def lead_designer_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("lead designer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="ekenas")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kempele')
def lead_designer_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("lead designer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kempele")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-lapua')
def lead_designer_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("lead designer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lapua")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-lieksa')
def lead_designer_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("lead designer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lieksa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-naantali')
def lead_designer_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("lead designer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="naantali")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-aanekoski')
def lead_designer_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("lead designer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="aanekoski")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-ylivieska')
def lead_designer_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("lead designer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="ylivieska")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kontiolahti')
def lead_designer_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("lead designer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kontiolahti")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kankaanpaa')
def lead_designer_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("lead designer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kankaanpaa")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-ulvila')
def lead_designer_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("lead designer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="ulvila")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-pieksamaki')
def lead_designer_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("lead designer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="pieksamaki")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kiiminki')
def lead_designer_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("lead designer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kiiminki")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-pargas')
def lead_designer_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("lead designer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="pargas")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-nurmo')
def lead_designer_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("lead designer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="nurmo")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-ilmajoki')
def lead_designer_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("lead designer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="ilmajoki")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-liperi')
def lead_designer_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("lead designer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="liperi")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-keuruu')
def lead_designer_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("lead designer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="keuruu")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-leppavirta')
def lead_designer_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("lead designer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="leppavirta")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kurikka')
def lead_designer_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("lead designer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kurikka")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-nivala')
def lead_designer_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("lead designer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="nivala")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-joutseno')
def lead_designer_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("lead designer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="joutseno")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-pedersore')
def lead_designer_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("lead designer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="pedersore")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-sotkamo')
def lead_designer_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("lead designer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="sotkamo")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-kuhmo')
def lead_designer_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("lead designer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kuhmo")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-paimio')
def lead_designer_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("lead designer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="paimio")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-saarijarvi')
def lead_designer_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("lead designer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="saarijarvi")
	
@lead_designer.route('/lead-designer-avoimet-tyopaikat-helsinki')
def lead_designer_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("lead designer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="helsinki")


####################################################################


##############################################
@lead_designer.route('/lead-designer-jobs-espoo')
def lead_designer_jobs2(page=1):

    job_list = job_obj.get_job("lead designer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="espoo")

@lead_designer.route('/lead-designer-jobs-tampere')
def lead_designer_jobs3(page=1):

    job_list = job_obj.get_job("lead designer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="tampere")
	
@lead_designer.route('/lead-designer-jobs-vantaa')
def lead_designer_jobs4(page=1):

    job_list = job_obj.get_job("lead designer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="vantaa")
	
@lead_designer.route('/lead-designer-jobs-turku')
def lead_designer_jobs5(page=1):

    job_list = job_obj.get_job("lead designer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="turku")
	
@lead_designer.route('/lead-designer-jobs-oulu')
def lead_designer_jobs6(page=1):

    job_list = job_obj.get_job("lead designer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="oulu")
	
@lead_designer.route('/lead-designer-jobs-lahti')
def lead_designer_jobs7(page=1):

    job_list = job_obj.get_job("lead designer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lahti")
	
@lead_designer.route('/lead-designer-jobs-kuopio')
def lead_designer_jobs8(page=1):

    job_list = job_obj.get_job("lead designer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kuopio")
	
@lead_designer.route('/lead-designer-jobs-jyvvaskyla')
def lead_designer_jobs9(page=1):

    job_list = job_obj.get_job("lead designer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="jyvvaskyla")

@lead_designer.route('/lead-designer-jobs-pori')
def lead_designer_jobs10(page=1):

    job_list = job_obj.get_job("lead designer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="pori")

@lead_designer.route('/lead-designer-jobs-lappeenranta')
def lead_designer_jobs11(page=1):

    job_list = job_obj.get_job("lead designer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lappeenranta")	
	
@lead_designer.route('/lead-designer-jobs-vaasa')
def lead_designer_jobs12(page=1):

    job_list = job_obj.get_job("lead designer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="vaasa")
	
@lead_designer.route('/lead-designer-jobs-kotka')
def lead_designer_jobs13(page=1):

    job_list = job_obj.get_job("lead designer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kotka")
	
@lead_designer.route('/lead-designer-jobs-joensuu')
def lead_designer_jobs14(page=1):

    job_list = job_obj.get_job("lead designer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="joensuu")
	
@lead_designer.route('/lead-designer-jobs-hameenlinna')
def lead_designer_jobs15(page=1):

    job_list = job_obj.get_job("lead designer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="hameenlinna")
	
@lead_designer.route('/lead-designer-jobs-porvoo')
def lead_designer_jobs16(page=1):

    job_list = job_obj.get_job("lead designer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="porvoo")
	
@lead_designer.route('/lead-designer-jobs-mikkeli')
def lead_designer_jobs17(page=1):

    job_list = job_obj.get_job("lead designer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="mikkeli")

@lead_designer.route('/lead-designer-jobs-hyvinkaa')
def lead_designer_jobs18(page=1):

    job_list = job_obj.get_job("lead designer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="hyvinkaa")
	
@lead_designer.route('/lead-designer-jobs-nurmijarvi')
def lead_designer_jobs19(page=1):

    job_list = job_obj.get_job("lead designer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="nurmijarvi")

@lead_designer.route('/lead-designer-jobs-jarvenpaa')
def lead_designer_jobs20(page=1):

    job_list = job_obj.get_job("lead designer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="jarvenpaa")
	
@lead_designer.route('/lead-designer-jobs-rauma')
def lead_designer_jobs21(page=1):

    job_list = job_obj.get_job("lead designer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="rauma")
	
@lead_designer.route('/lead-designer-jobs-lohja')
def lead_designer_jobs22(page=1):

    job_list = job_obj.get_job("lead designer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lohja")
	
@lead_designer.route('/lead-designer-jobs-karleby')
def lead_designer_jobs23(page=1):

    job_list = job_obj.get_job("lead designer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="karleby")
	
@lead_designer.route('/lead-designer-jobs-kajaani')
def lead_designer_jobs24(page=1):

    job_list = job_obj.get_job("lead designer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kajaani")
	
@lead_designer.route('/lead-designer-jobs-rovaniemi')
def lead_designer_jobs25(page=1):

    job_list = job_obj.get_job("lead designer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="rovaniemi")
	
@lead_designer.route('/lead-designer-jobs-tuusula')
def lead_designer_jobs26(page=1):

    job_list = job_obj.get_job("lead designer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="tuusula")
	
@lead_designer.route('/lead-designer-jobs-kirkkonummi')
def lead_designer_jobs27(page=1):

    job_list = job_obj.get_job("lead designer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kirkkonummi")
	
@lead_designer.route('/lead-designer-jobs-seinajoki')
def lead_designer_jobs28(page=1):

    job_list = job_obj.get_job("lead designer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="seinajoki")
	
@lead_designer.route('/lead-designer-jobs-kerava')
def lead_designer_jobs29(page=1):

    job_list = job_obj.get_job("lead designer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kerava")
	
@lead_designer.route('/lead-designer-jobs-kouvola')
def lead_designer_jobs30(page=1):

    job_list = job_obj.get_job("lead designer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kouvola")
	
@lead_designer.route('/lead-designer-jobs-imatra')
def lead_designer_jobs31(page=1):

    job_list = job_obj.get_job("lead designer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="imatra")
	
@lead_designer.route('/lead-designer-jobs-nokia')
def lead_designer_jobs32_1(page=1):

    job_list = job_obj.get_job("lead designer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="nokia")
	
@lead_designer.route('/lead-designer-jobs-savonlinna')
def lead_designer_jobs32(page=1):

    job_list = job_obj.get_job("lead designer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="savonlinna")
	
@lead_designer.route('/lead-designer-jobs-riihimaki')
def lead_designer_jobs33(page=1):

    job_list = job_obj.get_job("lead designer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="riihimaki")
	
@lead_designer.route('/lead-designer-jobs-vihti')
def lead_designer_jobs34(page=1):

    job_list = job_obj.get_job("lead designer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="vihti")
	
@lead_designer.route('/lead-designer-jobs-salo')
def lead_designer_jobs35(page=1):

    job_list = job_obj.get_job("lead designer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="salo")
	
@lead_designer.route('/lead-designer-jobs-kangasala')
def lead_designer_jobs36(page=1):

    job_list = job_obj.get_job("lead designer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kangasala")
	
@lead_designer.route('/lead-designer-jobs-raisio')
def lead_designer_jobs37_1(page=1):

    job_list = job_obj.get_job("lead designer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="raisio")
	
@lead_designer.route('/lead-designer-jobs-karhula')
def lead_designer_jobs37(page=1):

    job_list = job_obj.get_job("lead designer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="karhula")
	
@lead_designer.route('/lead-designer-jobs-kemi')
def lead_designer_jobs38(page=1):

    job_list = job_obj.get_job("lead designer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kemi")
	
@lead_designer.route('/lead-designer-jobs-iisalmi')
def lead_designer_jobs39(page=1):

    job_list = job_obj.get_job("lead designer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="iisalmi")
	
@lead_designer.route('/lead-designer-jobs-varkaus')
def lead_designer_jobs40(page=1):

    job_list = job_obj.get_job("lead designer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="varkaus")
	
@lead_designer.route('/lead-designer-jobs-raahe')
def lead_designer_jobs41(page=1):

    job_list = job_obj.get_job("lead designer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="raahe")
	
@lead_designer.route('/lead-designer-jobs-ylojarvi')
def lead_designer_jobs42_1(page=1):

    job_list = job_obj.get_job("lead designer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="ylojarvi")
	
@lead_designer.route('/lead-designer-jobs-hamina')
def lead_designer_jobs42(page=1):

    job_list = job_obj.get_job("lead designer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="hamina")
	
@lead_designer.route('/lead-designer-jobs-kaarina')
def lead_designer_jobs43(page=1):

    job_list = job_obj.get_job("lead designer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kaarina")
	
@lead_designer.route('/lead-designer-jobs-tornio')
def lead_designer_jobs44(page=1):

    job_list = job_obj.get_job("lead designer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="tornio")
	
@lead_designer.route('/lead-designer-jobs-heinola')
def lead_designer_jobs45(page=1):

    job_list = job_obj.get_job("lead designer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="heinola")
	
@lead_designer.route('/lead-designer-jobs-hollola')
def lead_designer_jobs46(page=1):

    job_list = job_obj.get_job("lead designer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="hollola")
	
@lead_designer.route('/lead-designer-jobs-valkeakoski')
def lead_designer_jobs47(page=1):

    job_list = job_obj.get_job("lead designer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="valkeakoski")
	
@lead_designer.route('/lead-designer-jobs-siilinjarvi')
def lead_designer_jobs48(page=1):

    job_list = job_obj.get_job("lead designer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="siilinjarvi")
	
@lead_designer.route('/lead-designer-jobs-kuusankoski')
def lead_designer_jobs49(page=1):

    job_list = job_obj.get_job("lead designer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kuusankoski")
	
@lead_designer.route('/lead-designer-jobs-sibbo')
def lead_designer_jobs50(page=1):

    job_list = job_obj.get_job("lead designer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="sibbo")
	
@lead_designer.route('/lead-designer-jobs-jakostad')
def lead_designer_jobs51(page=1):

    job_list = job_obj.get_job("lead designer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="jakostad")
	
@lead_designer.route('/lead-designer-jobs-lempaala')
def lead_designer_jobs52(page=1):

    job_list = job_obj.get_job("lead designer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lempaala")
	
@lead_designer.route('/lead-designer-jobs-mantsala')
def lead_designer_jobs52_1(page=1):

    job_list = job_obj.get_job("lead designer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="mantsala")
	
@lead_designer.route('/lead-designer-jobs-forssa')
def lead_designer_jobs53(page=1):

    job_list = job_obj.get_job("lead designer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="forssa")
	
@lead_designer.route('/lead-designer-jobs-kuusamo')
def lead_designer_jobs54(page=1):

    job_list = job_obj.get_job("lead designer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kuusamo")
	
@lead_designer.route('/lead-designer-jobs-haukipudas')
def lead_designer_jobs55(page=1):

    job_list = job_obj.get_job("lead designer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="haukipudas")
	
@lead_designer.route('/lead-designer-jobs-korsholm')
def lead_designer_jobs56(page=1):

    job_list = job_obj.get_job("lead designer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="korsholm")
	
@lead_designer.route('/lead-designer-jobs-laukaa')
def lead_designer_jobs57(page=1):

    job_list = job_obj.get_job("lead designer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="laukaa")
	
@lead_designer.route('/lead-designer-jobs-anjala')
def lead_designer_jobs58(page=1):

    job_list = job_obj.get_job("lead designer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="anjala")
	
@lead_designer.route('/lead-designer-jobs-uusikaupunki')
def lead_designer_jobs59(page=1):

    job_list = job_obj.get_job("lead designer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="uusikaupunki")
	
@lead_designer.route('/lead-designer-jobs-janakkala')
def lead_designer_jobs60(page=1):

    job_list = job_obj.get_job("lead designer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="janakkala")
	
@lead_designer.route('/lead-designer-jobs-pirkkala')
def lead_designer_jobs61(page=1):

    job_list = job_obj.get_job("lead designer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="pirkkala")
	
@lead_designer.route('/lead-designer-jobs-lansi-turunmaa')
def lead_designer_jobs62(page=1):

    job_list = job_obj.get_job("lead designer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lansi-turunmaa")
	
@lead_designer.route('/lead-designer-jobs-jamsa')
def lead_designer_jobs63(page=1):

    job_list = job_obj.get_job("lead designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="jamsa")
	
@lead_designer.route('/lead-designer-jobs-jamsa')
def lead_designer_jobs64(page=1):

    job_list = job_obj.get_job("lead designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="jamsa")
	
@lead_designer.route('/lead-designer-jobs-vammala')
def lead_designer_jobs65(page=1):

    job_list = job_obj.get_job("lead designer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="vammala")
	
@lead_designer.route('/lead-designer-jobs-nastola')
def lead_designer_jobs66(page=1):

    job_list = job_obj.get_job("lead designer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="nastola")
	
@lead_designer.route('/lead-designer-jobs-orimattila')
def lead_designer_jobs67(page=1):

    job_list = job_obj.get_job("lead designer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="orimattila")
	
@lead_designer.route('/lead-designer-jobs-kauhajoki')
def lead_designer_jobs68(page=1):

    job_list = job_obj.get_job("lead designer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kauhajoki")
	
@lead_designer.route('/lead-designer-jobs-ekenas')
def lead_designer_jobs69(page=1):

    job_list = job_obj.get_job("lead designer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="ekenas")
	
@lead_designer.route('/lead-designer-jobs-kempele')
def lead_designer_jobs70(page=1):

    job_list = job_obj.get_job("lead designer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kempele")
	
@lead_designer.route('/lead-designer-jobs-lapua')
def lead_designer_jobs71(page=1):

    job_list = job_obj.get_job("lead designer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lapua")
	
@lead_designer.route('/lead-designer-jobs-lieksa')
def lead_designer_jobs72(page=1):

    job_list = job_obj.get_job("lead designer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="lieksa")
	
@lead_designer.route('/lead-designer-jobs-naantali')
def lead_designer_jobs73(page=1):

    job_list = job_obj.get_job("lead designer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="naantali")
	
@lead_designer.route('/lead-designer-jobs-aanekoski')
def lead_designer_jobs74(page=1):

    job_list = job_obj.get_job("lead designer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="aanekoski")
	
@lead_designer.route('/lead-designer-jobs-ylivieska')
def lead_designer_jobs75(page=1):

    job_list = job_obj.get_job("lead designer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="ylivieska")
	
@lead_designer.route('/lead-designer-jobs-kontiolahti')
def lead_designer_jobs76(page=1):

    job_list = job_obj.get_job("lead designer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kontiolahti")
	
@lead_designer.route('/lead-designer-jobs-kankaanpaa')
def lead_designer_jobs77(page=1):

    job_list = job_obj.get_job("lead designer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kankaanpaa")
	
@lead_designer.route('/lead-designer-jobs-ulvila')
def lead_designer_jobs78(page=1):

    job_list = job_obj.get_job("lead designer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="ulvila")
	
@lead_designer.route('/lead-designer-jobs-pieksamaki')
def lead_designer_jobs79(page=1):

    job_list = job_obj.get_job("lead designer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="pieksamaki")
	
@lead_designer.route('/lead-designer-jobs-kiiminki')
def lead_designer_jobs80(page=1):

    job_list = job_obj.get_job("lead designer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kiiminki")
	
@lead_designer.route('/lead-designer-jobs-pargas')
def lead_designer_jobs81(page=1):

    job_list = job_obj.get_job("lead designer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="pargas")
	
@lead_designer.route('/lead-designer-jobs-nurmo')
def lead_designer_jobs82(page=1):

    job_list = job_obj.get_job("lead designer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="nurmo")
	
@lead_designer.route('/lead-designer-jobs-ilmajoki')
def lead_designer_jobs83(page=1):

    job_list = job_obj.get_job("lead designer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="ilmajoki")
	
@lead_designer.route('/lead-designer-jobs-liperi')
def lead_designer_jobs84(page=1):

    job_list = job_obj.get_job("lead designer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="liperi")
	
@lead_designer.route('/lead-designer-jobs-keuruu')
def lead_designer_jobs85(page=1):

    job_list = job_obj.get_job("lead designer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="keuruu")
	
@lead_designer.route('/lead-designer-jobs-leppavirta')
def lead_designer_jobs86(page=1):

    job_list = job_obj.get_job("lead designer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="leppavirta")
	
@lead_designer.route('/lead-designer-jobs-kurikka')
def lead_designer_jobs87(page=1):

    job_list = job_obj.get_job("lead designer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kurikka")
	
@lead_designer.route('/lead-designer-jobs-nivala')
def lead_designer_jobs88(page=1):

    job_list = job_obj.get_job("lead designer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="nivala")
	
@lead_designer.route('/lead-designer-jobs-joutseno')
def lead_designer_jobs89(page=1):

    job_list = job_obj.get_job("lead designer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="joutseno")
	
@lead_designer.route('/lead-designer-jobs-pedersore')
def lead_designer_jobs90(page=1):

    job_list = job_obj.get_job("lead designer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="pedersore")
	
@lead_designer.route('/lead-designer-jobs-sotkamo')
def lead_designer_jobs91(page=1):

    job_list = job_obj.get_job("lead designer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="sotkamo")
	
@lead_designer.route('/lead-designer-jobs-kuhmo')
def lead_designer_jobs92(page=1):

    job_list = job_obj.get_job("lead designer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="kuhmo")
	
@lead_designer.route('/lead-designer-jobs-paimio')
def lead_designer_jobs93(page=1):

    job_list = job_obj.get_job("lead designer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="paimio")
	
@lead_designer.route('/lead-designer-jobs-saarijarvi')
def lead_designer_jobs94(page=1):

    job_list = job_obj.get_job("lead designer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="saarijarvi")
	
@lead_designer.route('/lead-designer-jobs-helsinki')
def lead_designer_jobs95(page=1):

    job_list = job_obj.get_job("lead designer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer ", location="helsinki")


####################################################################


##############################################
@lead_designer.route('/lead-designer-tyopaikat-espoo')
def lead_designer_tyopaikat2(page=1):

    job_list = job_obj.get_job("lead designer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="espoo")

@lead_designer.route('/lead-designer-tyopaikat-tampere')
def lead_designer_tyopaikat3(page=1):

    job_list = job_obj.get_job("lead designer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="tampere")
	
@lead_designer.route('/lead-designer-tyopaikat-vantaa')
def lead_designer_tyopaikat4(page=1):

    job_list = job_obj.get_job("lead designer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="vantaa")
	
@lead_designer.route('/lead-designer-tyopaikat-turku')
def lead_designer_tyopaikat5(page=1):

    job_list = job_obj.get_job("lead designer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="turku")
	
@lead_designer.route('/lead-designer-tyopaikat-oulu')
def lead_designer_tyopaikat6(page=1):

    job_list = job_obj.get_job("lead designer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="oulu")
	
@lead_designer.route('/lead-designer-tyopaikat-lahti')
def lead_designer_tyopaikat7(page=1):

    job_list = job_obj.get_job("lead designer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="lahti")
	
@lead_designer.route('/lead-designer-tyopaikat-kuopio')
def lead_designer_tyopaikat8(page=1):

    job_list = job_obj.get_job("lead designer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kuopio")
	
@lead_designer.route('/lead-designer-tyopaikat-jyvvaskyla')
def lead_designer_tyopaikat9(page=1):

    job_list = job_obj.get_job("lead designer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="jyvvaskyla")

@lead_designer.route('/lead-designer-tyopaikat-pori')
def lead_designer_tyopaikat10(page=1):

    job_list = job_obj.get_job("lead designer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="pori")

@lead_designer.route('/lead-designer-tyopaikat-lappeenranta')
def lead_designer_tyopaikat11(page=1):

    job_list = job_obj.get_job("lead designer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="lappeenranta")	
	
@lead_designer.route('/lead-designer-tyopaikat-vaasa')
def lead_designer_tyopaikat12(page=1):

    job_list = job_obj.get_job("lead designer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="vaasa")
	
@lead_designer.route('/lead-designer-tyopaikat-kotka')
def lead_designer_tyopaikat13(page=1):

    job_list = job_obj.get_job("lead designer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kotka")
	
@lead_designer.route('/lead-designer-tyopaikat-joensuu')
def lead_designer_tyopaikat14(page=1):

    job_list = job_obj.get_job("lead designer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="joensuu")
	
@lead_designer.route('/lead-designer-tyopaikat-hameenlinna')
def lead_designer_tyopaikat15(page=1):

    job_list = job_obj.get_job("lead designer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="hameenlinna")
	
@lead_designer.route('/lead-designer-tyopaikat-porvoo')
def lead_designer_tyopaikat16(page=1):

    job_list = job_obj.get_job("lead designer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="porvoo")
	
@lead_designer.route('/lead-designer-tyopaikat-mikkeli')
def lead_designer_tyopaikat17(page=1):

    job_list = job_obj.get_job("lead designer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="mikkeli")

@lead_designer.route('/lead-designer-tyopaikat-hyvinkaa')
def lead_designer_tyopaikat18(page=1):

    job_list = job_obj.get_job("lead designer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="hyvinkaa")
	
@lead_designer.route('/lead-designer-tyopaikat-nurmijarvi')
def lead_designer_tyopaikat19(page=1):

    job_list = job_obj.get_job("lead designer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="nurmijarvi")

@lead_designer.route('/lead-designer-tyopaikat-jarvenpaa')
def lead_designer_tyopaikat20(page=1):

    job_list = job_obj.get_job("lead designer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="jarvenpaa")
	
@lead_designer.route('/lead-designer-tyopaikat-rauma')
def lead_designer_tyopaikat21(page=1):

    job_list = job_obj.get_job("lead designer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="rauma")
	
@lead_designer.route('/lead-designer-tyopaikat-lohja')
def lead_designer_tyopaikat22(page=1):

    job_list = job_obj.get_job("lead designer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="lohja")
	
@lead_designer.route('/lead-designer-tyopaikat-karleby')
def lead_designer_tyopaikat23(page=1):

    job_list = job_obj.get_job("lead designer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="karleby")
	
@lead_designer.route('/lead-designer-tyopaikat-kajaani')
def lead_designer_tyopaikat24(page=1):

    job_list = job_obj.get_job("lead designer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kajaani")
	
@lead_designer.route('/lead-designer-tyopaikat-rovaniemi')
def lead_designer_tyopaikat25(page=1):

    job_list = job_obj.get_job("lead designer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="rovaniemi")
	
@lead_designer.route('/lead-designer-tyopaikat-tuusula')
def lead_designer_tyopaikat26(page=1):

    job_list = job_obj.get_job("lead designer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="tuusula")
	
@lead_designer.route('/lead-designer-tyopaikat-kirkkonummi')
def lead_designer_tyopaikat27(page=1):

    job_list = job_obj.get_job("lead designer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kirkkonummi")
	
@lead_designer.route('/lead-designer-tyopaikat-seinajoki')
def lead_designer_tyopaikat28(page=1):

    job_list = job_obj.get_job("lead designer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="seinajoki")
	
@lead_designer.route('/lead-designer-tyopaikat-kerava')
def lead_designer_tyopaikat29(page=1):

    job_list = job_obj.get_job("lead designer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kerava")
	
@lead_designer.route('/lead-designer-tyopaikat-kouvola')
def lead_designer_tyopaikat30(page=1):

    job_list = job_obj.get_job("lead designer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kouvola")
	
@lead_designer.route('/lead-designer-tyopaikat-imatra')
def lead_designer_tyopaikat31(page=1):

    job_list = job_obj.get_job("lead designer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="imatra")
	
@lead_designer.route('/lead-designer-tyopaikat-nokia')
def lead_designer_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("lead designer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="nokia")
	
@lead_designer.route('/lead-designer-tyopaikat-savonlinna')
def lead_designer_tyopaikat32(page=1):

    job_list = job_obj.get_job("lead designer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="savonlinna")
	
@lead_designer.route('/lead-designer-tyopaikat-riihimaki')
def lead_designer_tyopaikat33(page=1):

    job_list = job_obj.get_job("lead designer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="riihimaki")
	
@lead_designer.route('/lead-designer-tyopaikat-vihti')
def lead_designer_tyopaikat34(page=1):

    job_list = job_obj.get_job("lead designer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="vihti")
	
@lead_designer.route('/lead-designer-tyopaikat-salo')
def lead_designer_tyopaikat35(page=1):

    job_list = job_obj.get_job("lead designer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="salo")
	
@lead_designer.route('/lead-designer-tyopaikat-kangasala')
def lead_designer_tyopaikat36(page=1):

    job_list = job_obj.get_job("lead designer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kangasala")
	
@lead_designer.route('/lead-designer-tyopaikat-raisio')
def lead_designer_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("lead designer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="raisio")
	
@lead_designer.route('/lead-designer-tyopaikat-karhula')
def lead_designer_tyopaikat37(page=1):

    job_list = job_obj.get_job("lead designer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="karhula")
	
@lead_designer.route('/lead-designer-tyopaikat-kemi')
def lead_designer_tyopaikat38(page=1):

    job_list = job_obj.get_job("lead designer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kemi")
	
@lead_designer.route('/lead-designer-tyopaikat-iisalmi')
def lead_designer_tyopaikat39(page=1):

    job_list = job_obj.get_job("lead designer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="iisalmi")
	
@lead_designer.route('/lead-designer-tyopaikat-varkaus')
def lead_designer_tyopaikat40(page=1):

    job_list = job_obj.get_job("lead designer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="varkaus")
	
@lead_designer.route('/lead-designer-tyopaikat-raahe')
def lead_designer_tyopaikat41(page=1):

    job_list = job_obj.get_job("lead designer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="raahe")
	
@lead_designer.route('/lead-designer-tyopaikat-ylojarvi')
def lead_designer_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("lead designer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="ylojarvi")
	
@lead_designer.route('/lead-designer-tyopaikat-hamina')
def lead_designer_tyopaikat42(page=1):

    job_list = job_obj.get_job("lead designer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="hamina")
	
@lead_designer.route('/lead-designer-tyopaikat-kaarina')
def lead_designer_tyopaikat43(page=1):

    job_list = job_obj.get_job("lead designer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kaarina")
	
@lead_designer.route('/lead-designer-tyopaikat-tornio')
def lead_designer_tyopaikat44(page=1):

    job_list = job_obj.get_job("lead designer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="tornio")
	
@lead_designer.route('/lead-designer-tyopaikat-heinola')
def lead_designer_tyopaikat45(page=1):

    job_list = job_obj.get_job("lead designer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="heinola")
	
@lead_designer.route('/lead-designer-tyopaikat-hollola')
def lead_designer_tyopaikat46(page=1):

    job_list = job_obj.get_job("lead designer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="hollola")
	
@lead_designer.route('/lead-designer-tyopaikat-valkeakoski')
def lead_designer_tyopaikat47(page=1):

    job_list = job_obj.get_job("lead designer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="valkeakoski")
	
@lead_designer.route('/lead-designer-tyopaikat-siilinjarvi')
def lead_designer_tyopaikat48(page=1):

    job_list = job_obj.get_job("lead designer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="siilinjarvi")
	
@lead_designer.route('/lead-designer-tyopaikat-kuusankoski')
def lead_designer_tyopaikat49(page=1):

    job_list = job_obj.get_job("lead designer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kuusankoski")
	
@lead_designer.route('/lead-designer-tyopaikat-sibbo')
def lead_designer_tyopaikat50(page=1):

    job_list = job_obj.get_job("lead designer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="sibbo")
	
@lead_designer.route('/lead-designer-tyopaikat-jakostad')
def lead_designer_tyopaikat51(page=1):

    job_list = job_obj.get_job("lead designer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="jakostad")
	
@lead_designer.route('/lead-designer-tyopaikat-lempaala')
def lead_designer_tyopaikat52(page=1):

    job_list = job_obj.get_job("lead designer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="lempaala")
	
@lead_designer.route('/lead-designer-tyopaikat-mantsala')
def lead_designer_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("lead designer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="mantsala")
	
@lead_designer.route('/lead-designer-tyopaikat-forssa')
def lead_designer_tyopaikat53(page=1):

    job_list = job_obj.get_job("lead designer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="forssa")
	
@lead_designer.route('/lead-designer-tyopaikat-kuusamo')
def lead_designer_tyopaikat54(page=1):

    job_list = job_obj.get_job("lead designer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kuusamo")
	
@lead_designer.route('/lead-designer-tyopaikat-haukipudas')
def lead_designer_tyopaikat55(page=1):

    job_list = job_obj.get_job("lead designer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="haukipudas")
	
@lead_designer.route('/lead-designer-tyopaikat-korsholm')
def lead_designer_tyopaikat56(page=1):

    job_list = job_obj.get_job("lead designer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="korsholm")
	
@lead_designer.route('/lead-designer-tyopaikat-laukaa')
def lead_designer_tyopaikat57(page=1):

    job_list = job_obj.get_job("lead designer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="laukaa")
	
@lead_designer.route('/lead-designer-tyopaikat-anjala')
def lead_designer_tyopaikat58(page=1):

    job_list = job_obj.get_job("lead designer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="anjala")
	
@lead_designer.route('/lead-designer-tyopaikat-uusikaupunki')
def lead_designer_tyopaikat59(page=1):

    job_list = job_obj.get_job("lead designer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="uusikaupunki")
	
@lead_designer.route('/lead-designer-tyopaikat-janakkala')
def lead_designer_tyopaikat60(page=1):

    job_list = job_obj.get_job("lead designer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="janakkala")
	
@lead_designer.route('/lead-designer-tyopaikat-pirkkala')
def lead_designer_tyopaikat61(page=1):

    job_list = job_obj.get_job("lead designer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="pirkkala")
	
@lead_designer.route('/lead-designer-tyopaikat-lansi-turunmaa')
def lead_designer_tyopaikat62(page=1):

    job_list = job_obj.get_job("lead designer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="lansi-turunmaa")
	
@lead_designer.route('/lead-designer-tyopaikat-jamsa')
def lead_designer_tyopaikat63(page=1):

    job_list = job_obj.get_job("lead designer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="jamsa")
	
@lead_designer.route('/lead-designer-tyopaikat-jamsa')
def lead_designer_tyopaikat64(page=1):

    job_list = job_obj.get_job("lead designer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="jamsa")
	
@lead_designer.route('/lead-designer-tyopaikat-vammala')
def lead_designer_tyopaikat65(page=1):

    job_list = job_obj.get_job("lead designer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="vammala")
	
@lead_designer.route('/lead-designer-tyopaikat-nastola')
def lead_designer_tyopaikat66(page=1):

    job_list = job_obj.get_job("lead designer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="nastola")
	
@lead_designer.route('/lead-designer-tyopaikat-orimattila')
def lead_designer_tyopaikat67(page=1):

    job_list = job_obj.get_job("lead designer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="orimattila")
	
@lead_designer.route('/lead-designer-tyopaikat-kauhajoki')
def lead_designer_tyopaikat68(page=1):

    job_list = job_obj.get_job("lead designer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kauhajoki")
	
@lead_designer.route('/lead-designer-tyopaikat-ekenas')
def lead_designer_tyopaikat69(page=1):

    job_list = job_obj.get_job("lead designer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="ekenas")
	
@lead_designer.route('/lead-designer-tyopaikat-kempele')
def lead_designer_tyopaikat70(page=1):

    job_list = job_obj.get_job("lead designer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kempele")
	
@lead_designer.route('/lead-designer-tyopaikat-lapua')
def lead_designer_tyopaikat71(page=1):

    job_list = job_obj.get_job("lead designer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="lapua")
	
@lead_designer.route('/lead-designer-tyopaikat-lieksa')
def lead_designer_tyopaikat72(page=1):

    job_list = job_obj.get_job("lead designer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="lieksa")
	
@lead_designer.route('/lead-designer-tyopaikat-naantali')
def lead_designer_tyopaikat73(page=1):

    job_list = job_obj.get_job("lead designer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="naantali")
	
@lead_designer.route('/lead-designer-tyopaikat-aanekoski')
def lead_designer_tyopaikat74(page=1):

    job_list = job_obj.get_job("lead designer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="aanekoski")
	
@lead_designer.route('/lead-designer-tyopaikat-ylivieska')
def lead_designer_tyopaikat75(page=1):

    job_list = job_obj.get_job("lead designer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="ylivieska")
	
@lead_designer.route('/lead-designer-tyopaikat-kontiolahti')
def lead_designer_tyopaikat76(page=1):

    job_list = job_obj.get_job("lead designer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kontiolahti")
	
@lead_designer.route('/lead-designer-tyopaikat-kankaanpaa')
def lead_designer_tyopaikat77(page=1):

    job_list = job_obj.get_job("lead designer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kankaanpaa")
	
@lead_designer.route('/lead-designer-tyopaikat-ulvila')
def lead_designer_tyopaikat78(page=1):

    job_list = job_obj.get_job("lead designer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="ulvila")
	
@lead_designer.route('/lead-designer-tyopaikat-pieksamaki')
def lead_designer_tyopaikat79(page=1):

    job_list = job_obj.get_job("lead designer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="pieksamaki")
	
@lead_designer.route('/lead-designer-tyopaikat-kiiminki')
def lead_designer_tyopaikat80(page=1):

    job_list = job_obj.get_job("lead designer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kiiminki")
	
@lead_designer.route('/lead-designer-tyopaikat-pargas')
def lead_designer_tyopaikat81(page=1):

    job_list = job_obj.get_job("lead designer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="pargas")
	
@lead_designer.route('/lead-designer-tyopaikat-nurmo')
def lead_designer_tyopaikat82(page=1):

    job_list = job_obj.get_job("lead designer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="nurmo")
	
@lead_designer.route('/lead-designer-tyopaikat-ilmajoki')
def lead_designer_tyopaikat83(page=1):

    job_list = job_obj.get_job("lead designer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="ilmajoki")
	
@lead_designer.route('/lead-designer-tyopaikat-liperi')
def lead_designer_tyopaikat84(page=1):

    job_list = job_obj.get_job("lead designer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="liperi")
	
@lead_designer.route('/lead-designer-tyopaikat-keuruu')
def lead_designer_tyopaikat85(page=1):

    job_list = job_obj.get_job("lead designer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="keuruu")
	
@lead_designer.route('/lead-designer-tyopaikat-leppavirta')
def lead_designer_tyopaikat86(page=1):

    job_list = job_obj.get_job("lead designer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="leppavirta")
	
@lead_designer.route('/lead-designer-tyopaikat-kurikka')
def lead_designer_tyopaikat87(page=1):

    job_list = job_obj.get_job("lead designer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kurikka")
	
@lead_designer.route('/lead-designer-tyopaikat-nivala')
def lead_designer_tyopaikat88(page=1):

    job_list = job_obj.get_job("lead designer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="nivala")
	
@lead_designer.route('/lead-designer-tyopaikat-joutseno')
def lead_designer_tyopaikat89(page=1):

    job_list = job_obj.get_job("lead designer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="joutseno")
	
@lead_designer.route('/lead-designer-tyopaikat-pedersore')
def lead_designer_tyopaikat90(page=1):

    job_list = job_obj.get_job("lead designer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="pedersore")
	
@lead_designer.route('/lead-designer-tyopaikat-sotkamo')
def lead_designer_tyopaikat91(page=1):

    job_list = job_obj.get_job("lead designer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="sotkamo")
	
@lead_designer.route('/lead-designer-tyopaikat-kuhmo')
def lead_designer_tyopaikat92(page=1):

    job_list = job_obj.get_job("lead designer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="kuhmo")
	
@lead_designer.route('/lead-designer-tyopaikat-paimio')
def lead_designer_tyopaikat93(page=1):

    job_list = job_obj.get_job("lead designer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="paimio")
	
@lead_designer.route('/lead-designer-tyopaikat-saarijarvi')
def lead_designer_tyopaikat94(page=1):

    job_list = job_obj.get_job("lead designer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer", location="saarijarvi")
	
@lead_designer.route('/lead-designer-tyopaikat-helsinki')
def lead_designer_tyopaikat95(page=1):

    job_list = job_obj.get_job("lead designer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="lead designer  ", location="helsinki")
	  

