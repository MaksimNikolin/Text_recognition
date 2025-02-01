const tesseract = require('tesseract.js');

tesseract.recognize('./text3.png', ['rus', 'eng'], {
    logger: e => {
        console.log(e);
    }
})
.then(out => {
    let text = out.data.text;
    text = text.split('\n').map(line => line.replace(/[^a-zA-Zа-яА-Я0-9ёЁ.,-—:;!?\s]/g, '').trim()).join(' ');
    console.log('Output text:', text);
})
.catch(error => {
    console.error(error);
});
