# PerpNeg-StableDiffusion

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


If you find it useful for your work, please cite:
```
@article{armandpour2023re,
  title={Re-imagine the Negative Prompt Algorithm: Transform 2D Diffusion into 3D, alleviate Janus problem and Beyond},
  author={Armandpour, Mohammadreza and Zheng, Huangjie and Sadeghian, Ali and Sadeghian, Amir and Zhou, Mingyuan},
  journal={arXiv preprint arXiv:2304.04968},
  year={2023}
}
```