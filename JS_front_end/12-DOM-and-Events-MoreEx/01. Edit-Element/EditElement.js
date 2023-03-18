function editElement(el, match, replacer) {
    let reg = new RegExp(match, 'g');
    let newText = el.textContent.replace(reg, replacer);
    el.textContent = newText;
}