let load = new Phaser.Scene('load');

load.preload = function() {
    this.make_loading_text();
    this.start_progress_loader();
    this.load_assets();
};

load.create = function() {
    this.scene.start('stage');
};

// ############################################################################

load.make_loading_text = function() {
    let x = config.width / 2;
    let y = config.height / 3;

    let text = this.add.text(
        x, y, 'Loading',
        {font: '50px Arial', fill: '#fff'}
    );

    text.setOrigin(0, 0);
};

load.start_progress_loader = function() {
    let progress = this.add.graphics();

    this.load.on('progress', function(value) {
        progress.clear();
        progress.fillStyle(0xffffff, 1);
        progress.fillRect(0, 270, 800 * value, 60);

    });

    this.load.on('complete', function () {
        progress.destroy();
    });
};

load.load_assets = function() {
    load_images(this);
    load_spritesheets(this);
    load_audios(this);
    load_bitmap_font(this);
}
