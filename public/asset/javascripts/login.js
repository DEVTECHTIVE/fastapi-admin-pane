$(document).ready(function () {
  let username = $('#username');
  let password = $('#password');
  let msg = $('#msg');
  let login = $('#login');

  const get_user = username => {
    let res = $.ajax({
      url: `/user/${username}`,
      type: 'GET',
      async: false,
      success: function (data) {
        return data;
      },
      error: function (err) {
        return err;
      },
    }).responseText;
    return JSON.parse(res);
  };

  username.focusout(function () {
    user = username.val();
    const data = get_user(username.val());
    if (data === null || data === undefined) {
      msg.text('Username not found');
    } else if (data.message === 'User not found') {
      msg.text('Username not found');
    }
  });

  username.keypress(function (e) {
    msg.text('');
  });

  login.click(function (e) {
    e.preventDefault();
    if (password.val() == '') {
      msg.text('Please enter your password');
    }
    console.log(password.val());
  });
});
