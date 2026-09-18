# CSPC Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

## PW1
Lab A: Reproducible Foundations
**What I built:** Configured CSPC repository, setup conda environment, implemented decay simulation tests, and measured performance differences.

**Speed comparison (loop vs NumPy):**
- loop: 1.6810 s
- numpy: 0.0002 s
- speed-up: 7946.92x faster

**Tests:** all passing? yes

**Conclusion:** Successfully built the reproducible lab environment. Verified that vectorization with NumPy provides significant computational speed-up over pure-Python loops.