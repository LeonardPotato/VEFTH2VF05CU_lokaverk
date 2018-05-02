%rebase('item.tpl',Page_Title='Todo list')
<div class="task_title">
<h2>{{ttitle}}</h2>
</div>
<div class="task_date">Posted: {{tdate}}</div>
<div class="task_desc"><p>{{tdesc}}</p></div>
<button type="button" onClick="goBack()">Back</button><button type="button" onClick="location.href='/edit{{todoid}}}'">Edit</button>
<script>
function goBack() {
	window.history.back();
}
</script>