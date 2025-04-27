# Dyber Genshin AI VITS

DyberPet_GenshinImpact + KimiChat + BertVITS2

[![license](https://img.shields.io/github/license/Genius-Society/dyber_genshin_ai_vits.svg)](./LICENSE)
[![itch](https://img.shields.io/badge/release-itch.io-fa5c5c.svg)](https://genius-society.itch.io/dyber-genshin-ai-vits)
[![hf](https://img.shields.io/badge/huggingface-hoyoTTS-ffd21e.svg)](https://huggingface.co/spaces/Genius-Society/hoyoTTS)
[![ms](https://img.shields.io/badge/modelscope-hoyoTTS-624aff.svg)](https://www.modelscope.cn/studios/Genius-Society/hoyoTTS)
[![bili](https://img.shields.io/badge/bilibili-BV1hergYRENX-fc8bab.svg)](https://www.bilibili.com/video/BV1hergYRENX)

[DyberPet_GenshinImpact](https://github.com/ChaozhongLiu/DyberPet_GenshinImpact) is an open-source desktop pet framework that serves as the foundation for custom virtual companions. We have augmented this framework by integrating a large language model (LLM) alongside a VITS-based (Variational Inference with adversarial learning for end-to-end Text-to-Speech) text-to-speech (TTS) module, which together enable intelligent, context-aware dialogue with designated Genshin Impact characters. VITS is a state-of-the-art, single-stage TTS model that delivers natural, high-quality voice synthesis without external alignment annotations. As such, [dyber_genshin_ai_vits](https://github.com/Genius-Society/dyber_genshin_ai_vits) represents an AI-enhanced desktop pet game.

![](https://github.com/Genius-Society/dyber_genshin_ai_vits/assets/20459298/e03c7bf4-bb49-434d-9145-dab1622ee215)

## Environment
Please note that to achieve real-time or near-real-time voice inference, the application requires an NVIDIA GeForce GTX 1080 Ti or a more powerful GPU; on lesser hardware, audio synthesis latency may become unacceptably high.

```bash
conda create -n py311 python=3.11 -y
conda activate py311
pip install -r requirements.txt
```

## Code download
```bash
git clone git@github.com:Genius-Society/dyber_genshin_ai_vits.git
cd dyber_genshin_ai_vits
```

## Run
```bash
python main.py
```

## Build
```bash
python build.py
# Fetch the DyberGenshinAI-win10x64-*.zip from ./dist
```

## Thanks
- [DyberPet](https://github.com/ChaozhongLiu/DyberPet)
- [DyberPet_GenshinImpact](https://github.com/ChaozhongLiu/DyberPet_GenshinImpact)
- [KimiChat](https://platform.moonshot.cn/console/api-keys)
- [Bert-VITS2](https://github.com/fishaudio/Bert-VITS2)
- [Bert-VITS2_Genshin_TTS](https://www.modelscope.cn/studios/erythrocyte/Bert-VITS2_Genshin_TTS)
