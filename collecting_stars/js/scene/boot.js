let boot = new Phaser.Scene('boot');

boot.preload = function() {
    this.load.image('progress_bar', 'img/progress_bar.png');
}

boot.create = function() {
    this.scene.launch('load');
}
