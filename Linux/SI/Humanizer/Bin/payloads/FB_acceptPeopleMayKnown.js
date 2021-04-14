class FB_acceptPeopleMayKnown
{

    mainContainer;
    childSpans;
    params = {
        "MAIN_SELECTOR": 'div[aria-label="Friend Requests"]',
        "TEXT_SELECTOR": 'span',
        "NEEDLE_INDICATOR": "Confirm",
        "SUCCESS_COLOR": "green",
        "MARKER_CLASS": "HUMANIZER_ACCEPT_MAY_KNOWN",
        "SEND_REQ_MSG": "Accepted friend request from > "
    }

    constructor() {
        this.mainContainer = document.querySelector(this.params.MAIN_SELECTOR);
        if (this.mainContainer !== undefined) { this.childSpans = this.mainContainer.querySelectorAll(this.params.TEXT_SELECTOR); }
    }

    async markTarget(target_element, index)
    {
        target_element.setAttribute(this.params.MARKER_CLASS,this.params.MARKER_CLASS+"_"+index)
        let elementLink = target_element.parentNode.parentNode.parentNode.parentNode.querySelector('a[href*="/friends/?profile_id="');
        await this.debug(this.params.SEND_REQ_MSG + elementLink.textContent.toString() + "(" + elementLink.getAttribute("href") +")");
    }
    async exploit(target_element, index)
    {
        let self = this;
        setTimeout(function ()
        {
            if (target_element !== null)
            {
                if(target_element.textContent === self.params.NEEDLE_INDICATOR)
                {
                    target_element.click();
                    self.markTarget(target_element, index);
                }
            }
        }, 700 * index)
    }
    async acceptRequest()
    {
        let self = this;
        this.childSpans.forEach(function (target_element, index) {
            self.exploit(target_element, index);
        })
    }

    async debug(value) { console.dir("[FB_acceptPeopleMayKnown] ", value); }
}
fb_acceptPeopleMayKnown = new FB_acceptPeopleMayKnown();
fb_acceptPeopleMayKnown.acceptRequest().then();