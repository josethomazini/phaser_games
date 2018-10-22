let stage = new Phaser.Scene('stage');

stage.preload = function() {

};

stage.create = function() {
    this.add.image(400, 300, 'sky');

    platforms = this.physics.add.staticGroup();

    platforms.create(400, 568, 'platform').setScale(2).refreshBody();

    platforms.create(600, 400, 'platform');
    platforms.create(50, 250, 'platform');
    platforms.create(750, 220, 'platform');
};
