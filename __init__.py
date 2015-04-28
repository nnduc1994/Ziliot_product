__author__ = 'nnduc_000'
from flask import Flask
from share import db, mail, bootstrap



app = Flask(__name__)
db.app = app
db.init_app(app)
app.config.from_object('config')
db.metadata.reflect(db.engine)

# Initial sending Email
mail.init_app(app)

#Initial bootstrap
bootstrap.init_app(apps)

# Register blueprint
from .views.home import home
app.register_blueprint(home)
from .views.company import company
app.register_blueprint(company)

#Register Estonia blueprint
from.views.estonia import estonia
app.register_blueprint(estonia, subdomain="ee")


#### SEO blueprint #########

# sitemap contains all sitemap
from .views.seo_views.finland_seo.sitemap import site_map
app.register_blueprint(site_map)


from .views.seo_views.finland_seo.cold_fusion_finland import coldFusion
app.register_blueprint(coldFusion)

from .views.seo_views.finland_seo.fortran_finland import fortran
app.register_blueprint(fortran)

from .views.seo_views.finland_seo.actionscript_finland import actionscript
app.register_blueprint(actionscript)

from .views.seo_views.finland_seo.c_finland import c
app.register_blueprint(c)

from .views.seo_views.finland_seo.cplusplus_finland import c_plusplus
app.register_blueprint(c_plusplus)

from .views.seo_views.finland_seo.c_sharp_finland import c_sharp
app.register_blueprint(c_sharp)
from .views.seo_views.finland_seo.visual_basic_finland import visual_basic
app.register_blueprint(visual_basic)
from .views.seo_views.finland_seo.php_finland import php
app.register_blueprint(php)
from .views.seo_views.finland_seo.python_finland import python
app.register_blueprint(python)
from .views.seo_views.finland_seo.scala_finland import scala
app.register_blueprint(scala) 
from .views.seo_views.finland_seo.java_finland import java
app.register_blueprint(java)
from .views.seo_views.finland_seo.javascript_finland import javascript
app.register_blueprint(javascript)
from .views.seo_views.finland_seo.ruby_finland import ruby
app.register_blueprint(ruby)
from .views.seo_views.finland_seo.perl_finland import perl
app.register_blueprint(perl)
from .views.seo_views.finland_seo.pascal_finland import pascal
app.register_blueprint(pascal)
from .views.seo_views.finland_seo.delphi_finland import delphi
app.register_blueprint(delphi)
from .views.seo_views.finland_seo.cobol_finland import cobol
app.register_blueprint(cobol)
from .views.seo_views.finland_seo.assembly_finland import assembly
app.register_blueprint(assembly)
from .views.seo_views.finland_seo.asp_net_finland import asp_net
app.register_blueprint(asp_net)
from .views.seo_views.finland_seo.sql_finland import sql
app.register_blueprint(sql)
from .views.seo_views.finland_seo.objective_c_finland import objective_c
app.register_blueprint(objective_c)
from .views.seo_views.finland_seo.frontend_finland import frontend
app.register_blueprint(frontend)
from .views.seo_views.finland_seo.art_director_finland import art_director
app.register_blueprint(art_director)
from .views.seo_views.finland_seo.concept_artist_finland import concept_artist
app.register_blueprint(concept_artist)
from .views.seo_views.finland_seo.principal_artist_finland import principal_artist
app.register_blueprint(principal_artist)
from .views.seo_views.finland_seo.animator_finland import animator
app.register_blueprint(animator)

from .views.seo_views.finland_seo.environment_artist_finland import environment_artist
app.register_blueprint(environment_artist)
from .views.seo_views.finland_seo.audio_engineer_finland import audio_engineer
app.register_blueprint(audio_engineer)
from .views.seo_views.finland_seo.threed_artist_finland import three_d_artist
app.register_blueprint(three_d_artist)
from .views.seo_views.finland_seo.creative_director_finland import creative_director
app.register_blueprint(creative_director)
from .views.seo_views.finland_seo.lead_designer_finland import lead_designer
app.register_blueprint(lead_designer)
from .views.seo_views.finland_seo.senior_designer_finland import senior_designer
app.register_blueprint(senior_designer)
from .views.seo_views.finland_seo.designer_finland import designer
app.register_blueprint(designer)
from .views.seo_views.finland_seo.graphic_designer_finland import graphic_designer
app.register_blueprint(graphic_designer)
from .views.seo_views.finland_seo.executive_producer_finland import executive_producer
app.register_blueprint(executive_producer)

#########################################
# sitemap contains all sitemap
from .views.seo_views.estonia_seo.sitemap import site_map_estonia
app.register_blueprint(site_map_estonia, subdomain="ee")


from .views.seo_views.estonia_seo.cold_fusion_estonia import coldFusion
app.register_blueprint(coldFusion, subdomain="ee")

from .views.seo_views.estonia_seo.fortran_estonia import fortran
app.register_blueprint(fortran, subdomain="ee")

from .views.seo_views.estonia_seo.actionscript_estonia import actionscript
app.register_blueprint(actionscript, subdomain="ee")

from .views.seo_views.estonia_seo.c_estonia import c
app.register_blueprint(c, subdomain="ee")

from .views.seo_views.estonia_seo.cplusplus_estonia import c_plusplus
app.register_blueprint(c_plusplus, subdomain="ee")

from .views.seo_views.estonia_seo.c_sharp_estonia import c_sharp
app.register_blueprint(c_sharp, subdomain="ee")
from .views.seo_views.estonia_seo.visual_basic_estonia import visual_basic
app.register_blueprint(visual_basic, subdomain="ee")
from .views.seo_views.estonia_seo.php_estonia import php
app.register_blueprint(php, subdomain="ee")
from .views.seo_views.estonia_seo.python_estonia import python
app.register_blueprint(python, subdomain="ee")
from .views.seo_views.estonia_seo.scala_estonia import scala
app.register_blueprint(scala, subdomain="ee") 
from .views.seo_views.estonia_seo.java_estonia import java
app.register_blueprint(java, subdomain="ee")
from .views.seo_views.estonia_seo.javascript_estonia import javascript
app.register_blueprint(javascript, subdomain="ee")
from .views.seo_views.estonia_seo.ruby_estonia import ruby
app.register_blueprint(ruby, subdomain="ee")
from .views.seo_views.estonia_seo.perl_estonia import perl
app.register_blueprint(perl, subdomain="ee")
from .views.seo_views.estonia_seo.pascal_estonia import pascal
app.register_blueprint(pascal, subdomain="ee")
from .views.seo_views.estonia_seo.delphi_estonia import delphi
app.register_blueprint(delphi, subdomain="ee")
from .views.seo_views.estonia_seo.cobol_estonia import cobol
app.register_blueprint(cobol, subdomain="ee")
from .views.seo_views.estonia_seo.assembly_estonia import assembly
app.register_blueprint(assembly, subdomain="ee")
from .views.seo_views.estonia_seo.asp_net_estonia import asp_net
app.register_blueprint(asp_net, subdomain="ee")
from .views.seo_views.estonia_seo.sql_estonia import sql
app.register_blueprint(sql, subdomain="ee")
from .views.seo_views.estonia_seo.objective_c_estonia import objective_c
app.register_blueprint(objective_c, subdomain="ee")
from .views.seo_views.estonia_seo.frontend_estonia import frontend
app.register_blueprint(frontend, subdomain="ee")
