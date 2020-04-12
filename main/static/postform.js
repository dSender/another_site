var content_of_post = document.getElementById('id_content');
content_of_post.placeholder = 'Content'
content_of_post.id = 'editor1';
var editor = CKEDITOR.replace('editor1',{height: 500, width: 1500});
AjexFileManager.init({returnTo: 'ckeditor', editor: editor});

var title_of_post = document.getElementById('id_title');
title_of_post.style = 'width: 505px;';
content_of_post.style = 'width: 505px;';
title_of_post.placeholder = 'Title';


var btn_back = document.getElementsByClassName('back');

btn_back[0].onclick = function(){
	location.replace("/"); 
}

title_of_post.addEventListener('keyup', function(event){
	title.innerHTML = title.innerHTML.replace('<', '&lt;');
	title.innerHTML = title.innerHTML.replace('>', '&gt;');
});
