# Digilent

Uma breve descrição sobre o que esse projeto faz e para quem ele é

## Referências

 - [Getting Started with Raspberry Pi](https://digilent.com/reference/test-and-measurement/guides/getting-started-with-raspberry-pi)
 - [DWFPY Examples](https://github.com/mariusgreuel/dwfpy/tree/main/examples)
 - [Waveforms Beta Downloads](https://forum.digilent.com/topic/8908-waveforms-beta-download/)

```bash
    sudo apt update
    sudo apt install code
```

```bash
    python -m pip install --upgrade pip
    pip install dwfpy
    python -m pip install -U matplotlib
```

```bash
    sudo dpkg -P --force-depends libc6-armel-cross libc6-armhf-cross libc6-dev-armel-cross libc6-dev-armhf-cross
    sudo apt clean
    sudo apt update
    sudo apt -f install
    sudo apt install libc6-dev-armel-cross libc6-dev-armhf-cross
```

```bash
    sudo dpkg -i digilent.adept.runtime_2.27.9-armhf.deb
    sudo dpkg -i digilent.waveforms_beta_3.20.24_arm64.deb
```

