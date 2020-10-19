var query = location.search;
var value = query.split('=');

var name = decodeURIComponent(value[1])
$(document).ready(function() {
  $(document.body).hide().fadeIn("slow");
  $('#winner p').text(name);
});
