
var title_of_post = document.getElementById('id_title');
title_of_post.style = 'width: 505px;';
title_of_post.placeholder = 'Title';


var btn_back = document.getElementById('back');
btn_back.onclick = function(){
	console.log(1);
	location.replace("/"); 
}

title_of_post.addEventListener('keyup', function(event){
	title.innerHTML = title.innerHTML.replace('<', '&lt;');
	title.innerHTML = title.innerHTML.replace('>', '&gt;');
});

var content_of_post = document.getElementById('id_content');
content_of_post.placeholder = 'Content'
content_of_post.id = 'editor1';
content_of_post.style = 'width: 505px;';

var editor = CKEDITOR.replace('editor1',{height: 500, width: 700});
AjexFileManager.init({returnTo: 'ckeditor', editor: editor});
