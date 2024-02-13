@namespace
class SpriteKind:
    coin = SpriteKind.create()

def on_overlap_tile(sprite, location):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_a_pressed():
    if bob.vy == 0:
        bob.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite2, otherSprite):
    info.change_score_by(1)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.coin, on_on_overlap)

def on_overlap_tile2(sprite3, location2):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile2)

coin2: Sprite = None
bob: Sprite = None
bob = sprites.create(assets.image("""
    design1
"""), SpriteKind.player)
controller.move_sprite(bob, 100, 0)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
scene.set_background_color(9)
tiles.place_on_random_tile(bob, assets.tile("""
    myTile7
"""))
bob.ay = 350
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe55555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff455fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ee5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5cfffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5557cccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5555cccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5557cccccffffcfffffffffffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffff
        fffffffff55feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff557cccccccffcccffffffffffffffffffffffffffffffffffffffffffffff45ffffffffffffffffffff
        fffffff555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55ccccccccfffffffffffffffffffffffffffffffffffffffffffffffff5555554fffffffffffffffff
        fffffff55555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ccccccccffffccfffffffffffffffffffffffffffffffffffffffffff555554ffffffffffffffffff
        fffffffff5555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccfffccfffffffffffffffffffffffffffffffffffffffffffff555fffffffffffffffffff
        fffffffff55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccfffffffffffffffffffffffffffffffffffffffffffffffff55555efffffffffffffffff
        ffffffff55ff5efffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccccccccccccccfffffffffffffffffffffffffffffffffffffffffffffff555ff55fffffffffffffffff
        ffffffff5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe444eccccccceccecccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeee444444eeee4cceceeceeec4efeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5554444eeee444ee44eee4eee44444eefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff444ee4eeeeee4444ee4444ee44eee44444eeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe444444eeeeee44444eee4444eee444ee44444ee4ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff44444444eeeeeee4444ee444444ee444eeee44eee4444fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffff444444444eee444eee44ee4444444ee4444eeeeeee4444444fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffff444444444eee444444eeeee4444eeeeeeeee4eeee44444444444fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff444444444eee44444444eeeeeeeeeee4eeeeeeeeee444444444444ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffff444444444ee44444444444eeeeeee44444ee44444eee444444444444fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff444444444ee44444444444ee44444444444ee444444ee4444444444444ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffff444444444ee444444444444ee444444444444ee444444ee444444444444ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffff44444444ee444444444444ee4444444444444ee4444444ee444444444444fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff44444444ee4444444444444ee4444444444444ee4444444ee444444444444effffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffe4444444eee444444444444eee44444444444444ee4444444ee444444444444ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff44444444ee44444444444411d44444444444444d1d4444444ee444444444444efffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff44444444ee444444444444111dd444444444444d11ddb444444ee444444444444fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff44444444ee44444444444d115ddd444444444441155ddb44444ee4444444444444ffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff44444444ee44444444444411555dd4444444444115555dd444444ee444444444444efffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff44444444ee444444444441155555dd4444444431555555dd44444ee4444444444444effffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff4444444ee4444444444445555555dd4444444445554e45dd444444ee444444444444effffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff4444444ee44444444444555ee455dd4444444455554ee55dd44444ee444444444444effffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff4444444ee444444444444454ee44ddd44444444545544eeddb44444ee444444444444effffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff4444444ee44444444444444ee44444444444444444444ee444444444ee44444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff4444444ee44444444444444ee44444444444444444444ee444444444ee44444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff444444ee444444444444444ee44444444444444444444ee4444444444ee4444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff444444ee44444444444444ee444444444411d444444444e4444444444ee4444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff444444ee44444444444444ee444444444111dd44444444ee444444444ee4444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff44444ee444444444444444ee444444444115dd44444444ee444444444ee4444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff44444ee444444444444444e44444444411555dd4444444ee4444444444ee444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff44444ee44444444444444ee4444444441d555dd4444444ee4444444444ee44444444eeefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff44444ee44444444444444ee444444445dddddddd444444eed444444444ee44444444eeecccccccccccccc88888888888888888888888888888
        888888888888888888888888888888888888888888888844444e444444444444444e51d4444445dddddddd444444edd4444444444e4444444eeee8888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888c444ee444444444444444e511144444444444444444444ddd4444444444e4444444eeec8888888888888888888888888888888888888888888
        888888866b9999999999999999999999999999999988888444ee44444444444444ee55111d444444444444444454dd44444444444ee444444eee88888888888888888888888888888888888888888888
        99999999999999999999999999999999999999999968888444ee44444444444444ee4555111d444444444444455ddb44444444444ee44444eeee88888888888888888888888888888888888888888888
        99996666688888888888888888888888888888888888888844ee44444444444444ee4455551144444444444445ddde44444444444ee44444eeec88888888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888844ee44444444444444ee4445555544455551114445ddee44444444444ee4444eeee888888888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888884ee44444444444444ee444555555555555555555dddee44444444444ee4444eeec888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888844ee4444444444444e4444455555555555555555dd4ee44444444444ee444eee88888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888884ee4444444444444e444444555555511115555dd44ee44444444444ee44eeeffff88888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888888ee4444444444444ee44444455dddd511dddddd444ee4444444444ee4eeeeffffffffc8888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888888ce4444444444444ee44444445dd444ddddbdd4444ee4444444444eeeeeeffffffffff8888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888ee444444444444ee44444444bd44455444db4444ee4444444444eeeecfffffffffffff88888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888e444444444444ee444444444444444444444444ee444444444eeeefffffffffffffffc8888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888888888884444444444ee444444444444444444444444ee4444444eeeeeffffffffffffffffff888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888884444444444ee44444444444444444444444ee44444eeeeefffffffffffffffffff8888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888e4444444ee4444444444444444444444ee444eeeeeefffffffffffffffffffff8888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888e4444ee4444444444444444444444eeeeeeeefffffffffffffffffffffff88888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888888feeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffc888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888fffffffffeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffff8888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffff888888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888888888cffffffffffffffffffffffffffffffffffffffffffc888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888888888888888888888888888cffcffffffffffffffffffffcc88888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888886866666666666b9999888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888886999999999999999999999999999999999999999999888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888889999999999999999999999966666666666666688888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
"""))
scene.camera_follow_sprite(bob)
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile3
""")):
    coin2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . . f 5 5 5 5 5 f . . . . . 
                    . . . f 5 4 4 4 4 5 5 f . . . . 
                    . . f 5 4 5 5 5 5 4 5 5 f . . . 
                    . . f 5 4 5 5 5 5 5 5 5 f . . . 
                    . . f 5 4 5 5 5 5 5 5 5 f . . . 
                    . . f 5 4 5 5 5 5 5 5 5 f . . . 
                    . . f 5 4 5 5 5 5 4 5 5 f . . . 
                    . . . f 5 4 4 4 4 5 5 f . . . . 
                    . . . . f 5 5 5 5 5 f . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.coin)
    animation.run_image_animation(coin2,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 5 5 5 5 5 5 f . . . . . 
                        . . f 5 4 4 4 4 4 4 5 f . . . . 
                        . . f 5 4 5 5 5 5 4 5 f . . . . 
                        . . f 5 4 5 5 5 5 5 5 f . . . . 
                        . . f 5 4 5 5 5 5 5 5 f . . . . 
                        . . f 5 4 5 5 5 5 5 5 f . . . . 
                        . . f 5 4 5 5 5 5 4 5 f . . . . 
                        . . f 5 4 4 4 4 4 4 5 f . . . . 
                        . . . f 5 5 5 5 5 5 f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f f f . . . . . . . . 
                        . . . f 5 5 5 5 f . . . . . . . 
                        . . f 5 4 4 4 4 5 f . . . . . . 
                        . . f 5 4 5 5 4 5 f . . . . . . 
                        . . f 5 4 5 5 5 5 f . . . . . . 
                        . . f 5 4 5 5 5 5 f . . . . . . 
                        . . f 5 4 5 5 5 5 f . . . . . . 
                        . . f 5 4 5 5 4 5 f . . . . . . 
                        . . f 5 4 4 4 4 5 f . . . . . . 
                        . . . f 5 5 5 5 f . . . . . . . 
                        . . . . f f f f . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f f . . . . . . . . . 
                        . . . f 5 5 5 f . . . . . . . . 
                        . . f 5 4 4 4 5 f . . . . . . . 
                        . . f 5 4 5 4 5 f . . . . . . . 
                        . . f 5 4 5 5 5 f . . . . . . . 
                        . . f 5 4 5 5 5 f . . . . . . . 
                        . . f 5 4 5 5 5 f . . . . . . . 
                        . . f 5 4 5 4 5 f . . . . . . . 
                        . . f 5 4 4 4 5 f . . . . . . . 
                        . . . f 5 5 5 f . . . . . . . . 
                        . . . . f f f . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f . . . . . . . . . . 
                        . . . f 5 5 f . . . . . . . . . 
                        . . f 5 4 4 5 f . . . . . . . . 
                        . . f 5 4 4 5 f . . . . . . . . 
                        . . f 5 4 5 5 f . . . . . . . . 
                        . . f 5 4 5 5 f . . . . . . . . 
                        . . f 5 4 5 5 f . . . . . . . . 
                        . . f 5 4 4 5 f . . . . . . . . 
                        . . f 5 4 4 5 f . . . . . . . . 
                        . . . f 5 5 f . . . . . . . . . 
                        . . . . f f . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f . . . . . . . . . . 
                        . . . f 5 f . . . . . . . . . . 
                        . . f 5 4 5 f . . . . . . . . . 
                        . . f 5 4 5 f . . . . . . . . . 
                        . . f 5 5 5 f . . . . . . . . . 
                        . . f 5 5 5 f . . . . . . . . . 
                        . . f 5 5 5 f . . . . . . . . . 
                        . . f 5 4 5 f . . . . . . . . . 
                        . . f 5 4 5 f . . . . . . . . . 
                        . . . f 5 f . . . . . . . . . . 
                        . . . . f f . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f . . . . . . . . . . . 
                        . . . f f . . . . . . . . . . . 
                        . . f 5 5 f . . . . . . . . . . 
                        . . f 5 5 f . . . . . . . . . . 
                        . . f 5 5 f . . . . . . . . . . 
                        . . f 5 5 f . . . . . . . . . . 
                        . . f 5 5 f . . . . . . . . . . 
                        . . f 5 5 f . . . . . . . . . . 
                        . . f 5 5 f . . . . . . . . . . 
                        . . . f f . . . . . . . . . . . 
                        . . . . f . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . f . f . . . . . . . . . . . 
                        . . f f 5 . . . . . . . . . . . 
                        . . 5 f 4 . . . . . . . . . . . 
                        . . 5 f 4 . . . . . . . . . . . 
                        . . 5 f 5 . . . . . . . . . . . 
                        . . 5 f 5 . . . . . . . . . . . 
                        . . 5 f 5 . . . . . . . . . . . 
                        . . 5 f 4 . . . . . . . . . . . 
                        . . 5 f 4 . . . . . . . . . . . 
                        . . f f 5 . . . . . . . . . . . 
                        . . f . f . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . f f . . . . . . . . . . . 
                        . . . 5 f f . . . . . . . . . . 
                        . . . 4 5 f . . . . . . . . . . 
                        . . . 4 5 f . . . . . . . . . . 
                        . . . 5 5 f . . . . . . . . . . 
                        . . . 5 5 f . . . . . . . . . . 
                        . . . 5 5 f . . . . . . . . . . 
                        . . . 4 5 f . . . . . . . . . . 
                        . . . 4 5 f . . . . . . . . . . 
                        . . . 5 f f . . . . . . . . . . 
                        . . . f f . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . f f . . . . . . . . . . . 
                        . . . 5 f f . . . . . . . . . . 
                        . . . 4 5 f . . . . . . . . . . 
                        . . . 4 5 f . . . . . . . . . . 
                        . . . 5 5 f . . . . . . . . . . 
                        . . . 5 5 f . . . . . . . . . . 
                        . . . 5 5 f . . . . . . . . . . 
                        . . . 4 5 f . . . . . . . . . . 
                        . . . 4 5 f . . . . . . . . . . 
                        . . . 5 f f . . . . . . . . . . 
                        . . . f f . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f f . . . . 
                        . . . f f 5 5 5 5 5 5 f f . . . 
                        . . . f 5 4 4 4 4 4 4 5 f . . . 
                        . . . f 5 4 5 5 5 5 4 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 4 5 f . . . 
                        . . . f 5 4 4 4 4 4 4 5 f . . . 
                        . . . f f 5 5 5 5 5 5 f f . . . 
                        . . . . f f f f f f f f . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        100,
        True)
    tiles.place_on_tile(coin2, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))