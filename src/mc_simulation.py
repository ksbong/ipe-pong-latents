from dataclasses import dataclass
import numpy as np


@dataclass
class PongState:
    x: float
    y: float
    vx: float
    vy: float


@dataclass
class PongBounds:
    y_min: float
    y_max: float


def step_pong(state: PongState, dt: float, bounds: PongBounds) -> PongState:
    """One deterministic Euler step with vertical wall bounce."""
    x_new = state.x + state.vx * dt
    y_new = state.y + state.vy * dt
    vx_new = state.vx
    vy_new = state.vy

    if y_new > bounds.y_max:
        y_new = bounds.y_max - (y_new - bounds.y_max)
        vy_new = -vy_new

    if y_new < bounds.y_min:
        y_new = bounds.y_min + (bounds.y_min - y_new)
        vy_new = -vy_new

    return PongState(x=x_new, y=y_new, vx=vx_new, vy=vy_new)


def simulate_deterministic(
    x0: float,
    y0: float,
    vx: float,
    vy: float,
    duration: float,
    dt: float,
    bounds: PongBounds,
) -> dict:
    """Simulate deterministic Pong trajectory."""
    n_steps = int(np.ceil(duration / dt))
    state = PongState(x=x0, y=y0, vx=vx, vy=vy)

    xs = np.zeros(n_steps + 1)
    ys = np.zeros(n_steps + 1)

    xs[0] = state.x
    ys[0] = state.y

    bounce_count = 0

    for i in range(1, n_steps + 1):
        old_vy = state.vy
        state = step_pong(state, dt, bounds)

        if np.sign(old_vy) != np.sign(state.vy):
            bounce_count += 1

        xs[i] = state.x
        ys[i] = state.y

    return {
        "x": xs,
        "y": ys,
        "y_final": ys[-1],
        "bounce_count": bounce_count,
    }