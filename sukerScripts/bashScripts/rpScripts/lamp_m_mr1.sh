repolr -b lamp_m_mr1_release -m msm8909/msm8909-recent.xml
repo sync -qcj8 --no-tags
repo start lamp_m_mr1_release --all
repo forall -c 'git remote set-url --push lr ssh://lr.lge.com:029475/${REPO_PROJECT}'
