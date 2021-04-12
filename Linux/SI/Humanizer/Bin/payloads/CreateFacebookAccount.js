class CreateFacebookAccount
{
    sleep (time) { return new Promise((resolve) => setTimeout(resolve, time));}
    async acceptCookies() { document.querySelector('button[title="Accept All"]').click(); }
    openRegistrationForm() { Array.from(document.querySelectorAll('a')).find(el => el.textContent === 'Create New Account').click();}
}

let FB = new CreateFacebookAccount();
FB.sleep(100).then(() => FB.acceptCookies()) .then(() => FB.sleep(100).then(() => FB.openRegistrationForm()))


