$(document).ready(function() {
	fetch()
	setInterval(fetch, 1000);
});

function fetch() {
		$.ajax({
			url: "throw/fetch",
			type: "GET",
			async: false,
			
			success: function(data) {
				var count = $('#counter');
				count.html(parseInt(count.html()) + 1);

				var tweet_id = Math.floor(Math.random() * 10000);
				var tweet_bundle = '.tweet_bundle#' + tweet_id;
				var tweet_html = make_html(data, tweet_id);

				$('.tweet_space').prepend(tweet_html);
				$(tweet_bundle).css('top', data.css_top.toString() + "%");
				$(tweet_bundle).css('left', data.css_left.toString() + "%");
				$(tweet_bundle).addClass('animated slideInUp');

				handle_animation(tweet_bundle);
				handle_hover(tweet_bundle, data);
				handle_click(tweet_bundle, data);
			},
			error: function(data) {
				console.log("Cant fetch tweeeet");
			},
		});
}

function handle_hover(tweet_bundle, data) {
	$(tweet_bundle).hover(
		function () {
			if (data.location != null) {
				$(this).find('#location').stop(true, true).fadeIn();
			}
		},
		function () {
			$(this).find('#location').stop(true, true).fadeOut();
		}
	);
}

function handle_click(tweet_bundle, data) {
	$(tweet_bundle).click(
		function () {
			populate_modal(data);
			$('.tweet-modal').modal();
			$('.tweet-modal').show();
			$('.tweet-modal').on('hidden.bs.modal', function() {
				$('.tweet-modal').hide();
			});
		}
	);
}

function handle_animation(tweet_bundle) {
	$(tweet_bundle).on(
	'webkitAnimationEnd mozAnimationEnd MSAnimationEnd onanimationend animationend',
		function () {
			$(this).removeClass('animated bounceIn').delay(1500).fadeOut(4500, function() {
				$(this).remove();
			});
		}
	);
}

function populate_modal(data) {
	$('#modal-avatar').attr('src', data.larger_pic);
	$('#modal-tweet').text(data.tweet);
	$('#modal-screen-name').text(data.screen_name);
	$('#modal-screen-name-value').val('@' + data.screen_name);
	$('textarea#modal-reply-text').val('');
	$('textarea#modal-reply-text').attr('maxlength', 138 - data.screen_name.length);
}

function make_html(data, tweet_id) {
	var link_html = "";
	for (var l in data.links) {
		link_html += "</br><span hidden class='link'><a href='{}'></a></span>".replace(
				/{}/, data.links['found']);
	}
	var tweet_html = 
		"<span class='tweet_bundle' id='" + tweet_id + "'>" +
			"<img src='{}'/>".replace(/{}/, data.profile_pic) + 
			"<span class='screen_name'>{" + data.screen_name + "}</span></br>" +
			"<span class='tweet'> " + data.tweet + "</span>" +
			"</br><span hidden id='location'>" + data.location + "</span>" +
			"</br><span hidden id='links'>" + data.links['found'] + "</span>" +
			link_html +
		"</br></span>";
	return tweet_html;
}
