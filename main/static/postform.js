var content_of_post = document.getElementById('id_content');
content_of_post.placeholder = 'Content'
var textLocation = document.getElementById('content-text-area');
var f_content = function(){
	
	var content_text_value = content_of_post.value;
		textLocation.innerHTML = content_text_value;
}

var title_of_post = document.getElementById('id_title');
title_of_post.style = 'width: 505px;';
content_of_post.style = 'width: 505px;';
title_of_post.placeholder = 'Title';
f_content();

var btn_back = document.getElementsByClassName('back');

btn_back[0].onclick = function(){
	location.replace("/"); 
}

content_of_post.addEventListener('keyup', f_content);