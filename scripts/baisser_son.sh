volume=`amixer sget Master|grep %|cut -d "[" -f 2|cut -d "%" -f 1`
let "volume -= 10"
amixer sset Master $volume%

