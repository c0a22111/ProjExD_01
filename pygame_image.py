import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    fig_img = pg.image.load("ex01/fig/3.png")
    fig_img = pg.transform.flip(fig_img,True,False)
    fig_r_img = pg.transform.rotozoom(fig_img, 10, 1.0)
    imgs = [fig_img, fig_r_img]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        # 画像surfaceを貼り付け
        screen.blit(bg_img, [0, 0])
        screen.blit(fig_img, [0, 0])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()