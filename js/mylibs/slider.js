$(function(){
	if(!flux.browser.supportsTransitions)
		alert("Flux Slider requires a browser that supports CSS3 transitions, please update to Firefox5+ or Chrome12+");
	window.slider = new flux.slider('#slider', {
        	pagination: true,
                autoplay: true
	});
	window.slider = new flux.slider('#sliderhome', {
        	pagination: false,
		transitions: [ 'zip' ],
                autoplay: true
	});
});
