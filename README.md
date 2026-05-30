# IPE-inspired Probabilistic Forward Simulation for Occluded Pong

This project explores whether latent variables derived from an Intuitive Physics Engine (IPE)-style probabilistic forward simulation can serve as interpretable candidate variables for analyzing behavior, model predictions, and DMFC population dynamics in an occluded Pong task.

The goal is not to claim that the brain directly implements this simulator. Instead, the simulator is used as a hypothesis-generating model that produces physically interpretable latent variables such as predicted ball position, final target estimate, bounce count, and trajectory uncertainty.

## Next steps

1. Validate coordinate system and wall-bounce convention against existing task metadata.
2. Implement probabilistic forward simulation by sampling noisy initial position and velocity.
3. Compare deterministic and probabilistic predictions against human and RNN predictions.
4. Extract model-derived latent variables for later comparison with DMFC population activity.
