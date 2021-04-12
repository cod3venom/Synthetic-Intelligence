`
    This file is used to iterate 
    over proposed friends list
    given from the facebook and
    send to the all of them friend requests.
`
// document.querySelector('div[aria-label="People You May Know"]');
class FacebookGetProposedPeopleContainer
{
    mainContainer;
    childSpans;
    params = {
        "MAIN_SELECTOR": 'div[aria-label="People You May Know"]',
        "TEXT_SELECTOR": 'span',
        "NEEDLE_INDICATOR": "Add Friend",
        "SUCCESS_COLOR": "green",
        "MARKER_CLASS": "HUMANIZER_PROPOSAL_FRIEND",
        "SEND_REQ_MSG": "Send friends request to > "
    }

    constructor() {
        this.mainContainer = document.querySelector(this.params.MAIN_SELECTOR);
        if (this.mainContainer !== undefined) { this.childSpans = this.mainContainer.querySelectorAll(this.params.TEXT_SELECTOR); }
    }
    sleep (time) { return new Promise((resolve) => setTimeout(resolve, time));}

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
    async addAllFriends()
    {
        let self = this;
        this.childSpans.forEach(function (target_element, index) {
            self.exploit(target_element, index);
        })
    }

    async debug(value) { console.log("[FacebookGetProposedPeopleContainer] ", value); }
}

facebookGetProposedPeopleContainer = new FacebookGetProposedPeopleContainer();
facebookGetProposedPeopleContainer.addAllFriends().then();
