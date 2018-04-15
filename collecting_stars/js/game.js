let config = {
    type: Phaser.AUTO,
    width: 640,
    height: 360,
    parent: 'phaser-app',
    scenes: [load, load, load]
};
 
let game = new Phaser.Game(config);