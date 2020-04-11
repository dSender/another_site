var content_of_post = document.getElementById('id_content');
content_of_post.placeholder = 'Content'
var textLocation = document.getElementById('content-text-area');
var f_content = function(br){
	if(br){
		content_of_post.value += '</br>';
	}
	else{
		content_of_post.value += '';
	}
	var content_text_value = content_of_post.value;
	textLocation.innerHTML = content_text_value;

}

var title_of_post = document.getElementById('id_title');
title_of_post.style = 'width: 505px;';
content_of_post.style = 'width: 505px;';
title_of_post.placeholder = 'Title';
f_content(false);

var btn_back = document.getElementsByClassName('back');

btn_back[0].onclick = function(){
	location.replace("/"); 
}
var title = document.getElementById('title');
title_of_post.addEventListener('keyup', function(){
	title.innerHTML = title_of_post.value;
});

content_of_post.addEventListener('keyup', function(event){
	if(event.key === 'Enter'){
		var br = true;
	}
	else{
		var br = false;
	}
	f_content(br);
});