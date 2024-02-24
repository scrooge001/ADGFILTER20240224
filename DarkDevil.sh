if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/scrooge001/ADGFILTER20240224
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Film-Detective
fi
cd /Film-Detective
pip3 install -U -r requirements.txt
echo "🕵️Starting Film Detective....."
python3 Film-Detective.py
