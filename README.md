# zh-youtube-to-anki

Make an Anki deck out of a YouTube video:

```
./download-transcript.py --url "https://www.youtube.com/watch?v=xq_oAzD2afU" --out-dir out/
anki-chinese out/video-transcript.txt out/video-transcript.tsv
```

## Setup

Create a conda environment and activate it.

```
conda create -n zh-youtube-to-anki python=3.9 -y
conda activate zh-youtube-to-anki
```

Install dependencies.

```
pip install youtube-transcript-api
```

### anki-chinese

Install anki-chinese in the conda environment.

```sh
# Install anki-chinese
curl -sSL https://raw.githubusercontent.com/khughitt/anki-chinese/57b8c97afc761a515ccba6427f65f04db0e43b14/anki-vocab.py > "$CONDA_PREFIX/bin/anki-chinese"
chmod +x "$CONDA_PREFIX/bin/anki-chinese"

# Install trans, a dependency of anki-chinese
curl -sSL git.io/trans > "$CONDA_PREFIX/bin/trans"
chmod +x "$CONDA_PREFIX/bin/trans"

# Install gawk, a dependency of trans
mamba install gawk -y

# Install dependencies of anki-chinese
pip install \
  stanza \
  pandas \
  dragonmapper \
  hanziconv \
  zhon
```
