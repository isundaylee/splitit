function get_checkbox(type, id) {
  return $(".transaction-member[data-member-id='" + id + "'] ." + type + " input[type=checkbox]");
}

function get_text(type, id) {
  return $(".transaction-member[data-member-id='" + id + "'] ." + type + " p");
}

function uncheck(type, id) {
  get_checkbox(type, id).attr('checked', false);
  get_text(type, id).hide();
}

function check(type, id) {
  get_checkbox(type, id).prop('checked', '1');
  get_text(type, id).show();
}

function toggle(type, id) {
  var box = get_checkbox(type, id);

  if (box.prop('checked'))
    uncheck(type, id);
  else
    check(type, id);
}

$(function() {
  $('.transaction-member .owes, .transaction-member .paid').click(function() {
    toggle($(this).data('toggle-type'), parseInt($(this).data('member-id')))
  })
});