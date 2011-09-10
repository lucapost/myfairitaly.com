import datetime

site_name = "My Fair Italy"
author = "Luca Postregna"
home = "/"
path_separator = "/"
src_ext = {"textile": "textile"}
dst_ext = "html"
hidden = set(["404.textile", "privacy.textile", "info.textile", "contacts.textile", "contatti.textile"])
current_time = datetime.datetime.now()

def header(node):
	"""Builds the header and returns it to a string."""
	return '''<!doctype html>
	<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
	<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="''' + language + '''"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="''' + language + '''"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="''' + language + '''"> <![endif]-->
	<!-- Consider adding a manifest.appcache: h5bp.com/d/Offline -->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="''' + language + '''"> <!--<![endif]-->
	<head>
		<meta charset="utf-8">

  		<!-- Use the .htaccess and remove these lines to avoid edge case issues.
		More info: h5bp.com/b/378 -->
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

		<title>''' + site_name + ' - ' + node.name + '''</title>
		<meta name="author" content="''' + author + '''" />
		<meta name="description" content="''' + description + ', ' + node.name + '''" /> 
  		<meta name="keywords" content="''' + keywords + ', ' + node.name + '''" /> 

  		<!-- Mobile viewport optimized: j.mp/bplateviewport -->
  		<meta name="viewport" content="width=device-width,initial-scale=1">

  		<!-- Place favicon.ico and apple-touch-icon.png in the root directory: mathiasbynens.be/notes/touch-icons -->

  		<link rel="stylesheet" href="/css/style.css">
  
  		<!-- More ideas for your <head> here: h5bp.com/d/head-Tips -->

		<link rel="stylesheet" type="text/css" media="all" href="/css/custom.css" /> 

  		<!-- All JavaScript at the bottom, except this Modernizr build incl. Respond.js
       		Respond is a polyfill for min/max-width media queries. Modernizr enables HTML5 elements & feature detects; 
       		for optimal performance, create your own custom Modernizr build: www.modernizr.com/download/ -->
  		<script src="js/libs/modernizr-2.0.6.min.js"></script>
	</head>
	<body>
		<div id="container" class="container_12">
			<div class="grid_8 prefix_1">
				<div class="barra">
					<p>''' + subtitle + '''</p>
				</div>
			</div>
			<div id="flagit" class="grid_1">
				<a href="/home.html" title="lingua italiana">
					<p class="hide">lingua italiana</p>
				</a>
			</div>
			<div id="flagen" class="grid_1">
				<a href="/en/home.html" title="english language">
					<p class="hide">english language</p>
				</a>
			</div>
			<header class="grid_10 prefix_1 suffix_1">
				<div id="title">
					<a href="''' + prefix + '''home.html" title="home">
						<h1 class="hide">''' + site_name + '''</h1>
						<p>&reg;</p>
					</a>
				</div>
				<div class="barra">
					<p>''' + site_desc + '''</p>
				</div>
			</header>
			<div class="clear"></div>
			<div id="boxsx" class="grid_6 prefix_1">
'''
def footer(node):
	"""Builds the footer and returns it to a string."""
	return '''<p><a href="#top" title="back to top">top</a></p>
			</div><!-- end boxsx -->
			<div id="boxdx" class="grid_4 suffix_1">
				<a href="''' + prefix + linkcontacts + '''.html" id="contacts" title="''' + linkcontacts + '''">
					<p class="hide">''' + linkcontacts + '''</p>
				</a>
				<menu>
					%%%MENU%%%
				</menu>
				<a href="http://www.booking.com/index.html?aid=339074" id="booking" title="booking">
					<p class="hide">booking</p>
				</a>
				<div id="twitter">
					<script src="http://widgets.twimg.com/j/2/widget.js"></script>
					<script>
					new TWTR.Widget({
					  version: 2,
					  type: 'profile',
					  rpp: 5,
					  interval: 6000,
					  width: 'auto',
					  height: 300,
					  theme: {
					    shell: {
					      background: '#dcdcdc',
					      color: '#000000'
					    },
					    tweets: {
					      background: '#ffffff',
					      color: '#000000',
					      links: '#6e5a00'
					    }	
					  },
					  features: {
					    scrollbar: false,
					    loop: false,
					    live: false,
					    hashtags: true,
					    timestamp: true,
					    avatars: false,
					    behavior: 'all'
					  }
					}).render().setUser('myfairitaly').start();
					</script>
				</div>
				<a href="https://www.facebook.com/pages/My-Fair-Italy/102008026501737" id="facebook" title="facebook">
					<p class="hide">facebook</p>
				</a>
			</div><!-- end boxdx -->
			<div class="clear"></div>
			<footer class="grid_10 prefix_1 suffix_1 clearfix">
				<div class="barra top20"></div>
				<p> My Fair Italy di Feel Italy snc di Giuditta Presenti, Allegra La Rosa, Paola Barsanti &amp; C. ::
				    Registered Office: v. 25 Aprile 1/A 56024 Ponte a Egola (Pi) :: C.F. 01956590507 :: REA: PI - 0168615 ::
				    Logo design: Arch. Pietro Dani - DNA STUDIO :: <a href="privacy.html">privacy</a> ::
				    <a href="''' + prefix + '''info.html">info</a><br/>
					&copy; ''' + str(current_time.year) + ''' <a href="http://luca.postregna.name">Luca Postregna</a> ::
					update: ''' + str(current_time.strftime("%Y%m%d")) + ''' ::
				<a href="http://validator.w3.org/check?uri=referer">xhtml</a> <a href="http://jigsaw.w3.org/css-validator/check/referer">css</a>
			</footer>
			<div class="clear"></div>
		</div>

  		<!-- JavaScript at the bottom for fast page loading -->

		<!-- Grab Google CDN's jQuery, with a protocol relative URL; fall back to local if offline -->
	  	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.6.3/jquery.min.js"></script>
	  	<script>window.jQuery || document.write('<script src="js/libs/jquery-1.6.3.min.js"><\/script>')</script>
	
	  	<!-- scripts concatenated and minified via build script -->
	  	<script defer src="js/plugins.js"></script>
	  	<script defer src="js/script.js"></script>
	 	<!-- end scripts -->

		<script type="text/javascript" src="/js/hashgrid.js"></script>  
		<script type="text/javascript" src="/js/flux.min.js"></script>
		<script type="text/javascript" src="/js/block.js"></script>  
		<script type="text/javascript" src="/js/slider.js"></script> 
			
  		<!-- Asynchronous Google Analytics snippet. Change UA-XXXXX-X to be your site's ID.
	       	mathiasbynens.be/notes/async-analytics-snippet -->
	  	<script>
	    		var _gaq=[['_setAccount','UA-6164762-11'],['_trackPageview'],['_trackPageLoadTime']];
	    		(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
	    		g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
	    		s.parentNode.insertBefore(g,s)}(document,'script'));
	  	</script>
	
		<!-- Prompt IE 6 users to install Chrome Frame. Remove this if you want to support IE 6.
			chromium.org/developers/how-tos/chrome-frame-getting-started -->
	  	<!--[if lt IE 7 ]>
	    		<script defer src="//ajax.googleapis.com/ajax/libs/chrome-frame/1.0.3/CFInstall.min.js"></script>
	    		<script defer>window.attachEvent('onload',function(){CFInstall.check({mode:'overlay'})})</script>
	  	<![endif]-->
	</body>
</html>'''
