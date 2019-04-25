repolr -b SAS_msm8909_l_mr1_m1_spr_us_smt_150717 --reference=/home001/mirror/lr
repo sync -qcj8 --no-tags
repo start SAS_msm8909_l_mr1_m1_spr_us_smt_150717 --all
repo forall -c 'git remote set-url --push lr ssh://lr.lge.com:029475/${REPO_PROJECT}'
