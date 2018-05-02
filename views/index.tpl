%rebase('base.tpl',Page_Title='Todo list')
<ul>
%for row in rows:
<li><a href="/item{{row[0]}}">{{row[1]}}</li>
</ul>