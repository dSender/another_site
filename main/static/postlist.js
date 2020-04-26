$(document).ready(function(){
	var $publish_button = $('.publish');
	var $csrf_mid = $("[name=csrfmiddlewaretoken]").val();

	$publish_button.click(function(){
		$.ajax({
			type: 'POST',
			headers:{
				"X-CSRFToken": $csrf_mid
			},			
			data: {id: $publish_button.attr('id')},
			
		});
		if($(this).attr('class') === 'btn publish btn-success'){
			$(this).attr('class', 'btn publish btn-danger');
			$(this).text('Unpublish');
		}
		else{
			$(this).attr('class', 'btn publish btn-success');
			$(this).text('Publish');
		}
	});
});