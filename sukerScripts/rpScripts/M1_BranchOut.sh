repolr -b msm8909_l_mr1_e1m1_mp_151110 --reference=/data001/mirror/lap
repo sync -qcj8 --no-tags
repo start msm8909_l_mr1_e1m1_mp_151110 --all
repo forall -c 'git remote set-url --push lr ssh://lr.lge.com:029475/${REPO_PROJECT}'
