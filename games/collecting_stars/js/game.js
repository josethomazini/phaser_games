let config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    parent: 'phaser-app',
    scene: [boot, load]
};

window.onload = function() {
    let game = new Phaser.Game(config);
};
