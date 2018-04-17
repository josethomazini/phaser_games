document.title = "Collecting Stars";

function make_loading_text(obj) {
    let x = obj.sys.game.config.width / 2;
    let y = obj.sys.game.config.height / 3;

    let text = obj.add.text(
        x, y, 'Loading',
        {font: '50px Arial', fill: '#fff'}
    );

    text.setOrigin(0, 0);
}