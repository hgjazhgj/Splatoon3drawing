# Picture to Spaltoon 3 drawing 喷喷3名片图片转写

1. Run `python3 main.py <your image file> | split -l 30000 -d <file name prefix>` somewhere, require opencv-python.  
   It will generate a macro of controller key serial from your picture.  
   运行`main.py`, 这会从图片生成手柄按键序列  
2. Run `sudo pip3 install nxbt` on your Raspberry Pi. Other Linux should be ok but I have not tested.  
   See [nxbt](https://github.com/Brikwerk/nxbt), it can simulate your Raspberry Pi as a Pro controller.  
   安装`nxbt`用于将树莓派模拟成Pro手柄, 应该是个Linux都行, 但是我没试过  
3. Enter drawing interface in game, move the curser to left-top, select the smallest brush.  
   在游戏中进入绘图, 将光标移到左上角, 选择最小的笔刷  
4. Run `sudo python3 ctrl.py <file gengrated by main.py>` in sequence to run the macro.  
   But! This always Failed to connect! So I prefer to paste the code in `ctrl.py` to a Python interactive shell,  
   or paste the macro to the macro text input in nxbt webapp.  
   这通常不管用, 所以我建议在Python交互中逐行粘贴代码  
   或是直接把宏粘贴到nxbt webapp的宏文本框中然后执行  

`main.py`is optimised to when there are less balck pixels or the balck pixels are more intensive, the faster painting is.  
If your picture has lot of pixel to paint, try to fill the canvas with the biggest brush manually,  
and then replace `A` to `B` in the macro generated with the inversed picture to draw white pixels..  
程序经过优化, 黑色像素越少或越密集, 绘图越快  
如果你的图片中有大量黑色像素,尝试先手动用大号笔刷将画布涂黑,然后把用反相后的图片生成的宏中的A替换成B来绘制白色像素  

You'd better disconnect all of your real controller before running `nxbt`.  
In this case, you can use the touchscreen to move the cursor and select brush.  
你最好在运行nxbt前断开所有其他手柄连接,此时你可以使用触摸屏来选择笔刷与移动光标  
