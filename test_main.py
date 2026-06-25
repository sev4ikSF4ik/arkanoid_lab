import pytest
from unittest.mock import patch, MagicMock
import sys
sys.modules['pygame'] = MagicMock()
import main

@pytest.fixture
def default_paddle(): return main.Paddle()

@pytest.fixture
def default_ball(): return main.Ball(speed=5)

@pytest.mark.physics
def test_ball_initial_speed(default_ball):
    assert default_ball.dx == 5
    assert default_ball.dy == -5

@pytest.mark.physics
@pytest.mark.parametrize("move_distance, expected_x", [(-10, 330), (10, 350), (0, 340)])
def test_paddle_movement(default_paddle, move_distance, expected_x):
    default_paddle.rect.x = 340
    default_paddle.move(move_distance)
    assert default_paddle.rect.x == expected_x

@patch('main.pygame.draw.rect')
def test_paddle_draw_calls_pygame(mock_draw_rect, default_paddle):
    mock_screen = MagicMock()
    default_paddle.draw(mock_screen)
    mock_draw_rect.assert_called_once()
