class CreateFacebookAccount
{
    async acceptCookies() { document.querySelector('button[title="Accept All"]').click(); }
    async openRegistrationForm() {Array.from(document.querySelectorAll('a')).find(el => el.textContent === 'Create New Account').click();}
    sleep (time) { return new Promise((resolve) => setTimeout(resolve, time));}
    async inputData(element, value)
    {
        element.focus();
        element.value = value;
        element.click();
    }
    async chooseGender() {Array.from(document.querySelectorAll('input[type="radio"][name="sex"]')).find(el => el.value === 'GENDER;').click();}
    async fillForm()
    {
        const firstName = await this.inputData(document.querySelector('input[name="firstname"]'), 'FIRSTNAME;');
        const lastName = await this.inputData(document.querySelector('input[name="lastname"]'), 'LASTNAME;');
        const email1 = await this.inputData(document.querySelector('input[name="reg_email__"]'), 'EMAIL;');
        const email2 = await this.inputData(document.querySelector('input[name="reg_email_confirmation__"]'),'EMAIL;');
        const password = await this.inputData(document.querySelector('input[name="reg_passwd__"]'), 'PASSWORD;');

        const month = await this.inputData(document.querySelector('select[id="month"]'), "BIRTH_MONTH;");
        // const day = await this.inputData(document.querySelector('select[id="day"]'), "BIRTH_DAY;");
        // const year = await this.inputData(document.querySelector('select[id="year"]'), "BIRTH_YEAR;");
        // const gender = await this.chooseGender();
        // const submit = document.querySelector('button[name="websubmit"]').click();
    }

    async create()
    {
        await this.acceptCookies();
        await this.openRegistrationForm();
        this.sleep(1000).then(()=>{
            this.fillForm();
        });
    }

}


let createFB = new CreateFacebookAccount();
createFB.create().then();
