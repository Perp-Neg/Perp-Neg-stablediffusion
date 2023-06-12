
### [Project Page](https://perp-neg.github.io/) | [Paper](https://arxiv.org/abs/2304.04968) | [Huggingface][huggingface-demo]
[![][huggingface]][huggingface-demo]


[huggingface]: <https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue>
[huggingface-demo]: <https://huggingface.co/spaces/rezaarmand/Perp-Neg>

![Video Demo](https://github.com/Perp-Neg/Perp-Neg-stablediffusion/assets/tiger.gif)

[![Alt Text](https://img.youtube.com/vi/3ofsPVYkMp0/0.jpg)](https://www.youtube.com/watch?v=3ofsPVYkMp0?autoplay=1)
# Perp-Neg Stable Diffusion

This is the repository for using Perp-Neg sampling with Stable Diffusion model, as presented in [Re-imagine the Negative Prompt Algorithm: Transform 2D Diffusion into 3D, alleviate Janus problem and Beyond.](https://Perp-Neg.github.io).



## Running code


**Run compositional ebm with diffusion model**
```
python scripts/image_sample_stable_diffusion.py --prompt="a boy wearing sunglasses|sunglasses with black frame" --weights="1|-1.5" --pipeline='cebm' --num_images=1
```

**Run PerpNeg**
```
python scripts/image_sample_stable_diffusion.py --prompt="a boy wearing sunglasses|sunglasses with black frame" --weights="1|-1.5" --pipeline='perpneg' --num_images=1
```

**Run PerpNeg-rotation**
```
python scripts/image_sample_stable_diffusion.py --prompt="a photo of lion, front view | a photo of lion, side view" --weights="1|-1.5|-1.5" --pipeline='rotation_perpneg' --num_images=1
```
**PerpNeg-Stable DreamFusion**

please use the scripts in 
stable-dreamfusion/scripts/run_if2_perpneg.sh to run the Stable DreamFusion + PerpNeg to avoid the Janus problem.


This code is manily based on [Stable-DreamFusion](https://github.com/ashawkey/stable-dreamfusion) 

If you find it useful for your work, please cite:
```
@article{armandpour2023re,
  title={Re-imagine the Negative Prompt Algorithm: Transform 2D Diffusion into 3D, alleviate Janus problem and Beyond},
  author={Armandpour, Mohammadreza and Sadeghian, Ali and Zheng, Huangjie and Sadeghian, Amir and Zhou, Mingyuan},
  journal={arXiv preprint arXiv:2304.04968},
  year={2023}
}
```
