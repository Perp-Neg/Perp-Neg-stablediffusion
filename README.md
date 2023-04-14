# PerpNeg-StableDiffusion
 Repo for using Perp-Neg sampling with Stable Diffusion model

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

