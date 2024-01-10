import pygame, sys, random
import os
import time
import neat

# def ball_animation(player):
    # global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    # ball.x += ball_speed_x
    # ball.y += ball_speed_y

    # if ball.top <= 0 or ball.bottom >= screen_height:
    # 	pygame.mixer.Sound.play(pong_sound)
    # 	ball_speed_y *= -1

    # # player score	
    # if ball.left <= 0:
    # 	pygame.mixer.Sound.play(score_sound)
    # 	player_score += 1
    # 	score_time = pygame.time.get_ticks()

    # # opponent score	
    # if ball.right >= screen_width:
    # 	pygame.mixer.Sound.play(score_sound)
    # 	opponent_score += 1
    # 	score_time = pygame.time.get_ticks()

    # if ball.colliderect(player.rect) and ball_speed_x > 0:
    # 	pygame.mixer.Sound.play(pong_sound)

    # 	# Determine bounce angle based on collision point
    # 	if abs(ball.right - player.rect.left) < 10:
    # 		ball_speed_x *= -1
    # 	elif abs(ball.bottom - player.rect.top) < 10:
    # 		ball_speed_y *= -1
    # 	elif abs(ball.top - player.rect.bottom) < 10:
    # 		ball_speed_y *= -1

    # if ball.colliderect(opponent) and ball_speed_x < 0: 
    # 	pygame.mixer.Sound.play(pong_sound)
    # 	if abs(ball.left - opponent.right) < 10:
    # 		ball_speed_x *= -1
    # 	elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
    # 		ball_speed_y *= -1
    # 	elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
    # 		ball_speed_y *= -1

# def player_animation(player_speed):
# 	player.y += player_speed
# 	if player.top <= 0:
# 		player.top = 0
# 	if player.bottom >= screen_height:
# 		player.bottom = screen_height
class Ball:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed_x = 7 * random.choice((1, -1))
        self.speed_y = 7 * random.choice((1, -1))
        self.y=y
    def update(self, player, opponent):
        global player_score, opponent_score, score_time

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Wall collisions
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            pygame.mixer.Sound.play(pong_sound)
            self.speed_y *= -1

        # Player score
        if self.rect.left <= 0:
            pygame.mixer.Sound.play(score_sound)
            player_score += 1
            score_time = pygame.time.get_ticks()

        # Opponent score
        if self.rect.right >= screen_width:
            pygame.mixer.Sound.play(score_sound)
            opponent_score += 1
            score_time = pygame.time.get_ticks()

        # Collisions with paddles
        if self.rect.colliderect(player.rect) and self.speed_x > 0:
            pygame.mixer.Sound.play(pong_sound)
            self.handle_paddle_collision(player)

        if self.rect.colliderect(opponent) and self.speed_x < 0:
            pygame.mixer.Sound.play(pong_sound)
            self.handle_paddle_collision(opponent)

    def handle_paddle_collision(self, paddle):
        # Determine bounce angle based on collision point
        if abs(self.rect.right - paddle.rect.left) < 10:
            self.speed_x *= -1
        elif abs(self.rect.bottom - paddle.rect.top) < 10:
            self.speed_y *= -1
        elif abs(self.rect.top - paddle.rect.bottom) < 10:
            self.speed_y *= -1
    def start(self):
        global ball_speed_x, ball_speed_y, score_time

        current_time = pygame.time.get_ticks()
        self.rect.center = (screen_width/2, screen_height/2)

        # ... countdown logic for displaying numbers ...

        if current_time - score_time < 2100:
            self.speed_x, self.speed_y = 0, 0
        else:
            self.speed_x = 7 * random.choice((1, -1))
            self.speed_y = 7 * random.choice((1, -1))
            score_time = None
class Opponent:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.y=y

    def update(self, ball):
        if self.rect.top < ball.rect.y:
            self.rect.y += self.speed
        if self.rect.bottom > ball.rect.y:
            self.rect.y -= self.speed

        # Keep opponent within screen boundaries
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


# def ball_start():
# 	global ball_speed_x, ball_speed_y, score_time

# 	current_time = pygame.time.get_ticks()
# 	ball.center = (screen_width/2, screen_height/2)

# 	if current_time - score_time < 700:
# 		number_three = game_font.render("3", False, white)
# 		screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
# 	if 700 < current_time - score_time < 1400:
# 		number_number = game_font.render("2", False, white)
# 		screen.blit(number_number, (screen_width/2 - 10, screen_height/2 + 20))
# 	if 1400 < current_time - score_time < 2100:
# 		number_one = game_font.render("2", False, white)
# 		screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

# 	if current_time - score_time < 2100:
# 		ball_speed_x, ball_speed_y = 0,0
# 	else:
# 		ball_speed_y = 7 * random.choice((1, -1))
# 		ball_speed_x = 7 * random.choice((1, -1))
# 		score_time = None
class PlayerPaddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.y= y
        self.speed = 0

    def move(self, speed):
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

        # Keep paddle within screen boundaries
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


# normal game set up
pygame.mixer.pre_init()
pygame.init()
clock = pygame.time.Clock()

# to set the screen size of the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Rectangles for the game

# ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
# player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
# opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)


bg_color = pygame.Color(0, 0, 0)
ball_color = (255, 255, 255)
line_color = (132, 132, 130)
player_color = (0, 255, 0)
opponent_color = (255, 0, 0)
white = (255, 255, 255)

# game variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# score timer
score_time = True


# text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# game sound
pong_sound = pygame.mixer.Sound("sound/sfx_point.wav")
score_sound = pygame.mixer.Sound("sound/sfx_swooshing.wav")
gen=0
score=0
def main(genomes,config):
    # condition for the game to run
    nets = []
    paddles= []
    ge = []
    global gen
    gen+=1
    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        
        nets.append(net)
        paddles.append(PlayerPaddle(screen_width - 20, screen_height/2 - 70, 10, 140))
        ge.append(genome)
    opponent= Opponent(10, screen_height/2 - 70, 10, 140, 7)
    ball = Ball(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
    while len(paddles) > 0:
        #	Handling input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if score_time:
            start_time = time.time()			
            ball.start()
        # Get inputs for the AI
       
        
        
        # AI output
        for paddle, net in zip(paddles, nets):
            output = net.activate((ball.y, paddle.y, opponent.y))
            # move_up = output[0] > 0.5
            # if move_up:
            #     paddle.move(-7)
            # else:
            #     paddle.move(7)
            # paddle.update()
            if ball.rect.colliderect(paddle.rect):
              genome.fitness += 5 
            scaled_speed = output[0] * 14 - 7  # Scale to -7 to 7
            paddle.move(scaled_speed)
            paddle.update()
        # Move the player's paddle based on AI's decision
        for paddle in paddles:
            

            ball.update(paddle, opponent)
            opponent.update(ball)
        
        
        
        for paddle in paddles:
            if ball.rect.left <= 0 or ball.rect.right >= screen_width:
                
                genome.fitness -=2
                nets.pop(paddles.index(paddle))
                ge.pop(paddles.index(paddle))
                paddles.pop(paddles.index(paddle))

        #game visuals
        screen.fill(bg_color)
        for paddle in paddles:
            pygame.draw.rect(screen, player_color, paddle.rect)
        pygame.draw.rect(screen, opponent_color, opponent)
        pygame.draw.ellipse(screen, ball_color, ball)
        pygame.draw.aaline(screen, line_color, (screen_width/2,0), (screen_width/2, screen_height))
                    

        player_text = game_font.render(f"{player_score}", False, white)
        screen.blit(player_text, (660, 470))

        opponent_text = game_font.render(f"{opponent_score}", False, white)
        screen.blit(opponent_text, (600, 470))

        gen_score = game_font.render(f"{gen}", False, white)
        screen.blit(gen_score, (630, 450))

        #updating the gamme window
        pygame.display.flip()
        clock.tick(75)

def run(config_file):
    """
    runs the NEAT algorithm to train a neural network to play flappy bird.
    :param config_file: location of config file
    :return: None
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(main, 30)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))
if __name__ == '__main__':
    
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'neat-config.txt')
    run(config_path)
    