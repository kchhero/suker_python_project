repolr -b msm8909_l_mr1_m1_cca_us_mp_160104 -m default.xml --reference=/home001/mirror/lr
repo sync -cdq -j4
repo start msm8909_l_mr1_m1_cca_us_mp_160104 --all
