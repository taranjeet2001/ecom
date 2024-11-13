document.getElementById('sign-up').addEventListener('click',function(){
    showForm('signupForm')
});

document.getElementById('log-in').addEventListener('click',function(){
    showForm('loginForm')
});


function showForm(formId) {
    const forms = document.querySelectorAll('.form');
    forms.forEach(form => {
        form.classList.remove('active');
    });
    document.getElementById(formId).classList.add('active');
}




document.getElementById('log-in').addEventListener('click', function() {
    showForm('loginForm'); // Assumes you have a login form setup
});

document.getElementById('resend-otp').addEventListener('click', function() {
    alert("OTP resent!"); // Placeholder action; replace with actual OTP resend functionality
});

function showForm(formId) {
    const forms = document.querySelectorAll('.form');
    forms.forEach(form => {
        form.classList.remove('active');
    });
    document.getElementById(formId).classList.add('active');
}
