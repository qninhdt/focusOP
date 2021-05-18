pyinstaller main.py --noconfirm^
	--name="FocusOP" ^
	--add-data="C:/Users/qninh/AppData/Local/Programs/Python/Python38/Lib/site-packages/mediapipe/modules/hand_landmark;mediapipe/modules/hand_landmark" ^
	--add-data="C:/Users/qninh/AppData/Local/Programs/Python/Python38/Lib/site-packages/mediapipe/modules/palm_detection;mediapipe/modules/palm_detection" ^
	--onedir ^
    --add-data="./static;static" ^
	--add-data="./fops;fops" ^
    --icon="./static/app/public/favicon.ico" ^
	--hidden-import="engineio.async_drivers.gevent"
pause