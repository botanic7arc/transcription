pip install SpeechRecognition
pip install mecab-python3
sudo apt install -y mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file swig
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
echo yes | ./bin/install-mecab-ipadic-neologd -n -a
cd ..
rm -rf mecab-ipadic-neologd
sudo cp /etc/mecabrc /usr/local/etc/
sudo cp -r /usr/lib/x86_64-linux-gnu/mecab /usr/local/lib/
