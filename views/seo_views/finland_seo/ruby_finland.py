from ....models import Job
from flask import render_template, request, redirect, url_for, Blueprint, current_app, make_response
import datetime

JOB_PER_PaGE = 7

ruby = Blueprint('ruby', __name__)
job_obj = Job()



####################################################################


@ruby.route('/ruby_sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)#.date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and "ruby" in rule.rule:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"

      return response
	  
	 
##############################################
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-espoo')
def ruby_ohjelmistosuunnittelija2(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="espoo")

@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-tampere')
def ruby_ohjelmistosuunnittelija3(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="tampere")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-vantaa')
def ruby_ohjelmistosuunnittelija4(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="vantaa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-turku')
def ruby_ohjelmistosuunnittelija5(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="turku")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-oulu')
def ruby_ohjelmistosuunnittelija6(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="oulu")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-lahti')
def ruby_ohjelmistosuunnittelija7(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="lahti")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kuopio')
def ruby_ohjelmistosuunnittelija8(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kuopio")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-jyvvaskyla')
def ruby_ohjelmistosuunnittelija9(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="jyvvaskyla")

@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-pori')
def ruby_ohjelmistosuunnittelija10(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="pori")

@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-lappeenranta')
def ruby_ohjelmistosuunnittelija11(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="lappeenranta")	
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-vaasa')
def ruby_ohjelmistosuunnittelija12(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="vaasa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kotka')
def ruby_ohjelmistosuunnittelija13(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kotka")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-joensuu')
def ruby_ohjelmistosuunnittelija14(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="joensuu")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-hameenlinna')
def ruby_ohjelmistosuunnittelija15(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="hameenlinna")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-porvoo')
def ruby_ohjelmistosuunnittelija16(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="porvoo")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-mikkeli')
def ruby_ohjelmistosuunnittelija17(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="mikkeli")

@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-hyvinkaa')
def ruby_ohjelmistosuunnittelija18(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="hyvinkaa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmijarvi')
def ruby_ohjelmistosuunnittelija19(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="nurmijarvi")

@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-jarvenpaa')
def ruby_ohjelmistosuunnittelija20(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="jarvenpaa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-rauma')
def ruby_ohjelmistosuunnittelija21(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="rauma")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-lohja')
def ruby_ohjelmistosuunnittelija22(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="lohja")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-karleby')
def ruby_ohjelmistosuunnittelija23(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="karleby")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kajaani')
def ruby_ohjelmistosuunnittelija24(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kajaani")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-rovaniemi')
def ruby_ohjelmistosuunnittelija25(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="rovaniemi")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-tuusula')
def ruby_ohjelmistosuunnittelija26(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="tuusula")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kirkkonummi')
def ruby_ohjelmistosuunnittelija27(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kirkkonummi")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-seinajoki')
def ruby_ohjelmistosuunnittelija28(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="seinajoki")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kerava')
def ruby_ohjelmistosuunnittelija29(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kerava")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kouvola')
def ruby_ohjelmistosuunnittelija30(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kouvola")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-imatra')
def ruby_ohjelmistosuunnittelija31(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="imatra")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-nokia')
def ruby_ohjelmistosuunnittelija32_1(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="nokia")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-savonlinna')
def ruby_ohjelmistosuunnittelija32(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="savonlinna")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-riihimaki')
def ruby_ohjelmistosuunnittelija33(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="riihimaki")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-vihti')
def ruby_ohjelmistosuunnittelija34(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="vihti")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-salo')
def ruby_ohjelmistosuunnittelija35(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="salo")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kangasala')
def ruby_ohjelmistosuunnittelija36(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kangasala")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-raisio')
def ruby_ohjelmistosuunnittelija37_1(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="raisio")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-karhula')
def ruby_ohjelmistosuunnittelija37(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="karhula")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kemi')
def ruby_ohjelmistosuunnittelija38(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kemi")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-iisalmi')
def ruby_ohjelmistosuunnittelija39(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="iisalmi")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-varkaus')
def ruby_ohjelmistosuunnittelija40(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="varkaus")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-raahe')
def ruby_ohjelmistosuunnittelija41(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="raahe")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-ylojarvi')
def ruby_ohjelmistosuunnittelija42_1(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="ylojarvi")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-hamina')
def ruby_ohjelmistosuunnittelija42(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="hamina")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kaarina')
def ruby_ohjelmistosuunnittelija43(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kaarina")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-tornio')
def ruby_ohjelmistosuunnittelija44(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="tornio")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-heinola')
def ruby_ohjelmistosuunnittelija45(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="heinola")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-hollola')
def ruby_ohjelmistosuunnittelija46(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="hollola")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-valkeakoski')
def ruby_ohjelmistosuunnittelija47(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="valkeakoski")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-siilinjarvi')
def ruby_ohjelmistosuunnittelija48(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="siilinjarvi")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusankoski')
def ruby_ohjelmistosuunnittelija49(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kuusankoski")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-sibbo')
def ruby_ohjelmistosuunnittelija50(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="sibbo")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-jakostad')
def ruby_ohjelmistosuunnittelija51(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="jakostad")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-lempaala')
def ruby_ohjelmistosuunnittelija52(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="lempaala")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-mantsala')
def ruby_ohjelmistosuunnittelija52_1(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="mantsala")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-forssa')
def ruby_ohjelmistosuunnittelija53(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="forssa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kuusamo')
def ruby_ohjelmistosuunnittelija54(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kuusamo")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-haukipudas')
def ruby_ohjelmistosuunnittelija55(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="haukipudas")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-korsholm')
def ruby_ohjelmistosuunnittelija56(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="korsholm")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-laukaa')
def ruby_ohjelmistosuunnittelija57(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="laukaa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-anjala')
def ruby_ohjelmistosuunnittelija58(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="anjala")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-uusikaupunki')
def ruby_ohjelmistosuunnittelija59(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="uusikaupunki")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-janakkala')
def ruby_ohjelmistosuunnittelija60(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="janakkala")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-pirkkala')
def ruby_ohjelmistosuunnittelija61(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="pirkkala")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-lansi-turunmaa')
def ruby_ohjelmistosuunnittelija62(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="lansi-turunmaa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def ruby_ohjelmistosuunnittelija63(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="jamsa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-jamsa')
def ruby_ohjelmistosuunnittelija64(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="jamsa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-vammala')
def ruby_ohjelmistosuunnittelija65(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="vammala")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-nastola')
def ruby_ohjelmistosuunnittelija66(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="nastola")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-orimattila')
def ruby_ohjelmistosuunnittelija67(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="orimattila")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kauhajoki')
def ruby_ohjelmistosuunnittelija68(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kauhajoki")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-ekenas')
def ruby_ohjelmistosuunnittelija69(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="ekenas")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kempele')
def ruby_ohjelmistosuunnittelija70(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kempele")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-lapua')
def ruby_ohjelmistosuunnittelija71(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="lapua")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-lieksa')
def ruby_ohjelmistosuunnittelija72(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="lieksa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-naantali')
def ruby_ohjelmistosuunnittelija73(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="naantali")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-aanekoski')
def ruby_ohjelmistosuunnittelija74(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="aanekoski")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-ylivieska')
def ruby_ohjelmistosuunnittelija75(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="ylivieska")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kontiolahti')
def ruby_ohjelmistosuunnittelija76(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kontiolahti")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kankaanpaa')
def ruby_ohjelmistosuunnittelija77(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kankaanpaa")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-ulvila')
def ruby_ohjelmistosuunnittelija78(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="ulvila")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-pieksamaki')
def ruby_ohjelmistosuunnittelija79(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="pieksamaki")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kiiminki')
def ruby_ohjelmistosuunnittelija80(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kiiminki")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-pargas')
def ruby_ohjelmistosuunnittelija81(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="pargas")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-nurmo')
def ruby_ohjelmistosuunnittelija82(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="nurmo")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-ilmajoki')
def ruby_ohjelmistosuunnittelija83(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="ilmajoki")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-liperi')
def ruby_ohjelmistosuunnittelija84(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="liperi")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-keuruu')
def ruby_ohjelmistosuunnittelija85(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="keuruu")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-leppavirta')
def ruby_ohjelmistosuunnittelija86(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="leppavirta")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kurikka')
def ruby_ohjelmistosuunnittelija87(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kurikka")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-nivala')
def ruby_ohjelmistosuunnittelija88(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="nivala")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-joutseno')
def ruby_ohjelmistosuunnittelija89(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="joutseno")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-pedersore')
def ruby_ohjelmistosuunnittelija90(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="pedersore")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-sotkamo')
def ruby_ohjelmistosuunnittelija91(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="sotkamo")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-kuhmo')
def ruby_ohjelmistosuunnittelija92(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="kuhmo")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-paimio')
def ruby_ohjelmistosuunnittelija93(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="paimio")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-saarijarvi')
def ruby_ohjelmistosuunnittelija94(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="saarijarvi")
	
@ruby.route('/ruby-ohjelmistosuunnittelija-avoimet-tyopaikat-helsinki')
def ruby_ohjelmistosuunnittelija95(page=1):

    job_list = job_obj.get_job("ruby ohjelmistosuunnittelija", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby ohjelmistosuunnittelija", location="helsinki")


####################################################################


##############################################
@ruby.route('/ruby-software-developer-jobs-espoo')
def ruby_software_developer2(page=1):

    job_list = job_obj.get_job("ruby software developer", "espoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="espoo")

@ruby.route('/ruby-software-developer-jobs-tampere')
def ruby_software_developer3(page=1):

    job_list = job_obj.get_job("ruby software developer", "tampere").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="tampere")
	
@ruby.route('/ruby-software-developer-jobs-vantaa')
def ruby_software_developer4(page=1):

    job_list = job_obj.get_job("ruby software developer", "vantaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="vantaa")
	
@ruby.route('/ruby-software-developer-jobs-turku')
def ruby_software_developer5(page=1):

    job_list = job_obj.get_job("ruby software developer", "turku").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="turku")
	
@ruby.route('/ruby-software-developer-jobs-oulu')
def ruby_software_developer6(page=1):

    job_list = job_obj.get_job("ruby software developer", "oulu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="oulu")
	
@ruby.route('/ruby-software-developer-jobs-lahti')
def ruby_software_developer7(page=1):

    job_list = job_obj.get_job("ruby software developer", "lahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="lahti")
	
@ruby.route('/ruby-software-developer-jobs-kuopio')
def ruby_software_developer8(page=1):

    job_list = job_obj.get_job("ruby software developer", "kuopio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kuopio")
	
@ruby.route('/ruby-software-developer-jobs-jyvvaskyla')
def ruby_software_developer9(page=1):

    job_list = job_obj.get_job("ruby software developer", "jyvvaskyla").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="jyvvaskyla")

@ruby.route('/ruby-software-developer-jobs-pori')
def ruby_software_developer10(page=1):

    job_list = job_obj.get_job("ruby software developer", "pori").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="pori")

@ruby.route('/ruby-software-developer-jobs-lappeenranta')
def ruby_software_developer11(page=1):

    job_list = job_obj.get_job("ruby software developer", "lappeenranta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="lappeenranta")	
	
@ruby.route('/ruby-software-developer-jobs-vaasa')
def ruby_software_developer12(page=1):

    job_list = job_obj.get_job("ruby software developer", "vaasa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="vaasa")
	
@ruby.route('/ruby-software-developer-jobs-kotka')
def ruby_software_developer13(page=1):

    job_list = job_obj.get_job("ruby software developer", "kotka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kotka")
	
@ruby.route('/ruby-software-developer-jobs-joensuu')
def ruby_software_developer14(page=1):

    job_list = job_obj.get_job("ruby software developer", "joensuu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="joensuu")
	
@ruby.route('/ruby-software-developer-jobs-hameenlinna')
def ruby_software_developer15(page=1):

    job_list = job_obj.get_job("ruby software developer", "hameenlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="hameenlinna")
	
@ruby.route('/ruby-software-developer-jobs-porvoo')
def ruby_software_developer16(page=1):

    job_list = job_obj.get_job("ruby software developer", "porvoo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="porvoo")
	
@ruby.route('/ruby-software-developer-jobs-mikkeli')
def ruby_software_developer17(page=1):

    job_list = job_obj.get_job("ruby software developer", "mikkeli").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="mikkeli")

@ruby.route('/ruby-software-developer-jobs-hyvinkaa')
def ruby_software_developer18(page=1):

    job_list = job_obj.get_job("ruby software developer", "hyvinkaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="hyvinkaa")
	
@ruby.route('/ruby-software-developer-jobs-nurmijarvi')
def ruby_software_developer19(page=1):

    job_list = job_obj.get_job("ruby software developer", "nurmijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="nurmijarvi")

@ruby.route('/ruby-software-developer-jobs-jarvenpaa')
def ruby_software_developer20(page=1):

    job_list = job_obj.get_job("ruby software developer", "jarvenpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="jarvenpaa")
	
@ruby.route('/ruby-software-developer-jobs-rauma')
def ruby_software_developer21(page=1):

    job_list = job_obj.get_job("ruby software developer", "rauma").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="rauma")
	
@ruby.route('/ruby-software-developer-jobs-lohja')
def ruby_software_developer22(page=1):

    job_list = job_obj.get_job("ruby software developer", "lohja").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="lohja")
	
@ruby.route('/ruby-software-developer-jobs-karleby')
def ruby_software_developer23(page=1):

    job_list = job_obj.get_job("ruby software developer", "karleby").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="karleby")
	
@ruby.route('/ruby-software-developer-jobs-kajaani')
def ruby_software_developer24(page=1):

    job_list = job_obj.get_job("ruby software developer", "kajaani").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kajaani")
	
@ruby.route('/ruby-software-developer-jobs-rovaniemi')
def ruby_software_developer25(page=1):

    job_list = job_obj.get_job("ruby software developer", "rovaniemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="rovaniemi")
	
@ruby.route('/ruby-software-developer-jobs-tuusula')
def ruby_software_developer26(page=1):

    job_list = job_obj.get_job("ruby software developer", "tuusula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="tuusula")
	
@ruby.route('/ruby-software-developer-jobs-kirkkonummi')
def ruby_software_developer27(page=1):

    job_list = job_obj.get_job("ruby software developer", "kirkkonummi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kirkkonummi")
	
@ruby.route('/ruby-software-developer-jobs-seinajoki')
def ruby_software_developer28(page=1):

    job_list = job_obj.get_job("ruby software developer", "seinajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="seinajoki")
	
@ruby.route('/ruby-software-developer-jobs-kerava')
def ruby_software_developer29(page=1):

    job_list = job_obj.get_job("ruby software developer", "kerava").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kerava")
	
@ruby.route('/ruby-software-developer-jobs-kouvola')
def ruby_software_developer30(page=1):

    job_list = job_obj.get_job("ruby software developer", "kouvola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kouvola")
	
@ruby.route('/ruby-software-developer-jobs-imatra')
def ruby_software_developer31(page=1):

    job_list = job_obj.get_job("ruby software developer", "imatra").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="imatra")
	
@ruby.route('/ruby-software-developer-jobs-nokia')
def ruby_software_developer32_1(page=1):

    job_list = job_obj.get_job("ruby software developer", "nokia").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="nokia")
	
@ruby.route('/ruby-software-developer-jobs-savonlinna')
def ruby_software_developer32(page=1):

    job_list = job_obj.get_job("ruby software developer", "savonlinna").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="savonlinna")
	
@ruby.route('/ruby-software-developer-jobs-riihimaki')
def ruby_software_developer33(page=1):

    job_list = job_obj.get_job("ruby software developer", "riihimaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="riihimaki")
	
@ruby.route('/ruby-software-developer-jobs-vihti')
def ruby_software_developer34(page=1):

    job_list = job_obj.get_job("ruby software developer", "vihti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="vihti")
	
@ruby.route('/ruby-software-developer-jobs-salo')
def ruby_software_developer35(page=1):

    job_list = job_obj.get_job("ruby software developer", "salo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="salo")
	
@ruby.route('/ruby-software-developer-jobs-kangasala')
def ruby_software_developer36(page=1):

    job_list = job_obj.get_job("ruby software developer", "kangasala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kangasala")
	
@ruby.route('/ruby-software-developer-jobs-raisio')
def ruby_software_developer37_1(page=1):

    job_list = job_obj.get_job("ruby software developer", "raisio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="raisio")
	
@ruby.route('/ruby-software-developer-jobs-karhula')
def ruby_software_developer37(page=1):

    job_list = job_obj.get_job("ruby software developer", "karhula").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="karhula")
	
@ruby.route('/ruby-software-developer-jobs-kemi')
def ruby_software_developer38(page=1):

    job_list = job_obj.get_job("ruby software developer", "kemi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kemi")
	
@ruby.route('/ruby-software-developer-jobs-iisalmi')
def ruby_software_developer39(page=1):

    job_list = job_obj.get_job("ruby software developer", "iisalmi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="iisalmi")
	
@ruby.route('/ruby-software-developer-jobs-varkaus')
def ruby_software_developer40(page=1):

    job_list = job_obj.get_job("ruby software developer", "varkaus").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="varkaus")
	
@ruby.route('/ruby-software-developer-jobs-raahe')
def ruby_software_developer41(page=1):

    job_list = job_obj.get_job("ruby software developer", "raahe").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="raahe")
	
@ruby.route('/ruby-software-developer-jobs-ylojarvi')
def ruby_software_developer42_1(page=1):

    job_list = job_obj.get_job("ruby software developer", "ylojarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="ylojarvi")
	
@ruby.route('/ruby-software-developer-jobs-hamina')
def ruby_software_developer42(page=1):

    job_list = job_obj.get_job("ruby software developer", "hamina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="hamina")
	
@ruby.route('/ruby-software-developer-jobs-kaarina')
def ruby_software_developer43(page=1):

    job_list = job_obj.get_job("ruby software developer", "kaarina").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kaarina")
	
@ruby.route('/ruby-software-developer-jobs-tornio')
def ruby_software_developer44(page=1):

    job_list = job_obj.get_job("ruby software developer", "tornio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="tornio")
	
@ruby.route('/ruby-software-developer-jobs-heinola')
def ruby_software_developer45(page=1):

    job_list = job_obj.get_job("ruby software developer", "heinola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="heinola")
	
@ruby.route('/ruby-software-developer-jobs-hollola')
def ruby_software_developer46(page=1):

    job_list = job_obj.get_job("ruby software developer", "hollola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="hollola")
	
@ruby.route('/ruby-software-developer-jobs-valkeakoski')
def ruby_software_developer47(page=1):

    job_list = job_obj.get_job("ruby software developer", "valkeakoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="valkeakoski")
	
@ruby.route('/ruby-software-developer-jobs-siilinjarvi')
def ruby_software_developer48(page=1):

    job_list = job_obj.get_job("ruby software developer", "siilinjarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="siilinjarvi")
	
@ruby.route('/ruby-software-developer-jobs-kuusankoski')
def ruby_software_developer49(page=1):

    job_list = job_obj.get_job("ruby software developer", "kuusankoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kuusankoski")
	
@ruby.route('/ruby-software-developer-jobs-sibbo')
def ruby_software_developer50(page=1):

    job_list = job_obj.get_job("ruby software developer", "sibbo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="sibbo")
	
@ruby.route('/ruby-software-developer-jobs-jakostad')
def ruby_software_developer51(page=1):

    job_list = job_obj.get_job("ruby software developer", "jakostad").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="jakostad")
	
@ruby.route('/ruby-software-developer-jobs-lempaala')
def ruby_software_developer52(page=1):

    job_list = job_obj.get_job("ruby software developer", "lempaala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="lempaala")
	
@ruby.route('/ruby-software-developer-jobs-mantsala')
def ruby_software_developer52_1(page=1):

    job_list = job_obj.get_job("ruby software developer", "mantsala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="mantsala")
	
@ruby.route('/ruby-software-developer-jobs-forssa')
def ruby_software_developer53(page=1):

    job_list = job_obj.get_job("ruby software developer", "forssa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="forssa")
	
@ruby.route('/ruby-software-developer-jobs-kuusamo')
def ruby_software_developer54(page=1):

    job_list = job_obj.get_job("ruby software developer", "kuusamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kuusamo")
	
@ruby.route('/ruby-software-developer-jobs-haukipudas')
def ruby_software_developer55(page=1):

    job_list = job_obj.get_job("ruby software developer", "haukipudas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="haukipudas")
	
@ruby.route('/ruby-software-developer-jobs-korsholm')
def ruby_software_developer56(page=1):

    job_list = job_obj.get_job("ruby software developer", "korsholm").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="korsholm")
	
@ruby.route('/ruby-software-developer-jobs-laukaa')
def ruby_software_developer57(page=1):

    job_list = job_obj.get_job("ruby software developer", "laukaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="laukaa")
	
@ruby.route('/ruby-software-developer-jobs-anjala')
def ruby_software_developer58(page=1):

    job_list = job_obj.get_job("ruby software developer", "anjala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="anjala")
	
@ruby.route('/ruby-software-developer-jobs-uusikaupunki')
def ruby_software_developer59(page=1):

    job_list = job_obj.get_job("ruby software developer", "uusikaupunki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="uusikaupunki")
	
@ruby.route('/ruby-software-developer-jobs-janakkala')
def ruby_software_developer60(page=1):

    job_list = job_obj.get_job("ruby software developer", "janakkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="janakkala")
	
@ruby.route('/ruby-software-developer-jobs-pirkkala')
def ruby_software_developer61(page=1):

    job_list = job_obj.get_job("ruby software developer", "pirkkala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="pirkkala")
	
@ruby.route('/ruby-software-developer-jobs-lansi-turunmaa')
def ruby_software_developer62(page=1):

    job_list = job_obj.get_job("ruby software developer", "lansi-turunmaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="lansi-turunmaa")
	
@ruby.route('/ruby-software-developer-jobs-jamsa')
def ruby_software_developer63(page=1):

    job_list = job_obj.get_job("ruby software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="jamsa")
	
@ruby.route('/ruby-software-developer-jobs-jamsa')
def ruby_software_developer64(page=1):

    job_list = job_obj.get_job("ruby software developer", "jamsa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="jamsa")
	
@ruby.route('/ruby-software-developer-jobs-vammala')
def ruby_software_developer65(page=1):

    job_list = job_obj.get_job("ruby software developer", "vammala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="vammala")
	
@ruby.route('/ruby-software-developer-jobs-nastola')
def ruby_software_developer66(page=1):

    job_list = job_obj.get_job("ruby software developer", "nastola").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="nastola")
	
@ruby.route('/ruby-software-developer-jobs-orimattila')
def ruby_software_developer67(page=1):

    job_list = job_obj.get_job("ruby software developer", "orimattila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="orimattila")
	
@ruby.route('/ruby-software-developer-jobs-kauhajoki')
def ruby_software_developer68(page=1):

    job_list = job_obj.get_job("ruby software developer", "kauhajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kauhajoki")
	
@ruby.route('/ruby-software-developer-jobs-ekenas')
def ruby_software_developer69(page=1):

    job_list = job_obj.get_job("ruby software developer", "ekenas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="ekenas")
	
@ruby.route('/ruby-software-developer-jobs-kempele')
def ruby_software_developer70(page=1):

    job_list = job_obj.get_job("ruby software developer", "kempele").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kempele")
	
@ruby.route('/ruby-software-developer-jobs-lapua')
def ruby_software_developer71(page=1):

    job_list = job_obj.get_job("ruby software developer", "lapua").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="lapua")
	
@ruby.route('/ruby-software-developer-jobs-lieksa')
def ruby_software_developer72(page=1):

    job_list = job_obj.get_job("ruby software developer", "lieksa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="lieksa")
	
@ruby.route('/ruby-software-developer-jobs-naantali')
def ruby_software_developer73(page=1):

    job_list = job_obj.get_job("ruby software developer", "naantali").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="naantali")
	
@ruby.route('/ruby-software-developer-jobs-aanekoski')
def ruby_software_developer74(page=1):

    job_list = job_obj.get_job("ruby software developer", "aanekoski").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="aanekoski")
	
@ruby.route('/ruby-software-developer-jobs-ylivieska')
def ruby_software_developer75(page=1):

    job_list = job_obj.get_job("ruby software developer", "ylivieska").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="ylivieska")
	
@ruby.route('/ruby-software-developer-jobs-kontiolahti')
def ruby_software_developer76(page=1):

    job_list = job_obj.get_job("ruby software developer", "kontiolahti").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kontiolahti")
	
@ruby.route('/ruby-software-developer-jobs-kankaanpaa')
def ruby_software_developer77(page=1):

    job_list = job_obj.get_job("ruby software developer", "kankaanpaa").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kankaanpaa")
	
@ruby.route('/ruby-software-developer-jobs-ulvila')
def ruby_software_developer78(page=1):

    job_list = job_obj.get_job("ruby software developer", "ulvila").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="ulvila")
	
@ruby.route('/ruby-software-developer-jobs-pieksamaki')
def ruby_software_developer79(page=1):

    job_list = job_obj.get_job("ruby software developer", "pieksamaki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="pieksamaki")
	
@ruby.route('/ruby-software-developer-jobs-kiiminki')
def ruby_software_developer80(page=1):

    job_list = job_obj.get_job("ruby software developer", "kiiminki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kiiminki")
	
@ruby.route('/ruby-software-developer-jobs-pargas')
def ruby_software_developer81(page=1):

    job_list = job_obj.get_job("ruby software developer", "pargas").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="pargas")
	
@ruby.route('/ruby-software-developer-jobs-nurmo')
def ruby_software_developer82(page=1):

    job_list = job_obj.get_job("ruby software developer", "nurmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="nurmo")
	
@ruby.route('/ruby-software-developer-jobs-ilmajoki')
def ruby_software_developer83(page=1):

    job_list = job_obj.get_job("ruby software developer", "ilmajoki").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="ilmajoki")
	
@ruby.route('/ruby-software-developer-jobs-liperi')
def ruby_software_developer84(page=1):

    job_list = job_obj.get_job("ruby software developer", "liperi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="liperi")
	
@ruby.route('/ruby-software-developer-jobs-keuruu')
def ruby_software_developer85(page=1):

    job_list = job_obj.get_job("ruby software developer", "keuruu").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="keuruu")
	
@ruby.route('/ruby-software-developer-jobs-leppavirta')
def ruby_software_developer86(page=1):

    job_list = job_obj.get_job("ruby software developer", "leppavirta").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="leppavirta")
	
@ruby.route('/ruby-software-developer-jobs-kurikka')
def ruby_software_developer87(page=1):

    job_list = job_obj.get_job("ruby software developer", "kurikka").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kurikka")
	
@ruby.route('/ruby-software-developer-jobs-nivala')
def ruby_software_developer88(page=1):

    job_list = job_obj.get_job("ruby software developer", "nivala").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="nivala")
	
@ruby.route('/ruby-software-developer-jobs-joutseno')
def ruby_software_developer89(page=1):

    job_list = job_obj.get_job("ruby software developer", "joutseno").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="joutseno")
	
@ruby.route('/ruby-software-developer-jobs-pedersore')
def ruby_software_developer90(page=1):

    job_list = job_obj.get_job("ruby software developer", "pedersore").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="pedersore")
	
@ruby.route('/ruby-software-developer-jobs-sotkamo')
def ruby_software_developer91(page=1):

    job_list = job_obj.get_job("ruby software developer", "sotkamo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="sotkamo")
	
@ruby.route('/ruby-software-developer-jobs-kuhmo')
def ruby_software_developer92(page=1):

    job_list = job_obj.get_job("ruby software developer", "kuhmo").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="kuhmo")
	
@ruby.route('/ruby-software-developer-jobs-paimio')
def ruby_software_developer93(page=1):

    job_list = job_obj.get_job("ruby software developer", "paimio").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="paimio")
	
@ruby.route('/ruby-software-developer-jobs-saarijarvi')
def ruby_software_developer94(page=1):

    job_list = job_obj.get_job("ruby software developer", "saarijarvi").paginate(page, JOB_PER_PaGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="saarijarvi")
	
@ruby.route('/ruby-software-developer-jobs-helsinki')
def ruby_software_developer95(page=1):

    job_list = job_obj.get_job("ruby software developer", "helsinki").paginate(page, JOB_PER_PAGE, False)
    return render_template("resultsTemp.html", jobs=job_list, title="ruby software developer", location="helsinki")


####################################################################

