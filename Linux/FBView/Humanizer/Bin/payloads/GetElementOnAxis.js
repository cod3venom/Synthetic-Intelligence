function initializeAxis() {
    let element = document.querySelector('NEEDLE');
    let x = 0, y = 0;

    if (element !== undefined && element !== null)
    {
        const rect = element.getBoundingClientRect();
        x = rect.left + window.scrollX;
        y = rect.top + window.scrollY;
    }
    return {X: x, Y: y};
}