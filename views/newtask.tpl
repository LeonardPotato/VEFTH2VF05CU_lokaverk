%rebase('base.tpl',Page_Title='Todo list')

<h3>Add new task to the ToDo list</h3><br>
<form ation="/new" method="POST">
<label>Task</label><br>
<input type="text" size="100" name="task"><br>
<label>Description</label><br>
<textarea name="desc" rows="10" cols="30"></textarea><br>
<input type="submit" name="save" value="Save"><br>
<input type="button" value="Cancel" onClick="parent.location='/'">
</form>
<p>This is not a dynamically driven web page. It is a static page.</p>