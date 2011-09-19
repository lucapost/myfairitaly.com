$(document).ready(function() {
	$(".block").hide(); 
	$("ul.tabs li:first").addClass("active").show();
	$(".block:first").show(); 
	$("ul.tabs li").click(function() {
		$("ul.tabs li").removeClass("active"); 
		$(this).addClass("active"); 
		$(".block").hide(); 
		var activeTab = $(this).find("a").attr("href"); 
		$(activeTab).fadeIn(1000); 
		return false;
	});
});	
