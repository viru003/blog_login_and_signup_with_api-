

function login() {
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    var csrf = document.getElementById('csrf').value
    if (username == "" && password == "") {
        alert('you must enter both')
    }
    else{
    var data = {
        'username': username,
        'password': password
    }
    fetch('api/login/', {
        method: "post",
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrf,
        },
        'body': JSON.stringify(data)
    }).then(result => result.json())
        .then(response => {
            if (response.status == 200) {
                window.location.href = '/dashboard'
            }
            else {
                alert(response.message)
            }
        })
    }
}


function register() {
    var username = document.getElementById('username').value;
    console.log(username)
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var password1 = document.getElementById('password1').value;
    var csrf = document.getElementById('csrf').value;
    if (username == "" || password == "" || email == "" || password1 == "") {
        alert('you must enter in all rows')
    }
    else {

    if (typeof jsVar == 'undefined') {
        console.log("good")
      }
    var data = {
        'username': username,
        'email': email,
        'password': password,
        'password1': password1
    }

    fetch('api/register/', {
        method: "post",
        headers: {
            'content-type': 'application/json',
            'x-CSRFToken': csrf
        },
        'body': JSON.stringify(data)
    }).then(result => result.json())
        .then(response => {
            if (response.status == 200) {
                alert(response.message)
                window.location.href = '/'
            }
            else {
                alert(response.message)
            }
        })
    }
}