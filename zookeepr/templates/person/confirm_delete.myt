<h2>Delete person</h2>

<% h.form(h.url_for()) %>
<p> Are you sure you want to delete this person?</p>
<% h.submitbutton('Delete') %>
<% h.end_form() %> or <% h.link_to('No, take me back.', url=h.url(action='index', id=None)) %>
