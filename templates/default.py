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
	return '''<!DOCTYPE html>
<html lang="''' + language + '''">
	<head>
		<title>''' + site_name + ' - ' + node.name + '''</title>
		<meta name="keywords" content="''' + keywords + ', ' + node.name + '''" /> 
		<meta name="description" content="''' + description + ', ' + node.name + '''" /> 
		<meta name="author" content="''' + author + '''" />
		<meta content="text/html; charset=UTF-8" http-equiv="content-type" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" /> 
		<link rel="icon" type="image/x-icon" href="/images/girasole.ico" />
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
		<script type="text/javascript" src="/js/hashgrid.js"></script>  
		<script type="text/javascript" src="/js/flux.min.js"></script>
		<script type="text/javascript" src="/js/block.js"></script>  
		<script type="text/javascript" src="/js/slider.js"></script> 
		<script type="text/javascript"> 
			var _gaq = _gaq || [];
			_gaq.push(['_setAccount', 'UA-15308846-1']);
			_gaq.push(['_trackPageview']);
			(function() {
				var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
				ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
				var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
			 })();
		</script> 
		<script type="text/javascript">
			var _gaq = _gaq || [];
			_gaq.push(['_setAccount', 'UA-6164762-11']);
			_gaq.push(['_trackPageview']);
			(function() {
				var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
				ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
				var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
			})();
		</script>
	</head>
	<body>
		<div id="container" class="container_12">
			<div class="grid_8 prefix_1">
				<div id="subtitle">	
					<p>''' + subtitle + '''</p>
				</div>
			</div>
			<a href="/home.html" title="lingua italiana">
				<div id="flagit" class="grid_1"></div>
			</a>
			<a href="/en/home.html" title="english language">
				<div id="flagen" class="grid_1"></div>
			</a>
			<header class="grid_10 prefix_1 suffix_1"><a href="''' + prefix + '''home.html" title="home">
				<div id="title">
					<h1 class="hide">''' + site_name + '''</h1>
					<p>&reg;</p>
				</div></a>	
				<div class="barra">
					<p>''' + site_desc + '''</p>
				</div>
				<div id="top"></div>
			</header>
			<div class="clear"></div>
			<div id="boxsx" class="grid_6 prefix_1">
'''
def footer(node):
	"""Builds the footer and returns it to a string."""
	return '''
			<p><a href="#top" title="back to top">top</a></p>
			</div><!-- end boxsx -->
			<div id="boxdx" class="grid_4 suffix_1">
				<a href="''' + prefix + linkcontacts + '''.html" title="''' + linkcontacts + '''"><div id="contacts"></div></a>
				<menu>
					%%%MENU%%%
				</menu>
				<a href="http://www.booking.com/index.html?aid=339074"><div id="booking"></div></a>
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
				<a href="https://www.facebook.com/pages/My-Fair-Italy/102008026501737"><div id="facebook"></div></a>
			</div><!-- end boxdx -->
			<div class="clear"></div>
			<footer class="grid_10 prefix_1 suffix_1 clearfix">
				<div class="barra"></div>
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
	</body>
</html>'''
