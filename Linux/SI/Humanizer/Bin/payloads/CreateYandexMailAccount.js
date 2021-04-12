class CreateYandexMailAccount
{

    async skipPhone()
    {
        let flag = false;
        document.querySelectorAll('div').forEach(function(element) {
             if (element.classList.contains('link_has-no-phone')){
                 element.querySelector("span").click();
                 flag = true;
             }
        })
        return flag;
    }
    async removeAllLabels(){ document.querySelectorAll("label").forEach(element => element.remove());}
    async create()
    {
        await this.removeAllLabels();
        return  await this.skipPhone();
    }

}

async function  getCaptcha(phone_skipped = false) {
    if (phone_skipped) {
        return new Promise(function (resolve, reject) {
            window.setTimeout(function () {
                resolve(document.querySelector('img[class="captcha__image"][alt="captcha image"]').getAttribute("src"));
            }, 1000)
        });
    }
}
async function runProcedure() {
    let createYandexMailAccount = new CreateYandexMailAccount();
    return createYandexMailAccount.create();
}
