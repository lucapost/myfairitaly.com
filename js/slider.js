$(function(){
	if(!flux.browser.supportsTransitions)
		alert("Flux Slider requires a browser that supports CSS3 transitions, please update to Firefox5+, Chrome12+ or Explorer9+");
	window.slider1 = new flux.slider('#slider1', {
        	pagination: false,
                autoplay: false
	});
	window.slider2 = new flux.slider('#slider2', {
        	pagination: false,
                autoplay: false
        });
	window.slider3 = new flux.slider('#slider3', {
        	pagination: false,
                autoplay: false
        });
	window.slider4 = new flux.slider('#slider4', {
        	pagination: false,
                autoplay: false
        });
	window.slider5 = new flux.slider('#slider5', {
        	pagination: false,
                autoplay: false
        });
	window.slider6 = new flux.slider('#slider6', {
        	pagination: false,
                autoplay: false
        });
	window.slider7 = new flux.slider('#slider7', {
        	pagination: false,
                autoplay: false
        });
});
