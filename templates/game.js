let config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    parent: 'phaser-app',
    scene: {{ scene_list }}
};

window.onload = function() {
    let game = new Phaser.Game(config);
};
