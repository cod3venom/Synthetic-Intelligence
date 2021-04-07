
class Theme
{
    style;
    theme_options = {
        RED_HACKER: 1,
        BLUE_HACKER: 2,
        GREEN_HACKER: 3,
        BLACK_WHITE: 4
    }

    constructor() { this.createStyleElement().then(); }
    async createStyleElement()
    {
        this.style = document.createElement("style");
        this.style.type = "text/css";
        this.style.id = "humanizer";
        document.head.appendChild(this.style);
    }
    async addStyle(code) { this.style.innerText = code.replaceAll("\n",""); }
    async installRED() { await this.addStyle(`*, *::before,*::after {background: rgb(57, 0, 0)  !important; color: rgb(87, 0, 0) !important; }`);}
    async installBLUE() { await this.addStyle(`*, *::before,*::after {background: rgb(0, 56, 71)  !important; color: rgb(38, 139, 200) !important; }`);}
    async installGREEN() { await this.addStyle(`*, *::before,*::after {background: rgb(0, 0, 0)  !important; color: rgb(19, 250, 6) !important; }`);}
    async installBLACK_WHITE() { await this.addStyle(`*, *::before,*::after {background: rgb(0, 0, 0)  !important; color: rgb(255, 255, 255) !important; }`);}
    async install(theme_num)
    {
        switch (theme_num) {
            case this.theme_options.RED_HACKER:
                await this.installRED();
                break;
            case this.theme_options.BLUE_HACKER:
                await this.installBLUE();
                break;
            case  this.theme_options.GREEN_HACKER:
                await this.installGREEN();
                break
            case  this.theme_options.BLACK_WHITE:
                await this.installBLACK_WHITE();
                break;
        }
    }
}

let theme = new Theme();
theme.install("THEME_NUM;").then();