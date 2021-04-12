function scrollToElement(element)
{
    if (element !== undefined && element !== null)
    {
        element.scrollIntoView({
            behavior: 'smooth'
        });
    }
}

scrollToElement(document.querySelector('SELECTOR;'));