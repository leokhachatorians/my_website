function fetch() {
	$.ajax({
		url: "trumpify/fetch",
		type: "GET",
		async: true,

		success: function(data) {
			$('#text').text(data['sentence']);
			$('#likes').text(data['likes']);
			$('#retweets').text(data['retweets']);
			$('#date').text(data['date']);

			var count = $('#counter');
			count.html(parseInt(count.html()) + 1);
		},
		error: function() {
			$('#text').text("Unable to Trumpify. Try Again!");
		},
	});
}
