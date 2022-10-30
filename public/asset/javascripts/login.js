const get_user = username => {
  $.ajax({
    url: `localhost:8000/users/{username}`,
    type: 'GET',
    success: function (data) {
      console.log(data);
      return data;
    }.bind(this),
    error: function (xhr, status, err) {
      console.error(status, err.toString());
      return null;
    }.bind(this),
  });
};

$(document).ready(function () {
  let username = $('#username');
  let password = $('#password');
  let msg = $('#msg');
  let login = $('#login');

  username.focusout(() => {
    const data = get_user(username.val());
    if (username.val() == data.username) {
      console.log('username is valid');
    } else {
      msg.text('username is invalid');
    }
  });

  login.click(function (e) {
    e.preventDefault();
    if (password.val() == '') {
      msg.text('Please enter your password');
    }
    console.log(password.val());
  });
});
