// js/index.js

// Function to copy code
function copyCode(code) {
    const pre = document.createElement('pre');
    pre.textContent = code;
    document.body.appendChild(pre);
    
    navigator.clipboard.writeText(code)
        .then(() => {
            alert('Code copied to clipboard!');
            pre.remove();
        })
        .catch(err => {
            console.error('Error copying code: ', err);
            pre.remove();
        });
}