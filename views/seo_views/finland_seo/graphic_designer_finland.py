from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

graphic_designer = Blueprint('graphic_designer', __name__)
job_obj = Job()



####################################################################


@graphic_designer.route('/graphic-designer_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "graphic-designer" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-espoo')
def graphic_designer_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("graphic designer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="espoo")

@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-tampere')
def graphic_designer_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("graphic designer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="tampere")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-vantaa')
def graphic_designer_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("graphic designer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="vantaa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-turku')
def graphic_designer_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("graphic designer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="turku")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-oulu')
def graphic_designer_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("graphic designer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="oulu")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-lahti')
def graphic_designer_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("graphic designer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lahti")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kuopio')
def graphic_designer_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("graphic designer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kuopio")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-jyvvaskyla')
def graphic_designer_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("graphic designer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="jyvvaskyla")

@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-pori')
def graphic_designer_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("graphic designer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="pori")

@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-lappeenranta')
def graphic_designer_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("graphic designer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lappeenranta")	
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-vaasa')
def graphic_designer_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("graphic designer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="vaasa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kotka')
def graphic_designer_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("graphic designer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kotka")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-joensuu')
def graphic_designer_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("graphic designer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="joensuu")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-hameenlinna')
def graphic_designer_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("graphic designer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="hameenlinna")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-porvoo')
def graphic_designer_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("graphic designer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="porvoo")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-mikkeli')
def graphic_designer_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("graphic designer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="mikkeli")

@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-hyvinkaa')
def graphic_designer_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("graphic designer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="hyvinkaa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-nurmijarvi')
def graphic_designer_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("graphic designer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="nurmijarvi")

@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-jarvenpaa')
def graphic_designer_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("graphic designer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="jarvenpaa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-rauma')
def graphic_designer_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("graphic designer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="rauma")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-lohja')
def graphic_designer_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("graphic designer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lohja")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-karleby')
def graphic_designer_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("graphic designer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="karleby")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kajaani')
def graphic_designer_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("graphic designer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kajaani")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-rovaniemi')
def graphic_designer_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("graphic designer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="rovaniemi")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-tuusula')
def graphic_designer_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("graphic designer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="tuusula")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kirkkonummi')
def graphic_designer_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("graphic designer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kirkkonummi")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-seinajoki')
def graphic_designer_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("graphic designer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="seinajoki")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kerava')
def graphic_designer_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("graphic designer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kerava")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kouvola')
def graphic_designer_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("graphic designer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kouvola")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-imatra')
def graphic_designer_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("graphic designer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="imatra")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-nokia')
def graphic_designer_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("graphic designer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="nokia")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-savonlinna')
def graphic_designer_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("graphic designer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="savonlinna")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-riihimaki')
def graphic_designer_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("graphic designer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="riihimaki")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-vihti')
def graphic_designer_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("graphic designer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="vihti")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-salo')
def graphic_designer_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("graphic designer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="salo")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kangasala')
def graphic_designer_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("graphic designer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kangasala")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-raisio')
def graphic_designer_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("graphic designer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="raisio")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-karhula')
def graphic_designer_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("graphic designer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="karhula")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kemi')
def graphic_designer_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("graphic designer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kemi")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-iisalmi')
def graphic_designer_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("graphic designer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="iisalmi")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-varkaus')
def graphic_designer_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("graphic designer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="varkaus")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-raahe')
def graphic_designer_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("graphic designer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="raahe")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-ylojarvi')
def graphic_designer_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("graphic designer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="ylojarvi")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-hamina')
def graphic_designer_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("graphic designer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="hamina")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kaarina')
def graphic_designer_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("graphic designer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kaarina")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-tornio')
def graphic_designer_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("graphic designer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="tornio")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-heinola')
def graphic_designer_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("graphic designer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="heinola")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-hollola')
def graphic_designer_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("graphic designer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="hollola")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-valkeakoski')
def graphic_designer_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("graphic designer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="valkeakoski")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-siilinjarvi')
def graphic_designer_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("graphic designer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="siilinjarvi")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kuusankoski')
def graphic_designer_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("graphic designer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kuusankoski")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-sibbo')
def graphic_designer_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("graphic designer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="sibbo")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-jakostad')
def graphic_designer_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("graphic designer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="jakostad")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-lempaala')
def graphic_designer_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("graphic designer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lempaala")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-mantsala')
def graphic_designer_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("graphic designer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="mantsala")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-forssa')
def graphic_designer_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("graphic designer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="forssa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kuusamo')
def graphic_designer_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("graphic designer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kuusamo")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-haukipudas')
def graphic_designer_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("graphic designer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="haukipudas")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-korsholm')
def graphic_designer_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("graphic designer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="korsholm")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-laukaa')
def graphic_designer_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("graphic designer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="laukaa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-anjala')
def graphic_designer_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("graphic designer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="anjala")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-uusikaupunki')
def graphic_designer_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("graphic designer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="uusikaupunki")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-janakkala')
def graphic_designer_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("graphic designer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="janakkala")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-pirkkala')
def graphic_designer_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("graphic designer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="pirkkala")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-lansi-turunmaa')
def graphic_designer_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("graphic designer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lansi-turunmaa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-jamsa')
def graphic_designer_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("graphic designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="jamsa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-jamsa')
def graphic_designer_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("graphic designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="jamsa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-vammala')
def graphic_designer_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("graphic designer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="vammala")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-nastola')
def graphic_designer_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("graphic designer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="nastola")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-orimattila')
def graphic_designer_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("graphic designer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="orimattila")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kauhajoki')
def graphic_designer_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("graphic designer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kauhajoki")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-ekenas')
def graphic_designer_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("graphic designer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="ekenas")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kempele')
def graphic_designer_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("graphic designer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kempele")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-lapua')
def graphic_designer_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("graphic designer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lapua")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-lieksa')
def graphic_designer_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("graphic designer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lieksa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-naantali')
def graphic_designer_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("graphic designer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="naantali")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-aanekoski')
def graphic_designer_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("graphic designer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="aanekoski")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-ylivieska')
def graphic_designer_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("graphic designer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="ylivieska")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kontiolahti')
def graphic_designer_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("graphic designer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kontiolahti")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kankaanpaa')
def graphic_designer_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("graphic designer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kankaanpaa")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-ulvila')
def graphic_designer_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("graphic designer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="ulvila")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-pieksamaki')
def graphic_designer_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("graphic designer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="pieksamaki")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kiiminki')
def graphic_designer_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("graphic designer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kiiminki")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-pargas')
def graphic_designer_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("graphic designer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="pargas")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-nurmo')
def graphic_designer_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("graphic designer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="nurmo")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-ilmajoki')
def graphic_designer_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("graphic designer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="ilmajoki")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-liperi')
def graphic_designer_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("graphic designer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="liperi")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-keuruu')
def graphic_designer_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("graphic designer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="keuruu")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-leppavirta')
def graphic_designer_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("graphic designer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="leppavirta")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kurikka')
def graphic_designer_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("graphic designer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kurikka")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-nivala')
def graphic_designer_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("graphic designer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="nivala")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-joutseno')
def graphic_designer_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("graphic designer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="joutseno")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-pedersore')
def graphic_designer_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("graphic designer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="pedersore")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-sotkamo')
def graphic_designer_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("graphic designer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="sotkamo")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-kuhmo')
def graphic_designer_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("graphic designer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kuhmo")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-paimio')
def graphic_designer_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("graphic designer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="paimio")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-saarijarvi')
def graphic_designer_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("graphic designer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="saarijarvi")
	
@graphic_designer.route('/graphic-designer-avoimet-tyopaikat-helsinki')
def graphic_designer_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("graphic designer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="helsinki")


####################################################################


##############################################
@graphic_designer.route('/graphic-designer-jobs-espoo')
def graphic_designer_jobs2(page=1):

    job_list = job_obj.get_job("graphic designer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="espoo")

@graphic_designer.route('/graphic-designer-jobs-tampere')
def graphic_designer_jobs3(page=1):

    job_list = job_obj.get_job("graphic designer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="tampere")
	
@graphic_designer.route('/graphic-designer-jobs-vantaa')
def graphic_designer_jobs4(page=1):

    job_list = job_obj.get_job("graphic designer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="vantaa")
	
@graphic_designer.route('/graphic-designer-jobs-turku')
def graphic_designer_jobs5(page=1):

    job_list = job_obj.get_job("graphic designer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="turku")
	
@graphic_designer.route('/graphic-designer-jobs-oulu')
def graphic_designer_jobs6(page=1):

    job_list = job_obj.get_job("graphic designer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="oulu")
	
@graphic_designer.route('/graphic-designer-jobs-lahti')
def graphic_designer_jobs7(page=1):

    job_list = job_obj.get_job("graphic designer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lahti")
	
@graphic_designer.route('/graphic-designer-jobs-kuopio')
def graphic_designer_jobs8(page=1):

    job_list = job_obj.get_job("graphic designer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kuopio")
	
@graphic_designer.route('/graphic-designer-jobs-jyvvaskyla')
def graphic_designer_jobs9(page=1):

    job_list = job_obj.get_job("graphic designer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="jyvvaskyla")

@graphic_designer.route('/graphic-designer-jobs-pori')
def graphic_designer_jobs10(page=1):

    job_list = job_obj.get_job("graphic designer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="pori")

@graphic_designer.route('/graphic-designer-jobs-lappeenranta')
def graphic_designer_jobs11(page=1):

    job_list = job_obj.get_job("graphic designer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lappeenranta")	
	
@graphic_designer.route('/graphic-designer-jobs-vaasa')
def graphic_designer_jobs12(page=1):

    job_list = job_obj.get_job("graphic designer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="vaasa")
	
@graphic_designer.route('/graphic-designer-jobs-kotka')
def graphic_designer_jobs13(page=1):

    job_list = job_obj.get_job("graphic designer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kotka")
	
@graphic_designer.route('/graphic-designer-jobs-joensuu')
def graphic_designer_jobs14(page=1):

    job_list = job_obj.get_job("graphic designer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="joensuu")
	
@graphic_designer.route('/graphic-designer-jobs-hameenlinna')
def graphic_designer_jobs15(page=1):

    job_list = job_obj.get_job("graphic designer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="hameenlinna")
	
@graphic_designer.route('/graphic-designer-jobs-porvoo')
def graphic_designer_jobs16(page=1):

    job_list = job_obj.get_job("graphic designer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="porvoo")
	
@graphic_designer.route('/graphic-designer-jobs-mikkeli')
def graphic_designer_jobs17(page=1):

    job_list = job_obj.get_job("graphic designer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="mikkeli")

@graphic_designer.route('/graphic-designer-jobs-hyvinkaa')
def graphic_designer_jobs18(page=1):

    job_list = job_obj.get_job("graphic designer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="hyvinkaa")
	
@graphic_designer.route('/graphic-designer-jobs-nurmijarvi')
def graphic_designer_jobs19(page=1):

    job_list = job_obj.get_job("graphic designer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="nurmijarvi")

@graphic_designer.route('/graphic-designer-jobs-jarvenpaa')
def graphic_designer_jobs20(page=1):

    job_list = job_obj.get_job("graphic designer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="jarvenpaa")
	
@graphic_designer.route('/graphic-designer-jobs-rauma')
def graphic_designer_jobs21(page=1):

    job_list = job_obj.get_job("graphic designer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="rauma")
	
@graphic_designer.route('/graphic-designer-jobs-lohja')
def graphic_designer_jobs22(page=1):

    job_list = job_obj.get_job("graphic designer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lohja")
	
@graphic_designer.route('/graphic-designer-jobs-karleby')
def graphic_designer_jobs23(page=1):

    job_list = job_obj.get_job("graphic designer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="karleby")
	
@graphic_designer.route('/graphic-designer-jobs-kajaani')
def graphic_designer_jobs24(page=1):

    job_list = job_obj.get_job("graphic designer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kajaani")
	
@graphic_designer.route('/graphic-designer-jobs-rovaniemi')
def graphic_designer_jobs25(page=1):

    job_list = job_obj.get_job("graphic designer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="rovaniemi")
	
@graphic_designer.route('/graphic-designer-jobs-tuusula')
def graphic_designer_jobs26(page=1):

    job_list = job_obj.get_job("graphic designer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="tuusula")
	
@graphic_designer.route('/graphic-designer-jobs-kirkkonummi')
def graphic_designer_jobs27(page=1):

    job_list = job_obj.get_job("graphic designer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kirkkonummi")
	
@graphic_designer.route('/graphic-designer-jobs-seinajoki')
def graphic_designer_jobs28(page=1):

    job_list = job_obj.get_job("graphic designer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="seinajoki")
	
@graphic_designer.route('/graphic-designer-jobs-kerava')
def graphic_designer_jobs29(page=1):

    job_list = job_obj.get_job("graphic designer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kerava")
	
@graphic_designer.route('/graphic-designer-jobs-kouvola')
def graphic_designer_jobs30(page=1):

    job_list = job_obj.get_job("graphic designer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kouvola")
	
@graphic_designer.route('/graphic-designer-jobs-imatra')
def graphic_designer_jobs31(page=1):

    job_list = job_obj.get_job("graphic designer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="imatra")
	
@graphic_designer.route('/graphic-designer-jobs-nokia')
def graphic_designer_jobs32_1(page=1):

    job_list = job_obj.get_job("graphic designer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="nokia")
	
@graphic_designer.route('/graphic-designer-jobs-savonlinna')
def graphic_designer_jobs32(page=1):

    job_list = job_obj.get_job("graphic designer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="savonlinna")
	
@graphic_designer.route('/graphic-designer-jobs-riihimaki')
def graphic_designer_jobs33(page=1):

    job_list = job_obj.get_job("graphic designer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="riihimaki")
	
@graphic_designer.route('/graphic-designer-jobs-vihti')
def graphic_designer_jobs34(page=1):

    job_list = job_obj.get_job("graphic designer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="vihti")
	
@graphic_designer.route('/graphic-designer-jobs-salo')
def graphic_designer_jobs35(page=1):

    job_list = job_obj.get_job("graphic designer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="salo")
	
@graphic_designer.route('/graphic-designer-jobs-kangasala')
def graphic_designer_jobs36(page=1):

    job_list = job_obj.get_job("graphic designer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kangasala")
	
@graphic_designer.route('/graphic-designer-jobs-raisio')
def graphic_designer_jobs37_1(page=1):

    job_list = job_obj.get_job("graphic designer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="raisio")
	
@graphic_designer.route('/graphic-designer-jobs-karhula')
def graphic_designer_jobs37(page=1):

    job_list = job_obj.get_job("graphic designer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="karhula")
	
@graphic_designer.route('/graphic-designer-jobs-kemi')
def graphic_designer_jobs38(page=1):

    job_list = job_obj.get_job("graphic designer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kemi")
	
@graphic_designer.route('/graphic-designer-jobs-iisalmi')
def graphic_designer_jobs39(page=1):

    job_list = job_obj.get_job("graphic designer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="iisalmi")
	
@graphic_designer.route('/graphic-designer-jobs-varkaus')
def graphic_designer_jobs40(page=1):

    job_list = job_obj.get_job("graphic designer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="varkaus")
	
@graphic_designer.route('/graphic-designer-jobs-raahe')
def graphic_designer_jobs41(page=1):

    job_list = job_obj.get_job("graphic designer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="raahe")
	
@graphic_designer.route('/graphic-designer-jobs-ylojarvi')
def graphic_designer_jobs42_1(page=1):

    job_list = job_obj.get_job("graphic designer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="ylojarvi")
	
@graphic_designer.route('/graphic-designer-jobs-hamina')
def graphic_designer_jobs42(page=1):

    job_list = job_obj.get_job("graphic designer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="hamina")
	
@graphic_designer.route('/graphic-designer-jobs-kaarina')
def graphic_designer_jobs43(page=1):

    job_list = job_obj.get_job("graphic designer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kaarina")
	
@graphic_designer.route('/graphic-designer-jobs-tornio')
def graphic_designer_jobs44(page=1):

    job_list = job_obj.get_job("graphic designer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="tornio")
	
@graphic_designer.route('/graphic-designer-jobs-heinola')
def graphic_designer_jobs45(page=1):

    job_list = job_obj.get_job("graphic designer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="heinola")
	
@graphic_designer.route('/graphic-designer-jobs-hollola')
def graphic_designer_jobs46(page=1):

    job_list = job_obj.get_job("graphic designer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="hollola")
	
@graphic_designer.route('/graphic-designer-jobs-valkeakoski')
def graphic_designer_jobs47(page=1):

    job_list = job_obj.get_job("graphic designer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="valkeakoski")
	
@graphic_designer.route('/graphic-designer-jobs-siilinjarvi')
def graphic_designer_jobs48(page=1):

    job_list = job_obj.get_job("graphic designer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="siilinjarvi")
	
@graphic_designer.route('/graphic-designer-jobs-kuusankoski')
def graphic_designer_jobs49(page=1):

    job_list = job_obj.get_job("graphic designer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kuusankoski")
	
@graphic_designer.route('/graphic-designer-jobs-sibbo')
def graphic_designer_jobs50(page=1):

    job_list = job_obj.get_job("graphic designer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="sibbo")
	
@graphic_designer.route('/graphic-designer-jobs-jakostad')
def graphic_designer_jobs51(page=1):

    job_list = job_obj.get_job("graphic designer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="jakostad")
	
@graphic_designer.route('/graphic-designer-jobs-lempaala')
def graphic_designer_jobs52(page=1):

    job_list = job_obj.get_job("graphic designer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lempaala")
	
@graphic_designer.route('/graphic-designer-jobs-mantsala')
def graphic_designer_jobs52_1(page=1):

    job_list = job_obj.get_job("graphic designer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="mantsala")
	
@graphic_designer.route('/graphic-designer-jobs-forssa')
def graphic_designer_jobs53(page=1):

    job_list = job_obj.get_job("graphic designer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="forssa")
	
@graphic_designer.route('/graphic-designer-jobs-kuusamo')
def graphic_designer_jobs54(page=1):

    job_list = job_obj.get_job("graphic designer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kuusamo")
	
@graphic_designer.route('/graphic-designer-jobs-haukipudas')
def graphic_designer_jobs55(page=1):

    job_list = job_obj.get_job("graphic designer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="haukipudas")
	
@graphic_designer.route('/graphic-designer-jobs-korsholm')
def graphic_designer_jobs56(page=1):

    job_list = job_obj.get_job("graphic designer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="korsholm")
	
@graphic_designer.route('/graphic-designer-jobs-laukaa')
def graphic_designer_jobs57(page=1):

    job_list = job_obj.get_job("graphic designer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="laukaa")
	
@graphic_designer.route('/graphic-designer-jobs-anjala')
def graphic_designer_jobs58(page=1):

    job_list = job_obj.get_job("graphic designer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="anjala")
	
@graphic_designer.route('/graphic-designer-jobs-uusikaupunki')
def graphic_designer_jobs59(page=1):

    job_list = job_obj.get_job("graphic designer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="uusikaupunki")
	
@graphic_designer.route('/graphic-designer-jobs-janakkala')
def graphic_designer_jobs60(page=1):

    job_list = job_obj.get_job("graphic designer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="janakkala")
	
@graphic_designer.route('/graphic-designer-jobs-pirkkala')
def graphic_designer_jobs61(page=1):

    job_list = job_obj.get_job("graphic designer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="pirkkala")
	
@graphic_designer.route('/graphic-designer-jobs-lansi-turunmaa')
def graphic_designer_jobs62(page=1):

    job_list = job_obj.get_job("graphic designer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lansi-turunmaa")
	
@graphic_designer.route('/graphic-designer-jobs-jamsa')
def graphic_designer_jobs63(page=1):

    job_list = job_obj.get_job("graphic designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="jamsa")
	
@graphic_designer.route('/graphic-designer-jobs-jamsa')
def graphic_designer_jobs64(page=1):

    job_list = job_obj.get_job("graphic designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="jamsa")
	
@graphic_designer.route('/graphic-designer-jobs-vammala')
def graphic_designer_jobs65(page=1):

    job_list = job_obj.get_job("graphic designer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="vammala")
	
@graphic_designer.route('/graphic-designer-jobs-nastola')
def graphic_designer_jobs66(page=1):

    job_list = job_obj.get_job("graphic designer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="nastola")
	
@graphic_designer.route('/graphic-designer-jobs-orimattila')
def graphic_designer_jobs67(page=1):

    job_list = job_obj.get_job("graphic designer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="orimattila")
	
@graphic_designer.route('/graphic-designer-jobs-kauhajoki')
def graphic_designer_jobs68(page=1):

    job_list = job_obj.get_job("graphic designer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kauhajoki")
	
@graphic_designer.route('/graphic-designer-jobs-ekenas')
def graphic_designer_jobs69(page=1):

    job_list = job_obj.get_job("graphic designer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="ekenas")
	
@graphic_designer.route('/graphic-designer-jobs-kempele')
def graphic_designer_jobs70(page=1):

    job_list = job_obj.get_job("graphic designer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kempele")
	
@graphic_designer.route('/graphic-designer-jobs-lapua')
def graphic_designer_jobs71(page=1):

    job_list = job_obj.get_job("graphic designer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lapua")
	
@graphic_designer.route('/graphic-designer-jobs-lieksa')
def graphic_designer_jobs72(page=1):

    job_list = job_obj.get_job("graphic designer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="lieksa")
	
@graphic_designer.route('/graphic-designer-jobs-naantali')
def graphic_designer_jobs73(page=1):

    job_list = job_obj.get_job("graphic designer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="naantali")
	
@graphic_designer.route('/graphic-designer-jobs-aanekoski')
def graphic_designer_jobs74(page=1):

    job_list = job_obj.get_job("graphic designer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="aanekoski")
	
@graphic_designer.route('/graphic-designer-jobs-ylivieska')
def graphic_designer_jobs75(page=1):

    job_list = job_obj.get_job("graphic designer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="ylivieska")
	
@graphic_designer.route('/graphic-designer-jobs-kontiolahti')
def graphic_designer_jobs76(page=1):

    job_list = job_obj.get_job("graphic designer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kontiolahti")
	
@graphic_designer.route('/graphic-designer-jobs-kankaanpaa')
def graphic_designer_jobs77(page=1):

    job_list = job_obj.get_job("graphic designer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kankaanpaa")
	
@graphic_designer.route('/graphic-designer-jobs-ulvila')
def graphic_designer_jobs78(page=1):

    job_list = job_obj.get_job("graphic designer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="ulvila")
	
@graphic_designer.route('/graphic-designer-jobs-pieksamaki')
def graphic_designer_jobs79(page=1):

    job_list = job_obj.get_job("graphic designer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="pieksamaki")
	
@graphic_designer.route('/graphic-designer-jobs-kiiminki')
def graphic_designer_jobs80(page=1):

    job_list = job_obj.get_job("graphic designer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kiiminki")
	
@graphic_designer.route('/graphic-designer-jobs-pargas')
def graphic_designer_jobs81(page=1):

    job_list = job_obj.get_job("graphic designer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="pargas")
	
@graphic_designer.route('/graphic-designer-jobs-nurmo')
def graphic_designer_jobs82(page=1):

    job_list = job_obj.get_job("graphic designer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="nurmo")
	
@graphic_designer.route('/graphic-designer-jobs-ilmajoki')
def graphic_designer_jobs83(page=1):

    job_list = job_obj.get_job("graphic designer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="ilmajoki")
	
@graphic_designer.route('/graphic-designer-jobs-liperi')
def graphic_designer_jobs84(page=1):

    job_list = job_obj.get_job("graphic designer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="liperi")
	
@graphic_designer.route('/graphic-designer-jobs-keuruu')
def graphic_designer_jobs85(page=1):

    job_list = job_obj.get_job("graphic designer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="keuruu")
	
@graphic_designer.route('/graphic-designer-jobs-leppavirta')
def graphic_designer_jobs86(page=1):

    job_list = job_obj.get_job("graphic designer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="leppavirta")
	
@graphic_designer.route('/graphic-designer-jobs-kurikka')
def graphic_designer_jobs87(page=1):

    job_list = job_obj.get_job("graphic designer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kurikka")
	
@graphic_designer.route('/graphic-designer-jobs-nivala')
def graphic_designer_jobs88(page=1):

    job_list = job_obj.get_job("graphic designer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="nivala")
	
@graphic_designer.route('/graphic-designer-jobs-joutseno')
def graphic_designer_jobs89(page=1):

    job_list = job_obj.get_job("graphic designer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="joutseno")
	
@graphic_designer.route('/graphic-designer-jobs-pedersore')
def graphic_designer_jobs90(page=1):

    job_list = job_obj.get_job("graphic designer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="pedersore")
	
@graphic_designer.route('/graphic-designer-jobs-sotkamo')
def graphic_designer_jobs91(page=1):

    job_list = job_obj.get_job("graphic designer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="sotkamo")
	
@graphic_designer.route('/graphic-designer-jobs-kuhmo')
def graphic_designer_jobs92(page=1):

    job_list = job_obj.get_job("graphic designer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="kuhmo")
	
@graphic_designer.route('/graphic-designer-jobs-paimio')
def graphic_designer_jobs93(page=1):

    job_list = job_obj.get_job("graphic designer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="paimio")
	
@graphic_designer.route('/graphic-designer-jobs-saarijarvi')
def graphic_designer_jobs94(page=1):

    job_list = job_obj.get_job("graphic designer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="saarijarvi")
	
@graphic_designer.route('/graphic-designer-jobs-helsinki')
def graphic_designer_jobs95(page=1):

    job_list = job_obj.get_job("graphic designer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer ", location="helsinki")


####################################################################


##############################################
@graphic_designer.route('/graphic-designer-tyopaikat-espoo')
def graphic_designer_tyopaikat2(page=1):

    job_list = job_obj.get_job("graphic designer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="espoo")

@graphic_designer.route('/graphic-designer-tyopaikat-tampere')
def graphic_designer_tyopaikat3(page=1):

    job_list = job_obj.get_job("graphic designer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="tampere")
	
@graphic_designer.route('/graphic-designer-tyopaikat-vantaa')
def graphic_designer_tyopaikat4(page=1):

    job_list = job_obj.get_job("graphic designer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="vantaa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-turku')
def graphic_designer_tyopaikat5(page=1):

    job_list = job_obj.get_job("graphic designer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="turku")
	
@graphic_designer.route('/graphic-designer-tyopaikat-oulu')
def graphic_designer_tyopaikat6(page=1):

    job_list = job_obj.get_job("graphic designer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="oulu")
	
@graphic_designer.route('/graphic-designer-tyopaikat-lahti')
def graphic_designer_tyopaikat7(page=1):

    job_list = job_obj.get_job("graphic designer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="lahti")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kuopio')
def graphic_designer_tyopaikat8(page=1):

    job_list = job_obj.get_job("graphic designer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kuopio")
	
@graphic_designer.route('/graphic-designer-tyopaikat-jyvvaskyla')
def graphic_designer_tyopaikat9(page=1):

    job_list = job_obj.get_job("graphic designer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="jyvvaskyla")

@graphic_designer.route('/graphic-designer-tyopaikat-pori')
def graphic_designer_tyopaikat10(page=1):

    job_list = job_obj.get_job("graphic designer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="pori")

@graphic_designer.route('/graphic-designer-tyopaikat-lappeenranta')
def graphic_designer_tyopaikat11(page=1):

    job_list = job_obj.get_job("graphic designer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="lappeenranta")	
	
@graphic_designer.route('/graphic-designer-tyopaikat-vaasa')
def graphic_designer_tyopaikat12(page=1):

    job_list = job_obj.get_job("graphic designer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="vaasa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kotka')
def graphic_designer_tyopaikat13(page=1):

    job_list = job_obj.get_job("graphic designer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kotka")
	
@graphic_designer.route('/graphic-designer-tyopaikat-joensuu')
def graphic_designer_tyopaikat14(page=1):

    job_list = job_obj.get_job("graphic designer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="joensuu")
	
@graphic_designer.route('/graphic-designer-tyopaikat-hameenlinna')
def graphic_designer_tyopaikat15(page=1):

    job_list = job_obj.get_job("graphic designer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="hameenlinna")
	
@graphic_designer.route('/graphic-designer-tyopaikat-porvoo')
def graphic_designer_tyopaikat16(page=1):

    job_list = job_obj.get_job("graphic designer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="porvoo")
	
@graphic_designer.route('/graphic-designer-tyopaikat-mikkeli')
def graphic_designer_tyopaikat17(page=1):

    job_list = job_obj.get_job("graphic designer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="mikkeli")

@graphic_designer.route('/graphic-designer-tyopaikat-hyvinkaa')
def graphic_designer_tyopaikat18(page=1):

    job_list = job_obj.get_job("graphic designer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="hyvinkaa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-nurmijarvi')
def graphic_designer_tyopaikat19(page=1):

    job_list = job_obj.get_job("graphic designer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="nurmijarvi")

@graphic_designer.route('/graphic-designer-tyopaikat-jarvenpaa')
def graphic_designer_tyopaikat20(page=1):

    job_list = job_obj.get_job("graphic designer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="jarvenpaa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-rauma')
def graphic_designer_tyopaikat21(page=1):

    job_list = job_obj.get_job("graphic designer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="rauma")
	
@graphic_designer.route('/graphic-designer-tyopaikat-lohja')
def graphic_designer_tyopaikat22(page=1):

    job_list = job_obj.get_job("graphic designer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="lohja")
	
@graphic_designer.route('/graphic-designer-tyopaikat-karleby')
def graphic_designer_tyopaikat23(page=1):

    job_list = job_obj.get_job("graphic designer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="karleby")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kajaani')
def graphic_designer_tyopaikat24(page=1):

    job_list = job_obj.get_job("graphic designer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kajaani")
	
@graphic_designer.route('/graphic-designer-tyopaikat-rovaniemi')
def graphic_designer_tyopaikat25(page=1):

    job_list = job_obj.get_job("graphic designer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="rovaniemi")
	
@graphic_designer.route('/graphic-designer-tyopaikat-tuusula')
def graphic_designer_tyopaikat26(page=1):

    job_list = job_obj.get_job("graphic designer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="tuusula")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kirkkonummi')
def graphic_designer_tyopaikat27(page=1):

    job_list = job_obj.get_job("graphic designer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kirkkonummi")
	
@graphic_designer.route('/graphic-designer-tyopaikat-seinajoki')
def graphic_designer_tyopaikat28(page=1):

    job_list = job_obj.get_job("graphic designer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="seinajoki")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kerava')
def graphic_designer_tyopaikat29(page=1):

    job_list = job_obj.get_job("graphic designer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kerava")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kouvola')
def graphic_designer_tyopaikat30(page=1):

    job_list = job_obj.get_job("graphic designer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kouvola")
	
@graphic_designer.route('/graphic-designer-tyopaikat-imatra')
def graphic_designer_tyopaikat31(page=1):

    job_list = job_obj.get_job("graphic designer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="imatra")
	
@graphic_designer.route('/graphic-designer-tyopaikat-nokia')
def graphic_designer_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("graphic designer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="nokia")
	
@graphic_designer.route('/graphic-designer-tyopaikat-savonlinna')
def graphic_designer_tyopaikat32(page=1):

    job_list = job_obj.get_job("graphic designer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="savonlinna")
	
@graphic_designer.route('/graphic-designer-tyopaikat-riihimaki')
def graphic_designer_tyopaikat33(page=1):

    job_list = job_obj.get_job("graphic designer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="riihimaki")
	
@graphic_designer.route('/graphic-designer-tyopaikat-vihti')
def graphic_designer_tyopaikat34(page=1):

    job_list = job_obj.get_job("graphic designer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="vihti")
	
@graphic_designer.route('/graphic-designer-tyopaikat-salo')
def graphic_designer_tyopaikat35(page=1):

    job_list = job_obj.get_job("graphic designer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="salo")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kangasala')
def graphic_designer_tyopaikat36(page=1):

    job_list = job_obj.get_job("graphic designer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kangasala")
	
@graphic_designer.route('/graphic-designer-tyopaikat-raisio')
def graphic_designer_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("graphic designer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="raisio")
	
@graphic_designer.route('/graphic-designer-tyopaikat-karhula')
def graphic_designer_tyopaikat37(page=1):

    job_list = job_obj.get_job("graphic designer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="karhula")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kemi')
def graphic_designer_tyopaikat38(page=1):

    job_list = job_obj.get_job("graphic designer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kemi")
	
@graphic_designer.route('/graphic-designer-tyopaikat-iisalmi')
def graphic_designer_tyopaikat39(page=1):

    job_list = job_obj.get_job("graphic designer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="iisalmi")
	
@graphic_designer.route('/graphic-designer-tyopaikat-varkaus')
def graphic_designer_tyopaikat40(page=1):

    job_list = job_obj.get_job("graphic designer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="varkaus")
	
@graphic_designer.route('/graphic-designer-tyopaikat-raahe')
def graphic_designer_tyopaikat41(page=1):

    job_list = job_obj.get_job("graphic designer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="raahe")
	
@graphic_designer.route('/graphic-designer-tyopaikat-ylojarvi')
def graphic_designer_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("graphic designer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="ylojarvi")
	
@graphic_designer.route('/graphic-designer-tyopaikat-hamina')
def graphic_designer_tyopaikat42(page=1):

    job_list = job_obj.get_job("graphic designer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="hamina")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kaarina')
def graphic_designer_tyopaikat43(page=1):

    job_list = job_obj.get_job("graphic designer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kaarina")
	
@graphic_designer.route('/graphic-designer-tyopaikat-tornio')
def graphic_designer_tyopaikat44(page=1):

    job_list = job_obj.get_job("graphic designer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="tornio")
	
@graphic_designer.route('/graphic-designer-tyopaikat-heinola')
def graphic_designer_tyopaikat45(page=1):

    job_list = job_obj.get_job("graphic designer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="heinola")
	
@graphic_designer.route('/graphic-designer-tyopaikat-hollola')
def graphic_designer_tyopaikat46(page=1):

    job_list = job_obj.get_job("graphic designer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="hollola")
	
@graphic_designer.route('/graphic-designer-tyopaikat-valkeakoski')
def graphic_designer_tyopaikat47(page=1):

    job_list = job_obj.get_job("graphic designer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="valkeakoski")
	
@graphic_designer.route('/graphic-designer-tyopaikat-siilinjarvi')
def graphic_designer_tyopaikat48(page=1):

    job_list = job_obj.get_job("graphic designer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="siilinjarvi")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kuusankoski')
def graphic_designer_tyopaikat49(page=1):

    job_list = job_obj.get_job("graphic designer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kuusankoski")
	
@graphic_designer.route('/graphic-designer-tyopaikat-sibbo')
def graphic_designer_tyopaikat50(page=1):

    job_list = job_obj.get_job("graphic designer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="sibbo")
	
@graphic_designer.route('/graphic-designer-tyopaikat-jakostad')
def graphic_designer_tyopaikat51(page=1):

    job_list = job_obj.get_job("graphic designer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="jakostad")
	
@graphic_designer.route('/graphic-designer-tyopaikat-lempaala')
def graphic_designer_tyopaikat52(page=1):

    job_list = job_obj.get_job("graphic designer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="lempaala")
	
@graphic_designer.route('/graphic-designer-tyopaikat-mantsala')
def graphic_designer_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("graphic designer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="mantsala")
	
@graphic_designer.route('/graphic-designer-tyopaikat-forssa')
def graphic_designer_tyopaikat53(page=1):

    job_list = job_obj.get_job("graphic designer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="forssa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kuusamo')
def graphic_designer_tyopaikat54(page=1):

    job_list = job_obj.get_job("graphic designer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kuusamo")
	
@graphic_designer.route('/graphic-designer-tyopaikat-haukipudas')
def graphic_designer_tyopaikat55(page=1):

    job_list = job_obj.get_job("graphic designer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="haukipudas")
	
@graphic_designer.route('/graphic-designer-tyopaikat-korsholm')
def graphic_designer_tyopaikat56(page=1):

    job_list = job_obj.get_job("graphic designer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="korsholm")
	
@graphic_designer.route('/graphic-designer-tyopaikat-laukaa')
def graphic_designer_tyopaikat57(page=1):

    job_list = job_obj.get_job("graphic designer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="laukaa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-anjala')
def graphic_designer_tyopaikat58(page=1):

    job_list = job_obj.get_job("graphic designer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="anjala")
	
@graphic_designer.route('/graphic-designer-tyopaikat-uusikaupunki')
def graphic_designer_tyopaikat59(page=1):

    job_list = job_obj.get_job("graphic designer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="uusikaupunki")
	
@graphic_designer.route('/graphic-designer-tyopaikat-janakkala')
def graphic_designer_tyopaikat60(page=1):

    job_list = job_obj.get_job("graphic designer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="janakkala")
	
@graphic_designer.route('/graphic-designer-tyopaikat-pirkkala')
def graphic_designer_tyopaikat61(page=1):

    job_list = job_obj.get_job("graphic designer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="pirkkala")
	
@graphic_designer.route('/graphic-designer-tyopaikat-lansi-turunmaa')
def graphic_designer_tyopaikat62(page=1):

    job_list = job_obj.get_job("graphic designer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="lansi-turunmaa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-jamsa')
def graphic_designer_tyopaikat63(page=1):

    job_list = job_obj.get_job("graphic designer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="jamsa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-jamsa')
def graphic_designer_tyopaikat64(page=1):

    job_list = job_obj.get_job("graphic designer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="jamsa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-vammala')
def graphic_designer_tyopaikat65(page=1):

    job_list = job_obj.get_job("graphic designer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="vammala")
	
@graphic_designer.route('/graphic-designer-tyopaikat-nastola')
def graphic_designer_tyopaikat66(page=1):

    job_list = job_obj.get_job("graphic designer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="nastola")
	
@graphic_designer.route('/graphic-designer-tyopaikat-orimattila')
def graphic_designer_tyopaikat67(page=1):

    job_list = job_obj.get_job("graphic designer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="orimattila")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kauhajoki')
def graphic_designer_tyopaikat68(page=1):

    job_list = job_obj.get_job("graphic designer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kauhajoki")
	
@graphic_designer.route('/graphic-designer-tyopaikat-ekenas')
def graphic_designer_tyopaikat69(page=1):

    job_list = job_obj.get_job("graphic designer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="ekenas")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kempele')
def graphic_designer_tyopaikat70(page=1):

    job_list = job_obj.get_job("graphic designer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kempele")
	
@graphic_designer.route('/graphic-designer-tyopaikat-lapua')
def graphic_designer_tyopaikat71(page=1):

    job_list = job_obj.get_job("graphic designer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="lapua")
	
@graphic_designer.route('/graphic-designer-tyopaikat-lieksa')
def graphic_designer_tyopaikat72(page=1):

    job_list = job_obj.get_job("graphic designer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="lieksa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-naantali')
def graphic_designer_tyopaikat73(page=1):

    job_list = job_obj.get_job("graphic designer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="naantali")
	
@graphic_designer.route('/graphic-designer-tyopaikat-aanekoski')
def graphic_designer_tyopaikat74(page=1):

    job_list = job_obj.get_job("graphic designer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="aanekoski")
	
@graphic_designer.route('/graphic-designer-tyopaikat-ylivieska')
def graphic_designer_tyopaikat75(page=1):

    job_list = job_obj.get_job("graphic designer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="ylivieska")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kontiolahti')
def graphic_designer_tyopaikat76(page=1):

    job_list = job_obj.get_job("graphic designer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kontiolahti")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kankaanpaa')
def graphic_designer_tyopaikat77(page=1):

    job_list = job_obj.get_job("graphic designer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kankaanpaa")
	
@graphic_designer.route('/graphic-designer-tyopaikat-ulvila')
def graphic_designer_tyopaikat78(page=1):

    job_list = job_obj.get_job("graphic designer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="ulvila")
	
@graphic_designer.route('/graphic-designer-tyopaikat-pieksamaki')
def graphic_designer_tyopaikat79(page=1):

    job_list = job_obj.get_job("graphic designer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="pieksamaki")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kiiminki')
def graphic_designer_tyopaikat80(page=1):

    job_list = job_obj.get_job("graphic designer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kiiminki")
	
@graphic_designer.route('/graphic-designer-tyopaikat-pargas')
def graphic_designer_tyopaikat81(page=1):

    job_list = job_obj.get_job("graphic designer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="pargas")
	
@graphic_designer.route('/graphic-designer-tyopaikat-nurmo')
def graphic_designer_tyopaikat82(page=1):

    job_list = job_obj.get_job("graphic designer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="nurmo")
	
@graphic_designer.route('/graphic-designer-tyopaikat-ilmajoki')
def graphic_designer_tyopaikat83(page=1):

    job_list = job_obj.get_job("graphic designer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="ilmajoki")
	
@graphic_designer.route('/graphic-designer-tyopaikat-liperi')
def graphic_designer_tyopaikat84(page=1):

    job_list = job_obj.get_job("graphic designer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="liperi")
	
@graphic_designer.route('/graphic-designer-tyopaikat-keuruu')
def graphic_designer_tyopaikat85(page=1):

    job_list = job_obj.get_job("graphic designer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="keuruu")
	
@graphic_designer.route('/graphic-designer-tyopaikat-leppavirta')
def graphic_designer_tyopaikat86(page=1):

    job_list = job_obj.get_job("graphic designer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="leppavirta")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kurikka')
def graphic_designer_tyopaikat87(page=1):

    job_list = job_obj.get_job("graphic designer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kurikka")
	
@graphic_designer.route('/graphic-designer-tyopaikat-nivala')
def graphic_designer_tyopaikat88(page=1):

    job_list = job_obj.get_job("graphic designer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="nivala")
	
@graphic_designer.route('/graphic-designer-tyopaikat-joutseno')
def graphic_designer_tyopaikat89(page=1):

    job_list = job_obj.get_job("graphic designer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="joutseno")
	
@graphic_designer.route('/graphic-designer-tyopaikat-pedersore')
def graphic_designer_tyopaikat90(page=1):

    job_list = job_obj.get_job("graphic designer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="pedersore")
	
@graphic_designer.route('/graphic-designer-tyopaikat-sotkamo')
def graphic_designer_tyopaikat91(page=1):

    job_list = job_obj.get_job("graphic designer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="sotkamo")
	
@graphic_designer.route('/graphic-designer-tyopaikat-kuhmo')
def graphic_designer_tyopaikat92(page=1):

    job_list = job_obj.get_job("graphic designer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="kuhmo")
	
@graphic_designer.route('/graphic-designer-tyopaikat-paimio')
def graphic_designer_tyopaikat93(page=1):

    job_list = job_obj.get_job("graphic designer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="paimio")
	
@graphic_designer.route('/graphic-designer-tyopaikat-saarijarvi')
def graphic_designer_tyopaikat94(page=1):

    job_list = job_obj.get_job("graphic designer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer", location="saarijarvi")
	
@graphic_designer.route('/graphic-designer-tyopaikat-helsinki')
def graphic_designer_tyopaikat95(page=1):

    job_list = job_obj.get_job("graphic designer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="graphic designer  ", location="helsinki")
	  

