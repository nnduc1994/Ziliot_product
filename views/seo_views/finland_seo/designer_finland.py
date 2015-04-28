from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

designer = Blueprint('designer', __name__)
job_obj = Job()



####################################################################


@designer.route('/designer_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "designer" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@designer.route('/designer-avoimet-tyopaikat-espoo')
def designer_avoimet_tyopaikat2(page=1):

    job_list = job_obj.get_job("designer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="espoo")

@designer.route('/designer-avoimet-tyopaikat-tampere')
def designer_avoimet_tyopaikat3(page=1):

    job_list = job_obj.get_job("designer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="tampere")
	
@designer.route('/designer-avoimet-tyopaikat-vantaa')
def designer_avoimet_tyopaikat4(page=1):

    job_list = job_obj.get_job("designer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vantaa")
	
@designer.route('/designer-avoimet-tyopaikat-turku')
def designer_avoimet_tyopaikat5(page=1):

    job_list = job_obj.get_job("designer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="turku")
	
@designer.route('/designer-avoimet-tyopaikat-oulu')
def designer_avoimet_tyopaikat6(page=1):

    job_list = job_obj.get_job("designer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="oulu")
	
@designer.route('/designer-avoimet-tyopaikat-lahti')
def designer_avoimet_tyopaikat7(page=1):

    job_list = job_obj.get_job("designer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lahti")
	
@designer.route('/designer-avoimet-tyopaikat-kuopio')
def designer_avoimet_tyopaikat8(page=1):

    job_list = job_obj.get_job("designer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuopio")
	
@designer.route('/designer-avoimet-tyopaikat-jyvvaskyla')
def designer_avoimet_tyopaikat9(page=1):

    job_list = job_obj.get_job("designer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jyvvaskyla")

@designer.route('/designer-avoimet-tyopaikat-pori')
def designer_avoimet_tyopaikat10(page=1):

    job_list = job_obj.get_job("designer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pori")

@designer.route('/designer-avoimet-tyopaikat-lappeenranta')
def designer_avoimet_tyopaikat11(page=1):

    job_list = job_obj.get_job("designer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lappeenranta")	
	
@designer.route('/designer-avoimet-tyopaikat-vaasa')
def designer_avoimet_tyopaikat12(page=1):

    job_list = job_obj.get_job("designer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vaasa")
	
@designer.route('/designer-avoimet-tyopaikat-kotka')
def designer_avoimet_tyopaikat13(page=1):

    job_list = job_obj.get_job("designer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kotka")
	
@designer.route('/designer-avoimet-tyopaikat-joensuu')
def designer_avoimet_tyopaikat14(page=1):

    job_list = job_obj.get_job("designer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="joensuu")
	
@designer.route('/designer-avoimet-tyopaikat-hameenlinna')
def designer_avoimet_tyopaikat15(page=1):

    job_list = job_obj.get_job("designer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hameenlinna")
	
@designer.route('/designer-avoimet-tyopaikat-porvoo')
def designer_avoimet_tyopaikat16(page=1):

    job_list = job_obj.get_job("designer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="porvoo")
	
@designer.route('/designer-avoimet-tyopaikat-mikkeli')
def designer_avoimet_tyopaikat17(page=1):

    job_list = job_obj.get_job("designer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="mikkeli")

@designer.route('/designer-avoimet-tyopaikat-hyvinkaa')
def designer_avoimet_tyopaikat18(page=1):

    job_list = job_obj.get_job("designer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hyvinkaa")
	
@designer.route('/designer-avoimet-tyopaikat-nurmijarvi')
def designer_avoimet_tyopaikat19(page=1):

    job_list = job_obj.get_job("designer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nurmijarvi")

@designer.route('/designer-avoimet-tyopaikat-jarvenpaa')
def designer_avoimet_tyopaikat20(page=1):

    job_list = job_obj.get_job("designer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jarvenpaa")
	
@designer.route('/designer-avoimet-tyopaikat-rauma')
def designer_avoimet_tyopaikat21(page=1):

    job_list = job_obj.get_job("designer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="rauma")
	
@designer.route('/designer-avoimet-tyopaikat-lohja')
def designer_avoimet_tyopaikat22(page=1):

    job_list = job_obj.get_job("designer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lohja")
	
@designer.route('/designer-avoimet-tyopaikat-karleby')
def designer_avoimet_tyopaikat23(page=1):

    job_list = job_obj.get_job("designer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="karleby")
	
@designer.route('/designer-avoimet-tyopaikat-kajaani')
def designer_avoimet_tyopaikat24(page=1):

    job_list = job_obj.get_job("designer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kajaani")
	
@designer.route('/designer-avoimet-tyopaikat-rovaniemi')
def designer_avoimet_tyopaikat25(page=1):

    job_list = job_obj.get_job("designer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="rovaniemi")
	
@designer.route('/designer-avoimet-tyopaikat-tuusula')
def designer_avoimet_tyopaikat26(page=1):

    job_list = job_obj.get_job("designer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="tuusula")
	
@designer.route('/designer-avoimet-tyopaikat-kirkkonummi')
def designer_avoimet_tyopaikat27(page=1):

    job_list = job_obj.get_job("designer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kirkkonummi")
	
@designer.route('/designer-avoimet-tyopaikat-seinajoki')
def designer_avoimet_tyopaikat28(page=1):

    job_list = job_obj.get_job("designer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="seinajoki")
	
@designer.route('/designer-avoimet-tyopaikat-kerava')
def designer_avoimet_tyopaikat29(page=1):

    job_list = job_obj.get_job("designer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kerava")
	
@designer.route('/designer-avoimet-tyopaikat-kouvola')
def designer_avoimet_tyopaikat30(page=1):

    job_list = job_obj.get_job("designer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kouvola")
	
@designer.route('/designer-avoimet-tyopaikat-imatra')
def designer_avoimet_tyopaikat31(page=1):

    job_list = job_obj.get_job("designer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="imatra")
	
@designer.route('/designer-avoimet-tyopaikat-nokia')
def designer_avoimet_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("designer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nokia")
	
@designer.route('/designer-avoimet-tyopaikat-savonlinna')
def designer_avoimet_tyopaikat32(page=1):

    job_list = job_obj.get_job("designer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="savonlinna")
	
@designer.route('/designer-avoimet-tyopaikat-riihimaki')
def designer_avoimet_tyopaikat33(page=1):

    job_list = job_obj.get_job("designer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="riihimaki")
	
@designer.route('/designer-avoimet-tyopaikat-vihti')
def designer_avoimet_tyopaikat34(page=1):

    job_list = job_obj.get_job("designer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vihti")
	
@designer.route('/designer-avoimet-tyopaikat-salo')
def designer_avoimet_tyopaikat35(page=1):

    job_list = job_obj.get_job("designer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="salo")
	
@designer.route('/designer-avoimet-tyopaikat-kangasala')
def designer_avoimet_tyopaikat36(page=1):

    job_list = job_obj.get_job("designer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kangasala")
	
@designer.route('/designer-avoimet-tyopaikat-raisio')
def designer_avoimet_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("designer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="raisio")
	
@designer.route('/designer-avoimet-tyopaikat-karhula')
def designer_avoimet_tyopaikat37(page=1):

    job_list = job_obj.get_job("designer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="karhula")
	
@designer.route('/designer-avoimet-tyopaikat-kemi')
def designer_avoimet_tyopaikat38(page=1):

    job_list = job_obj.get_job("designer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kemi")
	
@designer.route('/designer-avoimet-tyopaikat-iisalmi')
def designer_avoimet_tyopaikat39(page=1):

    job_list = job_obj.get_job("designer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="iisalmi")
	
@designer.route('/designer-avoimet-tyopaikat-varkaus')
def designer_avoimet_tyopaikat40(page=1):

    job_list = job_obj.get_job("designer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="varkaus")
	
@designer.route('/designer-avoimet-tyopaikat-raahe')
def designer_avoimet_tyopaikat41(page=1):

    job_list = job_obj.get_job("designer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="raahe")
	
@designer.route('/designer-avoimet-tyopaikat-ylojarvi')
def designer_avoimet_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("designer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ylojarvi")
	
@designer.route('/designer-avoimet-tyopaikat-hamina')
def designer_avoimet_tyopaikat42(page=1):

    job_list = job_obj.get_job("designer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hamina")
	
@designer.route('/designer-avoimet-tyopaikat-kaarina')
def designer_avoimet_tyopaikat43(page=1):

    job_list = job_obj.get_job("designer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kaarina")
	
@designer.route('/designer-avoimet-tyopaikat-tornio')
def designer_avoimet_tyopaikat44(page=1):

    job_list = job_obj.get_job("designer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="tornio")
	
@designer.route('/designer-avoimet-tyopaikat-heinola')
def designer_avoimet_tyopaikat45(page=1):

    job_list = job_obj.get_job("designer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="heinola")
	
@designer.route('/designer-avoimet-tyopaikat-hollola')
def designer_avoimet_tyopaikat46(page=1):

    job_list = job_obj.get_job("designer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hollola")
	
@designer.route('/designer-avoimet-tyopaikat-valkeakoski')
def designer_avoimet_tyopaikat47(page=1):

    job_list = job_obj.get_job("designer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="valkeakoski")
	
@designer.route('/designer-avoimet-tyopaikat-siilinjarvi')
def designer_avoimet_tyopaikat48(page=1):

    job_list = job_obj.get_job("designer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="siilinjarvi")
	
@designer.route('/designer-avoimet-tyopaikat-kuusankoski')
def designer_avoimet_tyopaikat49(page=1):

    job_list = job_obj.get_job("designer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuusankoski")
	
@designer.route('/designer-avoimet-tyopaikat-sibbo')
def designer_avoimet_tyopaikat50(page=1):

    job_list = job_obj.get_job("designer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="sibbo")
	
@designer.route('/designer-avoimet-tyopaikat-jakostad')
def designer_avoimet_tyopaikat51(page=1):

    job_list = job_obj.get_job("designer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jakostad")
	
@designer.route('/designer-avoimet-tyopaikat-lempaala')
def designer_avoimet_tyopaikat52(page=1):

    job_list = job_obj.get_job("designer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lempaala")
	
@designer.route('/designer-avoimet-tyopaikat-mantsala')
def designer_avoimet_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("designer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="mantsala")
	
@designer.route('/designer-avoimet-tyopaikat-forssa')
def designer_avoimet_tyopaikat53(page=1):

    job_list = job_obj.get_job("designer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="forssa")
	
@designer.route('/designer-avoimet-tyopaikat-kuusamo')
def designer_avoimet_tyopaikat54(page=1):

    job_list = job_obj.get_job("designer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuusamo")
	
@designer.route('/designer-avoimet-tyopaikat-haukipudas')
def designer_avoimet_tyopaikat55(page=1):

    job_list = job_obj.get_job("designer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="haukipudas")
	
@designer.route('/designer-avoimet-tyopaikat-korsholm')
def designer_avoimet_tyopaikat56(page=1):

    job_list = job_obj.get_job("designer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="korsholm")
	
@designer.route('/designer-avoimet-tyopaikat-laukaa')
def designer_avoimet_tyopaikat57(page=1):

    job_list = job_obj.get_job("designer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="laukaa")
	
@designer.route('/designer-avoimet-tyopaikat-anjala')
def designer_avoimet_tyopaikat58(page=1):

    job_list = job_obj.get_job("designer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="anjala")
	
@designer.route('/designer-avoimet-tyopaikat-uusikaupunki')
def designer_avoimet_tyopaikat59(page=1):

    job_list = job_obj.get_job("designer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="uusikaupunki")
	
@designer.route('/designer-avoimet-tyopaikat-janakkala')
def designer_avoimet_tyopaikat60(page=1):

    job_list = job_obj.get_job("designer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="janakkala")
	
@designer.route('/designer-avoimet-tyopaikat-pirkkala')
def designer_avoimet_tyopaikat61(page=1):

    job_list = job_obj.get_job("designer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pirkkala")
	
@designer.route('/designer-avoimet-tyopaikat-lansi-turunmaa')
def designer_avoimet_tyopaikat62(page=1):

    job_list = job_obj.get_job("designer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lansi-turunmaa")
	
@designer.route('/designer-avoimet-tyopaikat-jamsa')
def designer_avoimet_tyopaikat63(page=1):

    job_list = job_obj.get_job("designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jamsa")
	
@designer.route('/designer-avoimet-tyopaikat-jamsa')
def designer_avoimet_tyopaikat64(page=1):

    job_list = job_obj.get_job("designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jamsa")
	
@designer.route('/designer-avoimet-tyopaikat-vammala')
def designer_avoimet_tyopaikat65(page=1):

    job_list = job_obj.get_job("designer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vammala")
	
@designer.route('/designer-avoimet-tyopaikat-nastola')
def designer_avoimet_tyopaikat66(page=1):

    job_list = job_obj.get_job("designer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nastola")
	
@designer.route('/designer-avoimet-tyopaikat-orimattila')
def designer_avoimet_tyopaikat67(page=1):

    job_list = job_obj.get_job("designer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="orimattila")
	
@designer.route('/designer-avoimet-tyopaikat-kauhajoki')
def designer_avoimet_tyopaikat68(page=1):

    job_list = job_obj.get_job("designer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kauhajoki")
	
@designer.route('/designer-avoimet-tyopaikat-ekenas')
def designer_avoimet_tyopaikat69(page=1):

    job_list = job_obj.get_job("designer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ekenas")
	
@designer.route('/designer-avoimet-tyopaikat-kempele')
def designer_avoimet_tyopaikat70(page=1):

    job_list = job_obj.get_job("designer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kempele")
	
@designer.route('/designer-avoimet-tyopaikat-lapua')
def designer_avoimet_tyopaikat71(page=1):

    job_list = job_obj.get_job("designer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lapua")
	
@designer.route('/designer-avoimet-tyopaikat-lieksa')
def designer_avoimet_tyopaikat72(page=1):

    job_list = job_obj.get_job("designer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lieksa")
	
@designer.route('/designer-avoimet-tyopaikat-naantali')
def designer_avoimet_tyopaikat73(page=1):

    job_list = job_obj.get_job("designer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="naantali")
	
@designer.route('/designer-avoimet-tyopaikat-aanekoski')
def designer_avoimet_tyopaikat74(page=1):

    job_list = job_obj.get_job("designer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="aanekoski")
	
@designer.route('/designer-avoimet-tyopaikat-ylivieska')
def designer_avoimet_tyopaikat75(page=1):

    job_list = job_obj.get_job("designer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ylivieska")
	
@designer.route('/designer-avoimet-tyopaikat-kontiolahti')
def designer_avoimet_tyopaikat76(page=1):

    job_list = job_obj.get_job("designer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kontiolahti")
	
@designer.route('/designer-avoimet-tyopaikat-kankaanpaa')
def designer_avoimet_tyopaikat77(page=1):

    job_list = job_obj.get_job("designer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kankaanpaa")
	
@designer.route('/designer-avoimet-tyopaikat-ulvila')
def designer_avoimet_tyopaikat78(page=1):

    job_list = job_obj.get_job("designer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ulvila")
	
@designer.route('/designer-avoimet-tyopaikat-pieksamaki')
def designer_avoimet_tyopaikat79(page=1):

    job_list = job_obj.get_job("designer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pieksamaki")
	
@designer.route('/designer-avoimet-tyopaikat-kiiminki')
def designer_avoimet_tyopaikat80(page=1):

    job_list = job_obj.get_job("designer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kiiminki")
	
@designer.route('/designer-avoimet-tyopaikat-pargas')
def designer_avoimet_tyopaikat81(page=1):

    job_list = job_obj.get_job("designer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pargas")
	
@designer.route('/designer-avoimet-tyopaikat-nurmo')
def designer_avoimet_tyopaikat82(page=1):

    job_list = job_obj.get_job("designer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nurmo")
	
@designer.route('/designer-avoimet-tyopaikat-ilmajoki')
def designer_avoimet_tyopaikat83(page=1):

    job_list = job_obj.get_job("designer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ilmajoki")
	
@designer.route('/designer-avoimet-tyopaikat-liperi')
def designer_avoimet_tyopaikat84(page=1):

    job_list = job_obj.get_job("designer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="liperi")
	
@designer.route('/designer-avoimet-tyopaikat-keuruu')
def designer_avoimet_tyopaikat85(page=1):

    job_list = job_obj.get_job("designer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="keuruu")
	
@designer.route('/designer-avoimet-tyopaikat-leppavirta')
def designer_avoimet_tyopaikat86(page=1):

    job_list = job_obj.get_job("designer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="leppavirta")
	
@designer.route('/designer-avoimet-tyopaikat-kurikka')
def designer_avoimet_tyopaikat87(page=1):

    job_list = job_obj.get_job("designer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kurikka")
	
@designer.route('/designer-avoimet-tyopaikat-nivala')
def designer_avoimet_tyopaikat88(page=1):

    job_list = job_obj.get_job("designer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nivala")
	
@designer.route('/designer-avoimet-tyopaikat-joutseno')
def designer_avoimet_tyopaikat89(page=1):

    job_list = job_obj.get_job("designer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="joutseno")
	
@designer.route('/designer-avoimet-tyopaikat-pedersore')
def designer_avoimet_tyopaikat90(page=1):

    job_list = job_obj.get_job("designer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pedersore")
	
@designer.route('/designer-avoimet-tyopaikat-sotkamo')
def designer_avoimet_tyopaikat91(page=1):

    job_list = job_obj.get_job("designer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="sotkamo")
	
@designer.route('/designer-avoimet-tyopaikat-kuhmo')
def designer_avoimet_tyopaikat92(page=1):

    job_list = job_obj.get_job("designer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuhmo")
	
@designer.route('/designer-avoimet-tyopaikat-paimio')
def designer_avoimet_tyopaikat93(page=1):

    job_list = job_obj.get_job("designer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="paimio")
	
@designer.route('/designer-avoimet-tyopaikat-saarijarvi')
def designer_avoimet_tyopaikat94(page=1):

    job_list = job_obj.get_job("designer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="saarijarvi")
	
@designer.route('/designer-avoimet-tyopaikat-helsinki')
def designer_avoimet_tyopaikat95(page=1):

    job_list = job_obj.get_job("designer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="helsinki")


####################################################################


##############################################
@designer.route('/designer-jobs-espoo')
def designer_jobs2(page=1):

    job_list = job_obj.get_job("designer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="espoo")

@designer.route('/designer-jobs-tampere')
def designer_jobs3(page=1):

    job_list = job_obj.get_job("designer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="tampere")
	
@designer.route('/designer-jobs-vantaa')
def designer_jobs4(page=1):

    job_list = job_obj.get_job("designer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vantaa")
	
@designer.route('/designer-jobs-turku')
def designer_jobs5(page=1):

    job_list = job_obj.get_job("designer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="turku")
	
@designer.route('/designer-jobs-oulu')
def designer_jobs6(page=1):

    job_list = job_obj.get_job("designer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="oulu")
	
@designer.route('/designer-jobs-lahti')
def designer_jobs7(page=1):

    job_list = job_obj.get_job("designer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lahti")
	
@designer.route('/designer-jobs-kuopio')
def designer_jobs8(page=1):

    job_list = job_obj.get_job("designer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuopio")
	
@designer.route('/designer-jobs-jyvvaskyla')
def designer_jobs9(page=1):

    job_list = job_obj.get_job("designer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jyvvaskyla")

@designer.route('/designer-jobs-pori')
def designer_jobs10(page=1):

    job_list = job_obj.get_job("designer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pori")

@designer.route('/designer-jobs-lappeenranta')
def designer_jobs11(page=1):

    job_list = job_obj.get_job("designer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lappeenranta")	
	
@designer.route('/designer-jobs-vaasa')
def designer_jobs12(page=1):

    job_list = job_obj.get_job("designer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vaasa")
	
@designer.route('/designer-jobs-kotka')
def designer_jobs13(page=1):

    job_list = job_obj.get_job("designer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kotka")
	
@designer.route('/designer-jobs-joensuu')
def designer_jobs14(page=1):

    job_list = job_obj.get_job("designer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="joensuu")
	
@designer.route('/designer-jobs-hameenlinna')
def designer_jobs15(page=1):

    job_list = job_obj.get_job("designer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hameenlinna")
	
@designer.route('/designer-jobs-porvoo')
def designer_jobs16(page=1):

    job_list = job_obj.get_job("designer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="porvoo")
	
@designer.route('/designer-jobs-mikkeli')
def designer_jobs17(page=1):

    job_list = job_obj.get_job("designer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="mikkeli")

@designer.route('/designer-jobs-hyvinkaa')
def designer_jobs18(page=1):

    job_list = job_obj.get_job("designer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hyvinkaa")
	
@designer.route('/designer-jobs-nurmijarvi')
def designer_jobs19(page=1):

    job_list = job_obj.get_job("designer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nurmijarvi")

@designer.route('/designer-jobs-jarvenpaa')
def designer_jobs20(page=1):

    job_list = job_obj.get_job("designer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jarvenpaa")
	
@designer.route('/designer-jobs-rauma')
def designer_jobs21(page=1):

    job_list = job_obj.get_job("designer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="rauma")
	
@designer.route('/designer-jobs-lohja')
def designer_jobs22(page=1):

    job_list = job_obj.get_job("designer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lohja")
	
@designer.route('/designer-jobs-karleby')
def designer_jobs23(page=1):

    job_list = job_obj.get_job("designer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="karleby")
	
@designer.route('/designer-jobs-kajaani')
def designer_jobs24(page=1):

    job_list = job_obj.get_job("designer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kajaani")
	
@designer.route('/designer-jobs-rovaniemi')
def designer_jobs25(page=1):

    job_list = job_obj.get_job("designer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="rovaniemi")
	
@designer.route('/designer-jobs-tuusula')
def designer_jobs26(page=1):

    job_list = job_obj.get_job("designer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="tuusula")
	
@designer.route('/designer-jobs-kirkkonummi')
def designer_jobs27(page=1):

    job_list = job_obj.get_job("designer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kirkkonummi")
	
@designer.route('/designer-jobs-seinajoki')
def designer_jobs28(page=1):

    job_list = job_obj.get_job("designer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="seinajoki")
	
@designer.route('/designer-jobs-kerava')
def designer_jobs29(page=1):

    job_list = job_obj.get_job("designer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kerava")
	
@designer.route('/designer-jobs-kouvola')
def designer_jobs30(page=1):

    job_list = job_obj.get_job("designer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kouvola")
	
@designer.route('/designer-jobs-imatra')
def designer_jobs31(page=1):

    job_list = job_obj.get_job("designer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="imatra")
	
@designer.route('/designer-jobs-nokia')
def designer_jobs32_1(page=1):

    job_list = job_obj.get_job("designer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nokia")
	
@designer.route('/designer-jobs-savonlinna')
def designer_jobs32(page=1):

    job_list = job_obj.get_job("designer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="savonlinna")
	
@designer.route('/designer-jobs-riihimaki')
def designer_jobs33(page=1):

    job_list = job_obj.get_job("designer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="riihimaki")
	
@designer.route('/designer-jobs-vihti')
def designer_jobs34(page=1):

    job_list = job_obj.get_job("designer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vihti")
	
@designer.route('/designer-jobs-salo')
def designer_jobs35(page=1):

    job_list = job_obj.get_job("designer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="salo")
	
@designer.route('/designer-jobs-kangasala')
def designer_jobs36(page=1):

    job_list = job_obj.get_job("designer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kangasala")
	
@designer.route('/designer-jobs-raisio')
def designer_jobs37_1(page=1):

    job_list = job_obj.get_job("designer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="raisio")
	
@designer.route('/designer-jobs-karhula')
def designer_jobs37(page=1):

    job_list = job_obj.get_job("designer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="karhula")
	
@designer.route('/designer-jobs-kemi')
def designer_jobs38(page=1):

    job_list = job_obj.get_job("designer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kemi")
	
@designer.route('/designer-jobs-iisalmi')
def designer_jobs39(page=1):

    job_list = job_obj.get_job("designer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="iisalmi")
	
@designer.route('/designer-jobs-varkaus')
def designer_jobs40(page=1):

    job_list = job_obj.get_job("designer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="varkaus")
	
@designer.route('/designer-jobs-raahe')
def designer_jobs41(page=1):

    job_list = job_obj.get_job("designer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="raahe")
	
@designer.route('/designer-jobs-ylojarvi')
def designer_jobs42_1(page=1):

    job_list = job_obj.get_job("designer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ylojarvi")
	
@designer.route('/designer-jobs-hamina')
def designer_jobs42(page=1):

    job_list = job_obj.get_job("designer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hamina")
	
@designer.route('/designer-jobs-kaarina')
def designer_jobs43(page=1):

    job_list = job_obj.get_job("designer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kaarina")
	
@designer.route('/designer-jobs-tornio')
def designer_jobs44(page=1):

    job_list = job_obj.get_job("designer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="tornio")
	
@designer.route('/designer-jobs-heinola')
def designer_jobs45(page=1):

    job_list = job_obj.get_job("designer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="heinola")
	
@designer.route('/designer-jobs-hollola')
def designer_jobs46(page=1):

    job_list = job_obj.get_job("designer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hollola")
	
@designer.route('/designer-jobs-valkeakoski')
def designer_jobs47(page=1):

    job_list = job_obj.get_job("designer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="valkeakoski")
	
@designer.route('/designer-jobs-siilinjarvi')
def designer_jobs48(page=1):

    job_list = job_obj.get_job("designer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="siilinjarvi")
	
@designer.route('/designer-jobs-kuusankoski')
def designer_jobs49(page=1):

    job_list = job_obj.get_job("designer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuusankoski")
	
@designer.route('/designer-jobs-sibbo')
def designer_jobs50(page=1):

    job_list = job_obj.get_job("designer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="sibbo")
	
@designer.route('/designer-jobs-jakostad')
def designer_jobs51(page=1):

    job_list = job_obj.get_job("designer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jakostad")
	
@designer.route('/designer-jobs-lempaala')
def designer_jobs52(page=1):

    job_list = job_obj.get_job("designer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lempaala")
	
@designer.route('/designer-jobs-mantsala')
def designer_jobs52_1(page=1):

    job_list = job_obj.get_job("designer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="mantsala")
	
@designer.route('/designer-jobs-forssa')
def designer_jobs53(page=1):

    job_list = job_obj.get_job("designer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="forssa")
	
@designer.route('/designer-jobs-kuusamo')
def designer_jobs54(page=1):

    job_list = job_obj.get_job("designer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuusamo")
	
@designer.route('/designer-jobs-haukipudas')
def designer_jobs55(page=1):

    job_list = job_obj.get_job("designer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="haukipudas")
	
@designer.route('/designer-jobs-korsholm')
def designer_jobs56(page=1):

    job_list = job_obj.get_job("designer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="korsholm")
	
@designer.route('/designer-jobs-laukaa')
def designer_jobs57(page=1):

    job_list = job_obj.get_job("designer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="laukaa")
	
@designer.route('/designer-jobs-anjala')
def designer_jobs58(page=1):

    job_list = job_obj.get_job("designer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="anjala")
	
@designer.route('/designer-jobs-uusikaupunki')
def designer_jobs59(page=1):

    job_list = job_obj.get_job("designer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="uusikaupunki")
	
@designer.route('/designer-jobs-janakkala')
def designer_jobs60(page=1):

    job_list = job_obj.get_job("designer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="janakkala")
	
@designer.route('/designer-jobs-pirkkala')
def designer_jobs61(page=1):

    job_list = job_obj.get_job("designer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pirkkala")
	
@designer.route('/designer-jobs-lansi-turunmaa')
def designer_jobs62(page=1):

    job_list = job_obj.get_job("designer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lansi-turunmaa")
	
@designer.route('/designer-jobs-jamsa')
def designer_jobs63(page=1):

    job_list = job_obj.get_job("designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jamsa")
	
@designer.route('/designer-jobs-jamsa')
def designer_jobs64(page=1):

    job_list = job_obj.get_job("designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jamsa")
	
@designer.route('/designer-jobs-vammala')
def designer_jobs65(page=1):

    job_list = job_obj.get_job("designer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vammala")
	
@designer.route('/designer-jobs-nastola')
def designer_jobs66(page=1):

    job_list = job_obj.get_job("designer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nastola")
	
@designer.route('/designer-jobs-orimattila')
def designer_jobs67(page=1):

    job_list = job_obj.get_job("designer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="orimattila")
	
@designer.route('/designer-jobs-kauhajoki')
def designer_jobs68(page=1):

    job_list = job_obj.get_job("designer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kauhajoki")
	
@designer.route('/designer-jobs-ekenas')
def designer_jobs69(page=1):

    job_list = job_obj.get_job("designer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ekenas")
	
@designer.route('/designer-jobs-kempele')
def designer_jobs70(page=1):

    job_list = job_obj.get_job("designer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kempele")
	
@designer.route('/designer-jobs-lapua')
def designer_jobs71(page=1):

    job_list = job_obj.get_job("designer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lapua")
	
@designer.route('/designer-jobs-lieksa')
def designer_jobs72(page=1):

    job_list = job_obj.get_job("designer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lieksa")
	
@designer.route('/designer-jobs-naantali')
def designer_jobs73(page=1):

    job_list = job_obj.get_job("designer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="naantali")
	
@designer.route('/designer-jobs-aanekoski')
def designer_jobs74(page=1):

    job_list = job_obj.get_job("designer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="aanekoski")
	
@designer.route('/designer-jobs-ylivieska')
def designer_jobs75(page=1):

    job_list = job_obj.get_job("designer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ylivieska")
	
@designer.route('/designer-jobs-kontiolahti')
def designer_jobs76(page=1):

    job_list = job_obj.get_job("designer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kontiolahti")
	
@designer.route('/designer-jobs-kankaanpaa')
def designer_jobs77(page=1):

    job_list = job_obj.get_job("designer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kankaanpaa")
	
@designer.route('/designer-jobs-ulvila')
def designer_jobs78(page=1):

    job_list = job_obj.get_job("designer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ulvila")
	
@designer.route('/designer-jobs-pieksamaki')
def designer_jobs79(page=1):

    job_list = job_obj.get_job("designer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pieksamaki")
	
@designer.route('/designer-jobs-kiiminki')
def designer_jobs80(page=1):

    job_list = job_obj.get_job("designer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kiiminki")
	
@designer.route('/designer-jobs-pargas')
def designer_jobs81(page=1):

    job_list = job_obj.get_job("designer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pargas")
	
@designer.route('/designer-jobs-nurmo')
def designer_jobs82(page=1):

    job_list = job_obj.get_job("designer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nurmo")
	
@designer.route('/designer-jobs-ilmajoki')
def designer_jobs83(page=1):

    job_list = job_obj.get_job("designer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ilmajoki")
	
@designer.route('/designer-jobs-liperi')
def designer_jobs84(page=1):

    job_list = job_obj.get_job("designer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="liperi")
	
@designer.route('/designer-jobs-keuruu')
def designer_jobs85(page=1):

    job_list = job_obj.get_job("designer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="keuruu")
	
@designer.route('/designer-jobs-leppavirta')
def designer_jobs86(page=1):

    job_list = job_obj.get_job("designer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="leppavirta")
	
@designer.route('/designer-jobs-kurikka')
def designer_jobs87(page=1):

    job_list = job_obj.get_job("designer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kurikka")
	
@designer.route('/designer-jobs-nivala')
def designer_jobs88(page=1):

    job_list = job_obj.get_job("designer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nivala")
	
@designer.route('/designer-jobs-joutseno')
def designer_jobs89(page=1):

    job_list = job_obj.get_job("designer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="joutseno")
	
@designer.route('/designer-jobs-pedersore')
def designer_jobs90(page=1):

    job_list = job_obj.get_job("designer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pedersore")
	
@designer.route('/designer-jobs-sotkamo')
def designer_jobs91(page=1):

    job_list = job_obj.get_job("designer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="sotkamo")
	
@designer.route('/designer-jobs-kuhmo')
def designer_jobs92(page=1):

    job_list = job_obj.get_job("designer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuhmo")
	
@designer.route('/designer-jobs-paimio')
def designer_jobs93(page=1):

    job_list = job_obj.get_job("designer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="paimio")
	
@designer.route('/designer-jobs-saarijarvi')
def designer_jobs94(page=1):

    job_list = job_obj.get_job("designer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="saarijarvi")
	
@designer.route('/designer-jobs-helsinki')
def designer_jobs95(page=1):

    job_list = job_obj.get_job("designer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="helsinki")


####################################################################
##############################################
@designer.route('/designer-tyopaikat-espoo')
def designer_tyopaikat2(page=1):

    job_list = job_obj.get_job("designer ", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="espoo")

@designer.route('/designer-tyopaikat-tampere')
def designer_tyopaikat3(page=1):

    job_list = job_obj.get_job("designer ", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="tampere")
	
@designer.route('/designer-tyopaikat-vantaa')
def designer_tyopaikat4(page=1):

    job_list = job_obj.get_job("designer ", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vantaa")
	
@designer.route('/designer-tyopaikat-turku')
def designer_tyopaikat5(page=1):

    job_list = job_obj.get_job("designer ", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="turku")
	
@designer.route('/designer-tyopaikat-oulu')
def designer_tyopaikat6(page=1):

    job_list = job_obj.get_job("designer ", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="oulu")
	
@designer.route('/designer-tyopaikat-lahti')
def designer_tyopaikat7(page=1):

    job_list = job_obj.get_job("designer ", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lahti")
	
@designer.route('/designer-tyopaikat-kuopio')
def designer_tyopaikat8(page=1):

    job_list = job_obj.get_job("designer ", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuopio")
	
@designer.route('/designer-tyopaikat-jyvvaskyla')
def designer_tyopaikat9(page=1):

    job_list = job_obj.get_job("designer ", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jyvvaskyla")

@designer.route('/designer-tyopaikat-pori')
def designer_tyopaikat10(page=1):

    job_list = job_obj.get_job("designer ", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pori")

@designer.route('/designer-tyopaikat-lappeenranta')
def designer_tyopaikat11(page=1):

    job_list = job_obj.get_job("designer ", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lappeenranta")	
	
@designer.route('/designer-tyopaikat-vaasa')
def designer_tyopaikat12(page=1):

    job_list = job_obj.get_job("designer ", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vaasa")
	
@designer.route('/designer-tyopaikat-kotka')
def designer_tyopaikat13(page=1):

    job_list = job_obj.get_job("designer ", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kotka")
	
@designer.route('/designer-tyopaikat-joensuu')
def designer_tyopaikat14(page=1):

    job_list = job_obj.get_job("designer ", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="joensuu")
	
@designer.route('/designer-tyopaikat-hameenlinna')
def designer_tyopaikat15(page=1):

    job_list = job_obj.get_job("designer ", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hameenlinna")
	
@designer.route('/designer-tyopaikat-porvoo')
def designer_tyopaikat16(page=1):

    job_list = job_obj.get_job("designer ", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="porvoo")
	
@designer.route('/designer-tyopaikat-mikkeli')
def designer_tyopaikat17(page=1):

    job_list = job_obj.get_job("designer ", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="mikkeli")

@designer.route('/designer-tyopaikat-hyvinkaa')
def designer_tyopaikat18(page=1):

    job_list = job_obj.get_job("designer ", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hyvinkaa")
	
@designer.route('/designer-tyopaikat-nurmijarvi')
def designer_tyopaikat19(page=1):

    job_list = job_obj.get_job("designer ", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nurmijarvi")

@designer.route('/designer-tyopaikat-jarvenpaa')
def designer_tyopaikat20(page=1):

    job_list = job_obj.get_job("designer ", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jarvenpaa")
	
@designer.route('/designer-tyopaikat-rauma')
def designer_tyopaikat21(page=1):

    job_list = job_obj.get_job("designer ", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="rauma")
	
@designer.route('/designer-tyopaikat-lohja')
def designer_tyopaikat22(page=1):

    job_list = job_obj.get_job("designer ", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lohja")
	
@designer.route('/designer-tyopaikat-karleby')
def designer_tyopaikat23(page=1):

    job_list = job_obj.get_job("designer ", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="karleby")
	
@designer.route('/designer-tyopaikat-kajaani')
def designer_tyopaikat24(page=1):

    job_list = job_obj.get_job("designer ", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kajaani")
	
@designer.route('/designer-tyopaikat-rovaniemi')
def designer_tyopaikat25(page=1):

    job_list = job_obj.get_job("designer ", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="rovaniemi")
	
@designer.route('/designer-tyopaikat-tuusula')
def designer_tyopaikat26(page=1):

    job_list = job_obj.get_job("designer ", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="tuusula")
	
@designer.route('/designer-tyopaikat-kirkkonummi')
def designer_tyopaikat27(page=1):

    job_list = job_obj.get_job("designer ", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kirkkonummi")
	
@designer.route('/designer-tyopaikat-seinajoki')
def designer_tyopaikat28(page=1):

    job_list = job_obj.get_job("designer ", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="seinajoki")
	
@designer.route('/designer-tyopaikat-kerava')
def designer_tyopaikat29(page=1):

    job_list = job_obj.get_job("designer ", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kerava")
	
@designer.route('/designer-tyopaikat-kouvola')
def designer_tyopaikat30(page=1):

    job_list = job_obj.get_job("designer ", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kouvola")
	
@designer.route('/designer-tyopaikat-imatra')
def designer_tyopaikat31(page=1):

    job_list = job_obj.get_job("designer ", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="imatra")
	
@designer.route('/designer-tyopaikat-nokia')
def designer_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("designer ", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nokia")
	
@designer.route('/designer-tyopaikat-savonlinna')
def designer_tyopaikat32(page=1):

    job_list = job_obj.get_job("designer ", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="savonlinna")
	
@designer.route('/designer-tyopaikat-riihimaki')
def designer_tyopaikat33(page=1):

    job_list = job_obj.get_job("designer ", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="riihimaki")
	
@designer.route('/designer-tyopaikat-vihti')
def designer_tyopaikat34(page=1):

    job_list = job_obj.get_job("designer ", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vihti")
	
@designer.route('/designer-tyopaikat-salo')
def designer_tyopaikat35(page=1):

    job_list = job_obj.get_job("designer ", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="salo")
	
@designer.route('/designer-tyopaikat-kangasala')
def designer_tyopaikat36(page=1):

    job_list = job_obj.get_job("designer ", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kangasala")
	
@designer.route('/designer-tyopaikat-raisio')
def designer_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("designer ", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="raisio")
	
@designer.route('/designer-tyopaikat-karhula')
def designer_tyopaikat37(page=1):

    job_list = job_obj.get_job("designer ", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="karhula")
	
@designer.route('/designer-tyopaikat-kemi')
def designer_tyopaikat38(page=1):

    job_list = job_obj.get_job("designer ", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kemi")
	
@designer.route('/designer-tyopaikat-iisalmi')
def designer_tyopaikat39(page=1):

    job_list = job_obj.get_job("designer ", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="iisalmi")
	
@designer.route('/designer-tyopaikat-varkaus')
def designer_tyopaikat40(page=1):

    job_list = job_obj.get_job("designer ", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="varkaus")
	
@designer.route('/designer-tyopaikat-raahe')
def designer_tyopaikat41(page=1):

    job_list = job_obj.get_job("designer ", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="raahe")
	
@designer.route('/designer-tyopaikat-ylojarvi')
def designer_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("designer ", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ylojarvi")
	
@designer.route('/designer-tyopaikat-hamina')
def designer_tyopaikat42(page=1):

    job_list = job_obj.get_job("designer ", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hamina")
	
@designer.route('/designer-tyopaikat-kaarina')
def designer_tyopaikat43(page=1):

    job_list = job_obj.get_job("designer ", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kaarina")
	
@designer.route('/designer-tyopaikat-tornio')
def designer_tyopaikat44(page=1):

    job_list = job_obj.get_job("designer ", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="tornio")
	
@designer.route('/designer-tyopaikat-heinola')
def designer_tyopaikat45(page=1):

    job_list = job_obj.get_job("designer ", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="heinola")
	
@designer.route('/designer-tyopaikat-hollola')
def designer_tyopaikat46(page=1):

    job_list = job_obj.get_job("designer ", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="hollola")
	
@designer.route('/designer-tyopaikat-valkeakoski')
def designer_tyopaikat47(page=1):

    job_list = job_obj.get_job("designer ", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="valkeakoski")
	
@designer.route('/designer-tyopaikat-siilinjarvi')
def designer_tyopaikat48(page=1):

    job_list = job_obj.get_job("designer ", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="siilinjarvi")
	
@designer.route('/designer-tyopaikat-kuusankoski')
def designer_tyopaikat49(page=1):

    job_list = job_obj.get_job("designer ", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuusankoski")
	
@designer.route('/designer-tyopaikat-sibbo')
def designer_tyopaikat50(page=1):

    job_list = job_obj.get_job("designer ", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="sibbo")
	
@designer.route('/designer-tyopaikat-jakostad')
def designer_tyopaikat51(page=1):

    job_list = job_obj.get_job("designer ", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jakostad")
	
@designer.route('/designer-tyopaikat-lempaala')
def designer_tyopaikat52(page=1):

    job_list = job_obj.get_job("designer ", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lempaala")
	
@designer.route('/designer-tyopaikat-mantsala')
def designer_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("designer ", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="mantsala")
	
@designer.route('/designer-tyopaikat-forssa')
def designer_tyopaikat53(page=1):

    job_list = job_obj.get_job("designer ", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="forssa")
	
@designer.route('/designer-tyopaikat-kuusamo')
def designer_tyopaikat54(page=1):

    job_list = job_obj.get_job("designer ", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuusamo")
	
@designer.route('/designer-tyopaikat-haukipudas')
def designer_tyopaikat55(page=1):

    job_list = job_obj.get_job("designer ", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="haukipudas")
	
@designer.route('/designer-tyopaikat-korsholm')
def designer_tyopaikat56(page=1):

    job_list = job_obj.get_job("designer ", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="korsholm")
	
@designer.route('/designer-tyopaikat-laukaa')
def designer_tyopaikat57(page=1):

    job_list = job_obj.get_job("designer ", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="laukaa")
	
@designer.route('/designer-tyopaikat-anjala')
def designer_tyopaikat58(page=1):

    job_list = job_obj.get_job("designer ", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="anjala")
	
@designer.route('/designer-tyopaikat-uusikaupunki')
def designer_tyopaikat59(page=1):

    job_list = job_obj.get_job("designer ", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="uusikaupunki")
	
@designer.route('/designer-tyopaikat-janakkala')
def designer_tyopaikat60(page=1):

    job_list = job_obj.get_job("designer ", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="janakkala")
	
@designer.route('/designer-tyopaikat-pirkkala')
def designer_tyopaikat61(page=1):

    job_list = job_obj.get_job("designer ", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pirkkala")
	
@designer.route('/designer-tyopaikat-lansi-turunmaa')
def designer_tyopaikat62(page=1):

    job_list = job_obj.get_job("designer ", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lansi-turunmaa")
	
@designer.route('/designer-tyopaikat-jamsa')
def designer_tyopaikat63(page=1):

    job_list = job_obj.get_job("designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jamsa")
	
@designer.route('/designer-tyopaikat-jamsa')
def designer_tyopaikat64(page=1):

    job_list = job_obj.get_job("designer ", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="jamsa")
	
@designer.route('/designer-tyopaikat-vammala')
def designer_tyopaikat65(page=1):

    job_list = job_obj.get_job("designer ", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="vammala")
	
@designer.route('/designer-tyopaikat-nastola')
def designer_tyopaikat66(page=1):

    job_list = job_obj.get_job("designer ", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nastola")
	
@designer.route('/designer-tyopaikat-orimattila')
def designer_tyopaikat67(page=1):

    job_list = job_obj.get_job("designer ", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="orimattila")
	
@designer.route('/designer-tyopaikat-kauhajoki')
def designer_tyopaikat68(page=1):

    job_list = job_obj.get_job("designer ", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kauhajoki")
	
@designer.route('/designer-tyopaikat-ekenas')
def designer_tyopaikat69(page=1):

    job_list = job_obj.get_job("designer ", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ekenas")
	
@designer.route('/designer-tyopaikat-kempele')
def designer_tyopaikat70(page=1):

    job_list = job_obj.get_job("designer ", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kempele")
	
@designer.route('/designer-tyopaikat-lapua')
def designer_tyopaikat71(page=1):

    job_list = job_obj.get_job("designer ", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lapua")
	
@designer.route('/designer-tyopaikat-lieksa')
def designer_tyopaikat72(page=1):

    job_list = job_obj.get_job("designer ", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="lieksa")
	
@designer.route('/designer-tyopaikat-naantali')
def designer_tyopaikat73(page=1):

    job_list = job_obj.get_job("designer ", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="naantali")
	
@designer.route('/designer-tyopaikat-aanekoski')
def designer_tyopaikat74(page=1):

    job_list = job_obj.get_job("designer ", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="aanekoski")
	
@designer.route('/designer-tyopaikat-ylivieska')
def designer_tyopaikat75(page=1):

    job_list = job_obj.get_job("designer ", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ylivieska")
	
@designer.route('/designer-tyopaikat-kontiolahti')
def designer_tyopaikat76(page=1):

    job_list = job_obj.get_job("designer ", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kontiolahti")
	
@designer.route('/designer-tyopaikat-kankaanpaa')
def designer_tyopaikat77(page=1):

    job_list = job_obj.get_job("designer ", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kankaanpaa")
	
@designer.route('/designer-tyopaikat-ulvila')
def designer_tyopaikat78(page=1):

    job_list = job_obj.get_job("designer ", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ulvila")
	
@designer.route('/designer-tyopaikat-pieksamaki')
def designer_tyopaikat79(page=1):

    job_list = job_obj.get_job("designer ", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pieksamaki")
	
@designer.route('/designer-tyopaikat-kiiminki')
def designer_tyopaikat80(page=1):

    job_list = job_obj.get_job("designer ", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kiiminki")
	
@designer.route('/designer-tyopaikat-pargas')
def designer_tyopaikat81(page=1):

    job_list = job_obj.get_job("designer ", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pargas")
	
@designer.route('/designer-tyopaikat-nurmo')
def designer_tyopaikat82(page=1):

    job_list = job_obj.get_job("designer ", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nurmo")
	
@designer.route('/designer-tyopaikat-ilmajoki')
def designer_tyopaikat83(page=1):

    job_list = job_obj.get_job("designer ", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="ilmajoki")
	
@designer.route('/designer-tyopaikat-liperi')
def designer_tyopaikat84(page=1):

    job_list = job_obj.get_job("designer ", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="liperi")
	
@designer.route('/designer-tyopaikat-keuruu')
def designer_tyopaikat85(page=1):

    job_list = job_obj.get_job("designer ", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="keuruu")
	
@designer.route('/designer-tyopaikat-leppavirta')
def designer_tyopaikat86(page=1):

    job_list = job_obj.get_job("designer ", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="leppavirta")
	
@designer.route('/designer-tyopaikat-kurikka')
def designer_tyopaikat87(page=1):

    job_list = job_obj.get_job("designer ", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kurikka")
	
@designer.route('/designer-tyopaikat-nivala')
def designer_tyopaikat88(page=1):

    job_list = job_obj.get_job("designer ", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="nivala")
	
@designer.route('/designer-tyopaikat-joutseno')
def designer_tyopaikat89(page=1):

    job_list = job_obj.get_job("designer ", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="joutseno")
	
@designer.route('/designer-tyopaikat-pedersore')
def designer_tyopaikat90(page=1):

    job_list = job_obj.get_job("designer ", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="pedersore")
	
@designer.route('/designer-tyopaikat-sotkamo')
def designer_tyopaikat91(page=1):

    job_list = job_obj.get_job("designer ", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="sotkamo")
	
@designer.route('/designer-tyopaikat-kuhmo')
def designer_tyopaikat92(page=1):

    job_list = job_obj.get_job("designer ", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="kuhmo")
	
@designer.route('/designer-tyopaikat-paimio')
def designer_tyopaikat93(page=1):

    job_list = job_obj.get_job("designer ", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="paimio")
	
@designer.route('/designer-tyopaikat-saarijarvi')
def designer_tyopaikat94(page=1):

    job_list = job_obj.get_job("designer ", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="saarijarvi")
	
@designer.route('/designer-tyopaikat-helsinki')
def designer_tyopaikat95(page=1):

    job_list = job_obj.get_job("designer ", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="designer ", location="helsinki")


####################################################################

