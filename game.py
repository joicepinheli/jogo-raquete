#Jogo da raquete com pontuação e vidas
WIDTH = 500
HEIGHT = 500

ball = Rect((150, 400), (20, 20))
bat = Rect((200, 480), (60, 20))
vx = 4
vy = 4

score = 0
lives = 3

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, 'red')
    screen.draw.filled_rect(bat, 'white')
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="yellow")
    screen.draw.text(f"Lives: {lives}", (10, 40), fontsize=30, color="orange")

def update():
    global vx, vy, score, lives

    ball.x += vx
    ball.y += vy

    # Rebote nas laterais
    if ball.left < 0 or ball.right > WIDTH:
        vx = -vx

    # Rebote no topo
    if ball.top < 0:
        vy = -vy

    # Colisão com a raquete
    if ball.colliderect(bat):
        vy = -vy
        score += 1

    # Erro: bola passou pela raquete
    if ball.bottom > HEIGHT:
        lives -= 1
        score -= 1
        if lives < 0:
            print("Game Over")
            exit()
            
        # Reinicia posição da bola
        ball.x, ball.y = 150, 400
        vx, vy = 4, 4

    # Movimento da raquete
    if keyboard.right and bat.right < WIDTH:
        bat.x += 4
    if keyboard.left and bat.left > 0:
        bat.x -= 4