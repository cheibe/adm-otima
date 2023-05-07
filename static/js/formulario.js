var username = document.getElementById('username');
var senha = document.getElementById('senha');
var email = document.getElementById('email');

username.addEventListener('focus',()=>{
    username.style.borderColor = "#5e6266";
});

username.addEventListener('blur',()=>{
    username.style.borderColor = "#ccc";
});


senha.addEventListener('focus',()=>{
    senha.style.borderColor = "#5e6266";
});

senha.addEventListener('blur',()=>{
    senha.style.borderColor = "#ccc";
});


email.addEventListener('focus',()=>{
    email.style.borderColor = "#5e6266";
});

email.addEventListener('blur',()=>{
    email.style.borderColor = "#ccc";
});