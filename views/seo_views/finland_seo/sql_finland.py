from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

sql = Blueprint('sql', __name__)
job_obj = Job()



####################################################################


@sql.route('/sql_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "sql" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def sql_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="espoo")

@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def sql_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="tampere")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def sql_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="vantaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def sql_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="turku")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def sql_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="oulu")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def sql_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="lahti")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def sql_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kuopio")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def sql_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="jyvvaskyla")

@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def sql_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="pori")

@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def sql_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="lappeenranta")	
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def sql_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="vaasa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def sql_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kotka")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def sql_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="joensuu")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def sql_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="hameenlinna")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def sql_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="porvoo")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def sql_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="mikkeli")

@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def sql_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="hyvinkaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def sql_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="nurmijarvi")

@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def sql_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="jarvenpaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def sql_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="rauma")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def sql_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="lohja")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def sql_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="karleby")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def sql_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kajaani")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def sql_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="rovaniemi")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def sql_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="tuusula")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def sql_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kirkkonummi")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def sql_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="seinajoki")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def sql_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kerava")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def sql_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kouvola")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def sql_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="imatra")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def sql_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="nokia")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def sql_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="savonlinna")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def sql_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="riihimaki")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def sql_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="vihti")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def sql_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="salo")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def sql_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kangasala")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def sql_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="raisio")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def sql_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="karhula")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def sql_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kemi")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def sql_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="iisalmi")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def sql_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="varkaus")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def sql_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="raahe")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def sql_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="ylojarvi")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def sql_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="hamina")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def sql_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kaarina")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def sql_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="tornio")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def sql_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="heinola")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def sql_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="hollola")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def sql_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="valkeakoski")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def sql_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="siilinjarvi")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def sql_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kuusankoski")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def sql_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="sibbo")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def sql_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="jakostad")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def sql_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="lempaala")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def sql_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="mantsala")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def sql_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="forssa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def sql_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kuusamo")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def sql_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="haukipudas")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def sql_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="korsholm")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def sql_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="laukaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def sql_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="anjala")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def sql_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="uusikaupunki")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def sql_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="janakkala")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def sql_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="pirkkala")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def sql_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def sql_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="jamsa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def sql_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="jamsa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def sql_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="vammala")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def sql_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="nastola")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def sql_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="orimattila")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def sql_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kauhajoki")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def sql_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="ekenas")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def sql_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kempele")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def sql_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="lapua")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def sql_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="lieksa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def sql_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="naantali")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def sql_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="aanekoski")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def sql_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="ylivieska")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def sql_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kontiolahti")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def sql_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kankaanpaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def sql_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="ulvila")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def sql_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="pieksamaki")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def sql_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kiiminki")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def sql_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="pargas")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def sql_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="nurmo")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def sql_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="ilmajoki")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def sql_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="liperi")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def sql_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="keuruu")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def sql_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="leppavirta")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def sql_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kurikka")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def sql_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="nivala")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def sql_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="joutseno")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def sql_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="pedersore")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def sql_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="sotkamo")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def sql_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="kuhmo")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def sql_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="paimio")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def sql_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="saarijarvi")
	
@sql.route('/sql-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def sql_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("sql ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@sql.route('/sql-software-developer-jobs-espoo')
def sql_software_developer2(page=1):

    job_list = job_obj.get_job("sql software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="espoo")

@sql.route('/sql-software-developer-jobs-tampere')
def sql_software_developer3(page=1):

    job_list = job_obj.get_job("sql software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="tampere")
	
@sql.route('/sql-software-developer-jobs-vantaa')
def sql_software_developer4(page=1):

    job_list = job_obj.get_job("sql software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="vantaa")
	
@sql.route('/sql-software-developer-jobs-turku')
def sql_software_developer5(page=1):

    job_list = job_obj.get_job("sql software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="turku")
	
@sql.route('/sql-software-developer-jobs-oulu')
def sql_software_developer6(page=1):

    job_list = job_obj.get_job("sql software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="oulu")
	
@sql.route('/sql-software-developer-jobs-lahti')
def sql_software_developer7(page=1):

    job_list = job_obj.get_job("sql software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="lahti")
	
@sql.route('/sql-software-developer-jobs-kuopio')
def sql_software_developer8(page=1):

    job_list = job_obj.get_job("sql software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kuopio")
	
@sql.route('/sql-software-developer-jobs-jyvvaskyla')
def sql_software_developer9(page=1):

    job_list = job_obj.get_job("sql software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="jyvvaskyla")

@sql.route('/sql-software-developer-jobs-pori')
def sql_software_developer10(page=1):

    job_list = job_obj.get_job("sql software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="pori")

@sql.route('/sql-software-developer-jobs-lappeenranta')
def sql_software_developer11(page=1):

    job_list = job_obj.get_job("sql software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="lappeenranta")	
	
@sql.route('/sql-software-developer-jobs-vaasa')
def sql_software_developer12(page=1):

    job_list = job_obj.get_job("sql software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="vaasa")
	
@sql.route('/sql-software-developer-jobs-kotka')
def sql_software_developer13(page=1):

    job_list = job_obj.get_job("sql software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kotka")
	
@sql.route('/sql-software-developer-jobs-joensuu')
def sql_software_developer14(page=1):

    job_list = job_obj.get_job("sql software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="joensuu")
	
@sql.route('/sql-software-developer-jobs-hameenlinna')
def sql_software_developer15(page=1):

    job_list = job_obj.get_job("sql software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="hameenlinna")
	
@sql.route('/sql-software-developer-jobs-porvoo')
def sql_software_developer16(page=1):

    job_list = job_obj.get_job("sql software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="porvoo")
	
@sql.route('/sql-software-developer-jobs-mikkeli')
def sql_software_developer17(page=1):

    job_list = job_obj.get_job("sql software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="mikkeli")

@sql.route('/sql-software-developer-jobs-hyvinkaa')
def sql_software_developer18(page=1):

    job_list = job_obj.get_job("sql software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="hyvinkaa")
	
@sql.route('/sql-software-developer-jobs-nurmijarvi')
def sql_software_developer19(page=1):

    job_list = job_obj.get_job("sql software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="nurmijarvi")

@sql.route('/sql-software-developer-jobs-jarvenpaa')
def sql_software_developer20(page=1):

    job_list = job_obj.get_job("sql software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="jarvenpaa")
	
@sql.route('/sql-software-developer-jobs-rauma')
def sql_software_developer21(page=1):

    job_list = job_obj.get_job("sql software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="rauma")
	
@sql.route('/sql-software-developer-jobs-lohja')
def sql_software_developer22(page=1):

    job_list = job_obj.get_job("sql software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="lohja")
	
@sql.route('/sql-software-developer-jobs-karleby')
def sql_software_developer23(page=1):

    job_list = job_obj.get_job("sql software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="karleby")
	
@sql.route('/sql-software-developer-jobs-kajaani')
def sql_software_developer24(page=1):

    job_list = job_obj.get_job("sql software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kajaani")
	
@sql.route('/sql-software-developer-jobs-rovaniemi')
def sql_software_developer25(page=1):

    job_list = job_obj.get_job("sql software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="rovaniemi")
	
@sql.route('/sql-software-developer-jobs-tuusula')
def sql_software_developer26(page=1):

    job_list = job_obj.get_job("sql software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="tuusula")
	
@sql.route('/sql-software-developer-jobs-kirkkonummi')
def sql_software_developer27(page=1):

    job_list = job_obj.get_job("sql software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kirkkonummi")
	
@sql.route('/sql-software-developer-jobs-seinajoki')
def sql_software_developer28(page=1):

    job_list = job_obj.get_job("sql software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="seinajoki")
	
@sql.route('/sql-software-developer-jobs-kerava')
def sql_software_developer29(page=1):

    job_list = job_obj.get_job("sql software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kerava")
	
@sql.route('/sql-software-developer-jobs-kouvola')
def sql_software_developer30(page=1):

    job_list = job_obj.get_job("sql software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kouvola")
	
@sql.route('/sql-software-developer-jobs-imatra')
def sql_software_developer31(page=1):

    job_list = job_obj.get_job("sql software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="imatra")
	
@sql.route('/sql-software-developer-jobs-nokia')
def sql_software_developer32_1(page=1):

    job_list = job_obj.get_job("sql software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="nokia")
	
@sql.route('/sql-software-developer-jobs-savonlinna')
def sql_software_developer32(page=1):

    job_list = job_obj.get_job("sql software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="savonlinna")
	
@sql.route('/sql-software-developer-jobs-riihimaki')
def sql_software_developer33(page=1):

    job_list = job_obj.get_job("sql software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="riihimaki")
	
@sql.route('/sql-software-developer-jobs-vihti')
def sql_software_developer34(page=1):

    job_list = job_obj.get_job("sql software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="vihti")
	
@sql.route('/sql-software-developer-jobs-salo')
def sql_software_developer35(page=1):

    job_list = job_obj.get_job("sql software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="salo")
	
@sql.route('/sql-software-developer-jobs-kangasala')
def sql_software_developer36(page=1):

    job_list = job_obj.get_job("sql software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kangasala")
	
@sql.route('/sql-software-developer-jobs-raisio')
def sql_software_developer37_1(page=1):

    job_list = job_obj.get_job("sql software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="raisio")
	
@sql.route('/sql-software-developer-jobs-karhula')
def sql_software_developer37(page=1):

    job_list = job_obj.get_job("sql software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="karhula")
	
@sql.route('/sql-software-developer-jobs-kemi')
def sql_software_developer38(page=1):

    job_list = job_obj.get_job("sql software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kemi")
	
@sql.route('/sql-software-developer-jobs-iisalmi')
def sql_software_developer39(page=1):

    job_list = job_obj.get_job("sql software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="iisalmi")
	
@sql.route('/sql-software-developer-jobs-varkaus')
def sql_software_developer40(page=1):

    job_list = job_obj.get_job("sql software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="varkaus")
	
@sql.route('/sql-software-developer-jobs-raahe')
def sql_software_developer41(page=1):

    job_list = job_obj.get_job("sql software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="raahe")
	
@sql.route('/sql-software-developer-jobs-ylojarvi')
def sql_software_developer42_1(page=1):

    job_list = job_obj.get_job("sql software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="ylojarvi")
	
@sql.route('/sql-software-developer-jobs-hamina')
def sql_software_developer42(page=1):

    job_list = job_obj.get_job("sql software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="hamina")
	
@sql.route('/sql-software-developer-jobs-kaarina')
def sql_software_developer43(page=1):

    job_list = job_obj.get_job("sql software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kaarina")
	
@sql.route('/sql-software-developer-jobs-tornio')
def sql_software_developer44(page=1):

    job_list = job_obj.get_job("sql software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="tornio")
	
@sql.route('/sql-software-developer-jobs-heinola')
def sql_software_developer45(page=1):

    job_list = job_obj.get_job("sql software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="heinola")
	
@sql.route('/sql-software-developer-jobs-hollola')
def sql_software_developer46(page=1):

    job_list = job_obj.get_job("sql software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="hollola")
	
@sql.route('/sql-software-developer-jobs-valkeakoski')
def sql_software_developer47(page=1):

    job_list = job_obj.get_job("sql software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="valkeakoski")
	
@sql.route('/sql-software-developer-jobs-siilinjarvi')
def sql_software_developer48(page=1):

    job_list = job_obj.get_job("sql software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="siilinjarvi")
	
@sql.route('/sql-software-developer-jobs-kuusankoski')
def sql_software_developer49(page=1):

    job_list = job_obj.get_job("sql software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kuusankoski")
	
@sql.route('/sql-software-developer-jobs-sibbo')
def sql_software_developer50(page=1):

    job_list = job_obj.get_job("sql software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="sibbo")
	
@sql.route('/sql-software-developer-jobs-jakostad')
def sql_software_developer51(page=1):

    job_list = job_obj.get_job("sql software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="jakostad")
	
@sql.route('/sql-software-developer-jobs-lempaala')
def sql_software_developer52(page=1):

    job_list = job_obj.get_job("sql software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="lempaala")
	
@sql.route('/sql-software-developer-jobs-mantsala')
def sql_software_developer52_1(page=1):

    job_list = job_obj.get_job("sql software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="mantsala")
	
@sql.route('/sql-software-developer-jobs-forssa')
def sql_software_developer53(page=1):

    job_list = job_obj.get_job("sql software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="forssa")
	
@sql.route('/sql-software-developer-jobs-kuusamo')
def sql_software_developer54(page=1):

    job_list = job_obj.get_job("sql software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kuusamo")
	
@sql.route('/sql-software-developer-jobs-haukipudas')
def sql_software_developer55(page=1):

    job_list = job_obj.get_job("sql software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="haukipudas")
	
@sql.route('/sql-software-developer-jobs-korsholm')
def sql_software_developer56(page=1):

    job_list = job_obj.get_job("sql software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="korsholm")
	
@sql.route('/sql-software-developer-jobs-laukaa')
def sql_software_developer57(page=1):

    job_list = job_obj.get_job("sql software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="laukaa")
	
@sql.route('/sql-software-developer-jobs-anjala')
def sql_software_developer58(page=1):

    job_list = job_obj.get_job("sql software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="anjala")
	
@sql.route('/sql-software-developer-jobs-uusikaupunki')
def sql_software_developer59(page=1):

    job_list = job_obj.get_job("sql software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="uusikaupunki")
	
@sql.route('/sql-software-developer-jobs-janakkala')
def sql_software_developer60(page=1):

    job_list = job_obj.get_job("sql software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="janakkala")
	
@sql.route('/sql-software-developer-jobs-pirkkala')
def sql_software_developer61(page=1):

    job_list = job_obj.get_job("sql software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="pirkkala")
	
@sql.route('/sql-software-developer-jobs-lansi-turunmaa')
def sql_software_developer62(page=1):

    job_list = job_obj.get_job("sql software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="lansi-turunmaa")
	
@sql.route('/sql-software-developer-jobs-jamsa')
def sql_software_developer63(page=1):

    job_list = job_obj.get_job("sql software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="jamsa")
	
@sql.route('/sql-software-developer-jobs-jamsa')
def sql_software_developer64(page=1):

    job_list = job_obj.get_job("sql software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="jamsa")
	
@sql.route('/sql-software-developer-jobs-vammala')
def sql_software_developer65(page=1):

    job_list = job_obj.get_job("sql software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="vammala")
	
@sql.route('/sql-software-developer-jobs-nastola')
def sql_software_developer66(page=1):

    job_list = job_obj.get_job("sql software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="nastola")
	
@sql.route('/sql-software-developer-jobs-orimattila')
def sql_software_developer67(page=1):

    job_list = job_obj.get_job("sql software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="orimattila")
	
@sql.route('/sql-software-developer-jobs-kauhajoki')
def sql_software_developer68(page=1):

    job_list = job_obj.get_job("sql software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kauhajoki")
	
@sql.route('/sql-software-developer-jobs-ekenas')
def sql_software_developer69(page=1):

    job_list = job_obj.get_job("sql software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="ekenas")
	
@sql.route('/sql-software-developer-jobs-kempele')
def sql_software_developer70(page=1):

    job_list = job_obj.get_job("sql software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kempele")
	
@sql.route('/sql-software-developer-jobs-lapua')
def sql_software_developer71(page=1):

    job_list = job_obj.get_job("sql software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="lapua")
	
@sql.route('/sql-software-developer-jobs-lieksa')
def sql_software_developer72(page=1):

    job_list = job_obj.get_job("sql software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="lieksa")
	
@sql.route('/sql-software-developer-jobs-naantali')
def sql_software_developer73(page=1):

    job_list = job_obj.get_job("sql software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="naantali")
	
@sql.route('/sql-software-developer-jobs-aanekoski')
def sql_software_developer74(page=1):

    job_list = job_obj.get_job("sql software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="aanekoski")
	
@sql.route('/sql-software-developer-jobs-ylivieska')
def sql_software_developer75(page=1):

    job_list = job_obj.get_job("sql software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="ylivieska")
	
@sql.route('/sql-software-developer-jobs-kontiolahti')
def sql_software_developer76(page=1):

    job_list = job_obj.get_job("sql software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kontiolahti")
	
@sql.route('/sql-software-developer-jobs-kankaanpaa')
def sql_software_developer77(page=1):

    job_list = job_obj.get_job("sql software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kankaanpaa")
	
@sql.route('/sql-software-developer-jobs-ulvila')
def sql_software_developer78(page=1):

    job_list = job_obj.get_job("sql software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="ulvila")
	
@sql.route('/sql-software-developer-jobs-pieksamaki')
def sql_software_developer79(page=1):

    job_list = job_obj.get_job("sql software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="pieksamaki")
	
@sql.route('/sql-software-developer-jobs-kiiminki')
def sql_software_developer80(page=1):

    job_list = job_obj.get_job("sql software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kiiminki")
	
@sql.route('/sql-software-developer-jobs-pargas')
def sql_software_developer81(page=1):

    job_list = job_obj.get_job("sql software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="pargas")
	
@sql.route('/sql-software-developer-jobs-nurmo')
def sql_software_developer82(page=1):

    job_list = job_obj.get_job("sql software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="nurmo")
	
@sql.route('/sql-software-developer-jobs-ilmajoki')
def sql_software_developer83(page=1):

    job_list = job_obj.get_job("sql software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="ilmajoki")
	
@sql.route('/sql-software-developer-jobs-liperi')
def sql_software_developer84(page=1):

    job_list = job_obj.get_job("sql software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="liperi")
	
@sql.route('/sql-software-developer-jobs-keuruu')
def sql_software_developer85(page=1):

    job_list = job_obj.get_job("sql software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="keuruu")
	
@sql.route('/sql-software-developer-jobs-leppavirta')
def sql_software_developer86(page=1):

    job_list = job_obj.get_job("sql software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="leppavirta")
	
@sql.route('/sql-software-developer-jobs-kurikka')
def sql_software_developer87(page=1):

    job_list = job_obj.get_job("sql software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kurikka")
	
@sql.route('/sql-software-developer-jobs-nivala')
def sql_software_developer88(page=1):

    job_list = job_obj.get_job("sql software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="nivala")
	
@sql.route('/sql-software-developer-jobs-joutseno')
def sql_software_developer89(page=1):

    job_list = job_obj.get_job("sql software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="joutseno")
	
@sql.route('/sql-software-developer-jobs-pedersore')
def sql_software_developer90(page=1):

    job_list = job_obj.get_job("sql software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="pedersore")
	
@sql.route('/sql-software-developer-jobs-sotkamo')
def sql_software_developer91(page=1):

    job_list = job_obj.get_job("sql software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="sotkamo")
	
@sql.route('/sql-software-developer-jobs-kuhmo')
def sql_software_developer92(page=1):

    job_list = job_obj.get_job("sql software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="kuhmo")
	
@sql.route('/sql-software-developer-jobs-paimio')
def sql_software_developer93(page=1):

    job_list = job_obj.get_job("sql software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="paimio")
	
@sql.route('/sql-software-developer-jobs-saarijarvi')
def sql_software_developer94(page=1):

    job_list = job_obj.get_job("sql software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="saarijarvi")
	
@sql.route('/sql-software-developer-jobs-helsinki')
def sql_software_developer95(page=1):

    job_list = job_obj.get_job("sql software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql software developer", location="helsinki")


####################################################################


##############################################
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-espoo')
def sqlohjelmistosuunnittelija_tyopaikat2(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="espoo")

@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-tampere')
def sqlohjelmistosuunnittelija_tyopaikat3(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="tampere")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-vantaa')
def sqlohjelmistosuunnittelija_tyopaikat4(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="vantaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-turku')
def sqlohjelmistosuunnittelija_tyopaikat5(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="turku")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-oulu')
def sqlohjelmistosuunnittelija_tyopaikat6(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="oulu")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-lahti')
def sqlohjelmistosuunnittelija_tyopaikat7(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="lahti")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kuopio')
def sqlohjelmistosuunnittelija_tyopaikat8(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kuopio")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-jyvvaskyla')
def sqlohjelmistosuunnittelija_tyopaikat9(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="jyvvaskyla")

@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-pori')
def sqlohjelmistosuunnittelija_tyopaikat10(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="pori")

@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-lappeenranta')
def sqlohjelmistosuunnittelija_tyopaikat11(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="lappeenranta")	
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-vaasa')
def sqlohjelmistosuunnittelija_tyopaikat12(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="vaasa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kotka')
def sqlohjelmistosuunnittelija_tyopaikat13(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kotka")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-joensuu')
def sqlohjelmistosuunnittelija_tyopaikat14(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="joensuu")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-hameenlinna')
def sqlohjelmistosuunnittelija_tyopaikat15(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="hameenlinna")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-porvoo')
def sqlohjelmistosuunnittelija_tyopaikat16(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="porvoo")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-mikkeli')
def sqlohjelmistosuunnittelija_tyopaikat17(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="mikkeli")

@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-hyvinkaa')
def sqlohjelmistosuunnittelija_tyopaikat18(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="hyvinkaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-nurmijarvi')
def sqlohjelmistosuunnittelija_tyopaikat19(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="nurmijarvi")

@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-jarvenpaa')
def sqlohjelmistosuunnittelija_tyopaikat20(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="jarvenpaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-rauma')
def sqlohjelmistosuunnittelija_tyopaikat21(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="rauma")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-lohja')
def sqlohjelmistosuunnittelija_tyopaikat22(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="lohja")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-karleby')
def sqlohjelmistosuunnittelija_tyopaikat23(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="karleby")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kajaani')
def sqlohjelmistosuunnittelija_tyopaikat24(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kajaani")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-rovaniemi')
def sqlohjelmistosuunnittelija_tyopaikat25(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="rovaniemi")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-tuusula')
def sqlohjelmistosuunnittelija_tyopaikat26(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="tuusula")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kirkkonummi')
def sqlohjelmistosuunnittelija_tyopaikat27(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kirkkonummi")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-seinajoki')
def sqlohjelmistosuunnittelija_tyopaikat28(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="seinajoki")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kerava')
def sqlohjelmistosuunnittelija_tyopaikat29(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kerava")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kouvola')
def sqlohjelmistosuunnittelija_tyopaikat30(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kouvola")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-imatra')
def sqlohjelmistosuunnittelija_tyopaikat31(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="imatra")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-nokia')
def sqlohjelmistosuunnittelija_tyopaikat32_1(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="nokia")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-savonlinna')
def sqlohjelmistosuunnittelija_tyopaikat32(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="savonlinna")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-riihimaki')
def sqlohjelmistosuunnittelija_tyopaikat33(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="riihimaki")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-vihti')
def sqlohjelmistosuunnittelija_tyopaikat34(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="vihti")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-salo')
def sqlohjelmistosuunnittelija_tyopaikat35(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="salo")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kangasala')
def sqlohjelmistosuunnittelija_tyopaikat36(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kangasala")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-raisio')
def sqlohjelmistosuunnittelija_tyopaikat37_1(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="raisio")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-karhula')
def sqlohjelmistosuunnittelija_tyopaikat37(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="karhula")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kemi')
def sqlohjelmistosuunnittelija_tyopaikat38(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kemi")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-iisalmi')
def sqlohjelmistosuunnittelija_tyopaikat39(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="iisalmi")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-varkaus')
def sqlohjelmistosuunnittelija_tyopaikat40(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="varkaus")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-raahe')
def sqlohjelmistosuunnittelija_tyopaikat41(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="raahe")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-ylojarvi')
def sqlohjelmistosuunnittelija_tyopaikat42_1(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="ylojarvi")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-hamina')
def sqlohjelmistosuunnittelija_tyopaikat42(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="hamina")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kaarina')
def sqlohjelmistosuunnittelija_tyopaikat43(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kaarina")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-tornio')
def sqlohjelmistosuunnittelija_tyopaikat44(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="tornio")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-heinola')
def sqlohjelmistosuunnittelija_tyopaikat45(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="heinola")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-hollola')
def sqlohjelmistosuunnittelija_tyopaikat46(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="hollola")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-valkeakoski')
def sqlohjelmistosuunnittelija_tyopaikat47(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="valkeakoski")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-siilinjarvi')
def sqlohjelmistosuunnittelija_tyopaikat48(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="siilinjarvi")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kuusankoski')
def sqlohjelmistosuunnittelija_tyopaikat49(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kuusankoski")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-sibbo')
def sqlohjelmistosuunnittelija_tyopaikat50(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="sibbo")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-jakostad')
def sqlohjelmistosuunnittelija_tyopaikat51(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="jakostad")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-lempaala')
def sqlohjelmistosuunnittelija_tyopaikat52(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="lempaala")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-mantsala')
def sqlohjelmistosuunnittelija_tyopaikat52_1(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="mantsala")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-forssa')
def sqlohjelmistosuunnittelija_tyopaikat53(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="forssa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kuusamo')
def sqlohjelmistosuunnittelija_tyopaikat54(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kuusamo")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-haukipudas')
def sqlohjelmistosuunnittelija_tyopaikat55(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="haukipudas")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-korsholm')
def sqlohjelmistosuunnittelija_tyopaikat56(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="korsholm")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-laukaa')
def sqlohjelmistosuunnittelija_tyopaikat57(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="laukaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-anjala')
def sqlohjelmistosuunnittelija_tyopaikat58(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="anjala")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-uusikaupunki')
def sqlohjelmistosuunnittelija_tyopaikat59(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="uusikaupunki")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-janakkala')
def sqlohjelmistosuunnittelija_tyopaikat60(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="janakkala")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-pirkkala')
def sqlohjelmistosuunnittelija_tyopaikat61(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="pirkkala")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-lansi-turunmaa')
def sqlohjelmistosuunnittelija_tyopaikat62(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-jamsa')
def sqlohjelmistosuunnittelija_tyopaikat63(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="jamsa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-jamsa')
def sqlohjelmistosuunnittelija_tyopaikat64(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="jamsa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-vammala')
def sqlohjelmistosuunnittelija_tyopaikat65(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="vammala")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-nastola')
def sqlohjelmistosuunnittelija_tyopaikat66(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="nastola")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-orimattila')
def sqlohjelmistosuunnittelija_tyopaikat67(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="orimattila")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kauhajoki')
def sqlohjelmistosuunnittelija_tyopaikat68(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kauhajoki")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-ekenas')
def sqlohjelmistosuunnittelija_tyopaikat69(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="ekenas")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kempele')
def sqlohjelmistosuunnittelija_tyopaikat70(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kempele")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-lapua')
def sqlohjelmistosuunnittelija_tyopaikat71(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="lapua")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-lieksa')
def sqlohjelmistosuunnittelija_tyopaikat72(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="lieksa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-naantali')
def sqlohjelmistosuunnittelija_tyopaikat73(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="naantali")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-aanekoski')
def sqlohjelmistosuunnittelija_tyopaikat74(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="aanekoski")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-ylivieska')
def sqlohjelmistosuunnittelija_tyopaikat75(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="ylivieska")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kontiolahti')
def sqlohjelmistosuunnittelija_tyopaikat76(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kontiolahti")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kankaanpaa')
def sqlohjelmistosuunnittelija_tyopaikat77(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kankaanpaa")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-ulvila')
def sqlohjelmistosuunnittelija_tyopaikat78(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="ulvila")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-pieksamaki')
def sqlohjelmistosuunnittelija_tyopaikat79(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="pieksamaki")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kiiminki')
def sqlohjelmistosuunnittelija_tyopaikat80(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kiiminki")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-pargas')
def sqlohjelmistosuunnittelija_tyopaikat81(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="pargas")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-nurmo')
def sqlohjelmistosuunnittelija_tyopaikat82(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="nurmo")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-ilmajoki')
def sqlohjelmistosuunnittelija_tyopaikat83(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="ilmajoki")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-liperi')
def sqlohjelmistosuunnittelija_tyopaikat84(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="liperi")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-keuruu')
def sqlohjelmistosuunnittelija_tyopaikat85(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="keuruu")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-leppavirta')
def sqlohjelmistosuunnittelija_tyopaikat86(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="leppavirta")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kurikka')
def sqlohjelmistosuunnittelija_tyopaikat87(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kurikka")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-nivala')
def sqlohjelmistosuunnittelija_tyopaikat88(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="nivala")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-joutseno')
def sqlohjelmistosuunnittelija_tyopaikat89(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="joutseno")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-pedersore')
def sqlohjelmistosuunnittelija_tyopaikat90(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="pedersore")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-sotkamo')
def sqlohjelmistosuunnittelija_tyopaikat91(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="sotkamo")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-kuhmo')
def sqlohjelmistosuunnittelija_tyopaikat92(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="kuhmo")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-paimio')
def sqlohjelmistosuunnittelija_tyopaikat93(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="paimio")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-saarijarvi')
def sqlohjelmistosuunnittelija_tyopaikat94(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="saarijarvi")
	
@sql.route('/sql-ohjelmistosuunnittelija-tyopaikat-helsinki')
def sqlohjelmistosuunnittelija_tyopaikat95(page=1):

    job_list = job_obj.get_job("sql  ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="sql  ohjelmistosuunnittelija", location="helsinki")
	  

