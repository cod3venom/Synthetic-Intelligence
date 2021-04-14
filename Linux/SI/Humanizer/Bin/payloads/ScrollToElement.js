if (window.jQuery)
{
    function scrollToElement(element) {
        let target = $('SELECTOR;');
        if (target !== undefined && target !== null)
        {
            $('html, body').animate({ scrollTop: target.offset().top }, 1000);
        }
    }

    scrollToElement();
}